import pytest

from learnqa_pythonapi.api_session import ApiSession


@pytest.fixture(scope='session')
def api_session():
    session = ApiSession(base_url='https://swapi.dev/api/')
    return session
