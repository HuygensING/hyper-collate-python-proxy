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

    def add_witness(self, collation_id, sigil, xml):
        def adder():
            return self.hypercollate.put_data(util.endpoint_uri(self.endpoint, collation_id, 'witnesses', sigil), xml, content_type='text/xml; charset=UTF-8')

        add_result = RestRequester(adder).on_status(HTTPStatus.CREATED, util.response_as_is).invoke()
        return add_result

    def get_dot(self, collation_id):
        def getter():
            return self.hypercollate.get(util.endpoint_uri(self.endpoint, collation_id, 'dot'))

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text

    def get_ascii_table(self, collation_id):
        def getter():
            return self.hypercollate.get(util.endpoint_uri(self.endpoint, collation_id, 'ascii_table'))

        return RestRequester(getter).on_status(HTTPStatus.OK, util.response_as_is).invoke().response.text
