# def print_file(file_name):
#     with open(file_name,"r") as f:
#         print(f.read())
# print_file("love.py")

# def write_file(file_name):
#     with open(file_name,"w+") as f:
#         new_val = input("enter new value: ")
#         f.write(new_val)
#         print(f.read())
# write_file("love.txt")


# def make_list(file_name, name):
#     data = input("Enter data: ")
#     with open(file_name, "w+") as f:
#         name.append(data)
#         for item in name:
#             f.write(item + "\n")
#         f.seek(0)
#         print(f.read())

# # Example usage
# lst = []
# make_list("love.py", lst)


# lst = [12,45,78,99]
# index = int(input("enter index: "))
# word = input()
# if word == "c":
#     with open("love.txt","a") as f:
#         new_change = input()
#         f.write(new_change)
        

# val = 0
# with open("babloo.txt","r") as f:
#     for lines in f:
#         val += 1
# print(val)
        
# Id = 5
# task = input("nter new task: ")
id = input()
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