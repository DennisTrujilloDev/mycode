#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
the requests library."""

# standard library imports go above 3rd party imports (best practice)
import re

# python3 -m pip install requests
import requests

def main():
    """Search a website's content"""
    
    while True:
        
        counter = 0 
        print("Where should we search?")
        url = input("> ").lower()  # collect user input

        print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
        searchFor = input("> ").lower()

        if url == 'q' or searchFor == 'q':
            break 

        resp = requests.get(url)  # Send HTTP GET
        searchMe = resp.text      # strip everything off the response as a string (text)

    # use the re.search() to determine if our website has the pattern we are looking for
    # it works by taking arguments, the first is the regex search pattern, and the second
    # is the string to search within
        for line in searchMe:
            if re.search(searchFor, searchMe):
                counter += 1

            else:
                print("No match!")

        print(f"found {counter} matches")
    #ISSUE: not quitting if url == q, only if searchFor is q
if __name__ == "__main__":
    main()

