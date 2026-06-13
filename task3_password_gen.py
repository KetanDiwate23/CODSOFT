# Password Generator
# Lets user pick length and what character types to include

import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    pool = list(string.ascii_lowercase)

    # build character pool based on user prefs
    if use_upper:
        pool += list(string.ascii_uppercase)
    if use_digits:
        pool += list(string.digits)
    if use_symbols:
        pool += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

    if not pool:
        return None

    # make sure at least one char from each selected type appears
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"))

    # fill the rest randomly
    while len(password) < length:
        password.append(random.choice(pool))

    random.shuffle(password)
    return "".join(password)

def check_strength(pwd):
    score = 0
    if len(pwd) >= 12:
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in pwd):
        score += 1

    labels = {4: "Strong 💪", 3: "Good", 2: "Fair", 1: "Weak", 0: "Very Weak"}
    return labels.get(score, "Unknown")

def main():
    print("=== Password Generator ===\n")

    while True:
        try:
            length = int(input("Password length (min 6): "))
            if length < 6:
                print("Please use at least 6 characters.")
                continue
            break
        except ValueError:
            print("Enter a number.")

    print("\nCustomize your password:")
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    print()
    for _ in range(3):  # generate 3 options to pick from
        pwd = generate_password(length, use_upper, use_digits, use_symbols)
        if pwd:
            print(f"  {pwd}  [{check_strength(pwd)}]")

    print("\nGenerate more? (y/n): ", end="")
    while input().lower() == "y":
        print()
        for _ in range(3):
            pwd = generate_password(length, use_upper, use_digits, use_symbols)
            if pwd:
                print(f"  {pwd}  [{check_strength(pwd)}]")
        print("\nGenerate more? (y/n): ", end="")

    print("\nDone!")

if __name__ == "__main__":
    main()
