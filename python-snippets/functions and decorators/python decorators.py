# recap

def outer_function():
    message = 'Hi'

    def inner_function():  # the message variable was not creted inside the inner function
        # but still it remembered it this is called a free variable
        print(message)
    return inner_function()


outer_function()


def outer_function(msg):
    # message  = msg
    def inner_function():  # the message variable was not creted inside the inner function
        # but still it remembered it this is called a free variable
        print(msg)
    return inner_function  # if we do this without the paranthesis we


my_func = outer_function()
# my_func is basically inner function waiting to be called


hi_func = outer_function('hi')
hi_func()
hello_func = outer_function('hello')
hello_func()


# a decorator is a function that takes another function as an arguement
# adds some kind of functionality and returns another function all of this
# without altering the source code of the function   we passed  in


# a code thats almost identical to the above code
# we have changed the name of the outer function to decorator
# and the inner_function  to wrapper function

# whenever an instance of decorator_function is called
# it will create the inner_function(wrapperfunction) waiting to be
# called, and when its called it  will just print the message

# so insted of printing the message  we  passed  in we execute a
# function that we pass in, thats what a decorator does


def decorator_function(orignal_function):
    def wrapper_function():
        print(f'the warapper executed this before {orignal_function.__name__}')
        return orignal_function()
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)
decorated_display()

# so the decorated_display here is actually the wrapper_function
# waiting to be called/executed and when its executed it just
# runs the display function that we passed in
#  without spoiling our functionality of our display_funcitons
# we can come inside the wrapper function and add any kind of code
# we want

# ---->>> so far we are viewing decorators like this but the below code is
# simlar to setting our orignal function to the function wrapped within
# our decorator
# that is
# display =decorator_function(display) the decorater function
# is going to return the wrapper function waiting to be called and set that
# function to diaplay variable now when that display variable is called
# we actualty execuete the wrapper function


def decorator_function(orignal_function):
    def wrapper_function():
        print(f'the warapper executed this before {orignal_function.__name__}')
        return orignal_function()
    return wrapper_function


@decorator_function  # == display = decorator_function(display)
def display():
    print('display function ran')


display()  # this still has the warpper code insde the functions

# -----------------------------------------------------------------------------


def decorator_function(orignal_function):
    def wrapper_function(*args, **kwargs):
        # =============================================================================
        # we need  to mention *args , **kwargs in the wrappeer funcition as well
        # and not only for the orignal function
        # =============================================================================
        print(f'the warapper executed this before {orignal_function.__name__}')
        return orignal_function(*args, **kwargs)
    return wrapper_function


@decorator_function  # == display = decorator_function(display)
def display():
    print('display function ran')


@decorator_function
def display_info(name, age):
    print('display_info ran with ({} , {}) arguements'.format(name, age))


display()

display_info('john', 25)

# -- if we had tried to put decorator function above the display_info function
# without mentining the *args , **kwargs , it would have thrown an error
# as the display_info function takes in two arguemets we could have passsed name ,
# age in the wrapper function , and the same in the orignal function but if weran
# display() it wouldnt have run as it requires not arguemts but we mentioned2
# so in order to make it more generalised we did * args  ,**kwargs


# =============================================================================
# =============================================================================
# CLASSES AS DECORATORS INSTEAD OF  FUNCTIONS
# =============================================================================
# instead of decorating the functions  with decorator functions
# we will decorate our functions with decorator classes
# creating a class decorator that has the exact same functionality


class decorator_class():
    def __init__(self, orignal_function):
        self.orignal_function = orignal_function
# this will tie our function with the instance of the class
# =============================================================================
# the call method below is a special method that will run
# whenever  , the class is called
# =============================================================================

    def __call__(self, *args, **kwargs):
        print('call method executed this with {}'.format(args, kwargs))
        return self.orignal_function(*args, **kwargs)


@decorator_class  # == decorator_class(display)
def display():
    print('display function ran')


@decorator_class
def display_info(name, age):
    print('display_info ran with ({} , {}) arguements'.format(name, age))


display()
display_info('john', 544)
# =============================================================================
#
# =============================================================================
