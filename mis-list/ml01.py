#!/usr/bin/env python3
"""Creates a list and displays the elements in three separate strings"""

def main():
    #this is a list of three elements 
    my_list = [ "192.168.0.5", 5060, "UP" ]

    #display the first item in the list
    print("The first item in the list (IP): " + my_list[0] )

    #display the second item in the list
    print("The second item in the list (port): " + str(my_list[1]) )

    # display the third item in the list 
    print("The last item in the list (state): " + my_list[2] )
if __name__ == "__main__":
    main()

