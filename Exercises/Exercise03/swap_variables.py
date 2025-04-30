def swap(x, y):
    x = x + y;
    y = x - y;
    x = x - y;
    print(f"{x}, {y}")

def swap(arr):
    for element in arr:
        print(element)
        
    arr[0] = arr[0] + arr[1] + arr[2];
    arr[1] = arr[0] - (arr[1] + arr[2]);
    arr[2] = arr[0] - (arr[1] + arr[2]);
    arr[0] = arr[0] - (arr[1] + arr[2]);
    print(arr);

arr = [10, 20, 30]
#arr = [20, 30, 10]
swap(arr);
