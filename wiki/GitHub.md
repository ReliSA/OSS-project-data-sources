GitHub
======

**Web:** https://github.com/ 

**Version control system:** GIT

**Number of projects:** [> 200 mil](https://github.com/about)

**API:**

* [CLI](https://cli.github.com/) - GitHub command line functionality

```bash
janelle@janelle-VirtualBox:~/hub$ gh issue list

Showing 30 of 231 open issues in github/hub

#2858  Test                                                                                                                                         about 6 days ago
#2856  Personnel access token not working                                                                                                  bug      about 15 days ago
#2855  merge pull request into multiple branches                                                                                           bug      about 16 days ago
#2854  Commits are not being listed in the contribtion graph                                                                               bug      about 19 days ago
#2853  Non ergonomic back navigation on mobile: critical                                                                                   bug      about 21 days ago
#2852  I'm able to edit someone else's comment on my PR                                                                                    bug      about 21 days ago
#2848  PR count issue on projects                                                                                                          bug      about 26 days ago
#2847  What language?                                                                                                                               about 9 days ago
#2832  Is there a javascript wrapper for this for Node.js ?                                                                                feature  about 1 month ago
```

* [HUB](https://hub.github.com/)
* [GitStats](http://gitstats.sourceforge.net/) - getting statistics (total files, lines, commits, commits by hour of day) from projects.

**Open source projects:**

* [Awesome Open Source](https://awesomeopensource.com/) 
* [GitHUb Trending repos](https://github.com/trending)

## Structure

**Number of live projects:** plenty

### Issue tracking system

|Name|Existence|Comment|Link|
|---|---|---|---|
|bug/feature/task/|✅|solving by using labels|https://softwareengineering.stackexchange.com/questions/129714/how-to-manage-github-issues-for-priority-etc|
|priority/severity|✅|solving by using labels|https://softwareengineering.stackexchange.com/questions/129714/how-to-manage-github-issues-for-priority-etc|
|estimates|❌|
|planned/real deadline|✅|Milestones due date|https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones|
|subtasks/related issues|✅|markdown checklist pod issue/[milestone/labels]|https://help.zenhub.com/support/solutions/articles/43000010341-an-intro-to-zenhub-epics|
|pairing of commits|✅||https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors|
|issue change history including people assignment|✅||https://docs.github.com/en/issues/tracking-your-work-with-issues/assigning-issues-and-pull-requests-to-other-github-users|
|custom categories/tags|✅|topics | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics|
|status configuration/workflow|✅||https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions |
|iterations/phases/milestones/releases|✅|Milestones, release|https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones|
|roles or other characteristics of people|✅|Read, Triage, Write, Maintain, Admin|https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/repository-roles-for-an-organization|

### Version management system

|Name|Existence|Comment|Link|
|---|---|---|---|
|git flow|✅||https://docs.github.com/en/get-started/quickstart/github-flow |
|complete branch history|✅|commit history||
|named tags|✅||https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags |
|statistics on commits and people|✅|external programs + in project Insights (contributor-number of commits)|http://gitstats.sourceforge.net/examples/git/activity.html, https://github.com/morucci/repoxplorer |
|metrics on code/commits|✅||https://github.com/morucci/repoxplorer |
|merge requests (traceable in history)|✅||https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request|
|code review (traceable in history)|✅||https://github.com/features/code-review|


### Projects

|Name|Existence|Comment|Link|
|---|---|---|
|number of contributors|✅|can be found on the main project page as Contributors|
|committers|✅|can be found in Insights -> Pulse|
|code size|✅|https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci|
|licenses|✅|can be found on the main project page of the project|
|technologies used|✅|can be found on the main project page of the project as Languages|

* https://github.com/morucci/monocle
* https://github.com/morucci/repoxplorer

### Tools

|Name|Existence|Comment|Link|
|---|---|---|
|wiki|✅||
|internal mailing list|❌||
|ci/cd pipeline|✅|https://resources.github.com/ci-cd/#examples|
|release hosting|✅|https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages|
|product website|✅|https://pages.github.com|
|forum nebo Q&A|✅|https://docs.github.com/en/discussions|
|integration with VCS and ITS|❔ |

### Metrics

* **Code Lifecycle** - you can find out how often releases are made
* **Code Quality** - if the project uses labels for issues, the ratio of bugs and releases can be calculated
* **Team Dynamics** - in Insights you can seen how many commits are made per week
* **Project Health** - in Insights you can see how many contributors added commits

### Legend

* ✅ - exists
* ❌ - does not exist
* ❔ - not known