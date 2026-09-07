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


if __name__ == "__main__":
    print("=== Catching Specific Errors ===\n")

    try:
        show_plant_name("")
    except PlantError as e:
        print(f"Caught plant error: {e}\n")

    try:
        show_plant_name("Abbas")
    except PlantError as e:
        print(f"Caught plant error: {e}\n")

    try:
        show_water_amount(-10)
    except WaterError as e:
        print(f"Caught water error: {e}\n")

    try:
        show_water_amount(300)
    except WaterError as e:
        print(f"Caught water error: {e}\n")

    print("All custom error types work correctly!")
