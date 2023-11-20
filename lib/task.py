class Task():
    #user facing properties
    #   task: String
    #   complete: Bool

    def __init__(self, task):
        # Parameters
        #   task: String
        #   complete: Bool
        # Returns
        #   nothing
        # Side effects
        #   sets the task and complete properties
        self.text = task
        self.complete = False

    def complete_task(self):
        # Parameters
        #   none
        # Returns
        #   none
        # Side effects
        #   set complete to True
        pass