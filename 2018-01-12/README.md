# Gammapy Telcon

* Friday, January 12, 2018 at 11 am
* CTA eZuce, password "gammapyregular".  The connection details are [here](ConnectionDetails.txt)

# Agenda

* Updates
  * We've started to organise the Gammapy project and team, see http://gammapy.org/team.html .
    Defined coordination committee, project manager and lead developer roles and responsibilities.
    Plan to define more roles and responsibilities in the Gammapy team (e.g. sub-package maintainers)
    at the F2F meeting in Paris.
  * Gammapy documentation moved from ReadTheDocs to Github Pages.
    Now here: http://docs.gammapy.org/dev/, http://docs.gammapy.org/stable/
    Some more work to do, see [GH 1241](https://github.com/gammapy/gammapy/issues/1241#issuecomment-356444740)
  * Now that we have gammapy.org, we're doing some re-organisation of docs.gammapy.org ,
    e.g. remove the "news" section there and the "about" page.
  * We introduced a good process to plan and discuss changes for Gammapy.
    "Proposals for improvement of Gammapy (PIGs)"
    See discussion in [GH 1239](https://github.com/gammapy/gammapy/pull/1239)
    and result in  [PIG 1](http://docs.gammapy.org/dev/development/pigs/)
  * Gammapy CLI changed to a single multi-command "gammapy", implemented using click in ``gammapy.scripts``.
    Done in [GH 1240](https://github.com/gammapy/gammapy/pull/1240).
    See [gammapy.scripts docs page](http://docs.gammapy.org/dev/scripts/index.html) for information what
    we have, as well as some thoughts on what we could do for CLI or high-level interface in Gammapy in
    the future. See the sections on [limitations](http://docs.gammapy.org/dev/scripts/index.html#limitations)
    and [plan](http://docs.gammapy.org/dev/scripts/index.html#plan). What do we want?
    Feel free to give feedback today in the call, or any time later. Probably we should spend quite some
    time to discuss overall code organisation and this question of high-level interface extensively at the
    upcoming coding sprint, and then write down a detailed proposal as a PIG and then implement it in the
    coming months?
  * Work is now starting on new code to make maps (i.e. images & cubes) by Regis,
    and for modeling by Christoph (started writing a PIG, coding will start next week).
    We hope to have something already implemented and usable by the time of the upcoming coding sprint.
    If you're interested in this, contribute in the PIG discussion or review of pull requests by
    Regis & me in the coming weeks.
* Up next
  * Next Gammapy regular call in 2 weeks, on Jan 26, see [here](../2018-01-26)
    Contributions welcome! We will also discuss and prepare the coding sprint in that call.
  * Gammapy coding sprint in Paris Feb 5-9, see [here](../2018-02-05).
    If you can come, please sign up!
* Short tutorial: Python command line interfaces (CLIs) with click (Christoph)
  * In Gammapy, we now have a single multi-command "gammapy" with sub-commands like "gammapy info",
    implemented using Click in ``gammapy.scripts`` (see [here](http://docs.gammapy.org/dev/scripts/index.html))
  * I thought I'd talk for 5 minutes about this, in case some of you are interested to write their
    own CLIs in Python, or even contribute to the Gammapy CLI (by wrapping more functionality).
  * If you've never written a CLI in Python, here's a nice series of tutorials:
    [sys.argv](https://dbader.org/blog/how-to-make-command-line-commands-with-python),
    [click intro](https://dbader.org/blog/python-commandline-tools-with-click),
    [click advanced](https://dbader.org/blog/mastering-click-advanced-python-command-line-apps)
    (refresh the page or click the grey "X" in the top right to get rid of the email sign-up notification)
  * Before choosing click for Gammapy, Axel and I did look at argparse and cliff as well.
    Let's look at the simple examples at [python-cli-examples](https://github.com/cdeil/python-cli-examples/)
  * To briefly explain what we have in Gammapy, see [here](http://docs.gammapy.org/dev/scripts/index.html#implementation).
  * Any questions about Python CLIs generally or click specifically?
  * Any comments on what you'd like to have as high-level user interface for Gammapy?
    Would you use a Gammapy CLI or are you happy to write Python scripts and think implementing it is a waste of time?
* Discussion (all)
  * Anyone wants to present next week?
  * Anything else?

## Reminder

* Gammapy docs: http://docs.gammapy.org
* Gammapy webpage: http://gammapy.org/
* Gammapy development: github.com/gammapy/gammapy

Next Gammapy meetings: http://gammapy.org/news.html

See http://gammapy.org/contact.html for contact info, e.g. mailing list
for announcements or questions, Slack for help or to join development, ...
