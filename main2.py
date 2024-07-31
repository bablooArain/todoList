Todo = [{"ID" : 1,"status" : "undone","task" : "programming"},
       {"ID" : 2,"status" : "undone","task" : "finish book"},
       {"ID" : 3,"status" : "undone","task" : "learn English"},
       {"ID" : 4,"status" : "undone","task" : "burn calories"}]
id = 5
def add():
    newtodo = input("Enter new task: ")
    with open("TodoFile.txt","a") as file:
        file.write("\n"f'{id}     Undone     {newtodo}"')
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
            if id in line:
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

    # for i in Todo:
    #     print(f"{i["ID"]}\t{i["status"]}\t{i["task"]}")


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

