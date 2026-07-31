# Gammapy Developer Meeting 
 * Friday, July 31, 2026, at 2 pm (CET) 
 * Gammapy Developer Meeting on Zoom (direct link on Slack) 
Attendees: 

# Agenda
## General information

### AI Agents & Coding Assistants

- Bruno  has been experimenting with Microsoft Copilot's "agent" (Quentin clarified it's more an in-Copilot assistant than a standalone agent) using GammaPy-specific skills developed by CTAO. Open question raised: should this be tested more broadly during the Science Data Challenge (SDC), with feedback collected afterward? Considered possibly premature.
- Sharing the assistant across the collaboration currently requires adding users one by one; no known bulk-sharing option yet.
- Bruno cautioned against long-term planning around LLM tooling, given how fast models evolve; advocated a pragmatic, iterative approach rather than committing to a fixed roadmap.
- Bruno reported the agent gave an incorrect/fabricated documentation link when asked for a specific class reference — an example of unreliable behavior to keep in mind.
  - Quentin suggested adding a "stable" label to API documentation links for clarity.
- Dimitri K has independently built a  GammaPy-specific skill and has been testing them with agents. Régis proposed inviting him to present this work, tentatively in September.
  
### Science Data Challenge (SDC) — Fabio 
- Team is finalizing metadata fixes to comply with the CTAO data model (keywords proposed by Carl); no major blockers reported.
- Once metadata definitions are finalized, full simulations (North and South, 7-year schedule, including moon schedule) are expected to start around the beginning of next week.
- New IRFs for North and South sites have been received.

### Contribution Guidelines & AI-Generated PRs
- Discussion of an external contributor (unaffiliated with the field) attempting a complex, likely low-value PR (spectrum dataset serialization) based on an AI assessment that it was "easy" — deemed not a good approach by Atreyee.
- Concern that as more outside contributors use AI tools to find and propose issues, GammaPy needs clearer contribution guidelines to prevent unsolicited/unsuitable PRs.
- Decisions/action items:
  - Atreyee will finish and merge the Plotter PIG, then open beginner-friendly sub-issues, using a "good first issue" style label.
  - Consider updating contribution guidelines to require new/outside contributors to only work on issues explicitly marked beginner-friendly, and to express interest before starting work.
  - Discussed (inconclusively) whether a label or issue-text flag could discourage AI agents from picking up certain issues; Quentin noted this is unreliable since agents may not respect such conventions, though it might help agents identify beginner-friendly issues positively.
  - Atreyee will open a PR to remove overly broad "all contributions welcome" language from the README/landing page, redirecting readers to the contribution guidelines first.

## [Open issues](https://github.com/gammapy/gammapy/issues)

## [Bugs](https://github.com/orgs/gammapy/projects/36)

## [Documentation](https://github.com/orgs/gammapy/projects/27/views/2)

## [DevOps](https://github.com/orgs/gammapy/projects/31/views/1)

### CI / Infrastructure
- The weekly notebook-checking CI is currently broken due to a known bug involving regions handling.
- The nightly wheel build has been failing consistently for over a week.
  - Root cause: an upstream change in OpenAstronomy's packaging pipelines (dependency/version pinning mismatch).
  - A fix (PR #410) has reportedly been merged upstream, but it's unclear why the GammaPy CI is still failing.
  - Action item (Daniel): investigate whether GammaPy's CI needs to point to a newer commit/tag of the OpenAstronomy workflow, and follow up.

## Validation & benchmark

## Ongoing projects

### Fixed Pointing (Target: before 2.2)
- Tomas Bylund will attempt to complete the fixed-pointing fix and related function updates before the 2.2 release (currently targeted for end of October, possibly slipping toward November). Mainly involves reshuffling/deduplicating functions. Also relevant for future support of non-symmetric IRFs.

### Unbinned Likelihood Analysis
- Status: unclear/blocked.
- Tomas reported ~5 existing prototype implementations (including one from Guillaume and earlier ones inherited from previous contributors), each failing differently and inconsistently, with no clear criteria for which is "least wrong."
- Bruno and Atreyee pushed for more rigor: a documented page describing test cases, design decisions, what's wanted/not wanted, and current implementation status, plus more regular dedicated meetings on this topic.
- Decision: Not in scope for 2.2. Régis asked Tomas to prepare a status summary by end of September to inform a clearer roadmap for the next development cycle. Tomas is effectively working on this largely alone (earlier collaboration with has lapsed).
  
## Any other business

# Automatic activity report

### PRs opened last week (less than 8 days ago): 
* [#6799](https://github.com/gammapy/gammapy/pull/6799) Fix bug on JFactor nuisance.  - None
* [#6798](https://github.com/gammapy/gammapy/pull/6798) Minor fixes to documentation - Kirsty Feijen
* [#6796](https://github.com/gammapy/gammapy/pull/6796) Fix SVD convergence error in RegionGeom._rectangle_bbox - Tanishq Jain

### PRs merged last week (less than 8 days ago): 
* [#6801](https://github.com/gammapy/gammapy/pull/6801) Fix RegionGeom's ASDF roundtrip for DS9-format regions - Basmala Hekal
* [#6791](https://github.com/gammapy/gammapy/pull/6791) ASDF serialization for HpxNDMap class - Basmala Hekal

### issues opened last week (less than 8 days ago): 
* [#6800](https://github.com/gammapy/gammapy/issues/6800) ASDF serialization of Maps - Basmala Hekal
* [#6797](https://github.com/gammapy/gammapy/issues/6797) Add "validation" new section in optional dependencies in pyproject.toml - Daniel Morcuende
* [#6795](https://github.com/gammapy/gammapy/issues/6795) Enforce GADF specs when writing simulated DL3 files - Daniel Morcuende

 report created at 31/07/2026, 09:48:49
