## traffic-signal-database.csv order goes:      0:id       1:city-jurisdiction     2:hospital-nearby   3:rr-crossing   4:speed-limit      5:crossing artorials      6: ADT

## We are looking for intersections that meet one or multiple of the following requirements:
## ADT > 40,000 (30,000 rural)                         (A)
## Crossing arterials with ADT > 30,000 (22,000 rural) (X)
## Approaches > 50mph and ADT > 20,000 (15,000 rural)  (S)
## Within one mile of a hospital                       (H)
## Within 500 ft of a railroad                         (R)

## Intersections that meet at least one of these parameters are considered high priority

def master_intersection_sort():
    ## read data from traffic signal database and convert to lists
    with open('traffic-signal-database.csv','r') as tsdb:
        read_line = []
        traffic_data = []
        for line in tsdb:
            read_line.append(line)
        for line in read_line:
            traffic_data.append(line.split(','))

    ## create dictionary. Set each intersection id to an empty list. If the intersection meets 
    ## any of the specified requirements, the corrsponding letter-code will be appended to its dictionary entry
    id_dict = {}
    for line in traffic_data:
        id_dict[line[0]] = []
    #print(id_dict)

    ## list of rural cities. Taken from is_rural.py
    rural_cities = ['West Haven', 'Ogden/Harrisville', 'North Ogden/Weber County', 'Roy/Weber County', 'Roy/West Haven/Weber County', 'Ogden/West Haven', 'Marriott-Slaterville', 'Harrisville', 'Ogden/Marriott-Slaterville', 'West Point', 'Kaysville/Fruit Heights', 'Farmington', 'Farmington/Fruit Heights', 'Roy/Hooper', 'Hyrum', 'Centerville', 'Bountiful/West Bountiful', 'Willard', 'Cache County/Logan', 'Cache County/Smithfield', 'Logan', 'Cache County', 'North Logan/Hyde Park', 'North Logan/Logan', 'Logan/Cache County', 'Logan/Providence', 'Nibley', 'Richmond', 'North Logan', 'Hyde Park', 'Smithfield', 'Brigham City', 'Wellsville', 'North Salt Lake/Davis County', 'Uintah', 'Farr West', 'Pleasant View', 'Brigham City/Perry', 'West Bountiful', 'Davis County', 'Syracuse/Davis County', 'Garden City', 'Pleasant View/Weber County', 'Harrisville/Pleasant View', 'Weber County', 'Pleasant View/Farr West', 'Box Elder County', 'Tremonton', 'Garland', 'Wasatch County', 'Heber', 'Mapleton/Springville', 'Mapleton', 'Salem', 'Naples', 'Vernal', 'Duchesne', 'Vernal/Uintah County', 'Maeser', 'Uintah County', 'Utah County', 'Santaquin', 'Heber/Wasatch County', 'Midway', 'Daniel/Wasatch County', 'Salem/Utah County', 'Spanish Fork/Utah County/Salem', 'Spanish Fork/Utah County', 'Duchesne County', 'Roosevelt', 'Ballard/Uintah County', 'Nephi', 'Salt Lake County', 'Summit County', 'Park City', 'Park City/Summit County', 'Tooele County', 'Tooele', 'Grantsville', 'Kamas', 'Washington', 'Hurricane', 'LaVerkin', 'Bryce Canyon', 'Beaver', 'Kanab', 'Moab', 'Grand County', 'Monticello', 'Richfield', 'Ephraim', 'Mt. Pleasant', 'Salina', 'Delta', 'Price', 'Wellington', 'Huntington']


    # function returns true if intersection exceeds ADT
    ## ADT > 40,000 (30,000 rural)                         (A)
    def adt_rule(id):
        if int(id[6]) >= 40000:
            return True
        elif int(id[6]) >= 30000 and id[1] in rural_cities:
            return True
        else:
            return False
    ## END FUNCTION

    # function returns true if intersection exceeds ADT and is crossing artorials
    ## Crossing arterials with ADT > 30,000 (22,000 rural) (X)
    def artorial_rule(id):
        if 'y' in id[5] and int(id[6]) >= 30000:
            return True
        elif 'y' in id[5] and int(id[6]) >= 22000 and id[0] in rural_cities:
            return True
        else:
            return False
    ## END FUNCTION

    # function returns true if intersection exceeds ADT and 50mph
    ## Approaches > 50mph and ADT > 20,000 (15,000 rural)  (S)
    def speed_rule(id):
        if int(id[4]) >= 50 and int(id[6]) >= 20000:
            return True
        elif int(id[4]) >= 50 and int(id[6]) >= 15000 and id[1] in rural_cities:
            return True
        else:
            return False
    ## END FUNCTION

    # function returns true if intersection is within 1 mile of hospital
    def hospital_rule(id):
        if 'x' in id[2]:
            return True
        else:
            return False
    ## END FUNCTION

    # function returns true if intersection is within 500 ft of a railroad
    def rr_rule(id):
        if 'x' in id[3]:
            return True
        else:
            return False
    ## END FUNCTION


    # run each intersection through the 5 nested functions. Append the appropriate letter-codes to that intersection's dictionary entry
    for row in traffic_data:
        try:
            if adt_rule(row):
                id_dict[row[0]].append('A')
        except ValueError:
            pass
        try:
            if artorial_rule(row):
                id_dict[row[0]].append('X')
        except ValueError:
            pass
        try:
            if speed_rule(row):
                id_dict[row[0]].append('S')
        except ValueError:
            pass
        try:
            if hospital_rule(row):
                id_dict[row[0]].append('H')
        except ValueError:
            pass
        try:
            if rr_rule(row):
                id_dict[row[0]].append('R')
        except ValueError:
            pass
    ## END LOOP

    # write the data to two separate text files: high priority intersections, and low priority intersections.
    with open('high_priority_intersections.txt','w') as hpi:
        hpi.write('The following intersections are considered high priority for the reasons given by the letter codes immediately following the id:\n    A = exceeds ADT of 40,000 or 30,000 for rural areas.\n    X = crossing artorials and exceeds ADT of 30,000 (22,000 for rural areas).\n    S = Approach speed exceeds 50mph and ADT exceeds 20,000 (15,000 for rural areas).\n    H = Intersection is within 1 mile of a hospital.\n    R = Intersection is within 500 ft of a railroad crossing.\n\n')
        for intersection in id_dict:
            if id_dict[intersection] != []:
                hpi.write(f'{intersection} {id_dict[intersection]}\n')

    with open('low_priority_intersections.txt','w') as lpi:
        lpi.write('The following intersections are deemed low priority:\n\n')
        for intersection in id_dict:
            if id_dict[intersection] == []:
                lpi.write(f'{intersection}\n')

    # send terminal message, so user knows program ran successfully.
    print('Data processing success! \nSee returned text files for details.')

# run parent function
master_intersection_sort()
