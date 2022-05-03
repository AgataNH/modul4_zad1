def palindromy(a):
    b = a[::-1]
    if a == b:
        print('True')
    else:
        print('False')

palindromy('potopik')