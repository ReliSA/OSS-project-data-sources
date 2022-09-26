GitHub
======

**Web:** https://github.com/ 

**Version control system:** GIT

**Počet projektů:** [> 200 mil](https://github.com/about)

**API:**

* [CLI](https://cli.github.com/) - funkcionalita GitHubu v příkazové řádce

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
* [GitStats](http://gitstats.sourceforge.net/) - získání statistik (total files, lines, commits, commits by hour of day) z projektů.

**Open source projekty:**

* [Awesome Open Source](https://awesomeopensource.com/) 
* [GitHUb Trending repos](https://github.com/trending)

## Struktura

**Počet živých projektů:** hodně

### Issue tracking system

|Název|Existence|Poznámka|Odkaz|
|---|---|---|---|
|bug/feature/task/|✅|řešení přes labely|https://softwareengineering.stackexchange.com/questions/129714/how-to-manage-github-issues-for-priority-etc|
|priority/severity|✅|řešení přes labely|https://softwareengineering.stackexchange.com/questions/129714/how-to-manage-github-issues-for-priority-etc|
|estimates|❌|
|planned/real deadline|✅|Milestones due date|https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones|
|podúkoly/related issues|✅|markdown checklist pod issue/[milestone/labels]|https://help.zenhub.com/support/solutions/articles/43000010341-an-intro-to-zenhub-epics|
|spárování commitů|✅||https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors|
|historie změn issue vč. people assignment|✅||https://docs.github.com/en/issues/tracking-your-work-with-issues/assigning-issues-and-pull-requests-to-other-github-users|
|vlastní kategorie/štítky|✅|topics | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics|
|konfigurace stavů/workflow|✅||https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions |
|iterace/fáze/milestones/releases|✅|Milestones, release|https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones|
|role nebo jiné charakteristiky lidí|✅|Read, Triage, Write, Maintain, Admin|https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/repository-roles-for-an-organization|

### Version management system

|Název|Existence|Poznámka|Odkaz|
|---|---|---|---|
|git flow|✅||https://docs.github.com/en/get-started/quickstart/github-flow |
|kompletní historie větví|✅|historie commitů||
|named tags|✅||https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags |
|statistiky na commitech a lidech|✅|externí programy + v project Insights (contributor-počet commitů)|http://gitstats.sourceforge.net/examples/git/activity.html, https://github.com/morucci/repoxplorer |
|metriky na kódu/commitech|✅||https://github.com/morucci/repoxplorer |
|merge requests (v historii dohledatelné)|✅||https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request|
|code review (v historii dohledatelné)|✅||https://github.com/features/code-review|


### Projekty

|Název|Existence|Poznámka|
|---|---|---|
|počet přispěvatelů|✅|lze najít na hlavní stránce projektu jako Contributors|
|commiterů|✅|lze najít v Insights -> Pulse|
|code size|✅|https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci|
|licence|✅|lze najít na hlavní stránce projektu|
|použité technologie|✅|lze najít na hlavní stránce projektu jako Languages|

* https://github.com/morucci/monocle
* https://github.com/morucci/repoxplorer

### Nástroje

|Název|Existence|Poznámka|
|---|---|---|
|wiki|✅||
|interní mailing list|❌||
|ci/cd pipeline|✅|https://resources.github.com/ci-cd/#examples|
|release hosting|✅|https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages|
|produktový web|✅|https://pages.github.com|
|fórum nebo Q&A|✅|https://docs.github.com/en/discussions|
|integrace s VCS a ITS|❔ |

### Metriky

* **Code Lifecycle** - lze zjistit jak často se dělají releasy
* **Code Quality** - v případě jestli projekt použiva labely na issues, tak lze spočítat poměr bugu a releasů
* **Team Dynamics** - v Insights je vidět kolik commitů se dělá týdně
* **Project Health** - v Insights je vidět kolik contributorů přidalo commitů

### Legenda

* ✅ - existuje
* ❌ - neexistuje
* ❔ - nevím