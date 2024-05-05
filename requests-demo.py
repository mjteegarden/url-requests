#  going to import from https://xkcd.com/353/

#  this import below brings the requests module into memory
import requests

#  this request below will pull the xkcd webcomic from the website using the URL
req = requests.get('https://imgs.xkcd.com/comics/python.png')

#  print(req)
# the above print gets the response of "<Response [200]>"
# the "200" response is from website URL.  An HTTP response status code 200 means success. The client has requested documents from the server. The server has replied to the client and given the client the documents.

#  print(dir(req))
# this prints the directory of options, methods, etc., from that website, for that request
''' ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 
'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
'''

#  print(req.text)
#  the above will print out the entire html text for the website.  I saved it as file for comparison.

# this text below is the image-only url for the comic
#  https://imgs.xkcd.com/comics/python.png

with open('xkcd_comic2.png', 'wb') as comic:
    comic.write(req.content)
#  the above 2 lines are a CONTENT MANAGER couplet.  the "with" ensures the file will be closed after its use is done
