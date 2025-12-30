def fibonacci(n):
    if n == 0 or n == 1: # Stopping condition
        return n
    return fibonacci(n-1) + fibonacci(n-2) # Flow

if __name__ == '__main__':
    print(fibonacci(9))