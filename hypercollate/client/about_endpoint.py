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


class AboutEndpoint(HyperCollateEndpoint):
    endpoint = 'about'

    def __call__(self):
        return self.get()

    def get(self):
        def getter():
            return self.hypercollate.get(self.endpoint)

        return RestRequester(getter).on_status(HTTPStatus.OK, util.entity_as_json).invoke()
