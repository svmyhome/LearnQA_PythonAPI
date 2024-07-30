import pytest

from learnqa_pythonapi.api_session import ApiSession


@pytest.fixture(scope='session')
def api_session():
    session = ApiSession(base_url='https://swapi.dev/api/')
    # session.headers['x-test'] = 'true'
    # session.headers.update({'x-test': 'true'})
    # session.headers.update({'x-test2': 'true'})
    session.headers.update({'x-test': 'application/json', 'x-test2': 'application/json'})
    return session
