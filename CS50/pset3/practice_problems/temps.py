def main():
    temps = []
    temps.append({"city": "Austin", "temp": "97"})
    temps.append({"city": "Boston", "temp": "82"})
    temps.append({"city": "Chicago", "temp": "85"})
    temps.append({"city": "Denver", "temp": "90"})
    temps.append({"city": "Las Vegas", "temp": "105"})
    temps.append({"city": "Los Angeles", "temp": "82"})
    temps.append({"city": "Miami", "temp": "97"})
    temps.append({"city": "New York", "temp": "85"})
    temps.append({"city": "Phoenix", "temp": "107"})
    temps.append({"city": "San Francisco", "temp": "66"})

    
    temps = sort_cities(temps)
    print("\nAverage July Temperatures by City\n")

    for item in temps:
        print(f"{item['city'].ljust(10)} \t {item['temp'].rjust(5)}")


def sort_cities(temps):
    def merge_sort(temps):
        if len(temps) <= 1:
            return temps
        
        mid = len(temps) // 2
        left = merge_sort(temps[:mid])
        right = merge_sort(temps[mid:])

        return merge(left, right)


    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if int(left[i]["temp"]) >= int(right[j]["temp"]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result += left[i:]
        result += right[j:]

        return result


    return(merge_sort(temps))


if __name__ == "__main__":
    main()