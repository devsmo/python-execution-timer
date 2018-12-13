import time

class ExecutionTimer:
    """
    ExecutionTimer class
    Debug your code by logging it's performance

    Initialize at start of script
    > ExecutionTimer(<path_to_logfile.csv>, {<delimiter>})

    Start timer
    > ExecutionTimer.start(<action>[, <category>])

    End timer
    > ExecutionTimer.end(<action>[, <comment>])

    End of script
    > ExecutionTimer.complete()

    The result of this class is a CSV file with rows for each action

    """
    class __ExecutionTimer:

        action_stack = {}
        delimiter = ','
        log_file = None
        exec_start = None
        file_hander = None

        def __init__(self, log_file, delimiter=','):
            self.log_file = log_file
            self.delimiter = delimiter


        def __str__(self):
            return repr(self) + self.log_file


        # Write a line at the beginning of file
        def start(self):
            self.exec_start = int(round(time.time() * 1000))
            line = self.delimiter.join(['"Start execution"', '', '0', '0', ''])
            self.writeLog(line)


        # Write a line at the end of the file with complete exec time
        def complete(self):
            exec_end = int(round(time.time() * 1000)) - self.exec_start
            # Write a line at the end of tile?
            line = self.delimiter.join(['"End execution"', '', '0', str(exec_end), ''])
            self.writeLog(line)

            # terminate file_hander.
            self.file_hander.close()


        def addAction(self, action, category):
            if action in self.action_stack:
                # An action by this name is already ongoing.
                # End it, so that we can safely start a new one.
                # This is technically an error by the user, but we could call it a feature
                self.endAction(action)

            self.action_stack[action] = {
                'action': action,
                'category': category if category else '',
                'time': int(round(time.time() * 1000)),
                'exec_time': 0,
                'comment': ''
            }


        def endAction(self, action, comment):
            if not action in self.action_stack:
                return False

            data = self.action_stack[action]
            self.action_stack.pop(action, None)

            # Get end time
            data['time'] = int(round(time.time() * 1000)) - data['time']
            data['exec_time'] = int(round(time.time() * 1000)) - self.exec_start
            data['comment'] = comment

            # Sort fields

            line = self.delimiter.join(str(val) for val in data.values())
            self.writeLog(line)


        def writeLog(self, line):
            # Write data to log
            if not self.file_hander:
                # create file handler
                self.file_hander = open(self.log_file, "w+")

            self.file_hander.write(line +"\n")
            return True

    """
    In the root class we instnsiate the private subclass.
    We also expose a few methods to the ouside code,
    """
    instance = None     # Save the logger instance to be reused accross the script

    def __init__(self, log_file=None, delimiter=',', is_enabled = True):
        if not is_enabled:
            ExecutionTimer.instance = None
            return False

        if not ExecutionTimer.instance:
            ExecutionTimer.instance = ExecutionTimer.__ExecutionTimer(log_file, delimiter)
            ExecutionTimer.instance.start()



    def __getattr__(self, name):
        return getattr(self.instance, name)


    def start(action, category=None):
        """
        Start timeing an action 

        Parameters
        ----------
        action: string
            Name of action to be timed
        category: string [optinal]
            Category of the action
        """
        if ExecutionTimer.instance:
            ExecutionTimer.instance.addAction(action, category)

    def end(action, comment=''):
        """
        End the timer for an action

        Parameters
        ----------
        action: string
            Name of an action that was previously started
        comment: string [optinal]
            Add a free format comment column to log file
        """
        if ExecutionTimer.instance:
            ExecutionTimer.instance.endAction(action, comment)

    # name it terminate instead?
    def complete():
        """
        End the execution timer.
        Adds a row to the end of the log with the completion time 
        of the whole process.
        """
        if ExecutionTimer.instance:
            ExecutionTimer.instance.complete()

