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

from http import HTTPStatus

from hypercollate.client import util
from hypercollate.client.hypercollate_endpoint import HyperCollateEndpoint
from hypercollate.client.rest_requester import RestRequester


class CollationsEndpoint(HyperCollateEndpoint):
    endpoint = 'collations'

    def __call__(self):
        return self.get()

    def get_all_collation_ids(self):
        def getter():
            return self.hypercollate.get(self.endpoint)

        return RestRequester(getter).on_status(HTTPStatus.OK, util.entity_as_json).invoke().json

    def get_info(self, collation_id):
        def getter():
            return self.hypercollate.get(util.endpoint_uri(self.endpoint, collation_id))

        return RestRequester(getter).on_status(HTTPStatus.OK, util.entity_as_json).invoke().json

    def add_collation(self, collation_id):
        def adder():
            return self.hypercollate.put_data(util.endpoint_uri(self.endpoint, collation_id), '')

        add_result = RestRequester(adder).on_status(HTTPStatus.CREATED, util.response_as_is).invoke()
        return add_result

    def delete_collation(self, collation_id):
        def deleter():
            return self.hypercollate.delete(util.endpoint_uri(self.endpoint, collation_id))

        result = RestRequester(deleter).on_status(HTTPStatus.NO_CONTENT, util.response_as_is).invoke()
        return result

    def add_witness(self, collation_id, sigil, xml):
        def adder():
            return self.hypercollate.put_data(util.endpoint_uri(self.endpoint, collation_id, 'witnesses', sigil), xml,
                                              content_type='text/xml; charset=UTF-8')

        add_result = RestRequester(adder).on_status(HTTPStatus.CREATED, util.response_as_is).invoke()
        return add_result

    def get_dot(self, collation_id, emphasize_whitespace=False):
        def getter():
            dot_url = util.endpoint_uri(self.endpoint, collation_id) + '.dot'
            if emphasize_whitespace:
                dot_url += '?emphasize-whitespace=true'
            return self.hypercollate.get(dot_url)

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text

    def get_ascii_table(self, collation_id, emphasize_whitespace=False):
        def getter():
            uri = util.endpoint_uri(self.endpoint, collation_id, 'ascii_table')
            if emphasize_whitespace:
                uri += '?emphasize-whitespace=true'
            return self.hypercollate.get(uri)

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text
