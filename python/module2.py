# import module1

# module1.checkValue()

# google colab
# !python module2.py

from module1 import *
import myPackage.check as pkg
from myPackage.subPackage import subPackage

checkValue()

pkg.printFunction()

subPackage.sayHello()