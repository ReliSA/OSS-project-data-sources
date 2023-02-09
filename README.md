
Code Hosting Platforms Data and Scraper
=======================================

An [information repository about data on projects hosted on Code Hosting Platforms (CHP)](wiki/) like github, source forge etc., and a [tool to retrieve this data](src/) and provide it in a comma-separated values (CSV) format.

The software in this repository is distributed under the MIT licence.  The `LICENSE` file is available in the root folder.

Copyright 2022 University of West Bohemia

Authors: Premek Brada, Petr Picha, Zhanel Mukanova (texts under the `wiki` folder).


The `chps` Tool Usage
-----

1. Modify appropriate values in `config.ini` to configure tool's operation.
2. Run `chps` (linux) or `chps.bat` (Windows); redirect output to a file to save it.


Developer documentation
-----------------------

### Structure and design

Modules and flow

* Each CHP has its own module, called by the main `chps` script if the given CHP is "enabled" in the config by the `ScrapersToUse` variable.  Import of, and call to the module are done dynamically, the names provided in the `ScrapersToUse` config var must correspond to filenames of python modules of the CHP scrapers in the `src` directory (e.g. for `ScrapersToUse = gitlab jira` there need to be `gitlab.py` and `jira.py` files available).
* The CHP module is responsible for obtaining the projects' meta-data and statistics and storing these via the `data` module.  The data are added to any already stored by modules run before the given one.
* The main script outputs the aggregated projects' data in CSV format to stdout. 

Internal APIs and conventions

* Modules define the standard `__all__` dunder to signal which functions are available to other modules.
* Important API patterns:
** CHP modules are called through `scrape(cfg: dict)` from the main script.
** They must use `data.init()` and `data.add_prj(p: dict)` to store the project data.

Data structures 

* Data structure accumulating project meta-data and statistics is defined
as a `PROJECT` "record template" in the `data.py` module, initialized
with the CHP name in `data.init()`, and then "instantiated" for each analyzed
project in the CHP module through `p = dict(data.PROJECT)` .
* Projects' data are internally stored in `data._projects[]` list, which is to be accessed via the `data` module's API only.
* The config file (`config.ini`) is parsed into a dictionary, passed to the
CHP module, and there accessed through a module-global `_cfg` variable.

GitLab CHP module

* The last obtained API JSON and web page are cached (in `get_XXX_value()` functions), so as to spare further queries to the same URL, via a simple module-global `_cache` dictionary.

### Libraries used

The less common ones:

* `requests` (https://pypi.org/project/requests/) for simple API calls and web page retrieval
* `lxml` (https://lxml.de/) for web page scraping
* `jsonpath_rw` (https://github.com/kennknowles/python-jsonpath-rw) to cherrypick values from API-returned data

### References

* GitLab API: https://docs.gitlab.com/ee/api/ (mainly the projects part, https://docs.gitlab.com/ee/api/projects.html)
* GitHub API: https://docs.github.com/rest (mainly the projects part, https://docs.github.com/en/rest/projects)
