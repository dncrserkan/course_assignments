greeting = input("Greeting: ").lstrip().lower()

if greeting == "":
    print("say somthing next time")
elif greeting[:5] == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else :
    print("$100")
