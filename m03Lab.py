"""
###Program Author###
#John Bigelow

###Program Name###
#Car Stats Tracker v1.0

###Program Description: ###
#Program asks for various car statistics, and then stores them in an object
#Then, the individual stats are retrieved from the object and printed to the display

--------------
###Classes: ###

Vehicle - the parent class of Automobile. Contains self and v_type attributes

Automobile - class used for creating an object which will store car stats. Inherits from Vehicle class.
    Also contains unique attributes for year, make, model, doors, roof

-------------
###Variables: ###
Global variables are used for inputs in this program, then passed onto the object.
These have the same names as attributes for convenience, but are not the same objects as the attributes inside classes/objects

v_type - a string for vechicle type. This is automatically set to 'car.'
year - a string for year vehicle was made
make - a string for the make, or brand, of vehicle
model - a string for the model, or product name, of the vehicle
doors - a string for the number of doors, '2' or '4' are the only options
roof - a string for the type of roof, 'solid' or 'sun roof' are the only options

car_1 - an object into which all the values of the above variables will be stored as attributes

-------------

"""

#Define superclass and class
class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type

class Automobile(Vehicle):
    def __init__(self, v_type, year, make, model, doors, roof):
        super().__init__(v_type)
        
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#store car stats into variables
v_type = 'Car'
year = input('Input year of car: ')
make = input('Input make of car: ')
model = input('Input model of car: ')
doors = ""
roof = ""

#check for valid input on doors variable
while doors != '2' or doors != '4':
    doors = input('Number of doors (2 or 4):')
    if doors == '4':
        break
    elif doors == '2':
        break
    else:
        print('(Invalid input: Please enter 2 or 4.)')

#check for valid input on roof variable
while roof != 'solid' or roof != 'sun roof':
    roof = input('Select Roof (solid or sun roof): ')
    if roof == 'solid':
        break
    elif roof == 'sun roof':
        break
    else:
        print("(Invalid input: Please enter 'solid' or 'sun roof'.)")


#variables are passed onto the object created with the Automobile class
car_1 = Automobile(v_type, year, make, model, doors, roof)



# App will then output the data from the object
print(' ')
print('CAR STATS: ')
print("Vehicle type:", car_1.v_type)
print("Year:", car_1.year)
print("Make:", car_1.make)
print("Model:", car_1.model)
print("# of doors:", str(car_1.doors))
print("Type of Roof:", car_1.roof)