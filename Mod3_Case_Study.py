# Isabelle Hoitsma
# Mod3_Case_study
# This program takes various attributes of a vehicle, and stores it in a class, Automobile.
# Variables:
#   VehicleType temporarily stores vehicle type
#   CarYear temporarily stores the vehicles year
#   CarMake temporarily stores the vehicles make
#   CarModel temporarily stores the vehicle model
#   CarDoors temporarily stores the vehicle door count
#   CarRoof temporarily stores the vehicle roof type, like sunroof or convertible
#
# Classes:
#   Vehicle stores what kind of vehicle we will be taking information for
#   Attributes:
#       type
#
#   Automobile stores relevant information regarding a car
#   Attributes:
#       year
#       make
#       model
#       doors
#       roof 

# Contains what kind of vehicle we will be storing information for
class Vehicle():
    def __init__(self, type):
        self.type = "Vehicle type: " + type

# Stores information for cars
#   Including year, make, model, # of doors, and roof type.
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        # Takes type attribute from class Vehicle()
        super().__init__(type)

        # Initializes the rest of the attributes needed for car type
        self.year = "Year: " + year 
        self.make = "Make: " + make 
        self.model = "Model: " + model 
        self.doors = "Door count: " + doors
        self.roof = "Roof type: " + roof

# Stores user input in these temporary variables
VehicleType = input("Enter vehicle type:\n")

# Usually I would split this into a separate area (like use a while True) to allow for different vehicle types
# But we are only doing cars for this code

CarYear = str(input("Enter car year:\n"))
CarMake = input("Enter car make:\n")
CarModel = input("Enter car model:\n")
CarDoors = str(input("Enter door count of car:\n"))
CarRoof = input("Enter roof type:\n")

# Takes those variables and adds them all into the Automobile class at once
Vehicle1 = Automobile(VehicleType, CarYear, CarMake, CarModel, CarDoors, CarRoof)

# Extra space for design purposes :)
print("")

# Prints out all of the Automobile information
print(Vehicle1.type)
print(Vehicle1.year)
print(Vehicle1.make)
print(Vehicle1.model)
print(Vehicle1.doors)
print(Vehicle1.roof)
