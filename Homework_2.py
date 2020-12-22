user_info = input("Please enter your information in this format: Name, Last Name, Age, Year of Birth: ")

user_info = list(user_info.split(", "))

for i in user_info:
    print(i)

if int(user_info[2]) < 18:
    print("You can't go outside because it's too dangerous.")
elif int(user_info[2]) >= 18:
    print("You can go out to the street.")
    