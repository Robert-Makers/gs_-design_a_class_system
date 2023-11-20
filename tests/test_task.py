import pytest #type: ignore
from lib.task import *

"""
When creating a task, if task string is empty, raise an error
"""

def test_empty_task_creates_error():
    with pytest.raises(Exception) as e:
        task = Task("")
    assert str(e.value) == "Task string should not be empty"

"""
When creaing a task, confirm task is set to the string provided
"""
def test_task_has_been_set():
    task = Task("Walk the dog")
    assert task.text == "Walk the dog"

"""
When creating a task, complete is initially set to False
"""
def test_task_complete_is_false():
    task = Task("Walk the dog")
    assert task.complete == False

"""
When completing a task, 
confirm complete changes to True
"""

def test_task_complete():
    task = Task("Walk the dog")
    task.complete_task()
    assert task.complete == True

"""
When completing an already complete task, it remains completed - True
"""

def test_task_complete_a_completed_task():
    task = Task("Walk the dog")
    task.complete_task()
    task.complete_task()
    assert task.complete == True