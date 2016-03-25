import urllib
#https://docs.google.com/forms/d/1lgpSjcJAZGbxu5OiWXJbqFp8DYoKd1sFMZGrbtSySoY/viewform
#https://docs.google.com/forms/d/1ApwQXMpswgsnt5In4Ttt5W1w1iX0Ku7W3yGMa0FMfB8/viewform
s = 'https://docs.google.com/forms/d/1ApwQXMpswgsnt5In4Ttt5W1w1iX0Ku7W3yGMa0FMfB8/formResponse?entry.1919438111=Hello&entry.1717334207=Hi'

def ping():
	getSite = urllib.urlopen(s)

def loop(N):
	for x in range(0, N):
		ping()

loop(100)