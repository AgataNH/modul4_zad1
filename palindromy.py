def is_palindrome(word):
    if word == word[::-1]:
        print('True')
    else:
        print('False')

is_palindrome('potop')