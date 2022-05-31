# Invoking a method using super()

import abc
from abc import ABC, abstractmethod
 
class R(ABC):
    def rk(self):
        print("Abstract Base Class")
 
class K(R):
    def rk(self):
        super().rk()
        print("subclass ")
 
# Driver code
# Object r is instance of class K
r = K()

# Calls rk method within class K
# rk method calls the super().rk() method
# that returns "Abstract Base Class".
# Then "subclass" is printed
r.rk()