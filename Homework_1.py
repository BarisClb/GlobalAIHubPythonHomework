user_info = input("Please enter your information in this format: Name, Surname, Year of Birth, Height, Weight : ")

user_info = list(user_info.split(","))

user_name = user_info[0]
user_surname = user_info[1]
user_age = 2020 - int(user_info[2])
user_height = user_info[3]
user_weight = user_info[4]

print(f"Hello {user_name}{user_surname}, you are {user_age} years old, your height is{user_height} cm and you weight{user_weight} kg.")
