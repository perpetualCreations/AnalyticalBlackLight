[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/reading-6th-grade-level.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/ages-12.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-resentment.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/just-plain-nasty.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/gluten-free.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/fixed-bugs.svg)](https://forthebadge.com) 
## AnalyticalBlackLight (ABL)

*Ever see someone having fun, and you just think to yourself, "let's ruin they're day?"*

*No? What if they were ruining yours, and punched a hole in your window?*

ABL uses pytrends as a black light on student cheating during virtual testing.
It can export results through matplotlib and make a statistics graph you can annotate and discern information form.

ABL can be used for other keywords, feel free to edit the keywords.txt file to make your own set of keywords you want to collect bulk search interest data on.

### Why?
Normally, you could just manually download CSV spreadsheets on search keywords from Google Trends.
But more data is better data, using just 1 or 10 keywords as part of your data set is extremely small.

You need a lot more keywords, and that means more spreadsheets, and more merging those spreadsheets.
Have fun trying to manage 110+ keywords, and then using what little energy you have left making anything close to a neat graph.

ABL handles downloading all of this trend data through pytrends, a Python implementation of Google's Trends API. It is then able to merge data from each request into a single spreadsheet and graph the result.

#### No like, why. Why are you such a nerd, why can't you be like everyone else.
If my percentile scores are going down I'm pulling everyone down with it.
What are you going to do about it? It's an issue for sure, you can't just sweep it under the rug and act like everything's ok. What, do I have to cheat now? To level the playing field?
Because that sort of behavior is suddenly okay?

You think leaving webcams on and having a "responsible adult" around is going to solve anything? Can you not just, wait, 4 months? 

What kind of narrow minded b-

#### All jokes aside, what can I use this for, besides finding cheating?
Well, feel free to replace the keywords list with other things.
Want to know how many people are freaking out over the election in New York? 
Or how frantic the Australians are as air quality drops as fast as the number of natural habitats?  
Analyze away. The things you search, it can be anything you want, so long Google has data on it.

Do note however, the rest of the documentation was written in the context of student cheating.
Yeah. May or may not have been a mistake.

### Ok, fine. How do I use this.
Oh perfect. Ok so first thing you need to do is get a stress ball.
Hey. Look at me. Squeeze the stress ball if you're angry, ok?

#### Download and Extract
Download the latest release on the repository page, and extract contents

#### Install Python Dependencies
Install Python and packages listed in requirements.txt through PIP.

#### Arguments
ABL is a command-line tool. It takes in 5 positional parameters in time and space, 1 input parameter, and 2 output parameters.

The two output parameters are ``--csv`` and ``--graph`` which you need to add a 0 or 1 after the parameter to toggle. 
As their names suggest, they signal whether ABL should export a CSV file or a graph. Or both.

If you wish to forgo writing positional parameters, you can toggle ``-c`` with a 1 or 0 to read from targets.cfg instead.

The two start and end dates, being ``-s`` and ``-e`` are the range which data is collected from. Please have a reasonable cutoff, I doubt a testing service made this year will have any references in 2004.
If you use your brain, you might even be able to shave a few seconds out of processing time.
Please format these as YYYY-MM-DD

The three remaining parameters are country, state, and county. In command-line, not using targets.cfg, they are ``-n -p -x``, in the same order.
County or ``-x`` is a bit of a... weird... parameter. Google has integer codes for counties, in Google Trends at least. For example, NYC is 501. Houston in Texas is 618. You'll need to do a bit of digging.
Why is this useful? I hope it's obvious: because unless your school system has branches in Alaska or Shanghai, you probably can narrow it down a bit to your school district, right?

#### Graphs
Oh, you dare to actually pickup a pen and annotate a graph?
Good job. Pat yourself on the back.

Know the testing schedule?
During testing hours, look for spikes in keyword usage. 
If you find spikes where you drew marks for testing hours, ring the bell.

Because that's the blood on the wall, and if you can read it, it screams cheaters.

### That's it?
Yes. That's it.

#### This is a glorified CSV data manager, designed for collecting specific pieces of information.
Mhm.

#### I mean, this is pretty complicated. Any alternatives?
Well, you can see if:

- Top students are watching their placements drop from top 1% to 80%.
- Jumps in scores that are way above trend line (like the student struggling with arithmetic is suddenly burning through calculus).
- Jumps in scores without jumps in normal assignment grades.
- High accuracy and high skill on multiple choice question, with low accuracy and skill on open-ended writing questions.

Or of course you can also just:

- Wait literally 4 months.

That's it. 4 months. Please. Web cams don't do anything. I know people who have their eyes on the camera, but their fingers are playing competitive FPS.
You can't just "read" people either like some sort of psychic. 

#### Mainframe? Hackerman?
Look it's evolving! Just backwards!
