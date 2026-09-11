# Gammapy Developer Meeting 
 * Friday, September 11, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 

Attendees: 

# Agenda
## General information

### Working sessions / F2F meetings
- Two possible windows identified for a partial-team working session, likely in Paris/France:
   - November 9–10, right after the CADS school
   - December 2–4, after the CTA France meeting
- Decision: Régis will circulate a poll in the dev Slack channel today to gauge availability for each slot.
- Open: exact dates/venue, and which topic(s) to assign to each session — likely depends on 2.2 release status (see §2 and §13).

### CDR/PDR preparation (CTAO review)
- Matthias: the PDR will likely slip past December (no firm new date given), which gives more prep time for documentation but work should not be delayed on that account.
- A draft document mapping CTAO's top-down science cases to analysis use cases is being prepared (already circulated in a small circle); the plan is to link it to what Gammapy/SDC already covers (benchmarks, notebooks, tutorials) to demonstrate coverage. This mapping exercise will support not just the PDR but also the CDR.
- Still needed: technical-side documentation (how to use SAT/Gammapy in an automated pipeline), and input on IRF systematics.
- Decision: no final call yet on whether to align the first working session with the SAT/2.2 release prep or push to the December slot — depends on 2.2 progress.

### IRF systematics
- Atreyee asked for clarification of scope (IRF systematics specifically); acknowledged as a recurring topic without prior conclusion.
- Matthias: CTAO's DPPS work package (preparing DL3/IRF production pipelines) needs to be consulted; current IRF requirement/systematics documentation is insufficiently detailed on the CTAO side. Some discussion has already started involving Régis and Bruno.
- Decision: Régis proposed setting a fixed date (~early October, options Oct 2 or Oct 9) for an internal Gammapy-team discussion first, before broadening to CTAO/DPPS participants.
- [ ] Action:  propose a date; team to reflect on the topic beforehand (Régis).

### User call
- Atreyee: ~5 responses so far to the availability poll; proposed Tuesday the 29th, 2–3pm Paris time.
- Decision: Régis agreed with the proposed slot.
- [ ] Action: close the poll and send the announcement early next week (Atreyee).

### 2.2 release / roadmap status
- Atreyee asked about the hard deadline for 2.2 from the CTAO side.
- Régis: unclear/possibly slipping; the target date (~October 2) is very likely no longer realistic given remaining work; more clarity expected after next week's SDC workshop.
- Decision: aim for an early-October checkpoint to review roadmap status and reprioritize/postpone lower-priority backlog items
- Documentation discussion:
  - Bruno: unclear whether much documentation work remains for 2.2;  CTAO user documentation also unclear (partly expected to be driven by the Bologna group).
  - Bruno proposed using the user call to solicit community feedback on documentation gaps.
  - Decision: prioritize finishing/fixing existing documentation issues over new feature requests for 2.2, since there are currently no urgent pending feature requests in the backlog/Slack. Prepare a survey for documebtation feedback?
- Reminder: everyone to check their individually assigned issues in the 2.2 roadmap, as some items may already be further along (or finished) than tracked.

## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

## Validation & benchmark

## Ongoing projects

### ASDF serialization (GSoC)
- Kirsty: Basmala is in phase 4 of GSoC with one week remaining. The IRF-related ASDF PR is merged; work is now moving to models and datasets, with a PR expected today or early next week.
- Régis: a working prototype already exists for models and various dataset combinations; the hardest corner cases are handled. Standardization of analysis products into ASDF is expected to be usable by end of next week.
- Decision: none pending — work continues as planned.

### BasePlotter / plotting refactor
- Context: possible new contributors to gammapy; the plan is to prepare well-separated, beginner-friendly PRs.
- Régis presented the BasePlotter PR: it validates plot configuration by converting it into matplotlib rcParams (invalid keys/values raise errors); tests confirm instantiating a plotter doesn't leak into global matplotlib rcParams. Subclasses are defined by setting default parameters and implementing a plot function.
- Decision: keep the new Plotter-based code fully separate from the existing plot() methods for now (no mixing mid-transition); replace old plot calls with proper plotters at a later step.
- Decision: first suggested "good first issues" are IRF plotters (self-contained, easy) and Map; dataset/model plotters are deferred as more complex (fit/sky-model interplay).
- Decision: update the "Get in touch" page on the Gammapy website to require applicants for Slack to explain their background/motivation regarding Gammapy.

### Dark Matter
- Alex reports that Daniel is following up to schedule the Gammapy Dark Matter call; date/time TBD, to be announced on Slack (DM channel and/or dev channel).
- PR #6774 (full DM tutorial): updated per Quentin's feedback (simplified to use existing Gammapy functions instead of custom procedures) — ready for re-review.
- Issue #6828 ("Handle JFactor Central Pixel"): open problem — an odd number of pixels gives an incorrect central value. Discussion ongoing on a dynamic pixel-grid approach vs. a fixed value, trading off computational cost against accuracy (comparison with CLUMPY conventions suggested). Still open; relevant contributor (Julia) not present this week.
- Issue #6724 (heavy dark-matter spectra, e.g. cosmic-ray/PPPC-type tables): Shruti is working on it and a PR is expected soon.
- Benchmark issue #6820: Alex asked for clarification on requirements. Benchmarks should track reproducibility of well-established results (e.g. PPPC tables) via scripts callable in CI, comparing outputs across Gammapy versions and ideally against a published reference (similar in spirit to the existing AGN light-curve or Crab validation). No strict tolerance assertion is required a priori — consistency across versions is the main goal.

## Any other business

- Bruno: the APC multi-wavelength team flagged a possible issue with EBL/gamma-ray absorption in the multi-wavelength spectral fitting code; they will investigate further and open an issue if confirmed.
- Status of Unbinned likelihood analysis long-standing PIG.
  - Decision: Régis proposed closing it, as it isn't progressing in its current form. No objections raised.
- Pre-computed simulated datasets in gammapy-data (PR #6320)
  - Kirsty: this PR would load pre-computed simulated datasets from gammapy-data instead of regenerating them each time, reducing code duplication. Work paused because full benefit requires several distinct simulated datasets, not just one.
  - Open: whether to continue down this path — Kirsty asked others to review the PR and comment with opinions.

## Action items
[ ] Circulate Slack poll for Nov 9–10 / Dec 2–4 working-session availability	(Régis)
- [ ] Fix a date (Oct 2 or Oct 9) for internal team discussion on IRF systematics	(Régis)	
- [ ] Close user-call poll and send announcement (proposed: Tue 29th, 2–3pm Paris)	(Atreyee)
- [ ] Restore removed deprecated catalogue file to fix CI 	
- [ ] Open issue on catalog download strategy (on-demand, hosting, supported list)	(Atreyee)
- [ ] Draft list of "good first issues" for Plotter refactor (start: IRF, Map)	
- [ ] Open issue on deriving radial acceptance from exclusion region (early science)	Bruno	
- [ ] Open issue on making the Asimov dataset public + share tutorial notebook	
- [ ] Close unbinned-likelihood PIG	Régis	To do (no objections)
- [ ] Review/comment on PR #6320 (pre-computed simulated datasets)	Team	Open — awaiting input
- [ ] Review PR #6774 (DM full tutorial, updated)	Atreyee / reviewers	Ready for review
- [ ] Full 2.2 roadmap review to reprioritize backlog (early October)	Régis / Team	Planned
- [ ] Check individually assigned 2.2 roadmap issues	All	Ongoing
 
# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6845](https://github.com/gammapy/gammapy/pull/6845) Introduce BasePlotter class - Régis Terrier
* [#6838](https://github.com/gammapy/gammapy/pull/6838) [catalogs] Add Fourth Fermi-LAT Catalog of High-Energy Sources (4FHL) - Michele Peresano

### PRs merged last week (less than 8 days ago): 
* [#6833](https://github.com/gammapy/gammapy/pull/6833)  ASDF: serialization for IRFMap classes - Basmala Hekal

### issues opened last week (less than 8 days ago): 
* [#6844](https://github.com/gammapy/gammapy/issues/6844) Insert the GRB LAT calatog - Bruno Khélifi
* [#6843](https://github.com/gammapy/gammapy/issues/6843) Insert the Fourth LAT AGN Catalog - Bruno Khélifi
* [#6842](https://github.com/gammapy/gammapy/issues/6842) ASDF serialization for Datasets container - Basmala Hekal
* [#6841](https://github.com/gammapy/gammapy/issues/6841) ASDF serialization for FluxPointsDataset - Basmala Hekal
* [#6840](https://github.com/gammapy/gammapy/issues/6840) ASDF serialization for FluxPoints - Basmala Hekal
* [#6839](https://github.com/gammapy/gammapy/issues/6839) Clarification of the docstring note in ExcessMapEstimator - Fabio Acero

 report created at 11/09/2026, 12:07:31
