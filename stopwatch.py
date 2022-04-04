#! python3

# stopwatch.py - A script to track how much time you spend on something


import time

# Display program's instructions
print('Press ENTER to begin. Afterward, press ENTER to stop the stopwatch. Press Ctrl-C to quit.')

input() # Press ENTER to begin
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s seconds (Total: %s seconds)' % (lapNum, lapTime, totalTime), end='')
        lapNum += 1
        lastTime = time.time() # Reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    print('\nTotal time: %s seconds. Total laps: %s ' % (totalTime, lapNum))
