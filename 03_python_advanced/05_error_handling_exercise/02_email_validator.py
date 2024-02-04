from re import findall, match


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


class NoDotBeforeDomainError(Exception):
    pass


class InvalidCharacterInDomainError(Exception):
    pass


class InvalidCharacterInNameError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_SYMBOLS_COUNT = 4
pattern_name = r'\w+'
email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    name = email.split("@")[0]
    if not match(pattern_name, name):
        raise InvalidNameError("Name must contain only letters, digits, and underscores!")

    if len(name) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters!")

    if '.' not in email.split("@")[-1]:
        raise NoDotBeforeDomainError("Invalid email format: No dot before domain!")

    if not all(c.isalnum() or c == '.' for c in email.split("@")[-1]):
        raise InvalidCharacterInDomainError("Invalid characters in the domain!")

    if not all(c.isalnum() or c == '_' or c == '.' for c in name):
        raise InvalidCharacterInNameError("Invalid characters in the name!")

    if email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")

    print("Email is valid")
    email = input()
