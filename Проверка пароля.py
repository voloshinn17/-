from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits


def verification(login, password, success, failure):
    checks = [
        (lambda c: c in ascii_letters, 'в пароле нет ни одной буквы'),
        (lambda c: c in ascii_uppercase, 'в пароле нет ни одной заглавной буквы'),
        (lambda c: c in ascii_lowercase, 'в пароле нет ни одной строчной буквы'),
        (lambda c: c in digits, 'в пароле нет ни одной цифры'),
    ]

    for func, message in checks:
        if not any(map(func, password)):
            return failure(login, message)
 
    success(login)