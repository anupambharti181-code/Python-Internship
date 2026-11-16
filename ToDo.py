# To-do List App
tasks=[]

while True:
    print("/n1.add task")
    print("2.view task")
    print("3.exit")

    choice=input("enter choice:")

    if choice=="1":    
       task=input("enter task:")
       tasks.append(task)
       print("task added")

    elif choice=="2":
       print(tasks)

    elif choice=="3":
        print("Thank you!")
        break

    else:
        print("wrong choice!")

