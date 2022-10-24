import re


def cut_first_letter(word):
    '''lalal'''
    word = word[1:]
    return word

print(cut_first_letter('$33'))


def leave_only_digits(word):
    '''ddddddddd'''
    return re.sub(r'[^0-9.]', '', word)


print(type(leave_only_digits('axe: $56.99')))
