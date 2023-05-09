def f(*args, **kwargs):  # any number of args as a tupple/list, and any number of key word args as a dictionary
    print("Named:", kwargs)


f(100, 50, 25, galleons=100, sickles=50, knuts=25)
