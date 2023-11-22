import math

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
        if title == '' or contents == '':
            raise Exception('Diary entry must have a title and contents')

        self.title = title
        self.contents = contents

    def format(self):
        # Parameters
        #   none
        # Returns
        #   string with title and contents: title: contents
        # Side effects
        #   none
        return f'{self.title}:\n{self.contents}'
    
    def word_count(self):
        # Parameters
        #   none
        # Returns
        #   number: total words in diary entry
        # Side effects
        #   none
        return len(self.contents.split(' '))
    
    def reading_time(self, wpm):
        # Parameters
        #   wpm: int
        #   word_count (Note: will utilise the word_count method)
        # Returns
        #   int: reading time in minutes (round up)
        # Side effects
        #   none
        word_count = self.word_count()
        minutes = word_count / wpm
        rounded =  math.ceil(minutes)
        return rounded

    def get_phone_number(self):
        # Parameters
        #   none
        # Returns
        #   Phone number (if exists)
        # Side effects
        #   none
        '''
        search for '07' in contents
        find char index
        get characters[20:32]
        '''
        for (index, character) in enumerate(self.contents):
            if character == '0' and self.contents[index+1] == '7':
                number_string = self.contents[index:index+11]
                if number_string.isnumeric():
                    return number_string