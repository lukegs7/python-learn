import pytest


@pytest.fixture(scope="function")
def first():
    print('获取用户名')


@pytest.fixture(scope='function')
def second():
    print('获取密码')


@pytest.fixture(scope='class')
def third():
    print('third')


@pytest.fixture(scope='module')
def fourth():
    print("fourth")


def test_some_data(some_data):
    assert some_data == 42


def test_other_data(other_data):
    print('test')


def test_a_list(a_list):
    assert a_list[2] == 2


def test_1(first):
    print('测试账号：%s' % first)


def test_2(first):
    print('测试密码：%s' % first)

def test_four(fourth):
    print('test four')

class TestCase():
    def test_1(self, third):
        print('test_1')

    def test_2(self, third):
        print('test_2')

    def test_four(self, fourth):
        print('test_four')
