# Imports
import requests

# !!!REQ!!! Program correctly searches the DuckDuckGo api for the search string (see test_ddg0)
# DuckDuckGo (DDG) API info
api_url  = "https://api.duckduckgo.com"
api_path = "/?q=presidents of the united states&format=json"

# List of Presidents
presidents = [
    "Washington",   "Adams",        "Jefferson",    "Madison",
    "Monroe",       "Jackson",      "Buren",        "Tyler",
    "Polk",         "Taylor",       "Fillmore",     "Pierce",
    "Buchanan",     "Lincoln",      "Grant",        "Hayes",
    "Garfield",     "Arthur",       "Cleveland",    "Harrison",
    "McKinley",     "Roosevelt",    "Taft",         "Wilson",
    "Harding",      "Coolidge",     "Hoover",       "Truman",
    "Eisenhower",   "Kennedy",      "Johnson",      "Nixon",
    "Ford",         "Carter",       "Reagan",       "Bush",
    "Clinton",      "Obama",        "Trump",        "Biden"
]

# Test
def test_ddg0():

    # Print first to make the output prettier
    print()

    # Query DDG API
    resp = requests.get(api_url + api_path) # !!!REQ!!! Program searches the DuckDuckGo api only once

    # Get RelatedTopics from
    resp_related_topics = resp.json()["RelatedTopics"]

    # Make Text string from RelatedTopics
    text = ""
    for i in resp_related_topics:
        text += i["Text"] + '\n'

    # Check to make sure all presidents
    #  are in the response
    error_count = 0
    for pres in presidents:  # !!!REQ!!! program tests that each president is present in the response
        if pres not in text:
            error_count += 1
        else:
            print(pres + " found!")

    assert error_count == 0