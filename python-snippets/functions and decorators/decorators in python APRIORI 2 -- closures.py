# CLOSUres 
# a closure is an inner function that remembers and has access to variables and argurements
 # inthe local scope in which it was created ,even after the outer function was executed 

def outer_func():
    message = 'Hi'
    
    
    def inner_func():
        print(message)
        
        
    return inner_func() # with paranthesis 
        
outer_func()
# if we run the outer function above, as  it executes and doesnot take any parameters 
# whathappened is that we ran the function it came inside the outer function 
# assigned the message = 'Hi' , nad we created the inner function within
# out outer function , which prints the message variable which we call a free variable 
# and then we are returning the inner_func()(executed) and so outer_func() returned 'Hi'
# if the code was like this 

def outer_func():
    message = 'Hi'
        
    def inner_func():
        print(message)
                
    return inner_func # withot  paranthesis 

outer_func() # this will retnrn the inner function as we are returning inner_funciton from the outer_function and so this will not return the value 'Hi'
# function and if we do 
my_func = outer_func() 
my_func() # this will return 'hi' 
my_func() # all of these will retuen Hi
my_func()
my_func()
my_func()

# we are done with the execution of our outer function, but the inner function that we returnrd still has access to the message variable it has 
# thats what a closure is 

# --->>> adding parameters to our functions 

def outer_func(msg):
	message = msg
		
	def inner_func():
		print(message)

	return inner_func


hi_func = outer_func('hi')
hello_func = outer_func('hello')
hi_func()
hello_func()
# a qick note is that the inner function donot takes
 # any arguments so while calling hi_func() we dont need to pass any
# parameters


# a practical example 
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

add = lambda *x : sum(x)

def sub(x ,y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3 ,2 )
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)
 

