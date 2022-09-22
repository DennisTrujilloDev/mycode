#!/usr/bin/env python3
"""This app asks the user about their name and what day of the week it is then prints their answers"""
def main():
    user_name = input("what's your name?")
    week_day = input("what day of the week is it?")
#the two variables above are assigned the values of 
#whatever the user inputs following the two questions
#wrapped in quotes 
    print(f"Hello, {user_name}! Happy {week_day}!")
main()
