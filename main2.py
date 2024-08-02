
id = 1
def add():
    newtodo = input("Enter new task: ")
    with open("TodoFile.txt","a") as file:
        file.write("\n"f'{id}       Undone      {newtodo}"')
    print("New task added")
    


def delete():
    num1 = input("Enter ID: ")
    with open("TodoFile.txt","r") as file:
        lines = file.readlines()
    with open("TodoFile.txt","w") as file:
        for line in lines:
            if num1 not in line:
                file.write(line)
    print("Task deleted successfully")


def edit():
    num2 = input("Enter ID: ")
    with open("TodoFile.txt","r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if num2 in line:
                  if "undone" in line:
                        line = line.replace("undone","done")
                  else:
                        line = line.replace("done","undone")
            file.write(line)  
    print("Status changed successfully")


def show():
    with open("TodoFile.txt","r") as file:
        for line in file:
            print(line)

while True:
    choise = input("Show | Add | Status Edit | Delete | Qiute [s/a/e/d/q] : ")
    if choise == "s":
        show()
    elif choise == "a":
        add()
        id += 1
    elif choise == "e":
        edit()
    elif choise == "d":
        delete()
    elif choise == "q":
        break
    else:
        print("Please type valid character!")

