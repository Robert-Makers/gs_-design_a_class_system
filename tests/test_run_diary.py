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
Then select 5 to terminate the program
'''
def test_add_entry_with_option_one(capsys):
    captured_output = io.StringIO()
    with patch('builtins.input', side_effect=['1', '5']):
        old_stdout = sys.stdout
        sys.stdout = captured_output
        main()
        sys.stdout = old_stdout
    captured_text = captured_output.getvalue()
    assert 'Added entry' in captured_text