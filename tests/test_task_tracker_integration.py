from src.task import *
from src.task_tracker import *
import sys
import io
from unittest.mock import patch

'''
Given a tasker tracker
I can give an input and add a task
I can see a list of incomplete tasks
'''
def test_add_task_with_input():
    task_tracker = TaskTracker()
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['Walk the dog']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        task_tracker.add_task()
        task_tracker.get_incomplete()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    assert 'Walk the dog' in captured_text


"""
Given a task tracker, when we complete a task, we can see that task in the complete list
"""
def test_add_and_complete_and_show_complete():
    task_tracker = TaskTracker()
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['Walk the dog', 'Empty the dishwasher', 'Empty the dishwasher']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        task_tracker.add_task()
        task_tracker.add_task()
        task_tracker.complete_task()
        task_tracker.get_complete()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    print(captured_text)
    assert 'Empty the dishwasher' in captured_text

"""
Given a task tracker, if we 'give up' all tasks will be in the complete list.
Confirm that the incomplete list is empty
"""

def test_add_and_give_up():
    task_tracker = TaskTracker()
    task_tracker = TaskTracker()
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['Walk the dog', 'Washing']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        task_tracker.add_task()
        task_tracker.add_task()
        task_tracker.give_up()
        task_tracker.get_complete()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    assert 'Walk the dog' in captured_text
    assert 'Washing' in captured_text