'''
a variable is only available from inside the region it is created is known as scope 

a local variable  is a varibale created in side a function and it gives acess to the function only is  a local varibale 
'''
def fun():
    x = '790560XXXX'
    y = 'call me anytime '
    print(x,y)
fun()
#x and y are here local scope 
'''
Function Inside Function
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

Example
The local variable can be accessed from a function within the function:
'''

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

'''
Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

Example
A variable created outside of a function is global and can be used by anyone:

'''
x = 5000
def myn():
   print (x)

myn()

'''global keyword is used to set a value of a varible global so that it can be used any where and we can also use 
global keyword any where even inside a function 
'''

def v():
   global x 
   x = 'tmkc = tu  mam ki cat hai'
def tmkc():
   print (x)
v()
tmkc()

'''
Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.

Example
If you use the nonlocal keyword, the variable will belong to the outer function:
'''
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())