from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys

def make_tiny(url):
    request_url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': url})
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [url1] [url2] ...")
        sys.exit(1)
    
    for url in sys.argv[1:]:
        tinyurl = make_tiny(url)
        print(f"{url} -> {tinyurl}")

if __name__ == '__main__':
    main()
