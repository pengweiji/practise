#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Problem 1: What will be the output of the following program?
x = 1
def f():
	return x
print(x)
print(f())
# output:
#     1
#     1
'''

# Problem 2: What will be the output of the following program?
# 
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# def trace(f):
#     def g(*args):
#         print f.__name__, args
#         value = f(*args)
#         print 'function f id: ',id(f)
#         print 'return', repr(value)
#         return value
#     print 'function g id: ',id(g)
#     return g

# fib = trace(fib)
# print fib(3)
#print fib(3)
def trace(f):
    f.indent = 0
    def g(x):
        print '| '*f.indent+'|--',f.__name__,x
        f.indent += 1
        value = f(x)
        print '| '*f.indent+'|--','return', repr(value)
        f.indent -= 1
        return value
    return g

fib = trace(fib)
print fib(3)
output:
$ python /f/myProject/pythonCode/pengweiji/practise/about_function/about_function.py
|-- fib 3
| |-- fib 2
| | |-- fib 1
| | | |-- return 1
| | |-- fib 0
| | | |-- return 1
| | |-- return 2
| |-- fib 1
| | |-- return 1
| |-- return 3
3
