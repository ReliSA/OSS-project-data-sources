#!/usr/bin/env python3 
# encoding: utf-8

"""A crawler and scraper of data on projects hosted in platforms like GitHub.

This tool is used to obtain (meta)data on projects from Code Hosting Platforms,
in such a way that this data can be analyzed later e.g. for research 
purposes.  The following platforms are currently supported:

* Gitlab.com

Typical usage:

1. set up suitable values in `../config.ini` file
2. run `python3 <thisfile>.py > output.csv`
3. use the output ;-)

"""

__license__ = "MIT"
__copyright__ = "Copyright 2022 University of West Bohemia"
__author__ = "Premek Brada <brada@kiv.zcu.cz>"


import sys
import importlib

import data


if __name__ == "__main__":
    
    try:
        cfg: dict = data.read_cfg()
    except FileNotFoundError:
        print("chps: config file not found, exiting.", file=sys.stderr)
        sys.exit(1)
    except BaseException as e:
        print("chps: an error '"+str(e)+"' occurred reading config file, exiting.", file=sys.stderr)
        sys.exit(2)

    mlist = cfg['ScrapersToUse'].strip()
    if (mlist == ""):
        print("chps: no scraper was asked to be run, exiting.", file=sys.stderr)
        sys.exit(1)
        
    modules = set(mlist.split())
    # import and run the configured scrapers
    for scraper in modules:
        try:
            m = importlib.import_module(scraper)
            m.scrape(cfg)
        except ModuleNotFoundError:
            print("chps: scraper `"+scraper+"` could not be imported, skipping it.", file=sys.stderr)

    # make the user happy
    data.prj2csv(sys.stdout)
