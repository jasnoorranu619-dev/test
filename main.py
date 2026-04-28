
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

