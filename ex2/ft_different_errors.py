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
	print("=== Garden Error Types Demo ===")

	for operation_num in range(5):
		print(f"Testing number: {operation_num}")

		try:
			garden_operations(operation_num)
			print("Operation completed successfully")

		except ValueError as e:
			print(f"Caught ValueError: {e}\n")

		except ZeroDivisionError as e:
			print(f"Caught ZeroDivisionError: {e}\n")

		except FileNotFoundError as e:
			print(f"Caught FileNotFoundError: {e}\n")

		except TypeError as e:
				print(f"Caught TypeError: {e}\n")

if __name__ == "__main__":
	test_error_types()