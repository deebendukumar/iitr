#this function will return value of a character
#ord function is used to get the corrosponding unicode value
def decimal_to_base(c):
    print(f"unicode value of {c} {ord(c)} {ord('A')}");
    if c >= '0' and c <= '9':
        return ord(c) - ord('0');
    else:
        return ord(c) - ord('A') + 10;

def base_to_decimal(num):
    if(num >= 0 and num <= 9):
        return chr(num + ord('0'));
    else:
        return chr(num - 10 + ord('A'));

#This function converts any digit from base-N to base-10.
def to_decimal(base, number):
    result = 0
    power = 0
    for digit in reversed(str(number)):
        result += int(digit) * (base ** power)
        power += 1
    return result

def to_base_n(base, number):
    if number <= 0:
        return 0
    result = ""
    while number > 0:
        remainder = number % base
        print(f"remainder {remainder}")
        result = str(remainder) + result
        print(f"result {result}")
        number //= base
        print(f"number {number}")
    return result

print(f"decimal to base {decimal_to_base('B')}")

# print(to_decimal(8, 123))
# print(to_base_n(8, 47))