#before usage - in CMD: pip install cowsay

import time
import datetime as d
import sys, os, platform
#import math
#from math import sqrt, ceil
from math import sqrt as s, ceil
import MyModule
import cowsay

#time.sleep(2)
#print("Hello")

#print(d.datetime.now().day)

#print(sys.path)
#print(os.name)
#print(platform.system())

#print(math.ceil(math.sqrt(25)))
#print(ceil(sqrt(25)))
print(ceil(s(25)))

MyModule.hi()
print(MyModule.name)
print(MyModule.add_3_nubers([4, 5, 2, 5, 3, 34, 3, 34, 34, -34]))
cowsay.cow("Hello Worl")