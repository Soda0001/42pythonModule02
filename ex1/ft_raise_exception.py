def input_temperature(temp_str: str) -> int:
	temperature = int(temp_str)

	if temperature > 40:
		raise ValueError(f"{temperature}Celsius is too hot for plants (max 40Celsius)")
	if temperature < 0:
		raise ValueError(f"{temperature}Celsius is too cold for plants (min 0Celsius)")

	return temperature


def test_temperature() -> None:
	temperatures = ["25", "abc", "100", "-50"]

	print("=== Garden Temperature Checker ===")

	for temp in temperatures:
		print(f"Input data is '{temp}'")
		try:
			temperature = input_temperature(temp)
			print(f"Temperature is now {temperature}Celsius")
		except ValueError as e:
			print(f"Caught input_temperature error: {e}")

	print("All tests completed - program didn't crash!")


if __name__ == "__main__":
	test_temperature()

