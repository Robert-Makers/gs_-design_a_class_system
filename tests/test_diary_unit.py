from lib.diary import *

'''
Given I have a diary
Its initialised with an empty list of entries
'''
def test_diary_entry_list():
    diary = Diary()
    assert diary.entries == []

'''
Given I have a diary with no entries
Retrieve entries returns an empty list
'''

def test_retrieve_returns_empty():
    diary = Diary()
    assert diary.retrieve_entries() == []