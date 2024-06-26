from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    
    last= input("Please give me last name: ")
    if last == "q":
        break

    formated_name = get_formatted_name(first, last)
    print(f"\t Neatly  formatted name : {formated_name}")
