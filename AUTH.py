a = 5
b = 5.6
c = "слово"

m = [a, b, c]

# Словарь- dictionary

database = {
    'dim-akim': 'abcdf',
    'FominK': 'massefect',
    'Jack': 'Black',
    'Garolt': '12345678'
}


def check_password(login, password):
    if login in database:
        if database[login] == password:
            return True
    return False

password_count = 0
user_login = 'Garolt'


with open('pop-passwords.txt') as password_file:
    for line in password_file:
        user_password = line.strip()

        if check_password(user_login, user_password) is True:
            print(f'попытка № {password_count}: пароль {user_password} подошел')
            break

        password_count += 1

print(f'файл открыт, {password_count}')