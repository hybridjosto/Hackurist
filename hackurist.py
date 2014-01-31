import datetime
from time import *
from subprocess import call

compensate = 9
curTime = datetime.datetime.now()
compTime = curTime + datetime.timedelta(seconds=compensate)
compTime = compTime.time().strftime("%H:%M:%S")


phrase = """At the third stroke, the time sponsored by hackurist will be %s""" % (compTime)

start = time()
print phrase
call(["say", phrase])
end = time() - start
end = end - 6

beeps = range(3)

if end <1:
    print('z...')
    sleep(1-end)

for beep in beeps:
    print('\a'), strftime("%X")
    sleep(1)
