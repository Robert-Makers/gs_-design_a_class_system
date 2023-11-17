from lib.contacts import *
from lib.diary_entry import *

class Diary():
    # user facing properties
    # list_of_entries: []
    # contacts: Contacts()

    def __init__(self) :
        # Parameters
        #   list_of_entries: []
        #   contacts: Contacts()
        # Returns
        #   nothing
        # Side effects
        #   sets the entries list to empty
        #   creates an instance of Contacts()
        pass

    def add_diary_entry(self, entry):
        # Parameters
        #   entry: DiaryEntry()
        # Returns
        #   nothing
        # Side effects
        #   adds a new entry to the list of entries
        #   if there is a phone number in the contents add it to contacts.contact_list
        pass

    def retrieve_entries(self):
        # Parameters
        #   none
        # Returns
        #   a list of all entries formatted
        # Side effects
        #   none
        pass

    def select_entry_for_time(self, time, wpm):
        # Parameters
        #   time: Int the time in minutes available for reading
        #   wpm: Int words per minute
        # Returns
        #   a formatted diary entry that takes less time to read than the time available
        # Side effects
        #   none
        pass