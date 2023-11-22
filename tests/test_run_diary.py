from unittest.mock import patch
from run_diary import *
import pytest #type: ignore
import sys
import io

'''
Given I launch run_diary
I have a list of options I can see in the terminal
'''
@patch('builtins.input', lambda _ :'5')
def test_run_diary(capsys):
    main()
    captured = capsys.readouterr()
    print(captured)
    assert 'Type a number' in captured.out
    assert '1: Add diary entry' in captured.out
    assert '2: Retrieve all entries' in captured.out
    assert '3: Get an entry you can read in time' in captured.out
    assert '4: Go to task manager' in captured.out

'''
When I run_diary I can select 1 to add an entry
I can select 2 to see the entry
Then select 5 to terminate the program
'''
def test_add_entry_with_option_one():
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['1', 'Day One', 'My first entry!', '2', '5']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        main()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    print(captured_text)
    assert 'Day One' in captured_text

'''
When I run_diary I can add two entries and see a formatted list
Then terminate the program
'''
def test_add_two_entries_and_show_entries():
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['1', 'Day One', 'My first entry!', '1', 'Day Two', 'My second entry!', '2', '5']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        main()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    print(captured_text)
    assert 'Day Two' in captured_text

'''
When I run_diary I can add three entries
I can select option 3 and input how many minutes I have and my reading speed
I can see the longest entry I can read in time
'''
def test_add_entries_and_retrieve_based_on_time():
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['1', 'Day One', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu ornare sapien. Duis sapien lorem, condimentum in neque id, convallis cursus urna. Proin fringilla hendrerit dui, nec iaculis ex viverra in. Suspendisse volutpat dapibus nunc vitae interdum. Phasellus id nunc dictum leo vulputate egestas semper id tellus. Integer ullamcorper leo nec ipsum auctor cursus. Suspendisse blandit vehicula sem id dictum. Curabitur sed imperdiet tortor. Nulla quis velit a elit sagittis ultrices a a mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget urna sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam eleifend faucibus dapibus. Nunc ac elit pretium, scelerisque sem vel, sagittis ante. Pellentesque mattis dolor nec malesuada malesuada. Donec leo libero, vehicula nec dictum nec, tincidunt at neque. Sed vehicula libero ante, sed pulvinar metus tincidunt non. Nunc vehicula, tellus eget vestibulum cursus, lacus sapien porttitor magna, placerat pulvinar dui enim in neque. Suspendisse dapibus malesuada metus quis convallis. Ut suscipit quam tortor, sit amet congue metus feugiat sed. Mauris dapibus maximus enim ac rutrum. Praesent quis turpis eleifend, vestibulum neque sed, gravida dui. Morbi nec nulla quis felis placerat vulputate. Morbi cursus purus quis lorem congue hendrerit. Maecenas sit amet metus vel dui pulvinar sodales. Duis sed egestas lorem, vitae ornare diam. Suspendisse euismod venenatis tortor et tincidunt.', '1', 'Day Two', 'Today I am writing my first diary entry. Ive had a great day at bootcamp, desiging class systems and learning about the debugging tools in VS Code. Im having lasagna for dinner and its going to be delicious.', '1', 'Day Three', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu ornare sapien. Duis sapien lorem, condimentum in neque id, convallis cursus urna. Proin fringilla hendrerit dui, nec iaculis ex viverra in. Suspendisse volutpat dapibus nunc vitae interdum. Phasellus id nunc dictum leo vulputate egestas semper id tellus. Integer ullamcorper leo nec ipsum auctor cursus. Suspendisse blandit vehicula sem id dictum. Curabitur sed imperdiet tortor. Nulla quis velit a elit sagittis ultrices a a mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget urna sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam eleifend faucibus dapibus. Nunc ac elit pretium, scelerisque sem vel, sagittis ante. Pellentesque mattis dolor nec malesuada malesuada. Donec leo libero, vehicula nec dictum nec, tincidunt at neque. Sed vehicula libero ante, sed pulvinar metus tincidunt non.', '3', '2', '100', '5']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        main()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    assert 'Day Three' in captured_text

'''
When I run_diary I can launch the task tracker
I see an new menu of options for tasks
'''
def test_task_menu_options_shown():
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['4', '5', '5']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        main()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    assert 'Add a new task' in captured_text

'''
When I run_diary I can launch the task tracker
I can add a new task and see a list of incomplete tasks
'''
def test_add_task_and_show_tasks():
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['4', '1', 'Walk the dog', '2', '5', '5']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        main()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    print(captured_text)
    assert 'Walk the dog' in captured_text

'''
When I run_diary I can launch the task tracker
I can add a new task, complete it and see a list of completed tasks
'''
def test_add_task_complete_and_show_completed():
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['4', '1', 'Walk the dog', '4', 'Walk the dog', '3', '5', '5']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        main()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    assert 'Walk the dog' in captured_text