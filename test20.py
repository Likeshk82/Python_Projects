import random
import string
def pass_rand(l,l1,n,s):
    c=""
    if l1:
        c+=string.ascii_letters
    if n:
        c+=string.digits  
    if s:
        c+=string.punctuation 
    if not c:
        raise ValueError("At least one character type must be selected.")
    password="".join(random.choice(c) for i in range(l))
    return password
def main():
    print("Welcome to the Command-Line Password Generator!")
    while True:
        try:
            l=int(input("Enter the desired password length (e.g., 8, 12): "))
            if l<=0:
                raise ValueError("Password length must be greater than 0.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
    l1=input("Include letters? (y/n): ").strip().lower() == "y"
    n=input("Include numbers? (y/n): ").strip().lower() == "y"
    s=input("Include symbols? (y/n): ").strip().lower() == "y"
    try:
        password=pass_rand(l,l1,n,s)
        print("\nYour randomly generated password is:")
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()