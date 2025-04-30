import math

def calculate_ln(n, base) -> float:
    """
    Calculate the log value of n
    """
    result = 0
    temp = 0
    mid = 0

    if n == base:
        return 1
    elif n < base:
        lower_limit = 0
        upper_limit = 1

    while result < n:
        mid = calculate_midpoint(upper_limit, lower_limit);
        if(base ** mid) > n:
            upper_limit = mid;
        else:
            lower_limit = mid;
        result = base ** mid;
        print(f"lower limit {lower_limit} upper limit {upper_limit}");
    
    print(f"lower limit {lower_limit} upper limit {upper_limit}");
    return base ** mid;

def calculate_midpoint(ul, ll) -> float:
    return (ul + ll) / 2

# Usage
print(f"{calculate_ln(8, 10)}")
print(math.log(8, 10))
