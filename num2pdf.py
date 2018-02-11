#!/usr/bin/env python

"""
converts .numbers to .pdf using cloudconvert
"""

import cloudconvert
import os,sys

API_KEY = "YOUR_API_KEY_HERE"

def api_get_routine(path):
	try:
		files = os.listdir(path)
	except:
		print "path: "+path+" is invalid :("
		return

	api = cloudconvert.Api(API_KEY)

	for name in files:
	    if ".numbers" in name:
			print("\n--------------------------------------------------\nprocessing: "+name)
			process = api.convert({
			    "inputformat": "numbers",
			    "outputformat": "pdf",
			    "input": "upload",
			    "file": open(os.path.join(path,name), 'rb')
			})
			print "    + "+process['message']
			process.wait()
			print "    + "+process['message']
			try:
				process.download(path)
			except: 
				print "downloading failed >:("
			print "    + converted "+name+"-->"+name[0:-8]+".pdf"
	print("\n==================================================\n    complete!")

def main():
	path = ""
	if len(sys.argv) < 2:
		print("too few arguments, supply a path like `.` or `/my/directory`. Pass -h for help.")
		return
	if len(sys.argv) == 2:
	    path = sys.argv[1]
	if(path=="-h"):
		print "This program uses cloudconvert to convert a .numbers file to .pdf.\nYou will need to supply your own API key, which can be sourced from cloudconvert.\nEdit the API_KEY variable with your api key."
	else:
		api_get_routine(path)

main()
