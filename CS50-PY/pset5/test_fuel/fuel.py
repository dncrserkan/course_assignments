while True:
    try:
        text = input("Fraction: ").strip()
        nom, denom = text.split("/")
        
        nom, denom = float(nom), float(denom)
        if (nom % 1 != 0) or (denom % 1 != 0):
            raise ValueError
        
        nom, denom = int(nom), int(denom)
        if nom > denom:
            continue

        result = int(nom / denom * 100)
        if result == 100:
            print("F")
        elif result == 0:
            print("E")
        else:
            print(f"{result}%")
        
        break

    except ValueError:
        pass

    except ZeroDivisionError:
        pass
