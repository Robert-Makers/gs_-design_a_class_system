class DiaryEntry():
    # User facing properties:
    # title: string
    # contents: string

    def __init__(self, title, contents):
        # Parameters
        #   title: string
        #   contents: string

        # Returns
        #   nothing
        # Side effects
        #   sets the title and contents properties
        pass

    def format(self):
        # Parameters
        #   none
        # Returns
        #   string with title and contents: title: contents
        # Side effects
        #   none
        pass
    
    def word_count(self):
        # Parameters
        #   none
        # Returns
        #   number: total words in diary entry
        # Side effects
        #   none
        pass
    
    def reading_time(self, wpm):
        # Parameters
        #   wpm: int
        #   word_count (Note: will utilise the word_count method)
        # Returns
        #   int: reading time in minutes (round up)
        # Side effects
        #   none
        pass

    def get_phone_number(self):
        # Parameters
        #   none
        # Returns
        #   Phone number (if exists)
        # Side effects
        #   none
        pass