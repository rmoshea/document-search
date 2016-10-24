#Import python modules to simplify operations
import requests
import re
import time


#Document or documents to be searched
filename = "justinbieber.txt"
filename1 = 'https://raw.githubusercontent.com/rmoshea/document-search/master/searchFiles/french_armed_forces.txt'
filename2 = 'https://raw.githubusercontent.com/rmoshea/document-search/master/searchFiles/hitchhikers.txt'
filename3 = 'https://raw.githubusercontent.com/rmoshea/document-search/master/searchFiles/warp_drive.txt'

#Welcome message
print("\n--- Welcome to the search program Cerberus ---")

#Determine which method of search the user wants to execute
print("\nAvailable files to search: (1) french_armed_forces.txt (2) hitchhickers.txt (3) warp_drive.txt")
user_search_file = raw_input("Identify which text file to use by entering 1, 2 or 3: ")

if user_search_file == "1":
	content = filename1
	print "\n>>> You selected the file: french_armed_forces.txt"
elif user_search_file == "2":
	content = filename2
	print "\n>>> You selected the file: hitchhickers.txt"
elif user_search_file == "3":
	content = filename3
	print "\n>>> You selected the file: warp_drive.txt"
else:
	content = filename
	print "\n>>> You failed to choose a valid text file option and are now stuck searching through the lyrics of Justin Bieber's song 'Baby'"

#Determine which term to search -- fixed quotation requirements issue by changing 'input' to 'raw_input'
user_search_value = raw_input("\nEnter a value or string to search for in that file: ")
print("\n>>> You entered: " + user_search_value)

#Determine which method of search the user wants to execute
print("\nAvailable methods of search: (1) String Match (2) Regular Expressions (3) Indexed")
user_search_method = raw_input("To begin the search enter 1, 2 or 3: ")


count = 0

start_time = time.time() #user inputs have been captured, starting timer

try:

#If user selects String Match as their search method
	if user_search_method == "1":
		print "\n>>> You selected the String Match search method"
		#read file
		f = open(filename, "r")
		lines = f.readlines()
		f.close()
		#looking for patterns
		for line in lines:
			line = line.strip().lower().split()
			for words in line:
				#print words
				if words.find(user_search_value.lower()) != -1:
					count += 1
		print(">>> Your search value of '%s' appears %s times in this file" % (user_search_value, count))

#If user selects Regular Expressions as their search method --- "re.M" to signify multiline; re.I" used to ignore case
	elif user_search_method == "2":
		print "\n>>> You selected the Regular Expressions search method"
		f = open(filename, 'r')
		words = sum(1 for w in f if re.findall(user_search_value, w, re.M|re.I))
		f.close()
		print(">>> Your search value of '%s' appears %s times in this file" % (user_search_value, words))

#If user selects Indexed as their search method -- not complete
	elif user_search_method == "3":
		print "\n>>> You selected the Indexed search method"
		print(">>> Your search value of '%s' appears %s times in this file" % (user_search_value, "n/a"))

#If user fails to follow directions and enters an invalid search method
	else:
		print("You have entered an invalid option. Please re-run the program and enter either option 1, 2 or 3")

#In case an exception/error is discovered 
except:
	print("An error occured please re-run the program")


print("\nit took %s seconds to execute your search" % (time.time() - start_time))
print("\n---  program closing ---\n")