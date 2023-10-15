def display_title():
	print("Temperature Conversion\n")

def display_menu():
	print("Menu:")
	print("1. Convert Fahrenheit to Celsius")
	print("2. Convert Celsius to Fahrenheit")
	print("3. Leave the Program")

def get_selection():
	selection = input("Enter your selection: ")
	return int(selection)