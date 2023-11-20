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
        self.entries = []
        self.contacts = Contacts()

    def add_diary_entry(self, entry):
        # Parameters
        #   entry: DiaryEntry()
        # Returns
        #   nothing
        # Side effects
        #   adds a new entry to the list of entries
        #   if there is a phone number in the contents add it to contacts.contact_list
        if entry.get_phone_number() != None:
            self.contacts.contact_list.append(entry.get_phone_number())
        self.entries.append(entry)
        

    def retrieve_entries(self):
        # Parameters
        #   none
        # Returns
        #   a list of all entries formatted
        # Side effects
        #   none
        return [entry.format() for entry in self.entries]

    def select_entry_for_time(self, time, wpm):
        # Parameters
        #   time: Int the time in minutes available for reading
        #   wpm: Int words per minute
        # Returns
        #   a formatted diary entry that takes less time to read than the time available
        # Side effects
        #   none
        new_list = sorted([entry for entry in self.entries if entry.reading_time(wpm) <= time], key=lambda entry: entry.reading_time(wpm), reverse=True)

        if new_list == []:
            raise Exception("Not enough time to read any entries")
        return new_list[0].format()