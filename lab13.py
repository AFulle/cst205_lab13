#CST 205 Lab 13: Lists
#Ahdia
#Yulian
#Lyndsay


### Only a test story, we can switch to something else
### make sure the underscores are a total of 7 underscores, it won't work otherwise.
story_with_blanks = """Amazon just unveiled a _______ store without lines or checkout counters. 
Amazon Go, a 1800-square-foot retail space located in the company's hometown of _______, 
lets shoppers just grab the items they want and leave; the order gets charged to their _______ account afterwards.

Amazon Go works by using computer _______ and _______ to detect what items you're taking out of the store. 
You start by scanning an _______ as you enter the Amazon Go shop. 
You do your normal shopping, and the _______ throughout the store identify the items in your cart and charge them to your account when you walk out the door. 
It'll feel like _______, except you're actually being _______ by more cameras than you can imagine.

The shop will stock most items you'd find in a local convenience store: _______, _______, premade _______ like _______ and _______, and grocery essentials like _______ and _______. 
It'll also sell Blue Apron-like meal kits that let you cook your own dinners for two.

On the consumer level, the benefits are obvious --- no waiting in line or fussing around with _______ machines. 
But for Amazon, the company could potentially track you and your phone as you browse the store to track items you buy. 
By looking at your _______ in the store as you shop, Amazon could _______ items you may have noticed or were potentially interested in _______. 
Combine this with your Amazon.com browsing activities and the company could gear up to serve even more recommended products wherever you're online.

Though Amazon Go does do away with _______ cashiers, we haven't seen anything about robots physically _______ the store, 
so while it does eliminate some jobs, it's not a completely automated _______... at least, not yet.

The store is currently open in beta to Amazon employees only. A public opening is scheduled for early _______.
"""

mad_libs = []
    
def madlib2():
    story = story_with_blanks
    while story.count("_______") > 0:
        word = requestString(story+"\n\nPlease enter the first blank you see:")
        list_of_words = [word]
        blank_count = story.count("_______")
        if len(list_of_words) < blank_count:
          for i in range(0, blank_count - len(list_of_words)):
             list_of_words = list_of_words + ["_______"]
        formatter_version = story.replace("_______", "%s")
        story = formatter_version % tuple(list_of_words)
    return story
    
showInformation(madlib2())