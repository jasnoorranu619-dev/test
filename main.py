def collect_robot_info():
    robots = {}
    zones = ["Downtown", "Suburbs", "Industrial"]

    for i in range(3):
        name = input("Enter robot name: ")

        while True:
            zone = input(f"Choose a delivery zone for {name} (Downtown, Suburbs, Industrial): ").strip().title()
            if zone in zones:
                break
            else:
                print("Invalid zone. Please choose from the given options.")

        robots[name] = zone

    return robots


def get_distance():
    while True:
        try:
            distance = int(input("\nEnter total delivery distance (5-500 km): "))
            if 5 <= distance <= 500:
                print("Distance Check: Within Range")
                return distance
            else:
                print("Distance must be between 5 and 500.")
        except ValueError:
            print("Please enter a valid number.")


 # Get cargo weights
def get_cargo_weights(robots):
    cargo_weights = {}
    print("\nEnter cargo weight for each robot (1-50 kg):")

    for robot in robots:
        while True:
            try:
                weight = int(input(f"{robot}: "))
                if 1 <= weight <= 50:
                    cargo_weights[robot] = weight
                    break
                else:
                    print("Weight must be between 1 and 50 kg.")
            except ValueError:
                print("Please enter a valid number.")

    return cargo_weights


def get_weather():
    valid_weather = ["Clear", "Rain", "Storm"]

    while True:
        weather = input("\nEnter weather conditions (Clear, Rain, Storm): ").strip().title()
        if weather in valid_weather:
            if weather == "Storm":
                print("Weather Check: Unsafe")
            else:
                print("Weather Check: Safe")
            return weather
        else:
            print("Invalid weather condition.")


def final_safety_check(distance, weather, cargo_weights):
    unsafe = False
    unsafe_robots = []

    if distance > 300:
        unsafe = True

    if weather == "Storm":
        unsafe = True

    for robot, weight in cargo_weights.items():
        if weight > 45:
            unsafe = True
            unsafe_robots.append(robot)

    return unsafe, unsafe_robots


def final_output(unsafe_robots, robots, cargo_weights):
    if unsafe_robots:
        print("\nDeployment Unsafe! The following robots are not safe:")
        for robot in unsafe_robots:
            print(f"{robot}: {robots[robot]}, {cargo_weights[robot]}kg")
    else:
        print("\nAll robots are safe for delivery.")
        for robot in robots:
            print(f"{robot}: {robots[robot]}, {cargo_weights[robot]}kg")


def main():
    robots = collect_robot_info()
    distance = get_distance()
    weather = get_weather()
    cargo_weights = get_cargo_weights(robots)

    unsafe, unsafe_robots = final_safety_check(distance, weather, cargo_weights)

    if unsafe:
        print("\nSafety Alert: Not safe for delivery.")
    else:
        print("\nAll conditions safe.")

    final_output(unsafe_robots, robots, cargo_weights)


if __name__ == "__main__":
    main()
    