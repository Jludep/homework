from task04 import User
import pytest


@pytest.mark.parametrize('user_object', User)
def test_get_created_instances():
    assert User.get_created_instances() == 0
    user_1, user_2, user_3 = User(), User(), User()
    assert user_1.get_created_instances() == 3


def test_reset_instances_counter():
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0