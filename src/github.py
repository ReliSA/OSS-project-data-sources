# encoding: utf-8

"""A crawler and scraper of data on projects hosted in platforms like GitHub.

This module is the GitHub scraper.
"""

__all__ = ['scrape']

import time
import sys
import json
import requests
from lxml import html

import data


# global config, to be provided from above
_cfg: dict = {}

# URLs for API access
# /repos/{owner}/{repo}
base_api_url = "https://api.github.com/"
issues_api_url = "https://api.github.com/search/issues?q=repo:{0[owner]}/{0[repo-name]}+type:issue"
open_issues_api_url = "https://api.github.com/search/issues?q=repo:{0[owner]}/{0[repo-name]}+type:issue+state:open"
closed_issues_api_url = "https://api.github.com/search/issues?q=repo:{0[owner]}/{0[repo-name]}+type:issue+state:closed"
contributors_api_url = "https://api.github.com/repos/{0[owner]}/{0[repo-name]}/contributors"

projects_api_url = "search/repositories?q=page=1&per_page={0[ProjectsPerPage]}&q=pushed:>{0[DateLimit]}&order_by=id&sort=asc&"
merge_requests_api_url = "projects/{0[id]}/merge_requests"
releases_api_url = "projects/{0[id]}/releases"

# URLs of web pages for scraping
issues_url = "/issues"
topics_url = "-/topics"
contributors_url = "-/contributors"
teams_url = "-/teams"

# caching of things obtained just before
_cache : dict = {
    "api_url": None, "api_json": None,
    "scraped_url": None, "scraped_doc": None
}

# file with mock project data, to use instead of API calls for testing
_ApiMockDataFilePath = ""

def scrape(cfg: dict):
    """ 
    Runs the GitHub.com platform scraping and
    saves the results into the `data` module structures.
    """

    global _cfg 
    
    data.init("github")
    _cfg = cfg
    read_projects(cfg)


def read_projects(use_issue_num_limit: bool = True, use_only_starred: bool = True):
    """ Fills in the 'projects' list in 'data' module from the 
        GitHub-provided project data, as obtained from the API.
    """

    global _cfg

    url: str = None

    json_data = None
    links: dict = None  # the digested "Link" header of a 'requests' response

    # setting the parameters
    # params = {'q': 'language:python', 'sort': 'stars', 'order': 'desc'}

    print("---------- github.com scraper started ----------", file=sys.stderr)
    for page in range(int(_cfg['PageLimit'])):

        if (links == None):
            url = base_api_url + projects_api_url.format(_cfg)
        else:
            # pagination: https://docs.gitlab.com/ee/api/#keyset-based-pagination
            if ('next' in links):
                url = links['next']['url']
            else:
                break

        print('---------- getting page ' + str(page + 1) + ' in ' + _cfg[
            'PageLimit'] + ' of project data from url ' + url, file=sys.stderr)
        (json_data, links) = get_json(url, _cfg['GitHubAccessToken'])  # , use_mock = True)

        #print('got json, length:' + str(len(json_data)))
        #print('got links: ' + str(links))

        for item in json_data['items']:
            print('parsing prj ' + str(item['id']), file=sys.stderr)
            prj = fill_project(item)

            # if (use_issue_num_limit and prj["issues-all"] < _cfg['LimitIssues']):
            #     continue
            # if (use_only_starred and prj["stars"] < _cfg['LimitStars']):
            #     continue

            data.add_prj(prj)
            time.sleep(int(_cfg['SleepTime']))  # give the API a break

    print("---------- github.com scraper finished. ----------", file=sys.stderr)


def fill_project(obj: dict):
    """
    Gets project structure from `obj` JSON data and web page contents.
    """

    global _cfg

    p = dict(data.PROJECT)
    p['id'] = obj['id']
    p['owner'] = obj['owner']['login']
    p['repo-name'] = obj['name']
    p['repo-url'] = obj['url']
    p['url'] = obj['html_url']
    p['created-at'] = obj['created_at']  # datetime strings
    p['last-active-at'] = obj['updated_at']  # (convert do timestamp?)
    # "stars" are in project data (not like gitlab)
    p['stars'] = obj['stargazers_count']

    if 'forks_count' in obj:
        p['forks'] = obj['forks_count']
    if 'license' in obj and obj['license']:
        p['license'] = obj['license']['name']

    # get project statistics

    p['commits'] = get_scraped_value(p['url'], _cfg['GitHubCommitsCountXPath'])
    p['releases'] = get_scraped_value(p['url'], _cfg['GitHubReleasesCountXPath'])

    # make sure there really is not a license listed for the project
    if (p['license'] == ""):
        p['license'] = get_scraped_value(p['url'], _cfg['GitHubLicenseXPath'])

    # if "stars" are not in project data (doesn't happen often)
    if (p['stars'] == -1):
        p['stars'] = get_scraped_value(p['url'], _cfg['GitHubStarsCountXPath'])

    # just to be sure, in case project data lacked this for some reason
    if (p['forks'] == -1):
        # print('no forks in data, scraping', file=sys.stderr)
        p['forks'] = get_scraped_value(p['url'], _cfg['GitHubForksCountXPath'])


    p['issues-all'] = get_api_value(issues_api_url.format(p), _cfg['GitHubAccessToken'])

    # ^^^ constructs the API URL from the template strings and project's ID read above
    p['issues-open'] = get_api_value(open_issues_api_url.format(p), _cfg['GitHubAccessToken'])
    p['issues-closed'] = get_api_value(closed_issues_api_url.format(p), _cfg['GitHubAccessToken'])

    p['contributors'] = get_contributors_count(contributors_api_url.format(p), _cfg['GitHubAccessToken'])

    return p


def get_api_value(url: str, token: str):
    """
    Query the data obtained from API using JSONPath expressions.
    Returns the first value matching the given query.
    """

    global _cache

    #print("apiquery: using url: " + url + " query: ")
    # use cached value when scraping from the same URL
    if (url == _cache['api_url']):
        # print("apiquery: using cached response for url: " + url)
        json_data = _cache['api_json']
    else:
        # print("apiquery: fresh request to url:" + url)
        (json_data, _) = get_json(url, token)

    total_count = json_data['total_count']

    _cache['api_url'] = url
    _cache['api_json'] = json_data

    # print("apiquery: obtained value: " + str(res))
    return total_count

def get_contributors_count(url: str, token: str):
    """
    API only returns a maximum of 30 contributors per page.
    Goes through all the pages and counts the contributors.
    Returns the total count of contributors.
    """

    contributors_count = 0
    while url:

        (json_data,links) = get_json(url,token)
        contributors_count += len(json_data)

        if links:
            next_url = None
            for link in links.split(","):
                if "rel=\"next\"" in link:
                    next_url = link[link.index("<") + 1:link.index(">")]
                    break
            url = next_url
        else:
            break

    return contributors_count


def get_scraped_value(url: str, xpathq: str):
    """
    Obtain a value from the HTML page at the given url,
    as the inner text of element determined by the XPath query string.
    Uses cached page if the 'url' is the same as when called previously.
    """

    global _cache

    # use cached value when scraping from the same URL
    if (url == _cache['scraped_url']):
        # print("scraping: using cached response for url: " + url)
        doc = _cache['scraped_doc']
    else:
        # print("scraping: fresh request to url:" + url)
        req = requests.get(url)
        if (req.status_code != 200):
            return None
        doc = html.document_fromstring(req.text)

    e = doc.xpath(xpathq)
    #print("scraping: obtained html element: " + str(e) + " for xpath: " + xpathq + " in url: " + url)

    if (e):
        res = e[0].text.strip()
    else:
        res = None

    _cache['scraped_url'] = url
    _cache['scraped_doc'] = doc

    # print("scraping: obtained value: " + str(res))
    return res


def get_json(url: str, token: str, *, use_mock=False):
    """
    Gets data on projects from gitlab API.
    Returns a tuple (parsed JSON payload, dictionary-of-links from Link header)
    """

    if (use_mock):
        print("get_json: using mock project data for testing", file=sys.stderr)
        return (read_json(), {})

    json_data: str = ""

    # print("get_json: from url " + url)
    req = requests.get(url, headers={"Accept": "application", "Authorization": "Bearer %(GitHubAccessToken)s" % {'GitHubAccessToken': token}})

    if (req.status_code != 200):
        print("request doesn't equal to 200")
        return ([], {})
    json_data = req.json()
    #links = req.links
    links = req.headers.get("Link", None)

    # print("get_json: headers in response: " + str(req.headers))
    # print("get_json: links in response: " + str(req.links))
    return (json_data, links)


def read_json():
    """
    Returns mock data to test functionality.
    """

    file = _ApiMockDataFilePath
    with open(file, "r") as f:
        json_data = json.load(f)

    return json_data

