import os
from time import sleep
from os import system

current_dir = os.getcwd()
time_to_sleep = 4

def chdir(dir):
    os.chdir(dir)
    print("the path had been successfully changed")
    sleep(time_to_sleep)

def del_file(filename):
    os.remove(current_dir + "/" + filename)
    print("it has been successfully deleted")
    sleep(time_to_sleep)

def read_file(filename):
    while True:
        file_to_read = open(filename, mode="r")

        contents = file_to_read.read()
        print(contents)
        
        print("enter 'yes' if you are done")
        read_file_inp = input("")
        if read_file_inp == "yes" or read_file_inp == "Yes" or read_file_inp == "YES":
            file_to_read.close()
            break
        else:
            system("cls")
            print("please enter 'yes'")
            sleep(time_to_sleep)
    

def tutorial():
    print("""
    1 createing file
    before creating file you need to change the diratory(place)
    by pressing c and pasting the location and you can only 
    create text file
    
    2 reading file
    this will only work if the file is text file
    """)
    sleep(20)


def create_file(filename):
    os.mkdir(filename)
    print("the file has been successfully made")


def main():
    while True:
        system("cls")
        print("j terminal by Jason")
        print("change dir[c]")
        print("make an file[m]")
        print("delete file[d]")
        print("read file[r]")
        print("tutorial[t]")
        print("")
        print("* read file can only be txt file")
        inp = input(">> ")
        if inp == "c" or inp == "C":
            system("cls")
            print("enter the directory")
            change_dir_input = input(">> ")
            chdir(change_dir_input)

        elif inp == "m" or inp == "M":
            system("cls")
            print("enter the folder name")
            file_name_input = input(">> ")
            create_file(file_name_input)

        elif inp == "t" or inp == "T":
            system("cls")
            print(tutorial())

        elif inp == "d" or inp == "D":
            print("enter the folder name")
            del_file_input = input(">> ")
            del_file(del_file_input)

        elif inp == "r" or inp == "R":
            print("enter the text file")
            read_file_inp = input(">> ")
            read_file(read_file_inp)

        else:
            system("cls")
            print("please enter an valid choice")
            sleep(5)
            system("cls")



if __name__ == "__main__":
    main()