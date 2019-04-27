import sys
# from time import sleep
for i in range(100):
    sys.stdout.write(str(i))
    sleep(0.5)
    sys.stdout.write('\r')