
import secrets
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length (minimum 12): "))

if length < 12:
    print("Please choose at least 12 characters.")
else:
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    print("\nYour generated password is:")
    print(password)
