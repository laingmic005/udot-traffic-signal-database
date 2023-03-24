## this function will determine which cities are rural based on user input
## data is returned as a text file named "rural_cities.txt"

def is_rural():
    ## obtain data from csv and convert to lists
    with open('traffic-signal-database.csv','r') as tsd:
        tsd_list = []
        tsd_split = []
        for line in tsd:
            tsd_list.append(line)
        for line in tsd_list:
            tsd_split.append(line.split(','))

        ## append each city name to a list, and exclude duplicates
        city_names = []
        for line in tsd_split:
            if line[1] not in city_names:
                city_names.append(line[1])

        ## ask user if each city in city_names is rural ('y' for yes 'n' for no)
        rural_cities = []
        for i in city_names:
            my_var = input(f'Is {i} rural? ')
            if my_var == 'y':
                rural_cities.append(i)
                print(f'Affirmative. {i} is rural.')
            elif my_var == 'n':
                print(f'Negative. {i} is not rural.')
            else:
                print('Input not recognized.')
                my_var2 = input(f'Is {i} rural? LAST ATTEMPT!!! ')
                if my_var2 == 'y':
                    rural_cities.append(i)
                    print(f'Affirmative. {i} is rural')

        ## write data to text file
        with open('rural_cities.txt','w') as rural_write:
            rural_write.write(f'{rural_cities}')

is_rural()