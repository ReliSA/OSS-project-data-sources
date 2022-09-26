GitLab
======

**Web:** https://gitlab.com/ 

**Version control system:** GIT

**Počet projektů:** > 500 tisíc

**API:**

* [Export issues to CSV](https://docs.gitlab.com/ee/user/project/issues/csv_export.html) - pouze pro placenou verzi
* [Issues API](https://docs.gitlab.com/ee/api/issues.html#list-issues) - Rest API

**Open source projekty:**

* [GitLab Explore projects](https://gitlab.com/explore/projects?non_archived=true&page=2&sort=latest_activity_desc)

## Struktura

**Počet živých projektů:** > 1000 velkých projektů s častým aktualizováním

### Issue tracking system

|Název|Existence|Poznámka|Odkaz|
|---|---|---|---|
|bug/feature/task/|✅|řešení přes labely|https://docs.gitlab.com/ee/user/project/labels.html |
|priority/severity|✅|řešení přes labely|https://docs.gitlab.com/ee/development/contributing/issue_workflow.html |
|estimates|✅||https://docs.gitlab.com/ee/user/project/time_tracking.html |
|planned/real deadline|✅||https://docs.gitlab.com/ee/user/project/time_tracking.html |
|podúkoly/related issues|✅||https://docs.gitlab.com/ee/user/project/issues/related_issues.html |
|spárování commitů|❌|A commit can only have one author and one committer. But multiple people could have contributed to the final squashed commit. This proposal is to append these fields to the end of the commit message.|https://docs.gitlab.com/ee/user/project/merge_requests/squash_and_merge.html|
|historie změn issue vč. people assignment|✅||https://docs.gitlab.com/ee/user/project/issues/multiple_assignees_for_issues.html|
|vlastní kategorie/štítky|✅||https://docs.gitlab.com/ee/user/project/labels.html |
|konfigurace stavů/workflow|✅||https://docs.gitlab.com/ee/ci/pipelines/ |
|iterace/fáze/milestones/releases|✅||https://docs.gitlab.com/ee/topics/plan_and_track.html|
|role nebo jiné charakteristiky lidí|✅||https://docs.gitlab.com/ee/user/permissions.html |

### Version management system

|Název|Existence|Poznámka|Odkaz|
|---|---|---|---|
|git flow|✅||https://docs.gitlab.com/ee/topics/gitlab_flow.html |
|kompletní historie větví|✅|||
|named tags|✅||https://docs.gitlab.com/ee/topics/git/tags.html |
|statistiky na commitech a lidech|✅|(pouze pro Premium)|https://docs.gitlab.com/ee/user/analytics/productivity_analytics.html|
|metriky na kódu/commitech|✅|(pouze pro Premium)|https://docs.gitlab.com/ee/user/analytics/productivity_analytics.html|
|merge requests (v historii dohledatelné)|✅|||
|code review (v historii dohledatelné)|✅||https://docs.gitlab.com/ee/development/contributing/issue_workflow.html |


### Projekty

|Název|Existence|Poznámka|
|---|---|---|
|počet přispěvatelů|✅|Project information -> Members|
|commiterů|✅|Project information -> Members|
|code size|✅|hlavní stranka projektu|
|licence|❔||
|použité technologie|✅|V Analytics -> Repository|
|zdraví produktu z ci/cd pipeline|✅|Analytics -> CI/CD analytics|

* https://docs.gitlab.com/ee/user/analytics/

### Nástroje

|Název|Existence|Poznámka|
|---|---|---|
|wiki|✅|https://docs.gitlab.com/ee/user/project/wiki/ |
|interní mailing list|❌||
|ci/cd pipeline|✅|https://docs.gitlab.com/ee/ci/ |
|release hosting|❔||
|produktový web|✅|https://docs.gitlab.com/ee/user/project/pages/ |
|fórum nebo Q&A|❌||
|integrace s VCS a ITS|❔||

### Metriky

* **Code Lifecycle** - Deployments -> lze spočítat jak často se dělají releasy
* **Code Quality** - V Analytics -> CI/CD analytics lze najít úspěšnost pipelines v procentech 
* **Team Dynamics** - V Analytics -> value stream lze najít:
	* Lead Time (čas od vytváření issue do jeho uzavření)
	* Cycle time (střední doba od prvního commitu do uzavření issue)
	* New issues (počet nových issue)
	* Deployment Frequency (Průměrný počet nasazení do výroby za den)
* **Project Health** 
	* V Analytics -> Repository lze najít počet commitl za den
	* V Analytics -> Issue lze najít počet nových issue za měsic
	* V Project information -> Members lze najít počet nových contributerů

### Legenda

* ✅ - existuje
* ❌ - neexistuje
* ❔ - nevím