from lib.task_tracker import *

"""
When we initialise, task tracker list is empty
"""

def test_task_list_empty_initially():
    task_tracker = TaskTracker()
    assert task_tracker.task_list == []