import random
import string

def password_generator(length = 12):

  characters = string.ascii_letters + string.digits + string.punctuation

  password = ''.join(random.choice(characters) for _ in range(length))
    
  return password
  
if __name__ == "__main__":
  password_length = int(input("Enter password length: "))

  if password_length < 6:
    print("Password must be longer than 6 characters. Try again.")
  else:
    generate_password = password_generator(password_length)
    print("Password generated:", generate_password)
