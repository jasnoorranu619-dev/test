
robots = {}
zones = ["Downtown", "Suburbs", "Industrial"]

# Collect robot names and zones
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
 # Final safety check
unsafe = False

if distance > 300:
    unsafe = True

if weather == "Storm":
    unsafe = True

# Check if any robot exceeds weight
for weight in cargo_weights.values():
    if weight > 50:
        unsafe = True
if unsafe:
    print("\nSafety Alert: At least one robot is not safe for delivery.")
else:
    print("\nAll robots are safe for delivery.")

