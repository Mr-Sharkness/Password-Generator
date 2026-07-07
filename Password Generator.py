import datetime
from secrets import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

question_and_pools = [
    ('Should numbers be included? (y/n) ', digits),
    ('Should lowercase letters be included? (y/n) ', ascii_lowercase),
    ('Should uppercase letters be included? (y/n) ', ascii_uppercase),
    ('Should punctuations be included? (y/n) ', punctuation),
]

def get_number_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
            print('Please enter a number greater than 0.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

def request():
    while True:
        chars = ''
        for question, pool in question_and_pools:
            ans = input(question).strip().lower()
            if ans in ['y', 'yes']:
                chars += pool

        if chars:
            return chars
        print("\n[!] You must select at least one character type! Try again.\n")

def generate_password(count, length, chars):
    return ["".join(choice(chars) for _ in range(length)) for _ in range(count)]

def save_password(passwords):
    ans = input("Do you want to save these passwords to a file? (y/n) ").strip().lower()
    if ans == 'y':
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"password_{timestamp}.txt"

        try:
            with open(filename, 'w', encoding = "utf-8") as f:
                f.write("\n".join(passwords) + "\n")
            print(f"Passwords successfully saved to {filename}.")
        except IOError as e:
            print(f"Failed to save passwords to {filename}: {e}")
    else:
        print("Passwords were not saved.")

def main():
    cnt_pass = get_number_input('How many passwords do you want? ')
    len_pass = get_number_input('How long do you want? ')

    chars = request()

    password = generate_password(cnt_pass, len_pass, chars)

    print("\nYour generated password is: ")
    print(*password, sep='\n')
    print("-" * 20)

    save_password(password)

if __name__ == '__main__':
    main()


