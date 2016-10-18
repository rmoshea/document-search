#Import python modules to simplify operations
import requests
import re
import time
import urllib2 


#Repository where text files live
base_url = 'https://raw.githubusercontent.com/rmoshea/document-search/master/searchFiles/'


#Welcome message
print("\n----- Welcome to the search program Cerberus -----")


#Determine which method of search the user wants to execute
print("\nAvailable files to search: (1) french_armed_forces.txt (2) hitchhikers.txt (3) warp_drive.txt (4) gutenberg.txt")
user_search_file = raw_input("\n    <<< Identify which text file to use by entering 1, 2, 3 or 4: ")

#Confirm to the user what they selected
if user_search_file == "1":
	print "    >>> You selected the file: french_armed_forces.txt"
elif user_search_file == "2":
	print "    >>> You selected the file: hitchhikers.txt"
elif user_search_file == "3":
	print "    >>> You selected the file: warp_drive.txt"
elif user_search_file == "4":
	print "    >>> You selected the file: gutenberg.txt"
else:
	print "    >>> You failed to choose a valid text file option and are now stuck searching through the lyrics of Justin Bieber's song 'Baby'"


#Determine which term to search -- fixed quotation requirements issue by changing 'input' to 'raw_input'
user_search_value = raw_input("\n    <<< Enter a value or string to search for in that file: ")
print("    >>> You entered: " + user_search_value)


#Determine which method of search the user wants to execute
print("\nAvailable methods of search: (1) String Match (2) Regular Expressions (3) Indexed")
user_search_method = raw_input("\n    <<< Choose a method to begin the search enter 1, 2 or 3: ")


count = 0

start_time = time.time() #user inputs have been captured, starting timer

try:

#If user selects String Match as their search method
	if user_search_method == "1":
		print "    >>> You selected the String Match search method"

		# user selects first option, open and read french armed forces text
		if user_search_file == "1":
			#read file
			page = urllib2.urlopen(base_url + 'french_armed_forces.txt')
			content = page.readlines()
			page.close()

			#looking for patterns
			for line in content:
				line = line.strip().lower().split()
				for words in line:
					#print words
					if words.find(user_search_value.lower()) != -1:
						count += 1
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, count))

		# user selects second option, open and read hitch hikers text
		elif user_search_file == "2":
			#read file
			page = urllib2.urlopen(base_url + 'hitchhikers.txt')
			content = page.readlines()
			page.close()

			#looking for patterns
			for line in content:
				line = line.strip().lower().split()
				for words in line:
					#print words
					if words.find(user_search_value.lower()) != -1:
						count += 1
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, count))

		# user selects third option, open and read warp drive text
		elif user_search_file == "3":
			#read file
			page = urllib2.urlopen(base_url + 'warp_drive.txt')
			content = page.readlines()
			page.close()

			#looking for patterns
			for line in content:
				line = line.strip().lower().split()
				for words in line:
					#print words
					if words.find(user_search_value.lower()) != -1:
						count += 1
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, count))			

		# user selects fourth option, open and read warp drive text
		elif user_search_file == "4":
			#read file
			page = urllib2.urlopen(base_url + 'gutenberg.txt')
			content = page.readlines()
			page.close()

			#looking for patterns
			for line in content:
				line = line.strip().lower().split()
				for words in line:
					#print words
					if words.find(user_search_value.lower()) != -1:
						count += 1
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, count))

		# user fails to select a valid option, forced to search the bieber
		else:
			#read file
			page = urllib2.urlopen(base_url + 'justinbieber.txt')
			content = page.readlines()
			page.close()

			#looking for patterns
			for line in content:
				line = line.strip().lower().split()
				for words in line:
					#print words
					if words.find(user_search_value.lower()) != -1:
						count += 1
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, count))


#If user selects Regular Expressions as their search method
	elif user_search_method == "2":
		print "    >>> You selected the Regular Expressions search method"

		# user selects first option, open and read french armed forces text
		if user_search_file == "1":
			#read file
			page = urllib2.urlopen(base_url + 'french_armed_forces.txt')
			f = page.readlines()
			page.close()

			#looking for patterns
			words = sum(len(re.findall(user_search_value, w, re.M|re.I)) for w in f)
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, words))

		# user selects second option, open and read hitch hikers text
		elif user_search_file == "2":
			#read file
			page = urllib2.urlopen(base_url + 'hitchhikers.txt')
			f = page.readlines()
			page.close()

			#looking for patterns
			words = sum(len(re.findall(user_search_value, w, re.M|re.I)) for w in f)
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, words))

		# user selects third option, open and read warp drive text
		elif user_search_file == "3":
			#read file
			page = urllib2.urlopen(base_url + 'warp_drive.txt')
			f = page.readlines()
			page.close()

			#looking for patterns
			words = sum(len(re.findall(user_search_value, w, re.M|re.I)) for w in f)
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, words))	

		# user selects fourth option, open and read warp drive text
		elif user_search_file == "4":
			#read file
			page = urllib2.urlopen(base_url + 'gutenberg.txt')
			f = page.readlines()
			page.close()

			#looking for patterns
			words = sum(len(re.findall(user_search_value, w, re.M|re.I)) for w in f)
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, words))

		# user fails to select a valid option, forced to search the bieber
		else:
			#read file
			page = urllib2.urlopen(base_url + 'justinbieber.txt')
			f = page.readlines()
			page.close()

			#looking for patterns
			words = sum(len(re.findall(user_search_value, w, re.M|re.I)) for w in f)
			print("\n    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, words))


#If user selects Indexed as their search method -- not complete
	elif user_search_method == "3":
		print "    >>> You selected the Indexed search method"
		print("    >>> Your search value of '%s' appears %s times in this file" % (user_search_value, "n/a"))

#If user fails to follow directions and enters an invalid search method
	else:
		print("ERROR: You entered an invalid search method option. Please re-run the program and enter either option 1, 2 or 3")

#In case an exception/error is discovered 
except:
	print("An error occured please re-run the program")


print("\nIt took %s seconds to execute your search" % (time.time() - start_time))
print("\n---------------  program closing ---------------\n")