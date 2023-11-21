from lib.diary import *
from unittest.mock import Mock

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

'''
Given I have a diary
I can add an entry and see it in my list of entries
'''
def test_add_entry_show_list():
    diary = Diary()
    fake_entry = Mock()
    fake_entry.title = 'Day Seven'
    fake_entry.contents = 'Week two is going great, I love bootcamp!'
    diary.add_diary_entry(fake_entry)
    assert diary.entries == [fake_entry]

'''
Given I have a diary with entries
I can retrieve a formatted list of entries
'''
def test_retrieve_formatted_entries():
    diary = Diary()
    fake_entry = Mock()
    fake_entry.format.return_value = 'Day Eight: This is so hard what am I doing here?'
    diary.add_diary_entry(fake_entry)
    assert diary.retrieve_entries() == ['Day Eight: This is so hard what am I doing here?']

'''
Given I have a diary with entries
I can tell how much time I have and retrieve an entry I can read in time
'''
def test_retrieve_entry_based_off_reading_time():
    diary = Diary()
    fake_entry_01 = Mock()
    fake_entry_02 = Mock()
    fake_entry_01.title = 'Day Seven'
    fake_entry_01.contents = 'Week two is going great, I love bootcamp!'
    fake_entry_01.reading_time.return_value = 1
    fake_entry_01.format.return_value = 'Day Seven: Week two is going great, I love bootcamp!'
    fake_entry_02.title = 'Day Eight'
    fake_entry_02.contents = 'This is so hard what am I doing here?'
    fake_entry_02.reading_time.return_value = 3
    diary.add_diary_entry(fake_entry_02)
    diary.add_diary_entry(fake_entry_01)
    assert diary.select_entry_for_time(1, 50) == 'Day Seven: Week two is going great, I love bootcamp!'

'''
Given I have a diary and add an entry containing a phone number
I can see that number in my contacts list
'''
def test_get_number_from_entry():
    diary = Diary()
    fake_entry = Mock()
    fake_entry.get_phone_number.return_value = '07123456789'
    diary.add_diary_entry(fake_entry)
    fake_entry.get_phone_number.assert_called()
    assert diary.contacts.contact_list == ['07123456789']