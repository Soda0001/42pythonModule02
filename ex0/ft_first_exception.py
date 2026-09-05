def input_temperature(temp_str):
	return int(temp_str)

def test_temperature():
	print("Testing valid input:")
	print(input_temperature("25"))

	print("\nTesting invalid input:")
	try:
		print(input_temperature("abc"))
	except ValueError:
		print("Error: Invalid temperature!")

	print("\nProgram continues after error.")
	print("Testing another valid input:")
	print(input_temperature("30"))


if __name__ == "__main__":
	test_temperature()
