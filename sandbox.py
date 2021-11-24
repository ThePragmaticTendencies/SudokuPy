#%%

def PowerDecoratorFactory(n):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return [x**n for x in result]
        return wrapper
    return decorator

def NElementFilterDecoratorFactory(n):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return result[::n]
        return wrapper
    return decorator

SecondPowerDecorator = PowerDecoratorFactory(2)
ThirdElementFilter = NElementFilterDecoratorFactory(3)

# @SecondPowerDecorator
@ThirdElementFilter
def printer(stream):
	print(stream)
    
printer(list(range(101)))
# %%
