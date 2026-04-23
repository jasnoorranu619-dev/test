
# Stores exactly 3 robot names and their assigned delivery zones ("Downtown", "Suburbs", "Industrial") in a dictionary.
#Gets the total delivery distance (integer 5-500 km).
#Gets the cargo weight for each robot (between 1 and 50 kg).
#Gets the weather condition ("Clear", "Rain", "Storm").
#If distance is over 300 km, any robot carries more than 50 kg, or the weather is "Storm", print "🚨 Deployment Unsafe!".
#Otherwise, print a summary of robot names, zones, and cargo weights with the message: "🤖 Robots Ready for Delivery!".

# enter robot name.

def robot_name()    
"""enter robot name """
name =input("Enter your robot name.").strip().title()
#cheake for empty name
if name == "":
        print("Name cannot be empty.")
        exit()

def location():
    """choose the location"""
    print("Please choose the location.")
    print("1- Downtown")
    print("2- Suburbs")
    print("3- Industrial")
    location_choice = input("Enter choice: ").strip()

    if location_choice == "1":
        return "Downtown"
    elif location_choice == "2":
        return "Suburbs"
    elif location_choice == "3":
        return "Industrial"
    else:
        print("Invalid option. Please try again.")
        return None

def weight():
    """enter the cargo weight"""
    try:
        weight = float(input("Enter the cargo weight (kg): "))
        if weight < 1 or weight > 50:
            print("Invalid weight. Please enter a value between 1 and 50 kg.")
            return None
        return weight
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None













def main():
    #mainloop
    print("welcome to the robot delevery choose the robot,location and the weather." ) 

    while True: 
        print("\n Please choose the options blew.")
        print("1-please enter your robot name. " )
        print("2-Please choose the location. ")
        print("3-Please enter the cargo weight.")
        print("4-Please enter the weather condition.")
        print("dis")
        print("5-Exit")

        choice = input("enter choice").strip()

        if choice== "1":
            robot_name()
        elif choice=="2":
            location()
        elif choice=="3":
             weight()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
       


