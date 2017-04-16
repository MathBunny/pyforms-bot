# pyforms-bot
### Developed by: Horatiu Lazu

## Features:
* Minimal dependencies
* Executes quickly and low CPU usage
* Very simple code
* Comes with several pre-made methods for loops and string options

## Instructions on making it work:
1. Get the pre-filled URL from Google Forms (_Resources_, then _Get pre-filled URL_)
2. Change `viewform` to `formResponse` in the URL
3. After you have changed the URL, it should appear like this:
> https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/formResponse?entry.1919438111=TEXTONE&entry.1717334207=TEXTTWO

4. You can identify the number that appears under entry.x by inspecting element in the target form
5. Replace the text within the `TEXTONE` and `TEXTTWO` with your desired text, set this to the s variable
6. Call the appropriate methods, and you are done!
  * Note: You can use the `viewForm` to see the behavior of the form without submitting!

## Simple Demo:
```python
import urllib
s = 'https://docs.google.com/forms/d/14SKwIY6w_8CiQ8bnqKSkWP9bLdUw-9Iojd33EH4uqGQ/formResponse?entry.1919438111=Hello&entry.1717334207=Hi'
def ping():
	getSite = urllib.urlopen(s)
for x in range(0, 100):
	ping()
```

## Future Improvements:
* Ability to use arrays or read desired input from a text file and output to form

