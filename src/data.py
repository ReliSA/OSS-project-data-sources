# encoding: utf-8

"""A crawler and scraper of data on projects hosted in platforms like GitHub.

This module defines the data structures and operations.
"""

__all__ = ['init', 'read_cfg', 'add_prj', 'prj2csv']

import csv
import configparser

###
### Template/structure for project data record.
###
PROJECT : dict = {

    "platform" : "",   # github, gitlab
    "id" : "",
    "owner" : "",
    "repo-name" : "",
    "created-at" : "",
    "last-active-at" : "",
    "url" : "",
    "repo-url" : "",
    "license" : "",
    "commits" : -1,
    "contributors" : -1,
    "issues-all" : -1,
    "issues-open" : -1,
    "issues-closed" : -1,
    "stars" : -1,
    "forks" : -1,
    "releases" : -1,
    "components" : -1,   # jira
    "versions" : -1,     # jira
    "archived" : -1,     # jira
}

### Here the data of projects, scraped from the platforms, are stored
_projects: list = []


def init(platform: str, clean_dataset: bool = False):
    """
    Clean up the data set (if asked to) and set the platform name.
    """
    
    global _projects
    
    if (clean_dataset):
        _projects = []
    PROJECT['platform'] = platform


def read_cfg():
    """
    Parse the config file; the path to it is hard-coded here.
    """
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read_file(open('../config.ini'))
    res: dict = dict()
    for k in config['DEFAULT']:
        res[k] = config['DEFAULT'][k]
    return res


def add_prj(p: dict):
    """ 
    Adds a project's data record to the set.
    """
    _projects.append(p)

def prj2csv(file):
    """
    Outputs the projects data as CSV.
    Expects `file` to be ready for writing.
    """

    writer = csv.DictWriter(file, PROJECT.keys())
    writer.writeheader()
    for p in _projects:
        writer.writerow(p)
