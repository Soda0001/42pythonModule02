def garden_operations(operation_number):
	if operation_number == 0:
		int("abc")
	elif operation_number == 1:
		10 / 0
	elif operation_number == 2:
		open("missing_garden_file.txt")
	elif operation_number == 3:
		"plant" + 42

def test_error_types():
	try:
		garden_operations(0)
	except:
		print("Caught ValueError")

	try:
		garden_operations(1)
	except:
		print("Caught ZeroDivisionError")

	try:
		garden_operations(2)
	except:
		print("Caught FileNotFoundError")

	try:
		garden_operations(3)
	except:
		print("Caught incompatible type of datas")
