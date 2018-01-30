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
