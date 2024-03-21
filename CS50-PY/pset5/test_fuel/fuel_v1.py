def main():
    while True:
        try:
            text = input("Fraction: ").strip()
            temp = convert(text)
            result = gauge(temp)
        except (ValueError, ZeroDivisionError):
            continue
        print(result)
        break


def convert(fraction):
    if "/" not in fraction:
        raise ValueError

    nom, denom = fraction.split("/")
    nom, denom = float(nom), float(denom)   # raise ValueError itself

    if nom % 1 != 0 or denom % 1 != 0:
        # Values must be integer not float
        raise ValueError
    
    nom, denom = int(nom), int(denom)
    if nom < 0 or denom < 0:
        raise ValueError

    if denom == 0:
        raise ZeroDivisionError
    
    if nom > denom:
        raise ValueError
    
    return round(nom / denom * 100)


def gauge(percentage):
    if not isinstance(percentage, int):
        raise ValueError
    
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
