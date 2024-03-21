exp = input("Expression: ").strip()

x, y, z = exp.split(" ")
x, z = float(x), float(z)

if y == "+":
    print(f"{ x + z :.1f}")
elif y == "-":
    print(f"{ x - z :.1f}")
elif y == "*":
    print(f"{ x * z :.1f}")
elif y == "/":
    print(f"{ x / z :.1f}")
