# Iterators and Collection Protocols

This repository is created in order to consolidate the study, and practices for 
the Python Iterators, and other collection protocols. Following is, how the 
Iterator, and Iterable protocols are defined.

<img src="static/iterationprotocols.png" width="1000px" alt="Iterator and Iterable Protocols">

* The builtin `iter` function calls the `__iter__` method of the type. 
* The builtin `next` function calls the `__next__` method of the type.

The image also demonstrates, that all Iterators also conforms to the Iterable 
protocol. This is the reason, we can use and Iterator as Iterable with for 
loops.