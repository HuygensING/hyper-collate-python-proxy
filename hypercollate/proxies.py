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

from IPython.core.display import display, HTML
from IPython.lib.display import IFrame

from hypercollate.client import util
from hypercollate.client.hypercollate import HyperCollate


class CollationProxy:
    def __init__(self, collation_id: str, hypercollate: HyperCollate):
        self.collation_id = collation_id
        self.collations = hypercollate.collations
        self.hypercollate = hypercollate
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

    def get_dot(self, emphasize_whitespace=False):
        return self.collations.get_dot(self.collation_id, emphasize_whitespace)

    def get_ascii_table(self):
        return self.collations.get_ascii_table(self.collation_id)

    def get_witness(self, sigil):
        allowed_sigils = self.get_info()['witnesses'].keys()
        if sigil in allowed_sigils:
            return WitnessProxy(self.collation_id, sigil, self.hypercollate)
        else:
            raise Exception('collation \'' + self.collation_id + '\' has no witness \'' + sigil + '\'')

    def show_as_png(self, emphasize_whitespace=False):
        _show_img(self.base_uri + '.png')

    def show_as_svg(self, emphasize_whitespace=False):
        _show_img(self.base_uri + '.svg')


class WitnessProxy:
    def __init__(self, collation_id: str, sigil: str, hypercollate: HyperCollate):
        self.collation_id = collation_id
        self.collations = hypercollate.collations
        self.sigil = sigil
        self.base_uri = util.endpoint_uri(hypercollate.server_url[:-1], hypercollate.collations.endpoint, collation_id,
                                          'witnesses', sigil)

    def __str__(self):
        return "WitnessProxy::" + self.collation_id + ':' + self.sigil

    def __dir__(self):
        return ['get_dot', 'show_as_png', 'show_as_svg']

    def get_dot(self, emphasize_whitespace=False):
        return self.collations.get_witness_dot(self.collation_id, self.sigil, emphasize_whitespace)

    def show_as_png(self, emphasize_whitespace=False):
        _show_img(self.base_uri + '.png', emphasize_whitespace)

    def show_as_svg(self, emphasize_whitespace=False):
        _show_img(self.base_uri + '.svg', emphasize_whitespace)


def _show_img(url, emphasize_whitespace=False):
    if emphasize_whitespace:
        url += '?emphasize-whitespace=true'
    display(IFrame(src=url, width=950, height=300))
    display(HTML('<a href="' + url + '" target="_new" >open in new tab</a>'))
