import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r"https?://(?:www\.)?youtube\.com/embed/([^\"]+)"
    source = re.search(regex, s)
    if source:
        shorten = "https://youtu.be/" + source.group(1)
        return shorten


if __name__ == "__main__":
    main()
