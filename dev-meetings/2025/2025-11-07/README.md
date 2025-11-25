# Gammapy Developer Meeting 
 * Friday, November 07, 2025, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: Régis Terrier (RT), Tomas Bylund (TB), Atreyee Sinha (AS), Fabio Pintore (FP), Katharina Egg (KE), Bruno Khélifi (BK), Kirsty Feijen (KF), Nathan Pigoux (NP), Fabio Acero (FA)

# Agenda
## General information

### CDAS 2025
Overall a success; one of the lecturers got sick and gave their lecture over zoom and people were very busy before the school so the notebooks for the hands on sessions were updated quite rushed and uncoordinated.

During the final question session we had questions both about the technical details on gammapy analysis, and also more conceptual questions about science and statistics methods.

For the advance session Quentin produces some really advanced notebooks. For example, during the advances session it was shown that it's possible to run the nested sampling with multiprocessing. 

Would be useful if some of these notebooks are converted to gammapy-recipes.

### Upper limits
FA asks about how gammapy does upper limits in the case of very small or even negative signal. Nobody is terribly sure exactly what the code does, but there is a consensus that gammapy conceptually only contains one method of finding upper limits: finding the maximum likelihood and then scanning until the likelihood decreases by a prescribed amount.

Further discussion reveals some disagreement about what the statistical theory really say. A need of a dedicated meeting is clear, and preferably with a real statistician present.

## [Open issues](https://github.com/gammapy/gammapy/issues)

FP has opened [#6211](https://github.com/gammapy/gammapy/pull/6211) to extend the functionality of `make_theta_squared_table` to cover a larger range of radial offsets.

## [Bugs](https://github.com/orgs/gammapy/projects/36)
No update

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)
No update

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)


## Validation & benchmark

## Ongoing projects

## Any other business

### Co-working days
Organise some day were we meet and work on determine the prioritisation of tasks, unrelated to the CTAO timeline, for the next release. Also to work on common topics together.

### [Plotters PIG](https://github.com/gammapy/gammapy/pull/5726/)
A draft for a new plotter interface exists but after discussion on the meeting it seem it still needs more work.

# Automatic activity report

### PRs opened last week (less than 8 days ago): 

### PRs merged last week (less than 8 days ago): 
* [#6210](https://github.com/gammapy/gammapy/pull/6210) Backport PR #6205 on branch v2.0.x (Apply codespell) - Lumberbot (aka Jack)
* [#6209](https://github.com/gammapy/gammapy/pull/6209) Backport PR #6207 on branch v2.0.x (Bump stefanzweifel/git-auto-commit-action from 6.0.1 to 7.0.0) - Lumberbot (aka Jack)
* [#6208](https://github.com/gammapy/gammapy/pull/6208) Backport PR #6206 on branch v2.0.x (Bump actions/upload-artifact from 4 to 5) - Lumberbot (aka Jack)
* [#6207](https://github.com/gammapy/gammapy/pull/6207) Bump stefanzweifel/git-auto-commit-action from 6.0.1 to 7.0.0 - None
* [#6206](https://github.com/gammapy/gammapy/pull/6206) Bump actions/upload-artifact from 4 to 5 - None
* [#6205](https://github.com/gammapy/gammapy/pull/6205) Apply codespell - Régis Terrier
* [#6203](https://github.com/gammapy/gammapy/pull/6203) Add __repr__ method to Geom - Tomas Bylund

### issues opened last week (less than 8 days ago): 

 report created at 07/11/2025, 07:24:12
