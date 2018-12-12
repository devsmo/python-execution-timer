from ExecutionTimer import ExecutionTimer
from  random import randrange
import time


tasks = ['SQL query', 'REST call', 'PDF generation']
categories = ['Data collection', 'Data collection', '']

print(ExecutionTimer)

execTimer = ExecutionTimer('./log.csv', ',')


for x in range(1, 10):
	task = randrange(0, 3)

	execTimer.start(tasks[task], categories[task])
	time.sleep(randrange(5))
	execTimer.end('action1')
	print("Did this: {0}, {1} on key {2}".format(tasks[task], categories[task], task))

execTimer.complete()

