[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/reading-6th-grade-level.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/ages-12.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-resentment.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/just-plain-nasty.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/gluten-free.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/fixed-bugs.svg)](https://forthebadge.com) 
## AnalyticalBlackLight (ABL)

*Ever see someone having fun, and you just think to yourself, "let's ruin they're day?"*

*No? What if they were ruining yours, and punched a hole in your window?*

ABL uses Google search interest through pytrends as a black light on student cheating during virtual testing.

### Why?
Normally, you could just manually download CSV spreadsheets on search keywords from Google Trends.
However with more and more keywords it becomes harder to manage. ABL streamlines this.

ABL handles downloading all of this trend data through pytrends, a Python implementation of Google's Trends API. It is then able to merge data from each request into a single spreadsheet and graph the result.

#### No like, why. Why are you such a nerd, why can't you be like everyone else.
If my percentile scores are going down I'm pulling everyone down with it.
What are you going to do about it? It's an issue for sure, you can't just sweep it under the rug and act like everything's ok. What, do I have to cheat now? To level the playing field?
Because that sort of behavior is suddenly okay?

You think leaving webcams on and having a "responsible adult" around is going to solve anything? Can you not just, wait, 4 months? 

What kind of narrow minded b-

#### All jokes aside, what can I use this for, besides finding cheating?
Well, feel free to edit the keywords the list. Replace it with anything you want, so long the number of keywords is a multiple of five.
Want to know how many people are freaking out over the election in New York? 
Or how panicked the Aussies are as they watch their continent burn?
Maybe you want to know trending foods in California, to get away from all of this end-of-the-world nonsense?
Analyze away. As long as Google has the data, you can retrieve it. 

Do note however, the rest of the documentation was written in the context of student cheating.
Not sure if that was a mistake. 

### Ok, fine. How do I use this.
Oh perfect.

#### Download and Extract
Download the latest release on the repository page, and extract contents

#### Install Python Dependencies
Install Python and packages listed in requirements.txt through PIP.

#### Keywords
ABL is prepackaged with a list of keywords.
These may or may not be relevant to you. Please go through them, and change as needed. 

#### Arguments
ABL can be used as a command-line tool. It takes in 5 positional parameters in time and space, 1 input parameter, and 3 output parameters.

The three output parameters are ``--csv``, ``--showgraph`` and ``--graph`` which you need to add a 0 or 1 after the parameter to toggle. 
As their names suggest, they signal whether ABL should export a CSV file or a graph. Or both. ``--graph`` exports the graph to a .PNG file, while ``--showgraph`` uses the built-in viewer.

If you wish to forgo writing positional parameters, you can toggle ``-c`` with a 1 or 0 to read from targets.cfg instead.

The two start and end dates, being ``-s`` and ``-e`` are the range which data is collected from. Please have a reasonable cutoff, I doubt a testing service made this year will have any references in 2004.
If you use your brain, you might even be able to shave a few seconds out of processing time.
Please format these as YYYY-MM-DD

The three remaining parameters are country, state, and county. In command-line, not using targets.cfg, they are ``-n -p -x``, in the same order.
County or ``-x`` is a bit of a... weird... parameter. Google has integer codes for counties, in Google Trends at least. For example, NYC is 501. Houston in Texas is 618. You'll need to do a bit of digging.
Why is this useful? I hope it's obvious: because unless your school system has branches in Alaska or Shanghai, you probably can narrow it down a bit to your school district, right?

#### GUI
ABL additionally can be ran with a GUI, by running script gui.py.
The GUI version has entry boxes and a dropdown menu for selecting parameters, that are all labelled. 
After selecting your export type, and entering start and end date, country, state, and county, press process. A dialogue will show up, notifying you that the task has been issued.
In Windows, ABL will show up as not responding for a few seconds. This will be longer or shorter depending on the number of keywords you are processing, and your export type.

Another dialogue will appear to inform you that processing is complete. Check software directory for exported file if you ran CSV or graph export.

#### Analysis
I think this should be fairly obvious. You highlight the time of the testing session, and you check if search interest is higher than normal. 
If you have trouble dealing with raw spreadsheets, consider graphing instead.

### That's it?
Yes. That's it.

#### This is a glorified CSV data manager, designed for collecting specific pieces of information.
Mhm. No one said making specialized tools was a bad thing.

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
