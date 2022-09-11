import aiohttp, tasksio, json, colored, time, os, threading
from os import system, sys; from time import sleep as sleep
import zinclib
from zinclib import log

load_bars = ['/', '-', '\\']

def progressbar(it, prefix="", filling_char:str = None, size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "="*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)


def StartProgress():
    for i in progressbar(range(120), "Fetching Users: ", 40):
        sleep(0.00000000000000001)

threading.Thread(target=StartProgress).start()