import os
import requests
import urllib


class Downloader(object):
    def __init__(self, dirname, timeout=5.0):
        self.dirname = dirname
        self.timeout = timeout

    def client(self, paper):
        # For now, HTTPS is not supported
        query = paper['link'].replace('https', 'http')
        r = requests.get(query, stream=True, timeout=self.timeout)
        if r.status_code == 200:
            # Successful connection
            with open(os.path.join(self.dirname, paper['name']), 'wb') as f:
                f.write(r.content)
