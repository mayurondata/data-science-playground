# first-class functions basically mean that , here the functions are trated just 
# like anyother objects in python 
# everything is an object in python
# so we can return a funcion insted of a value , we can place functions 
# in arguements of another functions , we can also have functions inside of 
# functions , assigned to a variable 

#--->>> eg 


def square(x):
    return x*x


f = square(5)
print(square) # WILL return the funcitons 
print(f) # will return the answer 

# BUT WE can also do thus:
f = square # without the paranthersis and do 
f(5) # this will return 25 here we assigned the function to vaiable f 
# so now f is a function just like square 




# passing a function as an arguemnt to another funciton
def map(func, array):
    result = []
    for i in array:
        result.append(func(i))
    return result 
# func = lambda x : x**5
def func(x) :
    return x **5
x  =  map(func , [1, 2, 3, 4])
print(x)


# returning a function from another function 
# what the below function is basically doing is that 
#  the logger function takes in an arguement msg
# and inside that function there is anoher functions 
# that takes no arguements and prints 'Log' + msg(from the logger func)
# and we are returning the log_message 


def logger(msg):
    
    def log_message():
        print('Log' , msg)
        
    return log_message # there are no paranthesis here 
# we are not calling the log_message function 

log_hi = logger('hi')
# what we basically did is we created log_hi variable  = loggerfunc(msg = hi)
# as the logger is returning another funciton log_message
# now the log_hi varible is actually a log_message function 
# and we can call it like 
log_hi() # as this takes no arguements 
# this is basically called a closure and the log_hi variable 
# that is a function log_message remebers the message from the 
# logger function 




#e.g.2 

def html_tag(tag):
    def wrap_text(msg):
        return f'<{tag}> {msg} </{tag}>'
    return wrap_text



print_hi = html_tag('h1')
hi= print_hi('this msg is supercool')
hi
