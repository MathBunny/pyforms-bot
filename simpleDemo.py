import urllib

s = 'https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/formResponse?entry.1919438111=Hello&entry.1717334207=Hi'

def ping():
	getSite = urllib.urlopen(s)
	
for x in range(0, 100):
	ping()