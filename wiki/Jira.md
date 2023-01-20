Jira
======

**Web:** https://www.atlassian.com/

**Version control system:** 

**Number of projects:** > not tracked (over  75000 )

**API:**

* https://developer.atlassian.com/server/jira/platform/rest-apis/

**Open source projekty:**

* https://issues.apache.org/jira/projects

## Structure

**Number of live projects:** > not tracked

### Issue tracking system

|Name|Existence|Comment|Link|
|---|---|---|---|
|bug/feature/task/|✅||https://www.atlassian.com/agile/tutorials/issues|
|priority/severity|✅|solving by using flags| https://support.atlassian.com/jira-software-cloud/docs/flag-an-issue/|
|estimates|✅||https://support.atlassian.com/jira-software-cloud/docs/estimate-an-issue/|
|planned/real deadline|✅|| https://support.atlassian.com/jira-software-cloud/docs/what-are-releases-in-advanced-roadmaps/ |
|subtasks/related issues|✅||https://support.atlassian.com/jira-software-cloud/docs/create-an-issue-and-a-sub-task/|
|pairing of commits|❌|||
|issue change history including people assignment|✅|"View Issue" page of the Jira issue -> "History" tab|https://support.atlassian.com/jira-software-cloud/docs/what-are-the-different-types-of-activity-on-an-issue/ |
|custom categories/tags|✅|by using Jira's custom fields feature|https://support.atlassian.com/jira-software-cloud/docs/available-custom-fields-for-team-managed-projects/|
|status configuration/workflow|✅||https://support.atlassian.com/jira-software-cloud/docs/use-the-simplified-workflow/|
|iterations/phases/milestones/releases|✅||https://support.atlassian.com/jira-software-cloud/docs/assign-statuses-and-edit-columns-in-a-team-managed-project/|
|roles or other characteristics of people|✅||https://support.atlassian.com/jira-software-cloud/docs/how-do-jira-permissions-work/|

### Version management system

|Name|Existence|Comment|Link|
|---|---|---|---|
|git flow|✅||https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow|
|complete branch history|❌|||
|named tags|❌|but has labels||
|statistics on commits and people|✅||https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/|
|metrics on code/commits|❌|||
|merge requests (traceable in history)|❌|||
|code review (traceable in history)|✅||https://confluence.atlassian.com/crucible/using-the-review-history-dialog-298977452.html|


### Projects

|Name|Existence|Comment|Link|
|---|---|---|
|number of contributors|✅|"People" page -> list of contributors|
|committers|❌||
|code size|❌|You would need to use a third-party tool to measure the size of the code|
|license|❌||
|technologies used|✅|project's "Settings" page -> the "Technologies" tab|
|product health from ci/cd pipeline|✅|by viewing the pipeline's status, build results, and other metrics|



### Tools

|Name|Existence|Comment|Link|
|---|---|---|
|wiki|✅| project page -> the “Wiki” tab -> “Create Page”|
|internal mailing list|❌|However, there are a few third-party plugins available that can be used to create an internal mailing list for a project|
|ci/cd pipeline|❌|However, Jira can be integrated with a CI/CD pipeline, such as Jenkins, to provide visibility into the progress of the project.|
|release hosting|❌||
|product website|✅|Project settings page in Jira -> “Project Website” tab|
|forum or Q&A|✅|The Q&A forum can be accessed through the Jira Service Desk portal|
|integration with VCS and ITS|✅|Jira can be integrated with VCSs such as Git, Subversion, and Mercurial. It can also be integrated with popular ITSs such as Bugzilla, Trac, and Redmine.|

### Metrics

* **Code Lifecycle** - These metrics are available in the Jira Software application and can be accessed from the Reports tab. The Code Lifecycle metrics provide an overview of the development process, including the number of open and closed issues, the average time to close an issue, and the number of issues in each status. 
* **Code Quality** - Jira can be integrated with code analysis tools such as SonarQube, which can provide code quality metrics such as code coverage, complexity, duplication, and more. Additionally, Jira can be integrated with static code analysis tools such as Checkstyle, which can provide metrics such as code style, formatting, and potential bugs.
* **Team Dynamics** - Jira does not have Team Dynamics metrics. However, there are third-party plugins and add-ons that can be used to measure team dynamics and performance. These plugins and add-ons can provide metrics such as team velocity, task completion rate, and team collaboration.
* **Project Health** - These metrics are available in the Jira Software project health dashboard. The dashboard provides an overview of the project's progress, including the number of open issues, the number of closed issues, the number of unresolved issues, the average cycle time, the average lead time, and the average time to resolution.


### Legend

* ✅ - exists
* ❌ - does not exist
* ❔ - not known