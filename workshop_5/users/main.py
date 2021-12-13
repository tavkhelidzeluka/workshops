from user import User

def main():
    username = input("enter username: ")
    password = input("enter password: ")

    user = User.validate(username, password)


    print(user)




if __name__ == '__main__':
    main()
