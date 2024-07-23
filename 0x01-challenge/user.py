#!/usr/bin/python3
"""
User class
"""


class User():
    """ Documentation """

    def __init__(self, email):
        """ Documentation """
        self.email = email

    @property
    def email(self):
        """ Documentation """
        return self.__email

    @email.setter
    def email(self, value):
        """ Documentation """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        if value == "":
            raise ValueError("email is empty, use this temp <example@dom.com>")

        # means that value is finally valid for email
        self.__email = value


if __name__ == "__main__":

    u = User("john@snow.com")
    print(u.email)
