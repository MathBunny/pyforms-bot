import urllib
from random import randint

#example URL: https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/formResponse?entry.1919438111=Hello&entry.1717334207=Hi
base = "https://docs.google.com/forms/d/"
formID = 0
s = ""


def ping():
	site = urllib.urlopen(s)
	
#This method for loops from [0, N) 
def quick(N):
	for x in range(0, N):
		lol = urllib.urlopen(s)
		print "Done: ",
		print x



for x in range (0, 10000):
	random = randint(0,1000000)
	cmd = 'formResponse?entry.1025952146=MrsGugoiu&entry.677539646='
	cmd = cmd + str(random)
	ping ('https://docs.google.com/forms/d/1lgpSjcJAZGbxu5OiWXJbqFp8DYoKd1sFMZGrbtSySoY/)' + cmd)
	print "Done: ",
	print x

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