todo = []

def listTodo():
	val = input("Would you like to see your todos [y/N]? ")
	if val == 'y':
		showTodo()

def showTodo():
	if len(todo):
		print("Here are your todos:")
		for item in todo:
		    print(item)
	else:
		print("You have nothing in your todo list!")

def addTodo():
	val = input("Would you like to add a todo [y/N]? ")
	item = ""
	priority = ""
	dueBy = ""
	if val == 'y':
		task = input("\nPlease type the task: ")

		print("\nNow it is time to add the priority of the task, 1 is urgent, 5 is not important")
		priority = input("Please list the priority of the task: ")

		dueBy = input("\nPlease enter the date the task is due by: ")

		print("\nThis is what you entered:")
		print(f"\ttask: {task}")
		print(f"\tpriority: {priority}")
		print(f"\tdue: {dueBy}")

		todo.append((task, priority, dueBy))

def modifyTodo():
	index = input("Enter the index of the todo you wish to modify: ")

	print("\nWhat type of modification would you like to make?")
	print("1) entire change")
	print("2) task only")
	print("3) priority only")
	print("4) due date only")

def deleteTodo():
	if len(todo) == 0:
		print("You have no todos, please add one before calling del")
	else:
		lookup = input("Do you need to look-up the indices of your tasks [y/N]? ")
		if lookup == "y":
			print("Here are your tasks:")
			for i in range(len(todo)):
				print(f"{i} {todo[i]}")
		index = input("\nEnter the number of the task you wish to delete: ")
		try:
			index = int(index)
		except:
			print("The value you entered was not a number!")
			return
		itemDeleted = todo[int(index)]
		todo.remove(itemDeleted)
		print(f"This task was deleted:")
		print(itemDeleted)

def overviewTodo():
	print("A todo is something you need to be reminded of!")
	print("In order to create one, call the function add")
	print("To see your todo list, call list")
	print("To delete a todo call del!")
	print("To quit, type q")
	print("For more information call help")

def help():
	print("Help is not yet implemented...")

if True:
	running = True
	print("Welcome to calendar!\n")
	overviewTodo()

	while running:
		command = input("\nPlease enter a command: ")
		if command == "q":
		    running = False
		    print("Thank you for running calendar!")
		elif command == "add":
		    addTodo()
		elif command == "del":
		    deleteTodo()
		elif command == "help":
		    help()
		elif command == "list":
		    listTodo()
		else:
		    print("That is not a recognized command, press q if you wish to quit!")



