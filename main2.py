Todo = [{"ID" : 1,"status" : "undone","task" : "programming"},
       {"ID" : 2,"status" : "undone","task" : "finish book"},
       {"ID" : 3,"status" : "undone","task" : "learn English"},
       {"ID" : 4,"status" : "undone","task" : "burn calories"} ]
id = 5
def add():
    newtodo = input("Enter new task: ")
    new = {"ID" : id, "status" : "undone", "task" : newtodo}
    Todo.append(new)
    print("New task added")
    


def delete():
    num1 = int(input("Enter ID: "))
    Todo.pop(num1 - 1)
    print("Task deleted successfully")


def edit():
    num2 = int(input("Enter ID: "))
    temp = Todo[num2 - 1]
    temp["status"] = "done"
    print("Status changed successfully")


def show():
    for i in Todo:
        print(f"{i["ID"]}\t{i["status"]}\t{i["task"]}")


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

