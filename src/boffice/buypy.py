"""
BuyPy

A command-line backoffice application. This is an interactive 
shell application

(c) Joao Galamba, 2022
"""

import sys
from subprocess import run
from getpass import getpass

import db


def main():
    user_info = exec_login()

    while True:
        cls()
        print(f"\nBem vindo {user_info['firstname']}\n")
        print("U - Menu 'Utilizador'")
        print("P - Menu 'Produto'")
        print("B - Menu 'Backup'")
        print("S - Sair do BackOffice")
        print("L - Logout do BackOffice")

        print()
        option = input(">> ")

        if option.lower() == 'U':
            print("Menu UTILIZADOR")
        elif option.lower() == 'S':
            print("O BackOffice vai terminar")
            sys.exit(0)
        else:
            print(f"Opção <{option}> inválida ")
#:

def exec_login():
    """
    Asks for user login info and then tries to authenticate the user in 
    the DB.
    Stores user data the data in the local config file 'config.ini'.
    """
    while True:
        username = input("Username      : ")
        passwd = getpass("Palavra-passe : ")
        user_info = db.login(username, passwd)
        if user_info:
            break
        print("Invalid authentication")
        print()
    return user_info
#:

def cls():
    # pylint: disable=subprocess-run-check
    if sys.platform in ('linux', 'darwin', 'freebsd'):
        run(['clear'])
    elif sys.platform == 'win32':
        run(['cls'], shell=True)
#:

if __name__ == '__main__':
    main()
#:
