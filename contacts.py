#!/usr/bin/python3.5

# Johanna O'Day
# Physics 91SI Spring 2015
# Lab #12, Part 2

# Contacts list reader

import sys
import os
import re


def read_contacts(file):
	"""Reads contacts from the given file object, returning them as a list."""
	# Sample regex: replace this with your own
	# don't forget the raw string r prefix!
	regex = re.compile(r"(([A-Z]*[a-z]*){1}, ([A-Z]*[a-z]*)){1} (\([\w]+@{1}[\s\S]+\.[\w]+[\.[\s\S]]*\))")
	contacts = []	# Start an empty list

	for line in file:
		match = regex.match(line)
		# remember that match returns None if it doesn't match!
		if match:
			####
			# Your code goes here! (replace what's below)
			####
			person = match.groups()
			# c_dict = match.groupdict()
			contacts.append(person)
	contacts =sorted(contacts,key = lambda x:x[2],reverse=False)
	return contacts


def print_contacts(contacts):
	"""Prints contacts from a list, one per line."""
	# Pretty printing
	# See if you can figure out the formatting syntax from
	# the example below...
	for person in contacts:
		####
		# Your code goes here! (replace what's below)
		####
		last = person[1]
		first = person[2]
		email_long = person[3]
		email = email_long[1:len(email_long)-1]
		# This is Python's "string interpolation"
		# for C users, it's very similar to printf
		print ("%s %s" % (first, last) + ": " + (email))


def main():
	"""Read in contacts from a file, and print them to the terminal.
	Contacts are printed one per line, in the format:
	John Doe: username@domain.com

	Usage: python contacts.py filename"""

	filename = sys.argv[1]
	contacts_file = open(filename)

	# Read in contacts and print them, using above methods
	contacts = read_contacts(contacts_file)
	print_contacts(contacts)

	contacts_file.close()


if __name__ == '__main__':
	main()
