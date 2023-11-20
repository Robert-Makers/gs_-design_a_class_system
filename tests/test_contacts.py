from lib.contacts import *

'''
Given I initialise Contacts
I have an empty list of contacts
'''

def test_empty_contact_list():
    contacts = Contacts()
    assert contacts.contact_list == []