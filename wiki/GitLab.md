GitLab
======

**Web:** https://gitlab.com/ 

**Version control system:** GIT

**Number of projects:** > 500 000

**API:**

* [Export issues to CSV](https://docs.gitlab.com/ee/user/project/issues/csv_export.html) - only for the paid version
* [Issues API](https://docs.gitlab.com/ee/api/issues.html#list-issues) - Rest API

**Open source projekty:**

* [GitLab Explore projects](https://gitlab.com/explore/projects?non_archived=true&page=2&sort=latest_activity_desc)

## Structure

**Number of live projects:** > 1000 large projects with frequent updates

### Issue tracking system

|Name|Existence|Comment|Link|
|---|---|---|---|
|bug/feature/task/|✅|solving by using labels|https://docs.gitlab.com/ee/user/project/labels.html |
|priority/severity|✅|solving by using labels|https://docs.gitlab.com/ee/development/contributing/issue_workflow.html |
|estimates|✅||https://docs.gitlab.com/ee/user/project/time_tracking.html |
|planned/real deadline|✅||https://docs.gitlab.com/ee/user/project/time_tracking.html |
|subtasks/related issues|✅||https://docs.gitlab.com/ee/user/project/issues/related_issues.html |
|paring of commits|❌|A commit can only have one author and one committer. But multiple people could have contributed to the final squashed commit. This proposal is to append these fields to the end of the commit message.|https://docs.gitlab.com/ee/user/project/merge_requests/squash_and_merge.html|
|issue change history including people assignment|✅||https://docs.gitlab.com/ee/user/project/issues/multiple_assignees_for_issues.html|
|custom categories/tags|✅||https://docs.gitlab.com/ee/user/project/labels.html |
|status configuration/workflow|✅||https://docs.gitlab.com/ee/ci/pipelines/ |
|iterations/phases/milestones/releases|✅||https://docs.gitlab.com/ee/topics/plan_and_track.html|
|roles or other characteristics of people|✅||https://docs.gitlab.com/ee/user/permissions.html |

### Version management system

|Name|Existence|Comment|Link|
|---|---|---|---|
|git flow|✅||https://docs.gitlab.com/ee/topics/gitlab_flow.html |
|complete branch history|✅|||
|named tags|✅||https://docs.gitlab.com/ee/topics/git/tags.html |
|statistics on commits and people|✅|(only for Premium)|https://docs.gitlab.com/ee/user/analytics/productivity_analytics.html|
|metrics on code/commits|✅|(only for Premium)|https://docs.gitlab.com/ee/user/analytics/productivity_analytics.html|
|merge requests (traceable in history)|✅|||
|code review (traceable in history)|✅||https://docs.gitlab.com/ee/development/contributing/issue_workflow.html |


### Projects

|Name|Existence|Comment|Link|
|---|---|---|
|number of contributors|✅|Project information -> Members|
|commiters|✅|Project information -> Members|
|code size|✅|main page of the project|
|license|❔||
|technology used|✅|In Analytics -> Repository|
|product health from ci/cd pipeline|✅|Analytics -> CI/CD analytics|

* https://docs.gitlab.com/ee/user/analytics/

### Tools

|Name|Existence|Comment|Link|
|---|---|---|
|wiki|✅|https://docs.gitlab.com/ee/user/project/wiki/ |
|internal mailing list|❌||
|ci/cd pipeline|✅|https://docs.gitlab.com/ee/ci/ |
|release hosting|❔||
|product website|✅|https://docs.gitlab.com/ee/user/project/pages/ |
|forum nebo Q&A|❌||
|integration with VCS and ITS|❔||

### Metrics

* **Code Lifecycle** - In Deployments -> you can count how often releases are made
* **Code Quality** - In Analytics -> CI/CD analytics you can find the success rate of pipelines in percentage
* **Team Dynamics** - In Analytics -> value stream can be found:
	* Lead Time (time from issue creation to its closure)
	* Cycle time (average time from the first commit to issue closure)
	* New issues (number of new issues)
	* Deployment Frequency (average number of production deployments per day)
* **Project Health** 
	* V Analytics -> Repository - the number of commits per day can be found
	* V Analytics -> Issue - the number of new issues per month can be found
	* V Project information -> Members - the number of new contributors can be found

### Legend

* ✅ - exists
* ❌ - does not exist
* ❔ - not known