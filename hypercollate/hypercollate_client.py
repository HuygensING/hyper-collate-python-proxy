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

import sys

from hypercollate.client.hypercollate import HyperCollate
from hypercollate.collation_proxy import CollationProxy


class HyperCollateClient:
    def __init__(self, server_url):
        self.hypercollate = HyperCollate(server_url)

    def __dir__(self):
        return ['about', 'add_collation', 'list_collations', 'get_collation']

    def add_collation(self, collation_id):
        self.hypercollate.collations.add_collation(collation_id)
        return CollationProxy(collation_id, self.hypercollate)

    def delete_collation(self,collation_id):
        self.hypercollate.collations.delete_collation(collation_id)

    def list_collations(self):
        try:
            id_list = self.hypercollate.collations.get_all_collation_ids()
            return id_list
        except Exception as errMsg:
            print(errMsg, file=sys.stderr)
            raise errMsg

    def about(self):
        try:
            about = self.hypercollate.about.get().json
            return about
        except Exception as errMsg:
            print(errMsg, file=sys.stderr)
            raise errMsg

    def get_collation(self, collation_id):
        return CollationProxy(collation_id, self.hypercollate)
