OSDN
====

OSDN (dříve SourceForge.JP) je webové kolaborativní vývojové prostředí pro open-source projekty. Poskytuje úložiště zdrojového kódu a webhostingové služby.

**Web:** https://osdn.net/ 

**Version control system:** CVS, Git, Hg, SVN,BZR

**Počet projektů:** > 55000 

**API:**

* [OSDN API](https://osdn.net/projects/osdn-codes/wiki/APIGuide) - API je v procesu vývoje

**Plusy:** 

* Existuje _PROJECT RANKING_ a _DEVELOPER RANKING_, kde se zobrazují "nej" projekty 

**Open source projekty:**

* [Software Map](https://osdn.net/softwaremap/trove_list.php)

## Struktura

**Počet živých projektů:** 

* cca 200 projektů se pravidelně aktualizují 1x za měsic
* cca 900 projektů se pravidelně aktualizují 1x za rok

### Issue tracking system

|Název|Existence|Poznámka|Odkaz|
|---|---|---|---|
|bug/feature/task/|✅||https://osdn.net/docs/TicketAdmin#h2-Ticket.20Type.20Manager |
|priority/severity|✅||https://osdn.net/projects/mingw/ticket/ |
|estimates|❌||
|planned/real deadline| ✅|due date u milestonů|https://osdn.net/docs/TicketAdmin#h2-Milestone.20Management |
|podúkoly/related issues|❌||
|spárování commitů|❌||
|historie změn issue vč. people assignment|✅|Ticket History|
|vlastní kategorie/štítky|✅|Componenty|https://osdn.net/docs/TicketAdmin#h2-Component.20Manager |
|konfigurace stavů/workflow|❌|||
|iterace/fáze/milestones/releases|✅|milestones|https://osdn.net/docs/TicketAdmin#h2-Milestone.20Management |
|role nebo jiné charakteristiky lidí|✅|Admin/Developer/Moderator/..|https://osdn.net/docs/Manage_Developers |

### Version management system

|Název|Existence|Poznámka|
|---|---|---|
|git flow|✅||
|kompletní historie větví|✅||
|named tags|✅|https://osdn.net/projects/mingw/scm/git/mingw-org-wsl/|
|statistiky na commitech a lidech|❔||
|metriky na kódu/commitech|❔||
|merge requests (v historii dohledatelné)|❔✅|https://osdn.net/docs/TicketAdmin#h2-Ticket.20Type.20Manager|
|code review (v historii dohledatelné)|❔||


### Projekty

|Název|Existence|Poznámka|Odkaz|
|---|---|---|---|
|počet přispěvatelů|✅||https://osdn.net/projects/mingw/devel/|
|commiterů|✅||https://osdn.net/projects/mingw/devel/|
|code size|❌||
|licence|✅|Hlavní stránka projektu - Software Map|
|ticket statistics|✅|priority, open time, milestone, owner|
|milestones statistics|✅|submit date, due date, open tickets, closed tickets, progress|
|downloads statistics|✅||https://osdn.net/projects/mingw/stats/?report=last_30&default=projectview |
|použité technologie|✅|System Requirements + programming lang|`https://osdn.net/projects/[Project Name]/releases/`|
|zdraví produktu z ci/cd pipeline|❌||

* `http://osdn.net/projects/[projectname]/stats/` - https://osdn.net/projects/mingw/stats/?report=last_30&default=projectview

### Nástroje

|Název|Existence|Poznámka|Odkaz|
|---|---|---|---|
|wiki|✅||https://osdn.net/docs/OSDN_Serviceshttps://osdn.net/docs/OSDN_Services|
|mailing list|✅||https://osdn.net/docs/OSDN_Services|
|ci/cd pipeline|❌||
|release hosting|✅|VHOST|https://osdn.net/docs/OSDN_Services|
|produktový web|✅||https://osdn.net/docs/OSDN_Services|
|fórum nebo Q&A|✅||https://osdn.net/docs/OSDN_Services|
|integrace s VCS a ITS|❔||

### Legenda

* ✅ - existuje
* ❌ - neexistuje
* ❔ - nevím