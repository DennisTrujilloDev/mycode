#!/usr/bin/env python3
"""creating lists and practice using methods on them"""
#created then printed two identical lists below 
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)

#appended (w.o iterating) the same element to both lists, then printed them  
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print("simple list", proto)

#defined a new list
proto2 = [ 22, 80, 443, 53 ] # a list of common ports

#extended (w/ iteration) proto with proto2
#each element was added to the end of the list
proto.extend(proto2) # pass proto2 as an argument to the extend method
print("with extend():", proto)
print ("proto count http", proto.count("http"))

#the whole of proto2 was appended (w/o iteration) to the end of the list 
protoa.append(proto2) # pass proto2 as an argument to the append method
print("with append():", protoa)

