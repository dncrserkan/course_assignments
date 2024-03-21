def main():
    while True:
        try:
            noe = int(input("Number of elements: "))
            if noe > 0:
                break
        except ValueError:
            continue
    
    arr = []
    for i in range(noe):
        while True:
            try:
                arr.append(int(input(f"Element {i}: ")))
                break
            except ValueError:
                continue

    print(f"The max value is {maximum(arr, noe)}")
    # In python we don't need maximum function because there is a built in max() function

def maximum(arr, noe):
    temp = arr[0]
    for i in range(noe):
        if temp >= arr[i]:
            continue
        else:
            temp = arr[i]
    return temp


if __name__ == "__main__":
    main()
