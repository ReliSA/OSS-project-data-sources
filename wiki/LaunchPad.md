LaunchPad
=========

**Web:** https://launchpad.net/ 

**Version control system:** GIT, BZR

**Počet projektů:** [> 44000](https://launchpad.net/projects/)

**API:**

* [launchpadlib](https://help.launchpad.net/API/launchpadlib#Collections) - knihovna pro Python

```python
launchpad = Launchpad.login_anonymously('lplib.cookbook.json_fetcher', 'production', cachedir, version = 'devel')

project = launchpad.projects['ubuntu'] #where 'ubuntu' is the project name
bugs = project.searchTasks(status = ['New', 'Incomplete', 'Triaged', 'Opinion', 'Invalid', 'Won\'t Fix', 'Confirmed', 'In Progress', 'Fix Committed', 'Fix Released'])

for bug in bugs:
        browser = launchpad._browser
        bugInfo = browser.get(bug.self_link) #gets you the bug information
```


**Open source projekty:**

* [All projects](https://launchpad.net/projects/+all)

## Struktura

**Počet živých projektů:** ...

### Issue tracking system

|Název|Existence|Poznámka|Odkaz|
|---|---|---|---|
|bug/feature/task/|✅|bugs a bluesprints|https://help.launchpad.net/Blueprint |
|priority/severity|✅||https://blueprints.launchpad.net/kolla-ansible|
|estimates|❌||
|planned/real deadline|❌||
|podúkoly/related issues|✅|Related branches a Related bugs |
|spárování commitů|❔||
|historie změn issue vč. people assignment|✅|activity log||
|vlastní kategorie/štítky|❔||
|konfigurace stavů/workflow|❌||
|iterace/fáze/milestones/releases|✅|milestone, sprint |https://help.launchpad.net/Blueprint |
|role nebo jiné charakteristiky lidí|✅|Assignee/Drafter/Approver/Registrant|https://help.launchpad.net/BlueprintRoles |

### Version management system

|Název|Existence|Poznámka|
|---|---|---|
|git flow|✅|https://help.launchpad.net/Code/Review?action=show&redirect=BranchMergeProposals |
|kompletní historie větví|✅|https://code.launchpad.net/~bootstack-charmers/charm-local-users/+git/charm-local-users/+ref/main|
|named tags|❔||
|statistiky na commitech a lidech|✅|files changed, insertions, deletions|
|metriky na kódu/commitech|❔||
|merge requests (v historii dohledatelné)|✅|https://help.launchpad.net/Code/Review?action=show&redirect=BranchMergeProposals |
|code review (v historii dohledatelné)|✅|https://help.launchpad.net/Code/Review?action=show&redirect=BranchMergeProposals |


### Projekty

|Název|Existence|Poznámka|
|---|---|---|
|počet přispěvatelů|✅|Top contributors|
|commiterů|✅||
|code size|❌||
|licence|✅|in project Overview|
|použité technologie|❌||
|zdraví produktu z ci/cd pipeline|❌||

### Nástroje

|Název|Existence|Poznámka|
|---|---|---|
|wiki|❌||
|mailing list|✅|https://help.launchpad.net/Teams/MailingLists |
|ci/cd pipeline|❌||
|release hosting|✅|https://help.launchpad.net/Code/QuickStart |
|produktový web|✅|https://help.launchpad.net/Code/QuickStart |
|fórum nebo Q&A|✅|Answers|
|integrace s VCS a ITS|❔||


### Legenda

* ✅ - existuje
* ❌ - neexistuje
* ❔ - nevím