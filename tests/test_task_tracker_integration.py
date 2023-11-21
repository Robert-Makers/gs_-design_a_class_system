from src.task import *
from src.task_tracker import *

"""
Given a task tracker, when we add two tasks, we can see those tasks in the incomplete list
"""

def test_add_and_show_incomplete():
    task_tracker = TaskTracker()
    task_1 = Task("Walk the dog")
    task_2 = Task("Washing")
    task_tracker.add_task(task_1)
    task_tracker.add_task(task_2)
    assert task_tracker.get_incomplete() == ["Walk the dog", "Washing"]

"""
Given a task tracker, when we complete a task, we can see that task in the complete list
"""

def test_add_and_complete_and_show_complete():
    task_tracker = TaskTracker()
    task_1 = Task("Walk the dog")
    task_tracker.add_task(task_1)
    task_tracker.complete_task(task_1.text)
    assert task_tracker.get_complete() == ["Walk the dog"]


"""
Given a task tracker, if we add 2 tasks and complete one, 
we can still see the incomplete task in the incomplete list.
"""

def test_add_and_complete_and_show_incomplete_and_complete():
    task_tracker = TaskTracker()
    task_1 = Task("Walk the dog")
    task_2 = Task("Washing")
    task_tracker.add_task(task_1)
    task_tracker.add_task(task_2)
    task_tracker.complete_task(task_1.text)
    assert task_tracker.get_incomplete() == ["Washing"]
    assert task_tracker.get_complete() == ["Walk the dog"]

"""
Given a task tracker, if we 'give up' all tasks will be in the complete list.
Confirm that the incomplete list is empty
"""

def test_add_and_give_up():
    task_tracker = TaskTracker()
    task_1 = Task("Walk the dog")
    task_2 = Task("Washing")
    task_tracker.add_task(task_1)
    task_tracker.add_task(task_2)
    task_tracker.give_up()
    assert task_tracker.get_complete() == ["Walk the dog", "Washing"]