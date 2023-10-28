import pytest
from fixtures.data import dato1, dato2, dato3

@pytest.fixture(params=[dato1, dato2, dato3])
def test_users(request):
    return request.param

def test_edit_profile(test_users):
    print(test_users['name'])
    print(test_users['age'])
    print(test_users['band'])
