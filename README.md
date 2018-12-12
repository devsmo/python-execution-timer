
# Execution Timer

Get an Excel-friendly execution time log from your app.

This class is meant for debugging performance issues. You can log the execution time for specific parts of code and group actions by type/category.

The log is a CSV file which allows you to do simple visualization to help you understand what's going on in your code.

## Methods

TBD


## Usage

See example.py for a working example of ExecutionTimer. The output of the example can be found in example_log.csv

**Initialize the timer.**

This should be done at the start of the code.

```
ExecutionTimer('./example_log.csv', ',', True)
```


**Log some action**

The start method starts logging, the end method ends it. 

```
ExecutionTimer.start('Doing some stuff', 'Stuff')

print("Doing stuff for 2 secs...")
time.sleep(2)

ExecutionTimer.end('Doing some stuff')
```


**End logging**

At the end of your code, you should complete the log.
It will give you the total exec time.

```
ExecutionTimer.complete()
```

