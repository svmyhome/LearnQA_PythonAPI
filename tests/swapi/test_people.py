import requests


class TestSwapiPeople:

    def test_swapi_people(self, api_session):
        response = api_session.request(method='GET', path='people/')
        assert response.status_code == 200
