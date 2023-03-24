def is_rural():
    with open('traffic-signal-database.csv','r') as tsd:
        tsd_list = []
        tsd_split = []
        for line in tsd:
            tsd_list.append(line)
        for line in tsd_list:
            tsd_split.append(line.split(','))

        city_names = []
        for line in tsd_split:
            if line[1] not in city_names:
                city_names.append(line[1])

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

        with open('rural_cities.txt','w') as rural_write:
            rural_write.write(f'{rural_cities}')

is_rural()