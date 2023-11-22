from src.diary_entry import *
import pytest #type: ignore

'''
Given a diary entry
It has a title property
It has a contents property
'''
def test_diary_entry_has_all_its_properties():
    entry = DiaryEntry('Day One', 'My first day of bootcamp')
    assert entry.title == 'Day One'
    assert entry.contents == 'My first day of bootcamp'

'''
Given a diary entry with no title
Catch an error
'''
def test_error_if_no_title():
    with pytest.rasies(Exception) as e:
        entry = DiaryEntry('', 'My first day of bootcamp')
    assert str(e.value) == 'Diary entry must have a title and contents'

'''
Given a diary entry with no contents
Catch an error
'''
def test_error_if_no_title():
    with pytest.raises(Exception) as e:
        entry = DiaryEntry('Day One', '')
    assert str(e.value) == 'Diary entry must have a title and contents'

'''
Given a diary entry
I can see the formatted entry
'''
def test_format_entry():
    entry = DiaryEntry('Day One', 'My first day of bootcamp')
    assert entry.format() == f'Day One:\nMy first day of bootcamp'

'''
Given a diary entry
I can see a word count for the entry contents
'''
def test_word_count():
    entry = DiaryEntry('Day One', 'My first day of bootcamp')
    assert entry.word_count() == 5

'''
Given a diary entry
I can use the word count and a wpm parameter to see the reading time in minutes
Where the reading time is a float should return an Int
'''
def test_get_reading_time():
    entry = DiaryEntry('Day One', 'My first day of bootcamp')
    assert entry.reading_time(10) == 1

'''
Given a diary entry
I can add an entry with a phone number
The phone number will be returned if it exists
'''
def test_return_phone_number_if_found():
    entry = DiaryEntry('Day One', 'My first day of bootcamp I got someones number 07123456789')
    assert entry.get_phone_number() == '07123456789'

'''
Given a diary entry
I can add an entry without a phone number
No number will be returned
'''
def test_return_no_number_when_not_found():
    entry = DiaryEntry('Day One', 'My first day of bootcamp')
    assert entry.get_phone_number() == None