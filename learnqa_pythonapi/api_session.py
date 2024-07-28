import requests
from requests import Session


class ApiSession(Session):

    def __init__(self, base_url=None):
        super().__init__()
        self.base_url = base_url

    def request(self, method, path, verify=False, *args, **kwargs):
        joined_url = self.base_url + path

        return super().request(method, joined_url, *args, **kwargs)
