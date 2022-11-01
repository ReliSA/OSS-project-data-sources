LaunchPad
=========

**Web:** https://launchpad.net/ 

**Version control system:** GIT, BZR

**Number of projects:** [> 44000](https://launchpad.net/projects/)

**API:**

* [launchpadlib](https://help.launchpad.net/API/launchpadlib#Collections) - Python library

```python
launchpad = Launchpad.login_anonymously('lplib.cookbook.json_fetcher', 'production', cachedir, version = 'devel')

project = launchpad.projects['ubuntu'] #where 'ubuntu' is the project name
bugs = project.searchTasks(status = ['New', 'Incomplete', 'Triaged', 'Opinion', 'Invalid', 'Won\'t Fix', 'Confirmed', 'In Progress', 'Fix Committed', 'Fix Released'])

for bug in bugs:
        browser = launchpad._browser
        bugInfo = browser.get(bug.self_link) #gets you the bug information
```


**Open source projects:**

* [All projects](https://launchpad.net/projects/+all)

## Structure

**Number of live projects:** ...

### Issue tracking system

|Name|Existence|Comment|Link|
|---|---|---|---|
|bug/feature/task/|✅|bugs a bluesprints|https://help.launchpad.net/Blueprint |
|priority/severity|✅||https://blueprints.launchpad.net/kolla-ansible|
|estimates|❌||
|planned/real deadline|❌||
|subtasks/related issues|✅|Related branches a Related bugs |
|paring of commits|❔||
|issue change history including people assignment|✅|activity log||
|custom categories/tags|❔||
|status configuration/workflow|❌||
|iteration/phases/milestones/releases|✅|milestone, sprint |https://help.launchpad.net/Blueprint |
|roles or other characteristics of people|✅|Assignee/Drafter/Approver/Registrant|https://help.launchpad.net/BlueprintRoles |

### Version management system

|Name|Existence|Comment|
|---|---|---|
|git flow|✅|https://help.launchpad.net/Code/Review?action=show&redirect=BranchMergeProposals |
|complete branch history|✅|https://code.launchpad.net/~bootstack-charmers/charm-local-users/+git/charm-local-users/+ref/main|
|named tags|❔||
|statistics on commits and people|✅|files changed, insertions, deletions|
|metrics on code/commits|❔||
|merge requests (traceable in history)|✅|https://help.launchpad.net/Code/Review?action=show&redirect=BranchMergeProposals |
|code review (traceable in history)|✅|https://help.launchpad.net/Code/Review?action=show&redirect=BranchMergeProposals |


### Projects

|Name|Existence|Comment|
|---|---|---|
|number of contributors|✅|Top contributors|
|commiters|✅||
|code size|❌||
|license|✅|in project Overview|
|used technologies|❌||
|product health from ci/cd pipeline|❌||

### Tools

|Name|Existence|Comment|
|---|---|---|
|wiki|❌||
|mailing list|✅|https://help.launchpad.net/Teams/MailingLists |
|ci/cd pipeline|❌||
|release hosting|✅|https://help.launchpad.net/Code/QuickStart |
|production website|✅|https://help.launchpad.net/Code/QuickStart |
|forum or Q&A|✅|Answers|
|integration with VCS and ITS|❔||


### Legend

* ✅ - exists
* ❌ - does not exist
* ❔ - not known