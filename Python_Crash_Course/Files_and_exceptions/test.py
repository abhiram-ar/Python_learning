print("Give me two numbers I will divide them.")
print("enter q to quit")

while True:
    first_num = input("Enter first number : ")
    if first_num == "q":
        break

    sec_num = input("enter the second number : ")
    if sec_num == "q":
        break

    ans = int(first_num) / int(sec_num)
    print(ans)
