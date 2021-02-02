todo = []

def listTodo():
	"""
	This function will ask the user if they would like to see their
	todos

	On y it will call showTodo(), printing each item

	On anything else nothing happens
	"""
	val = input("Would you like to see your todos [y/N]? ")
	if val == 'y':
		showTodo()

def showTodo():
	"""
	this will print each task in our todo list
	"""
	if len(todo):
		print("Here are your todos:")
		for item in todo:
		    print(item)
	else:
		print("You have nothing in your todo list!")

def addTodo():
	"""
	function will ask the user if they wish to add a todo

	on a 'y' the user will be asked for the task, priority of the
	task and the due date

	the function will then print out what the user entered

	on any other input this function will not do anything
	"""
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
	"""
	"""
	if isTodoEmpty():
		return
	index = input("Enter the index of the todo you wish to modify: ")
	try:
		index = int(index)
	except:
		print("Please enter an index!")
		modifyTodo()
	originalTask = todo[index]

	print("\nWhat type of modification would you like to make?")
	print("1) entire change")
	print("2) task only")
	print("3) priority only")
	print("4) due date only")

	modType = input("Enter the type of change you would like to make: ")
	if modType == "1":
		print("Entire change")
	elif modType == "2":
		print("task only")
	elif modType == "3":
		print("priority only")
	elif modType == "4":
		print("due date only")

def deleteTodo():
	"""
	"""
	if isTodoEmpty():
		return
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
	"""
	"""
	print("A todo is something you need to be reminded of!")
	print("In order to create one, call the function add")
	print("To see your todo list, call list")
	print("To delete a todo call del!")
	print("To quit, type q")
	print("For more information call help")

def help():
	"""
	"""
	print("Here is a list of functions:")
	print("To learn more about a function, type its name and -h")

def isTodoEmpty():
	"""
	"""
	if len(todo) == 0:
		print("\nThere are currently no tasks to be completed!")
		print("Please add a task before using this command.")
		return True
	else:
		False

if True:
	"""
	"""
	running = True
	print("Welcome to calendar!\n")
	overviewTodo()

	while running:
		command = input("\nPlease enter a command: ")
		if command == "q":
		    running = False
		    print("Thank you for running calendar!\n")
		elif command == "add":
		    addTodo()
		elif command == "del":
		    deleteTodo()
		elif command == "help":
		    help()
		elif command == "list":
		    listTodo()
		elif command == "mod":
			modifyTodo()
		else:
		    print("That is not a recognized command, press q if you wish to quit!")



