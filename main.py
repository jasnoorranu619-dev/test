robots = {}
zones = ["Downtown", "Suburbs", "Industrial"]

# Collect robot names and zones
def add_robot():
    for i in range(3):
        name = input("Enter robot name: ")
        
        while True:
            zone = input(f"Choose a delivery zone for {name} (Downtown, Suburbs, Industrial): ").strip().title()
            if zone in zones:
                break
            else:
                print("Invalid zone. Please choose from the given options.")
        
        robots[name] = zone 

    # Get total distance
while True:
    try:
        distance = int(input("\nEnter total delivery distance (5-500 km): "))
        if 5 <= distance <= 500:
            print("Distance Check: Within Range")
            break
        else:
            print("Distance must be between 5 and 500.")
    except ValueError:
        print("Please enter a valid number.")
        
        #Check distance (affects all robots)
if distance > 300:
    unsafe_robots = list(robots.keys()) 

 # Get cargo weights
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

# Check individual robot weights
for robot, weight in cargo_weights.items():
    if weight > 50:
        unsafe_robots.append(robot)

# Get weather condition
valid_weather = ["Clear", "Rain", "Storm"]

while True:
    weather = input("\nEnter weather conditions (Clear, Rain, Storm): ").strip().title()
    if weather in valid_weather:
        if weather == "Storm":
            print("Weather Check: Unsafe")
        else:
            print("Weather Check: Safe")
        break
    else:
        print("Invalid weather condition.")

# Check weather (affects all robots)
if weather == "Storm":
    unsafe_robots = list(robots.keys())
 # Final safety check
unsafe = False
unsafe_robots = []

if distance > 300:
    unsafe = True

if weather == "Storm":
    unsafe = True

# Check if any robot exceeds weight
for robot, weight in cargo_weights.items():
    if weight > 45:
        unsafe = True
        unsafe_robots.append(robot)

if unsafe: 
    print("\nSafety Alert: not safe for delivery.")
else:
    print("\nAll robots are safe for delivery.")

# Final output
if unsafe_robots:
    print("\nDeployment Unsafe! The following robots are not safe:")
    for robot in unsafe_robots:
        print(f"{robot}: {robots[robot]}, {cargo_weights[robot]}kg")
else:
    print()
    for robot in robots:
        print(f"{robot}: {robots[robot]}, {cargo_weights[robot]}kg") 

def main():
    print("Welcome to the robot delivery system!")

    while True:
        print("\nPlease choose an option:")
        print("1 - Add robot")
        print("2 - Show robots")
        print("3 - Remove robot")
        print("4 - Show number of robots")
        print("5 - Show delivery info")
        print("0 - Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_robot()
        elif choice == "2":
            show_robots()
        elif choice == "3":
            remove_robot()
        elif choice == "4":
            show_robot_count()
        elif choice == "5":
            show_delivery_info()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
       