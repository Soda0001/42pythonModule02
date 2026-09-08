class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def show_plant_name(plant_name: str):
    if plant_name == "":
        raise PlantError("Plant name cannot be empty")

    if plant_name == "Abbas":
        raise PlantError("Plant name cannot be Abbas")

    print(f"Plant name is: {plant_name}")


def show_water_amount(water_amount: int):
    max_liters = 200

    if water_amount < 0:
        raise WaterError("Water amount cannot be negative")

    if water_amount > max_liters:
        raise WaterError(
            f"Water storage limit exceeded! Limit is: {max_liters}L"
        )

    print(water_amount)


def water_plant(plant_name: str):
    if plant_name != plant_name.capitalize():
        raise PlantError(
            f"Invalid plant name to water: '{plant_name}'"
        )

    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plant_names):
    print("Opening watering system")

    try:
        for plant in plant_names:
            water_plant(plant)

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
        return

    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "carrots"])

    print("Cleanup always happens, even with errors!")
