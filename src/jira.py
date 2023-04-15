# encoding: utf-8

"""A crawler and scraper of data on projects hosted in platforms like Jira.

This module is the Jira scraper.
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
base_api_url = "https://issues.apache.org/jira/rest/api/2/project"
project_api_url = "https://issues.apache.org/jira/rest/api/2/project/{project_id}"

# caching of things obtained just before
_cache: dict = {
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

    data.init("jira")
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

    print("---------- jira.com scraper started ----------", file=sys.stderr)
    for page in range(int(_cfg['PageLimit'])):

        if (links == None):
            url = base_api_url
        else:
            # pagination:
            if ('next' in links):
                url = links['next']['url']
            else:
                break

        print('---------- getting page ' + str(page + 1) + ' in ' + _cfg[
            'PageLimit'] + ' of project data from url ' + url, file=sys.stderr)
        # (json_data, links) = get_json(url)  # , use_mock = True)

        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve Apache projects: {response.status_code}")
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve Apache projects: {response.status_code}")

        #projects = response.json()
        (json_data, links) = get_json(url)
        limit = 0
        for pr in json_data:
            print('parsing prj ' + str(pr['id']), file=sys.stderr)
            prj = fill_project(pr)
            limit += 1

            data.add_prj(prj)
            if limit > 5:
                break
            time.sleep(int(_cfg['SleepTime']))  # give the API a break

    print("---------- jira.com scraper finished. ----------", file=sys.stderr)


def fill_project(obj: dict):
    """
    Gets project structure from `obj` JSON data and web page contents.
    """

    url = f"{base_api_url}/{obj['id']}"
    response = requests.get(url)
    global _cfg

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve Apache projects: {response.status_code}")
    if response.status_code == 200:
        obj = response.json()

    p = dict(data.PROJECT)
    p['id'] = obj["id"]
    p['owner'] = obj["lead"]["displayName"]
    p['repo-name'] = obj["name"]
    if 'url' in obj:
        p['repo-url'] = obj["url"]
    if 'self' in obj:
        p['url'] = obj["self"]
    p['components'] = len(obj["components"]),
    p['versions'] = len(obj["versions"]),
    p['archived'] = obj["archived"],

    return p


def get_component_count(project_id):
    url = f"https://issues.apache.org/jira/rest/api/2/project/{project_id}"
    response = requests.get(url)
    print(response.encoding, file=sys.stderr)
    if response.status_code == 200:
        data = response.json()
        return len(data.get("components", []))
    else:
        print(f"Error: {response.status_code}")
        return None


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
            print("RESPONSE IS NOT 200!")
            return None
        doc = html.document_fromstring(req.text)

    e = doc.xpath(xpathq)
    # print("scraping: obtained html element: " + str(e) + " for xpath: " + xpathq + " in url: " + url)

    if (e):
        res = e[0].text.strip()
    else:
        res = None

    _cache['scraped_url'] = url
    _cache['scraped_doc'] = doc

    # print("scraping: obtained value: " + str(res))
    return res

def get_json(url: str, use_mock=False):
    """
    Gets data on projects from Jira API.
    Returns a tuple (parsed JSON payload, dictionary-of-links from Link header)
    """

    if (use_mock):
        print("get_json: using mock project data for testing", file=sys.stderr)
        return (read_json(), {})

    json_data: str = ""

    # print("get_json: from url " + url)
    req = requests.get(url)

    if (req.status_code != 200):
        print("request status code doesn't equal to 200!")
        return ([], {})

    json_data = req.json()
    #links = req.links
    links = req.headers.get("Link", None)

    print("get_json: headers in response: " + str(req.headers))
    print("get_json: links in response: " + str(req.links))
    return (json_data, links)

def read_json():
    """
    Returns mock data to test functionality.
    """

    file = _ApiMockDataFilePath
    with open(file, "r") as f:
        json_data = json.load(f)

    return json_data
