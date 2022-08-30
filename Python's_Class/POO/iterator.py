""" 
..Python Iterator

*Technically, in Python, an iterator is an object which implements the
*iterator protocol, which consist of the methods __iter__() and __next__().

-Iterator vs Iterable
*Lists, tuples, dictionaries, and sets are all iterable objects. They 
* are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:

Ejemplo: 
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

"""