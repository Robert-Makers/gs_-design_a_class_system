from lib.contacts import *

'''
Given I initialise Contacts
I have an empty list of contacts
'''

def test_empty_contact_list():
    contacts = Contacts()
    assert contacts.contact_list == []

'''
Given I have a contact in my list
I can return a list of contacts
'''

def test_contact_list():
    contacts = Contacts()
    contacts.contact_list.append('07123456789')
    assert contacts.get_contact_list() == ['07123456789']