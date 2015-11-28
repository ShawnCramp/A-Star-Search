import time
import sys


def console():
    """
    This function will be setup to allow user interaction
    with visualizing the code.

    :return:
    """



    for i in range(6):
        time.sleep(0.5)
        print('.'),

    print('\n')

    for i in 'Awaiting Command:':
        time.sleep(0.05)
        sys.stdout.write(i)

    print('\n')

    while True:
        for i in '-\|/':
            time.sleep(0.4)
            sys.stdout.write(i + '\r')



