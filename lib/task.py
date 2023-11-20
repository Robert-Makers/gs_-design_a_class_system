class Task():
    #user facing properties
    #   task: String
    #   complete: Bool

    def __init__(self, task):
        if task == "":
            raise Exception("Task string should not be empty")
        self.text = task
        self.complete = False
        # Parameters
        #   task: String
        #   complete: Bool
        # Returns
        #   nothing
        # Side effects
        #   sets the task and complete properties
        

    def complete_task(self):
        self.complete = True
        # Parameters
        #   none
        # Returns
        #   none
        # Side effects
        #   set complete to True