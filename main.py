lst = [{"ID" : "1","status" : "undone","task" : "programming"},
       {"ID" : "2","status" : "undone","task" : "finish book"},
       {"ID" : "3","status" : "undone","task" : "learn English"}]
def add():
              new = input("Enter new task: ")
              newtask = {"ID" : len(lst)+1, "status" : "undone", "task" : new}
              lst.append(newtask)
              print(lst)
def delete():
    if temp == "e":
        if lst == []:
            print("No Task Availble!")
        else:
            print(lst)
            print("Which you want to delete?")
            for i in range(len(lst)):
                print(i+1,end=" , ")
            print()
            num = int(input("Choose number: "))
            for j in range(len(lst)):
                if num == j+1:
                    u = lst[num-1]
                    u["status"] = "done"
                    if u["status"] == "done":
                        lst.pop(num-1)
                    print()
                    print(lst)
while True:
    temp = input("Enter 's' for show, Enter 'a' for add and Enter 'e' for delete: ")
    if temp == "a":
          break
    elif temp == "e":
          break
    elif temp == "s":
          break
    else:
          print("Please type valid charecter!")
if lst == []:
     print("No Task Availble!")
elif temp == "a":
        add()
elif temp == "e":
        delete()
elif temp == "s":
       if lst == []:
            print("Empty To Do List!")
       else:
             print(lst)
