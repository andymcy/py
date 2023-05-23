import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character):
        self.illegal_character = illegal_character

    def __str__(self):
        return f"The username contains an illegal character: '{self.illegal_character}'"


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __init__(self, missing_character):
        self.missing_character = missing_character

    def __str__(self):
        return f"The password is missing a character: '{self.missing_character}'"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    if not all(c.isalnum() or c == '_' for c in username):
        raise UsernameContainsIllegalCharacter(next(c for c in username if not c.isalnum() and c != '_'))
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()
    required_characters = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
    for characters in required_characters:
        if not any(c in password for c in characters):
            missing_character = characters[0] if characters != string.punctuation else 'special character'
            raise PasswordMissingCharacter(missing_character)
    print("OK")


def main():
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            check_input(username, password)
            break
        except UsernameContainsIllegalCharacter as e:
            print(e)
        except UsernameTooShort as e:
            print(e)
        except UsernameTooLong as e:
            print(e)
        except PasswordMissingCharacter as e:
            print(e)
        except PasswordTooShort as e:
            print(e)
        except PasswordTooLong as e:
            print(e)


if __name__ == "__main__":
    main()
