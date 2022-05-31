import abc
from abc import ABC, abstractmethod
 
class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"


class child(parent):
    @property
    def geeks(self):
        return "child class"

# try to make r an instance of class parent.
# Does not work as parent is defined only with abstract properties 
# Base class cannt be instantiated because it only has an abstract verion of the geeks method.
try:
    r = parent()
    print(r.geeks)
except Exception as err:
    print (err)
  

r = child()
print (r.geeks)