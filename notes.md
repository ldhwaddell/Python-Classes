ABC = abstract base classes. Effectively a blueprint for other classes. Contains the
set of methods that must be included in child classes built from abstract class.

Abstract method is a method which only has declaration and doesn't have definition.

A class is called abstract class only if it has at least one abstract method.

When you inherit a abstract class as a parent to the child class, 
the child class should define all the abstract method present in parent class.

If it is not done then child class also becomes abstract class automatically.

Python by default doesn't support abstract class and abstract methods, 
so there is a package called ABC(abstract base classes) by which we can make a 
class or method abstract.

If you subclass directly from the base class, you do not need to explicitly define class as abstract.
However, you can also see all of the classes derived from the base class

`issubclass(child, parent)` can be used to determine if one class is a subclass of another

`isinstance(child(), parent)` can be used to determine if one object is an instance of a class. 

Concrete classes only have normal methods where abstract classes can have normal and abstract methods.
The concrete class can implement the abstract methods. The abstract base class can also implement these methods by invoking th emethods with `super()`

abstract classes can also include attributes(variables). You can require attributes in concrete classes
by defining them with `@abstractproperty`

Base classes cannot be instantiated if they only have abstract versions of methods

underscores to denote private methods
