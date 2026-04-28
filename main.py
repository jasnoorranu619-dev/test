
robots = {}
zones = ["Downtown", "Suburbs", "Industrial"]

# Collect robot names and zones
for i in range(3):
    name = input("Enter robot name: ")
    
    while True:
        zone = input(f"Choose a delivery zone for {name} (Downtown, Suburbs, Industrial): ")
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
        
