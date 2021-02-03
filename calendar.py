import os

todo = []
dictCmds = {
		"list": ("listTodo()", "list all of our todos"),
		"add": ("addTodo()", "add a task to our list"),
		"del": ("deleteTodo()", "remove a task from our list"),
		"mod": ("modifyTodo()", "modify a task"),
		"help": ("help", "gives more info on cmds"),
		"q": ("NaF", "quits program"),
	    }

# some ANSI escape sequences for adding color to our terminal
class fontcolors:
    Purple = '\033[95m'
    Blue = '\033[94m'
    Green = '\033[92m'
    Red = '\033[91m'
    End = '\033[0m'


def setupTodo():
	"""
	"""
	pass

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
	This function will modify a todo based on the type
	of modification the user requests
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
	remove todos based on the index passed in
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
	kinda like an intro message to the program
	"""
	print("Here is an overview of basic commands: \n")
	print("\tTo look at your tasks enter the 'list' command.")
	print("\tTo add a task use the 'add' command.")
	print("\tTo remove a task use the 'del' command.\n")
	print("For more information on commands call 'help'.")

def help():
	"""
	gives more information on the commands possible
	"""
	print("Here is a list of commands:\n")
	for key in dictCmds:
		print(f"\t{key}: {dictCmds[key][1]}")
	print("\nTo learn more about a command, type its name and -h")

def isTodoEmpty():
	"""
	a checker to see if we have any todos or not, returns a bool
	based on todo being empty or not
	"""
	if len(todo) == 0:
		print("\nThere are currently no tasks to be completed!")
		print("Please add a task before using this command.")
		return True
	else:
		False

def hello():
	"""
	a chat feature here would be cool
	"""
	print("Hello!")
	print("I hope you are enjoying this program so far!")

if True:
	"""
	where the magic happens :)
	"""
	running = True
	print(f"{fontcolors.Purple}Welcome to calendar!{fontcolors.End}\n")
	overviewTodo()

	while running:
		command = input(f"\n{fontcolors.Blue}Please enter a command: {fontcolors.End}")
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
		elif command == "hello":
			hello()
		else:
		    print(f"{fontcolors.Red}That is not a recognized command, press q if you wish to quit!{fontcolors.End}")



