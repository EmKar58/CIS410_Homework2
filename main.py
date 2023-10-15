import converter
import display

def main():
	display.display_title()
	
	while True:
		display.display_menu()
		selection = display.get_selection()

		if selection == 1:
			fahrenheit = int(input("Please enter temperature in Fahrenheit: "))
			celsius = converter.fahrenheit_to_celsius(fahrenheit)
			print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius. \n")
	
		elif selection == 2:
			celsius = int(input("Please enter temperature in Celsius: "))
			fahrenheit = converter.celsius_to_fahrenheit(celsius)
			print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.\n")

		elif selection == 3:
			print("Leaving the program. Goodbye!")
			break
		else:
			print("Invalid selection. Please try again.")

if __name__ == "__main__":
	main()