# coding: utf-8

"""
   Copyright 2018 Huygens ING

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from urllib.parse import urljoin

from IPython.core.display import display, HTML
from IPython.lib.display import IFrame

from hypercollate.client import util
from hypercollate.client.hypercollate import HyperCollate


class CollationProxy:
    def __init__(self, collation_id: str, hypercollate: HyperCollate):
        self.collation_id = collation_id
        self.collations = hypercollate.collations
        self.base_uri = util.endpoint_uri(hypercollate.server_url[:-1], hypercollate.collations.endpoint, collation_id)

    def __str__(self):
        return "CollationProxy::" + self.collation_id

    def __dir__(self):
        return ['get_info', 'add_witness_from_xml_text', 'add_witness_from_xml_file',
                'get_dot', 'get_ascii_table', 'show_as_png', 'show_as_svg']

    def get_info(self):
        return self.collations.get_info(self.collation_id)

    def add_witness_from_xml_text(self, sigil, xml):
        self.collations.add_witness(self.collation_id, sigil, xml)

    def add_witness_from_xml_file(self, sigil, path):
        with open(path, mode='r', encoding='utf-8') as f:
            xml = f.read()
        return self.add_witness_from_xml_text(sigil, xml)

    def get_dot(self):
        return self.collations.get_dot(self.collation_id)

    def get_ascii_table(self):
        return self.collations.get_ascii_table(self.collation_id)

    def show_as_png(self):
        self.show_img(self.base_uri + '.png')

    def show_as_svg(self):
        self.show_img(self.base_uri + '.svg')

    def show_img(self, url):
        display(IFrame(src=url, width=950, height=300))
        display(HTML('<a href="' + url + '" target="_new" >open in new tab</a>'))
