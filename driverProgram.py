import mods
import os
import backend as bk
def main():
    while True:
        os.system('clear')
        print ("1) Faculty Login")
        print ("2) Student Login")
        print ("3) Register student")
        print ("4) Exit")
        ch = input("Enter your Choice : ")
        if ch == '1':
            os.system('clear')
            usr = input("Enter Email : ")
            pwd = input('Enter Password : ')
            if bk.facultyLogin(usr, pwd):
                while True:
                    os.system('clear')
                    print ('1) Show Student Details')
                    print ('2) Record of Submitted Assignment')
                    print ('3) Show Cheated Assignment Record')
                    print ('4) Logout')
                    ch = input('Enter your choice : ')
                    if ch == '1':
                        bk.showStudent()
                        input()

                    elif ch == '2':
                        bk.showFileRecord()
                        input()

                    elif ch == '3':
                        bk.showCheatRecord()
                        input()

                    elif ch == '4':
                        print ("Logout Successfully...")
                        input()
                        break

            else:
                print ("Wrong Credentials!!!")
                input()

        elif ch == '2':
            usr = input("Enter Email : ")
            pwd = input('Enter Password : ')
            if bk.studnetLogin(usr, pwd):
                while True:
                    os.system('clear')
                    print ('1) Upload your Assignment')
                    print ('2) Check your status')
                    print ('3) Logout')
                    ch = input('Enter your Choice : ')
                    if ch == '1':
                        mods.main(usr)
                        input()

                    elif ch == '2':
                        bk.showParticularRecord(usr)
                        input()

                    elif ch == '3':
                        print ('Logout Successfully')
                        input()
                        break

            else:
                print ("Wrong Credentials!!!")
                input()

        elif ch == '3':
            os.system('clear')
            bk.registerStudent()
            input()

        elif ch == '4':
            break

        elif ch == ' ':
            continue
        else:
            print ("Invalid Choice !!!")
            input()


main()