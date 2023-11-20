from lib.diary_entry import *
from lib.diary import *
from lib.contacts import *
import pytest #type: ignore

'''
Given I have a diary
I can add an entry
I can see list of entries contains my entry
'''
def test_add_entry():
    diary = Diary()
    entry_one = DiaryEntry('Day one', "Today is my first day writing a diary!")
    diary.add_diary_entry(entry_one)
    assert diary.entries == [entry_one]

'''
Given I have a diary
I can add two entries
I can get back a formatted list of entries
'''
def test_add_entries_and_format_list():
    diary = Diary()
    entry_1 = DiaryEntry('Day One', 'Today is my first day writing a diary!')
    entry_2 = DiaryEntry('Day Two', 'I had pizza for lunch it was amazing')
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.retrieve_entries() == ['Day One: Today is my first day writing a diary', 'Day Two: I had pizza for lunch it was amazing']

'''
Given I initialise a Diary
It has a contacts property that is Contacts
'''
def test_contacts_exists():
    diary = Diary()
    assert diary.contacts.contact_list == []

'''
Given I have a diary
If I add an entry that contains a phone number
Number is added to contact list
I can see a list of contacts
'''
def test_add_entry_with_number_and_show_contacts():
    diary = Diary()
    entry_1 = DiaryEntry('Day Three', 'I made a new friend and this is their number: 07893748621')
    diary.add_diary_entry(entry_1)
    assert diary.contacts.contact_list == ['07893748621']

'''
Given I have a diary
If I add two entries where only one has a phone number
The contacts list only contains one number
'''
def test_add_two_entries_and_show_contacts():
    diary = Diary()
    entry_1 = DiaryEntry('Day Three', 'I made a new friend and this is their number: 07893748621')
    entry_2 = DiaryEntry('Day Four', 'I made a new friend but I didnt get their number')
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.contacts.contact_list == ['07893748621']

'''
Given I have a diary with three entries
I can input the amount of time I have to read and my reading speed
I get back a diary entry I can read in time
'''
def test_three_entries_return_entry_to_read_in_time():
    diary = Diary()
    #232 words
    entry_1 = DiaryEntry('Day One', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu ornare sapien. Duis sapien lorem, condimentum in neque id, convallis cursus urna. Proin fringilla hendrerit dui, nec iaculis ex viverra in. Suspendisse volutpat dapibus nunc vitae interdum. Phasellus id nunc dictum leo vulputate egestas semper id tellus. Integer ullamcorper leo nec ipsum auctor cursus. Suspendisse blandit vehicula sem id dictum. Curabitur sed imperdiet tortor. Nulla quis velit a elit sagittis ultrices a a mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget urna sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam eleifend faucibus dapibus. Nunc ac elit pretium, scelerisque sem vel, sagittis ante. Pellentesque mattis dolor nec malesuada malesuada. Donec leo libero, vehicula nec dictum nec, tincidunt at neque. Sed vehicula libero ante, sed pulvinar metus tincidunt non. Nunc vehicula, tellus eget vestibulum cursus, lacus sapien porttitor magna, placerat pulvinar dui enim in neque. Suspendisse dapibus malesuada metus quis convallis. Ut suscipit quam tortor, sit amet congue metus feugiat sed. Mauris dapibus maximus enim ac rutrum. Praesent quis turpis eleifend, vestibulum neque sed, gravida dui. Morbi nec nulla quis felis placerat vulputate. Morbi cursus purus quis lorem congue hendrerit. Maecenas sit amet metus vel dui pulvinar sodales. Duis sed egestas lorem, vitae ornare diam. Suspendisse euismod venenatis tortor et tincidunt.')
    #38 words
    entry_2 = DiaryEntry('Day Two', 'Today I am writing my first diary entry. Ive had a great day at bootcamp, desiging class systems and learning about the debugging tools in VS Code. Im having lasagna for dinner and its going to be delicious.')
    #150 words
    entry_3 = DiaryEntry('Day Three', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu ornare sapien. Duis sapien lorem, condimentum in neque id, convallis cursus urna. Proin fringilla hendrerit dui, nec iaculis ex viverra in. Suspendisse volutpat dapibus nunc vitae interdum. Phasellus id nunc dictum leo vulputate egestas semper id tellus. Integer ullamcorper leo nec ipsum auctor cursus. Suspendisse blandit vehicula sem id dictum. Curabitur sed imperdiet tortor. Nulla quis velit a elit sagittis ultrices a a mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget urna sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam eleifend faucibus dapibus. Nunc ac elit pretium, scelerisque sem vel, sagittis ante. Pellentesque mattis dolor nec malesuada malesuada. Donec leo libero, vehicula nec dictum nec, tincidunt at neque. Sed vehicula libero ante, sed pulvinar metus tincidunt non.')
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    diary.add_diary_entry(entry_3)
    assert diary.select_entry_for_time(2, 100) == entry_2.format()

'''
Given I have a diary
I can input the amount of time I have to read and my reading speed
I catch an error if no entries are short enough to read
'''
def test_error_if_no_entries_are_available_in_reading_time():
    diary = Diary()
    #232 words
    entry_1 = DiaryEntry('Day One', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu ornare sapien. Duis sapien lorem, condimentum in neque id, convallis cursus urna. Proin fringilla hendrerit dui, nec iaculis ex viverra in. Suspendisse volutpat dapibus nunc vitae interdum. Phasellus id nunc dictum leo vulputate egestas semper id tellus. Integer ullamcorper leo nec ipsum auctor cursus. Suspendisse blandit vehicula sem id dictum. Curabitur sed imperdiet tortor. Nulla quis velit a elit sagittis ultrices a a mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget urna sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam eleifend faucibus dapibus. Nunc ac elit pretium, scelerisque sem vel, sagittis ante. Pellentesque mattis dolor nec malesuada malesuada. Donec leo libero, vehicula nec dictum nec, tincidunt at neque. Sed vehicula libero ante, sed pulvinar metus tincidunt non. Nunc vehicula, tellus eget vestibulum cursus, lacus sapien porttitor magna, placerat pulvinar dui enim in neque. Suspendisse dapibus malesuada metus quis convallis. Ut suscipit quam tortor, sit amet congue metus feugiat sed. Mauris dapibus maximus enim ac rutrum. Praesent quis turpis eleifend, vestibulum neque sed, gravida dui. Morbi nec nulla quis felis placerat vulputate. Morbi cursus purus quis lorem congue hendrerit. Maecenas sit amet metus vel dui pulvinar sodales. Duis sed egestas lorem, vitae ornare diam. Suspendisse euismod venenatis tortor et tincidunt.')
    #150 words
    entry_2 = DiaryEntry('Day Three', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu ornare sapien. Duis sapien lorem, condimentum in neque id, convallis cursus urna. Proin fringilla hendrerit dui, nec iaculis ex viverra in. Suspendisse volutpat dapibus nunc vitae interdum. Phasellus id nunc dictum leo vulputate egestas semper id tellus. Integer ullamcorper leo nec ipsum auctor cursus. Suspendisse blandit vehicula sem id dictum. Curabitur sed imperdiet tortor. Nulla quis velit a elit sagittis ultrices a a mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget urna sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam eleifend faucibus dapibus. Nunc ac elit pretium, scelerisque sem vel, sagittis ante. Pellentesque mattis dolor nec malesuada malesuada. Donec leo libero, vehicula nec dictum nec, tincidunt at neque. Sed vehicula libero ante, sed pulvinar metus tincidunt non.')
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    with pytest.raises(Exception) as e:
        diary.select_entry_for_time(1, 50)
    assert str(e.value) == "Not enough time to read any entries"