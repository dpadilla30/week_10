#while loops = execute some code WHILE some condition remains true

# name = input ("enter your name")

# while name == "":
#     print("You did not type in your name")
#     name=input("enter your name") #if this is removed it makes an infinit loop which is bad #iterate means looping over something
# print(f"hello{name}")

# age = int(input("enter your age: "))

# while age < 0:
#     print("Age cant be negative")
#     age = int(input("enter your age: "))

# print(f"you are {age} years old")

# food = input("enter a food that you like (q to quit): ")

# while not food == "q":
#     print(f"you like {food}")
#     food = input ("enter another food you like (q to quit): ")

# print("bye")

# num = input("enter a number between 1 - 10: ")

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"your number is {num}")

#for loops = execute a block of code a fixed number of times
# you can iterate over a range, string, sequence, etc

# credit_card = "1234_5678-9012_3456"

# for x in credit_card:
#     print(x)

# for x in range(1,21):
#     if x == 13 or x == 15 or x == 20:
#         continue
#     else:
#         print(x)

# for x in range(1,21):
#     if x == 13 or x == 15 or x == 20:
#         break
#     else:
#         print(x)

# horror_charaters = ("Freddy Kruger","Jason Voorhess","Michael Myers","Pennywise","Chucky")
# for x in horror_charaters:
#     if x == "Jason Voorhess":
#         continue
#     else:
#         print(x)

horror_movies = ("Psycho","Rosemary","The Texas Chain Saw Massacre","The Shining","The Exorcist","Jaws","Alien")
for x in horror_movies:
    if x == "Jaws":
        break
    elif x == "Rosemary":
        x = "Halloween"
    print(x)





    

