Task 1
while True:
    age = int(input("Enter your age: "))
    
    if age < 18:
        print("You are a minor.")
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice == "no":
            break
    elif age >= 18 and age < 60:
        print("You are an adult.")
        break
    else:
        print("You are a senior citizen.")
        break

Task 2
while True:
    vehicle = input("Enter the name of a vehicle: ").lower()
    if vehicle == "bus":
        print("Finally, the wait is over!")
        break
    else:
        print("Waiting...")

Task 3
while True :
    fruit = input("Enter a fruit name: ")
    if fruit.lower() == "apple" :
        print("You got it")
        break
    else :
        print("Try again")

Task 4
password = "open sesame"
while True :
    user = input("Enter the password: ")
    if user == password :
        print("acess granted")
        break
    else :
        print("Wrong.Try again!")

TAsk 5 
weekend = "Sunday"
while True :
    user = input("Enter any day of the week: ")
    if user != weekend.lower() :
        print("Its not the weekend yet")
    else:
        print("Enjoy your weekend!")
        break

Task 6
import random
a = random.randint(1,10)
attempts = 0
while True :
    user = int(input("Guess the number: "))
    attempts += 1 
    if user == a :
        print("You guessed the correct number")
        break
    elif user > a :
        print("Try lower")
    elif user < a :
        print("Try Higher")
    else :
        print("Wrong Try again!")

Task 7
username = "admin"
password = "admin123"
chance = 0
max_attempts = 3
while chance < max_attempts:
    rahh = input("Enter your username: ")
    password_rahh = input("Enter your password: ")
    if password_rahh == password and rahh == username:
        print("You are logged in.")
        break
    else:
        chance+=1
        print(f'Invalid username or password, you have {max_attempts-chance} attempts left')
if chance == max_attempts:
    print("You are temporarily blocked. You have exceeded the number of attempts.")

Task 8
import random
while True :
    a = random.randint(1,30)
    b = random.randint(1,30)
    print(f'Multiplication of {a} and {b} is: ')
    num = int(input("Enter the number: "))
    if num == a*b :
        print("correct")
        num = input("Do you want to continue?(yes/no)").lower()
        if num == 'yes':
            continue
        else :
            break
    else :
        print("incorrect")

Task 9
while True:
    user = input("Enter a number: ")
    if user.lower() == "exit":
        break
    if user.isdigit():
        num = int(user)
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            print("The number is prime.")
        else:
            print("The number is not prime.")
    else:
        print("Please enter a valid number.")

Task 10
secret = "python"
while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == "quit":
        break
    elif guess.lower() == secret :
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Incorrect, try again.")

Task 11
count = 0
while count < 3:
    phrase = input("Enter a phrase: ").lower()
    if phrase == "good luck":
        count += 1
        print(f"You typed the same word {count} times.")
        if count == 3:
            print("You typed good luck three times.")
    else:
        print("Keep going!")
