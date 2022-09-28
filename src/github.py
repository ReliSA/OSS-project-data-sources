# encoding: utf-8

"""A crawler and scraper of data on projects hosted in platforms like GitHub.

This module is the GitHub scraper.
"""

__all__ = ['scrape']


# library imports here

import data


# global config, to be provided from above
_cfg: dict = {}


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
    
    # TODO implement the scraping here
    pass
