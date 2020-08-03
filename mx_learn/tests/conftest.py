import pytest
@pytest.fixture()
def some_data():
    return 42


def pytest_addoption(parser):
    group=parser.getgroup('run_this')
    group.addoption("--env",default='test',dest="env",help="set test run dev")
    group.addoption("--env1", default='test', dest="env1", help="set test run dev")