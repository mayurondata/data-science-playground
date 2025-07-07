# =============================================================================
# get our decorator function to accept arguements 
# lets say we want customisable prefixes before the print satatements
# within the wrapper  the wrapper , the argeuemnt to  the decorator is 
# the prefix
# =============================================================================
def prefix_decorator(prefix):
    def decorator_function(orignal_function):
        def  wrapper_function(*args,**kwargs):
            print(f'{prefix}Executed before {orignal_function.__name__}')
            a = orignal_function(*args,**kwargs)
            print(f'{prefix} Executed after {orignal_function.__name__}')
            return a 
        return wrapper_function
    return decorator_function

@prefix_decorator('Execute: ')
def display_info(name , age):
    print(f'Display info ran with {name}, {age} as argements')
    
    
    
display_info(name='naruto', age = 50)
display_info(name = 'ruyuk', age = 100)
