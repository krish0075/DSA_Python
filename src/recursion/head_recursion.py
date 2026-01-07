count = 0

""" 
    This is a classical example of head recursion 
    where task is performed and then
    recursive call is done at the end.
"""
def greet():
    global count
    if count == 4:
        return
    count += 1
    print("Krishna")
    greet()

greet()
