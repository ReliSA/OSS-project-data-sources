# encoding: utf-8

"""A crawler and scraper of data on projects hosted in platforms like GitHub.

This module is the GitLab scraper.
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
base_api_url = "https://gitlab.com/api/v4/"
issues_api_url = "projects/{0[id]}/issues_statistics"
members_api_url = "projects/{0[id]}/members"
contributors_api_url = "projects/{0[id]}/repository/contributors"
projects_api_url = "projects?last_activity_after={0[DateLimit]}&pagination=keyset&per_page={0[ProjectsPerPage]}&order_by=id&sort=asc&"
merge_requests_api_url = "projects/{0[id]}/merge_requests"
releases_api_url = "projects/{0[id]}/releases"

# URLs of web pages for scraping
issues_url = "-/issues"
members_url = "-/project_members"
contributors_url = "-/graphs/master"
merge_requests_url = "-/merge_requests"

# caching of things obtained just before
_cache : dict = { 
    "api_url": None, "api_json": None,
    "scraped_url": None, "scraped_doc": None
}

# file with mock project data, to use instead of API calls for testing
_ApiMockDataFilePath = "/home/brada/dev/chp-crawler/data/projects.json"



def scrape(cfg: dict):
    """ 
    Runs the gitlab.com platform scraping and
    saves the results into the `data` module structures.
    """

    global _cfg 
    
    data.init("gitlab.com")
    _cfg = cfg
    read_projects(cfg)


def read_projects(use_issue_num_limit: bool = True, use_only_starred: bool = True):
    """ Fills in the 'projects' list in 'data' module from the 
        GitLab-provided project data, as obtained from the API.
    """

    global _cfg
    
    url: str = None
    
    json_data = None
    links: dict = None  # the digested "Link" header of a 'requests' response

    print("---------- gitlab.com scraper started ----------",file=sys.stderr)
    for page in range(int(_cfg['PageLimit'])):

        if (links == None):
            url = base_api_url + projects_api_url .format(_cfg)
        else:
            # pagination: https://docs.gitlab.com/ee/api/#keyset-based-pagination
            if ('next' in links):
                url = links['next']['url']
            else:
                break
                
        print('---------- getting page '+str(page+1)+' in '+_cfg['PageLimit']+' of project data from url ' + url, file=sys.stderr)
        (json_data, links) = get_json(url, _cfg['GitLabAccessToken']) #, use_mock = True)
        #print('got json, length:' + str(len(json_data)))
        #print('got links: ' + str(links))
        
        for obj in json_data:
            print('parsing prj ' + str(obj['id']), file=sys.stderr)
            prj = fill_project(obj)

            # if (use_issue_num_limit and prj["issues-all"] < _cfg['LimitIssues']):
            #     continue
            # if (use_only_starred and prj["stars"] < _cfg['LimitStars']):
            #     continue
            
            data.add_prj(prj)
            time.sleep(int(_cfg['SleepTime']))   # give the API a break

    print("---------- gitlab.com scraper finished. ----------",file=sys.stderr)


def fill_project(obj: dict):
    """ 
    Gets project structure from `obj` JSON data and web page contents.
    """

    global _cfg

    p = dict(data.PROJECT)
    p['id'] = obj['id']
    repostr : list = obj['name_with_namespace'].split(' / ')
    p['owner'] = repostr[0]
    p['repo-name'] = repostr[1]
    p['repo-url'] = obj['http_url_to_repo']
    p['url'] = obj['web_url']
    p['created-at'] = obj['created_at']             # datetime strings
    p['last-active-at'] = obj['last_activity_at']   # (convert do timestamp?)

    if ('forks_count' in obj):
        p['forks'] = obj['forks_count']
    if ('license.name' in obj):
        p['license'] = obj['license.name']
    
    # get project statistics
    
    p['commits'] = get_scraped_value(p['url'], _cfg['GitLabCommitsCountXPath'])
    p['releases'] = get_scraped_value(p['url'], _cfg['GitLabReleasesCountXPath'])
    # make sure there really is not a license listed for the project
    if (p['license'] == ""):
        p['license'] = get_scraped_value(p['url'], _cfg['GitLabLicenseXPath'])

    # "stars" are not in project data
    p['stars'] = get_scraped_value(p['url'], _cfg['GitLabStarsCountXPath'])
    # just to be sure, in case project data lacked this for some reason
    if (p['forks'] == -1):
        #print('no forks in data, scraping', file=sys.stderr)
        p['forks'] = get_scraped_value(p['url'], _cfg['GitLabForksCountXPath'])
    
    p['issues-all'] = get_api_value(base_api_url + issues_api_url .format(p), _cfg['GitLabAccessToken'], _cfg['GitLabIssuesAllJsonPath'])
    # ^^^ constructs the API URL from the template strings and project's ID read above
    p['issues-open'] = get_api_value(base_api_url + issues_api_url .format(p), _cfg['GitLabAccessToken'], _cfg['GitLabIssuesOpenJsonPath'])
    p['issues-closed'] = get_api_value(base_api_url + issues_api_url .format(p), _cfg['GitLabAccessToken'], _cfg['GitLabIssuesClosedJsonPath'])

    (contrib_json, _) = get_json(base_api_url + contributors_api_url .format(p), _cfg['GitLabAccessToken'])
    p["contributors"] = len(contrib_json)

    return p


def get_api_value(url: str, token: str, query: str):
    """ 
    Query the data obtained from API using JSONPath expressions.
    Returns the first value matching the given query.
    """
    
    import jsonpath_rw

    global _cache
    
    #print("apiquery: using url: " + url + " query: " + query)
    # use cached value when scraping from the same URL 
    if (url == _cache['api_url']):
        #print("apiquery: using cached response for url: " + url)
        json_data = _cache['api_json']
    else:
        #print("apiquery: fresh request to url:" + url)
        (json_data, _) = get_json(url, token)
    
    jsonpath_expr = jsonpath_rw.parse(query)
    found = jsonpath_expr.find(json_data)
    res = found[0].value
    
    _cache['api_url'] = url
    _cache['api_json'] = json_data
    
    #print("apiquery: obtained value: " + str(res))
    return res
    

def get_scraped_value(url: str, xpathq: str):
    """ 
    Obtain a value from the HTML page at the given url, 
    as the inner text of element determined by the XPath query string.
    Uses cached page if the 'url' is the same as when called previously.
    """
    
    global _cache
    
    # use cached value when scraping from the same URL 
    if (url == _cache['scraped_url']):
        #print("scraping: using cached response for url: " + url)
        doc = _cache['scraped_doc']
    else:
        #print("scraping: fresh request to url:" + url)
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
    
    #print("scraping: obtained value: " + str(res))
    return res
    
    
def get_json(url: str, token: str, *, use_mock = False):
    """ 
    Gets data on projects from gitlab API.
    Returns a tuple (parsed JSON payload, dictionary-of-links from Link header)
    """

    if (use_mock):
        print("get_json: using mock project data for testing", file=sys.stderr)
        return (read_json(), {})
    
    json_data : str = ""

    #print("get_json: from url " + url)
    req = requests.get(url, headers = { "Accept":"application/json", "Authorization":"Bearer %(GitLabAccessToken)s" % {'GitLabAccessToken':token} } )
    if (req.status_code != 200):
        return ([], {})
    json_data = req.json()
    links = req.links 

    #print("get_json: headers in response: " + str(req.headers))
    #print("get_json: links in response: " + str(req.links))
    return (json_data, links)


def read_json():
    """ 
    Returns mock data to test functionality.
    """

    file = _ApiMockDataFilePath
    with open(file,"r") as f:
        json_data = json.load(f)
    
    return json_data
