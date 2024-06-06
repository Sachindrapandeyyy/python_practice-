'''
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py:
'''
import importmod 

importmod.greet("sachin")
'''
Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

'''
a= importmod.person1['age']
print(a)
#output is 36 as in importmod file 

'''
Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:'''

"""

import mymodule as mx

a = mx.person1["age"]
print(a)

"""
'''Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.
'''
import platform
x = platform.system
print(x)

'''
Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
'''
import platform

x = dir(platform)
print(x)

print('-------------------------------------------------------------------------------------------------------------')

import math
y = dir(math)
print (y)