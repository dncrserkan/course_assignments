import re
import sys


# IPv4 > #.#.#.# | # > 0-255

def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit(0)


def validate(ip=""):
    ip = ip.strip()
    regex = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    if nums := re.search(regex, ip):
        for num in nums.groups():
            if 0 > int(num)  or  int(num) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
