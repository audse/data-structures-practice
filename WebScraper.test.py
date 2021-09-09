
from bs4 import Beautifulsoup
import requests

example_webpage = '''
<html>
<head>
    <title>Example Webpage</title>
</head>
<body>
    <div class="wrapper">
        <p>Content</p>
    </div>
</body>
</html>
'''

class Webpage:

    def __init__ ( self, url=None, html=None ):
        self.url = url if url else None
        self.html = html if html else requests.get(url).text
        self.soup = BeautifulSoup(self.html, 'html.parser')
    
    def get_title ( self ):
        return self.soup.title.string

my_webpage = Webpage( html=example_webpage )
reddit = Webpage( url='https://reddit.com' )

print ( my_webpage.get_title() )
print ( reddit.get_title() )