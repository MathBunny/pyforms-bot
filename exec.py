import urllib
import urllib2

def ping(s):
	lol = urllib.urlopen(s)
	

def quick():
	for x in range(0, 100):
		lol = urllib.urlopen('https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/formResponse?entry.1919438111=Hello&entry.1717334207=Hi')
		print "Done: ",
		print x

quick()
print "Done!"	

'''
values = {'lol', 'sup'}

response = urllib2.urlopen('https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/viewform')

for x in range(0, 100):
	lol = urllib2.urlopen('https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/formResponse?entry.1919438111=Hello&entry.1717334207=Hi')
#https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/formResponse?entry.1919438111=Hello&entry.1717334207=Hi

test = urllib2.urlopen("http://jdcc.ca")
htmlJDCC = test.read()

html = response.read()
the_page = response.read()
print html

%https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/viewform?entry.1919438111=Hello&entry.1717334207=Hi
%https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/formResponse?entry.1919438111=Hello&entry.1717334207=Hi
'''