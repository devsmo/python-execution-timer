from execution_timer import ExecutionTimer
from  random import randrange
import time


tasks = ['SQL query', 'REST call', 'PDF generation']
categories = ['Data collection', 'Data collection', '']

print(ExecutionTimer)

execTimer = ExecutionTimer('./example_log.csv', ',')

# this will take a while to loop
for x in range(1, 25):
	# get random task
	task = randrange(0, 3)

	execTimer.start(tasks[task], categories[task])
	
	time.sleep(randrange(5))
	print("Did this: {0}, {1} on key {2}".format(tasks[task], categories[task], task))
	
	execTimer.end(tasks[task])

execTimer.complete()

