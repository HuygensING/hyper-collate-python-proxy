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

class RestResult:
    def __init__(self, uuid=None, json=None, failed=False, response=None):
        self.uuid = uuid
        self.json = json
        self.failed = failed
        self.response = response

    def __str__(self):
        return "<RestResult failed={}, uuid={}, json={}, response={}>" \
            .format(self.failed, self.uuid, self.json, self.response)
