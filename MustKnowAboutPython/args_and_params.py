# def complicated_functions(x,y,z=None): # x,y,z are called parameters when defining functions, providing default value to any parameter makes it a optional one
#     print(x,y)

# def complicated_functions(*args):
#     print(args)

# def complicated_functions(*args,**kwargs): # postional args and keyword arguments, used when you want to make functions dynamic
#     print(args,kwargs)

def complicated_functions(a,b,c=True,d=False):
    print(a,b,c,d)
    pass

# complicated_functions(2,1)
# complicated_functions(y=2,x=1)
# complicated_functions(1,z=2,y=3) # x,y,z are called arguments used for functions calling
# complicated_functions(1,y=3) # after giving default value, z becomes optional argument
    
# complicated_functions(1,3,2,3,4,5,1) # after postional arguments, the other values are unpacked and stored in a tuple

# complicated_functions() # passing no argument also works with *args params

    
# complicated_functions(1,2,3,x=1,s="hello",b=True) # keyword args stored in dictionary and returned

complicated_functions(*[1,2],**{"c":"Hello","d":"cool"})
