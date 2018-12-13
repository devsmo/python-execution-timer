from execution_timer import ExecutionTimer
from  random import randrange
import time


tasks = ['SQL query', 'REST call', 'PDF generation']
categories = ['Data collection', 'Data collection', '']

print(ExecutionTimer)

ExecutionTimer('./example_log.csv', ',')

# this will take a while to loop
for x in range(1, 25):
	# get random task
	task = randrange(0, 3)

	ExecutionTimer.start(tasks[task], categories[task])
	
	time.sleep(randrange(100, 900)/1000)
	print("Did this: {0}, {1}".format(tasks[task], categories[task]))
	
	ExecutionTimer.end(tasks[task])

ExecutionTimer.complete()

