from hm_1.tasks.task_06_01 import User

user, _, _ = User(), User(), User()


def test_get_created_instances_returns_created_instances():
    assert user.get_created_instances() == 3


def test_reset_instances_counter_returns_intences_before_reset():
    assert user.reset_instances_counter() == 3


def test_reset_instances_counter_reset_counter():
    assert next(user._ids) == 0
