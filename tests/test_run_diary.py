from run_diary import *
import pytest #type: ignore
import sys
import io

'''
Given I launch run_diary
I have a list of options I can see in the terminal
'''
def test_run_diary(capsys):
    main()
    captured = capsys.readouterr()
    assert 'Type a number' in captured.out
    assert '1: Add diary entry' in captured.out
    assert '2: Retrieve all entries' in captured.out
    assert '3: Get an entry you can read in time' in captured.out
    assert '4: Go to task manager' in captured.out

'''
When I run_diary I can select 1
I'm then prompted to add a title and contents and add a diary entry
'''
def test_add_entry_with_option_one(monkeypatch):
    # monkeypatch.setattr('builtins.input', lambda _: '1')
    # main()
    # captured = capsys.readouterr()

    # Temporarily disable output capture
    monkeypatch.setattr(sys, 'stdin', io.StringIO('1'))

    # Simulate user input
    input = monkeypatch.mock.input

    # Call the function that reads input from stdin
    main()

    # Re-enable output capture
    monkeypatch.setattr(sys, 'stdin', sys.__stdin__)

    assert 'Add a new entry' in captured.out