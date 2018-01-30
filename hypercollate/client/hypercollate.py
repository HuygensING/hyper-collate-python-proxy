from urllib.parse import urljoin

import requests

from hypercollate.client.about_endpoint import AboutEndpoint
from hypercollate.client.collations_endpoint import CollationsEndpoint


class HyperCollate:
    def __init__(self, server_url):
        self.server_url = self.normalized_server(server_url)
        self.session = requests.Session()
        self.about = AboutEndpoint(self)
        self.collations = CollationsEndpoint(self)

    @staticmethod
    def normalized_server(server_url):
        return server_url if server_url.endswith('/') else server_url + '/'

    def get(self, uri):
        url = urljoin(self.server_url, uri)
        r = self.session.get(url=url)
        r.raise_for_status()
        return r

    def put(self, uri, data):
        url = urljoin(self.server_url, uri)
        r = self.session.put(url=url, json=data)
        r.raise_for_status()
        return r

    def put_data(self, uri, data, content_type='text/plain'):
        url = urljoin(self.server_url, uri)
        current_content_type = self.session.headers.get('content-type')
        self.session.headers['content-type'] = content_type
        r = self.session.put(url=url, data=data)
        self.session.headers['content-type'] = current_content_type
        r.raise_for_status()
        return r

    def post(self, uri, json):
        url = urljoin(self.server_url, uri)
        r = self.session.post(url=url, json=json)
        r.raise_for_status()
        return r

    def post_data(self, uri, data, content_type='text/plain'):
        url = urljoin(self.server_url, uri)
        current_content_type = self.session.headers.get('content-type')
        self.session.headers['content-type'] = content_type
        r = self.session.post(url=url, data=data)
        self.session.headers['content-type'] = current_content_type
        r.raise_for_status()
        return r

    def delete(self, uri):
        r = self.session.delete(url=urljoin(self.server_url, uri))
        r.raise_for_status()
        return r
