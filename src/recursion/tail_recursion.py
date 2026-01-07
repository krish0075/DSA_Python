count = 0

def greet():
    global count
    if count == 4:
        return
    count += 1
    greet()
    print("Krishna")

greet()
