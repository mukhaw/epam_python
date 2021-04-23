from hm_1.tasks.task_06_01 import User


def test_get_created_instances_returns_created_instances():
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3
    assert user._counter == 0
