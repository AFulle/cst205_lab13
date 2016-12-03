#CST 205 Lab 13: Lists
#Ahdia
#Yulian
#Lyndsay


### Only a test story, we can switch to something else
story_with_blanks = """
Airlines made history this summer when they launched the first scheduled commercial flights from the US to _______ in more than 50 years, part of the thaw in relations between the US and the _______.
It already looks like too much too soon.
American Airlines this week said it plans to trim the number of flights it offers to _______ from 13 a day to 10. Starting in mid-February, the airline will only operate one flight a day to _______ and _______ from Miami instead of two.
"""

mad_libs = []


def madlib():
    words = requestString("Using the story below, please enter the words you wish to use for every blank spot, seperated by commas. Example: jump, stop, George, banana. \n\n" + story_with_blanks)
    list_of_words = [word.strip() for word in words.split(",")]
    formatter_version = story_with_blanks.replace("_______", "%s")
    return formatter_version % tuple(list_of_words)

printNow(madlib())