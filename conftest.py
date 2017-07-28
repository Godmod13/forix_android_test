import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture
    platform = request.config.getoption("--platform")
    if fixture is None:
        fixture = Application(platform=platform)
    else:
        if not fixture.is_valid():
            fixture = Application(platform=platform)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture



def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="Android ")