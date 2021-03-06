# Iterators and Collection Protocols

This repository is created in order to consolidate the study, and practices for 
the Python Iterators, and other collection protocols. 

## Iterator & Iterable Protocols

Following is, how the Iterator, and Iterable protocols are defined.

<img src="static/iterationprotocols.png" width="1000px" alt="Iterator and Iterable Protocols">

The above illustration shows, that every Iterator object is also an Iterable 
object.

* The builtin `iter` function calls the `__iter__` method of the type. 
* The builtin `next` function calls the `__next__` method of the type.

The image also demonstrates, that all Iterators also conforms to the Iterable 
protocol. This is the reason, we can use and Iterator as Iterable with for loops.

In the [basic_iterators](https://github.com/sarkarchandan/pycollections/blob/master/iter/basic_iterators.py) 
module we have demonstrated some basic implementations of the iterators. We have 
implemented some iterators, which performs basic level-order, inorder, and preorder 
tree traversal, when the tree is represented as a sequence. 

There are other kind of iterators, which behaves differently from the regular 
iterators e.g., filtering iterators, transformer iterators etc.

> While studying the filtering iterators we have introduced an imperfect binary 
> tree. We have seen for the previous iterators, that imperfect binary tree is 
> a problem. However, there are ways to work with imperfect binary trees by 
> introducing some placeholder objects. These objects, which represents something 
> else than their values, are called sentinel objects. Introducing these objects 
> enables an imperfect binary tree to be treated as a perfect binary tree. Using 
> `None` as sentinel objects are not a good idea, because if we do so, we won't 
> be able to have None as binary tree member. A better option is to create some 
> `object` instances having no value, and creating a custom iterator to skip these 
> special objects.

In the [filter_iterators](https://github.com/sarkarchandan/pycollections/blob/master/iter/filter_iterators.py) 
module, we have created `SkipMissingIterator` class, which takes an `Iterable` 
object, and filters the placeholder missing objects. We have demonstrated how 
we have reused the `InOrderIterator`, which needs the perfect binary tree in 
order to create an infix notation, and then filtered out the missing objects.

In the [transform_iterators](https://github.com/sarkarchandan/pycollections/blob/master/iter/transform_iterators.py) 
we have created `TranslationIterator` class, which takes a machine-readable 
expression as Iterable, and translates the same to humanreadable expression.

In the [iterable](https://github.com/sarkarchandan/pycollections/blob/master/iter/iterable.py) 
module, we have demonstrated a simple custom class `PerfectBinaryTree`, which 
implements the Iterable protocol. We observed, that it can be used anywhere, 
where an Iterable type is expected.

In the [alternative_iterable](https://github.com/sarkarchandan/pycollections/blob/master/iter/alternative_iterable.py) 
module we have demonstrated an alternative method to create Iterable collection 
using the `__getitem__` dunder method. Here we have created an Iterable sequence 
of rational numbers using `Fraction` objects. We have only provided the 
implementation of the `__getitem__` in order to effectively create an Iterable. 
This Iterable can be passed in to `iter` function to create an Iterator. The 
`__getitem__` method should have an integer index, and should raise IndexError 
when the index goes beyond the length of the underlying sequence. It can also 
be used in more sophisticated manner.

In the [extended_iter](https://github.com/sarkarchandan/pycollections/blob/master/iter/extended_iter.py) 
module we have explored an alternative form of the `iter` function. We have used 
this function so far in order to create an Iterator from an Iterable object. It 
has an alternative form, in which we pass in a Callable object along with a 
sentinel value. The Callable object takes zero argument, and it is invoked once 
per iteration. The Callable yields a value per iteration, and it stops, when the 
said value becomes equal to the passed in sentinel value. We can make use of 
this utility in order to create a sequence until some predefined terminating 
value is encountered. In this module we have explored several of such possibilities.

## Collection Protocols

Following are a list of the most common Collection protocols supported in Python 
standard library.

<img src="static/collectionprotocols.png" width="1000px" alt="Collection Protocols">

Most Collection protocols can be implemented by providing implementation of one 
or more dunder methods. First, we need to understand some specifications of the 
utilities, which these protocols support.

* `Container` protocol allows the membership testing using the `in`, and `not in` 
    operators.
* `Sized` protocol allows the checking of number of elements in the collection 
  by passing the object to the builtin `len` function.
* `Iterable` protocol, as we have seen already allows itself to be iterated 
  using `for in` construct It also allows creation of an Iterator out of itself 
  using the `iter` function.
* `Sequence` protocol supports a range of things,
  * Subscripting of values from a collection using index e.g., 
    `seq[index]`.
  * Find index of an item in the collection e.g., `index = seq.index(item)`.
  * Count number of items in the collection e.g., `num = seq.count(item)`.
  * Reverse a sequence using built in `reversed` function e.g., `r = reversed(seq)`.
* `Set` protocol allows algebraic set operations.
* `Mapping` protocol associates values with hashable keys. It is represented in 
  Python by the dict data structure.
* `Mutable Sequence`, `Mutable Set`, and `Mutable Mapping` protocols are 
  representatives of the mutable versions of the corresponding protocols.

In the [frozen_set](https://github.com/sarkarchandan/pycollections/blob/master/coll/frozen_set.py) 
module we have implemented a `SortedFrozenSet` type, which implements `Sized`, 
`Iterable`, `Sequence`, `Container`, and `Set` protocols. We have implemented 
the SortedFrozenSet with the Test Driven Development approach. Following are 
brief illustrations about the protocols, that we are going to implement.

### Container

Container protocol is the most fundamental collection protocol, and supports 
the membership checking using `in`, and `not in` keywords. It relies on the 
implementation of the `__contains__` dunder method. When that implementation is 
not found, it falls back to the Iterable protocol.

### Sized

Sized protocol enables the use of `len` builtin function on a collection to 
check the number of items, that it contains. It should not consume or modify 
the collection in any ways. One must implement the `__len__` dunder method in 
order to implement the Sized protocol. In this implementation, we have done 
a crucial refactoring in the initializer of the SortedFrozenSet to use `set` 
as an internal collection. This is done in order to preserve a crucial property, 
that set is a collection of distinct items, and SortedFrozenSet must conform to 
it.

### Iterable

Iterable protocol dictates, that a compliant object can be passed to builtin 
`iter` function in order to create an Iterator. This needs the implementation 
of the `__iter__` method. There is an alternative way to create an Iterable, 
which is to implement `__getitem__` method. This method takes an integer index 
as argument, and should raise IndexError, once the index goes beyond the length 
of the collection. In this part of the implementation we have taken the first 
approach, where we called the iter function on the internal collection. However, 
we also acknowledge, that using `__iter__` as a Generator function is also 
equally valid. Generator functions also produce Iterator objects.

### Sequence

Sequence protocol covers a larger ground, compared to all other protocols, which 
we have implemented so far. Moreover, Sequence protocol implies the Container, 
Sized, and Iterable protocols. Following are the very least of the requirements 
if the Sequence protocol.

* Subscripting - retrieve an item from the collection by index, 
  `item = seq[index]`. This way of accessing an item from the collection 
  delegates to the `__getitem__` dunder method. This method takes and integer 
  index as argument, and it is supposed to return the item at the index. If the 
  index is beyond permissible range, the method must raise the IndexError.
  In our implementation, the method should also support the negative indexing 
  allowed by Python.
* Optionally retrieve items by slicing, `items = seqp[start:stop]`. In our 
  implementation this requirement alone has made us to tweak the simpler 
  `__getitem__` implementation to handle inter index and slice index 
  differently. Also, the testcases written for this part made us to consider, 
  how Python interprets the equality of two different objects.
  
  > The default interpretation of equality in Python is inherited from the 
  > `object` class. That means, by default Python checks for the reference 
  > equality, and not the value equality. That means, when we compare, 
  > `object1 == object2`, Python actually compares is, `object1 is object2`. 
  
  In order to get an equivalence behavior i.e., the value equality, we need 
  to override the default equality behavior.
* Produce a reverse Iterator, `rev = reversed(seq)`. This utility is supported 
  by the implementation of the `__reversed__` method. In absence of this 
  implementation a fallback happens to the`__getitem__` method, which makes 
  attempt to yield and Iterator using reverse indexing. In our implementation 
  the said fallback takes place. Inside the `__getitem__` in this case we 
  delegate to the standard libreary implementation of `__reversed__` method 
  of the internal tuple object.
* Locate an item by value, `index = seq.index(item)`. We have provided this 
  implementation in order to comply with the Sequence protocol, despite the 
  set itself is an unordered collection.
* Count the occurrences of a given item, `num = seq.count(item)`.

In the implementation of the SortedFrozenSet, we have implemented all these 
requirements to comply with the Sequence protocol. In order to provide the 
implementation of the `index`, and `count` methods we have used the Python's 
abstract base class implementation of these methods. For that we have made 
our SortedFrozenSet class to inherit from the Sequence class of the 
[collections.abc](https://docs.python.org/3/library/collections.abc.html) 
module. However, we should mention, that these implementations are done for 
the sake of completing the Sequence protocol. A pure set is an unordered 
collection of distinct elements. Hence, it does not need any index or count 
utilities. These implementations for index ad count methods are not optimal 
though. Because of the fact, that the SortedFrozenSet is an ordered collection 
of the distinct elements we have scope of exploiting these properties and 
optimize the performance of index and count methods. We have discussed these 
in the **Refactoring Notes** section.

Apart from the utilities, which we have implemented here there are some 
other optional extensions, which are widely implemented by other collections 
which are part pf Python standard library. However, Sequence protocol does 
not enforce them. Some of these utilities are listed below.

* For both mutable, and immutable sequences,
  * Concatenation by `__add__`, and `__radd__` methods.
  * Repetition by `__mul__`, and `__rmul__` methods.
* Only for mutable sequences,
  * In-place concatenation by `__iadd__` method.
  * In-place repetition by `__imul__` method.
  * In-place append, extend, insert, pop, reverse, remove, sort.

Our SortedFrozenSet is an immutable collection, hence we would only implement 
the first group of the operations. Moreover, we need to understand, that adding 
to a set is not always intuitive due the set-immutability. Actually, we are 
going to implement the add as set union operation. The repetition would behave 
identical to the operation of `*` operator for the list. However, there is one 
key difference to keep in mind. Since our object is a set, we can not really 
repeat any elements apart from 0 or negative times. Our testcases cover this.

### Hashable

Hashable objects can be used as keys for the dictionary mapping. **Immutable 
objects, which support value equality should also comply with Hashable 
protocol**. By that convention our SortedFrozenSet should do that. In contrast 
to that mutable objects, should disable the Hashable protocol by marking the 
supporting method `__hash__` as None. Since SortedFrozenSet supports the 
Equality, the rule is equal objects should have same hashcode, whereas unequal 
objects may return different hashcode.

### Set

<img src="static/set_abc.png" width="1000px" alt="Set Protocol from ABC">

The Set protocol from the abstract base class (ABC) inherits from the Collection 
protocol, which in turn implies Sized, Iterable, and Container protocols. We 
have already satisfied the requirements from these protocols. Furthermore, the 
Set protocol from the abstract base class introduces the set operations as 
mixin methods. These operations can be classified into two groups, namely 
relational operations, and set algebra operations.

<img src="static/set_abc_relational_operators.png" width="1000px" alt="Relational operator of Set protocol">

Here in the above image we are seeing the relational operations. We are seeing 
here at a glance, the mapping behind the infix symbols, and their corresponding 
dunder methods, which we need to implement to have those behaviors. There are 
some named methods, which the builtin `set` types provides. However, if we want 
them then we need to implement them ourselves. There is one difference between 
the infix operator implementation powered by the dunder methods, and the name 
methods. The infix operators need the operands to be of the same type, whereas 
the named methods can take any Iterable as arguments.

<img src="static/set_algebra_operators.png" width="1000px" alt="Algebra operator of Set protocol">

Apart from the relational operators builtin `set` type also provides some 
methods for the set algebra operations, as we see above. As before, if we use 
the infix notation operators, both the operands need to be of the same type. 
If we instead go for the named methods, they accept any Iterable types as 
arguments. Our SortedFrozenSet provides implementation of all the relational, 
and algebraic operations of the Set protocol, and hence conforms to it. 

In this implementation, we inherited from the Set base class of the collection.abc 
module. In case we need to implement a sorted mutable set, we need to inherit 
from the MutableSet base class, and provide implementation of the two abstract 
methods, namely `add`, and `discard` at the very least. Since in this case we 
are working with a mutable collection, we should also provide implementation 
of a `copy` method.

In this development of the SortdFrozenSet we have conformed to the following 
collection protocols,

* `Container` protocol for testing set membership.
* `Sized` protocol for determining the length.
* `Iterable` & `Iterator` for traversing through the collection.
* `Sequence` protocol for random access by index.
* `Set` protocol for implementing collection of distinct elements.

## Refactoring Notes

> In the previous implementation the index and count methods come from the 
> collection.abc.Sequence base class. The issue is, these implementations do 
> not take advantage of the fact, that SortedFrozenSet is an ordered collection 
> of distinct elements. Hence, these implementations perform a linear search 
> in over the underlying collection. We could instead override these methods 
> in the SortedFrozenSet class, and use binary search instead. That would 
> give us the runtime complexity of O(log n) instead of O(n). In order to 
> incorporate the binary search we'd make use of the `bisect` module from the 
> standard library.

> The same argument as above is also applicable in the same way for the dunder 
> method `__contans__`, which checks set-membership for us. This implementation 
> currently also relies on the linear search. We can improve this implementation 
> using the bisect module in the same way as above.
