#Description: This function processes the cars data and prints out an exception
# report based on car status (Available,Rented, Maintenance)
def car_status_check(*args):
    ''' Params args : tuples with elements matching a car status
        Eg (rented,available)
        you can any number of elements you want in the tuple and the report will filter cars with those status and print out'''
    print()
    print('HAB TAXI SERVICES CAR STATUS TRACKER ') 
    print()
    print('CAR          STATUS               MAKE        MODEL           YEAR')
    print('NUMBER') 
    print('==================================================================')

    # Read revenues records from file

    with open('../DataFiles/cars.dat', 'r') as file:
        # intiating accumulator variables for totals
        total_cars = 0
        for record in file:
            record.strip()
            
            #reading each record and slicing elements and assigning elements to variables
            line = record.split(',')
            car_number=line[0].strip()
            make = line[1].strip()
            model = line[2].strip()
            year = line[3].strip()
            current_status = line[4].strip().lower()

            # report cars that are available or rented
            if current_status in args:
                total_cars +=1
            
                # printing car status financial listings  
                print(f'{car_number:<5}       {current_status:<20s} {make:<10s}  {model:<9s}       {year:<9s} ')
    print('==================================================================')
    print (f'Total CARS: {total_cars}' )          
    print()
