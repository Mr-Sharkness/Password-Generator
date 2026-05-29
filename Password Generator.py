from random import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

question = ['Should numbers be included? (y/n) ',
            'Should lowercase letters be included? (y/n) ',
            'Should uppercase letters be included? (y/n) ',
            'Should punctuations be included? (y/n) ']

answer = [digits, ascii_lowercase, ascii_uppercase, punctuation]

cnt_pass = int(input('How many passwords do you want? '))
len_pass = int(input('How long do you want? '))

def request():
    chars = ''
    for i in range(len(question)):
        ans = input(question[i]).lower()
        if ans == 'y':
            chars += answer[i]
    return chars

def generate_password(len_pass, chars):
    lst_pass = []
    for _ in range(cnt_pass):
        password = ''
        for _ in range(len_pass):
            password += choice(chars)
        lst_pass.append(password)
    return lst_pass


chars = request()
print(*generate_password(len_pass, chars), sep='\n')



