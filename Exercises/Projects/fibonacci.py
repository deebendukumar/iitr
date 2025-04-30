def print_fibonacci(n):
    previous = 0;
    current = 1;
    result = 0;
    for index in range(n):
        if (index == 0):
            result = 1;
        print(result);
        previous = current;
        current = result;
        result = previous + current;

print_fibonacci(10);