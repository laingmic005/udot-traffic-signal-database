# udot-traffic-signal-database
The goal of this project is to determine which intersections should be attended to if they fail during nighttime hours.

Intersections that are considered "high priority" should be maintained at all hours. An intersection is considered high
priority if it meets at least one of the following criteria:
    
    1. Average daily traffic (ADT) exceeds 40,000 in urban areas or 30,000 in rural 
       areas
    2. Consists of crossing artorials whose ADT exceeds 30,000 in urban areas or 
        22,000 in rural areas
    3. The highest speed approach exceeds 50mph and the ADT exceeds 20,000 in urban 
       areas or 15,000 for rural areas
    4. The intersection is within 1 mile of a major hospital
    5. The intersection is within 500 ft of a railroad crossing
    
Intersections are identified by ID in the comma-separated-values file titled 'intersection-database.csv'. This CSV lists the name of the township
in which the intersection lies geographically, if it is near a hospital or a railroad, the top speed of any of the approaches, and the average daily traffic.
The CSV file is not very easy to read, as its purpose was to feed information to the python scripts. To view the data yourself, try downloading the Excel 
file instead.

master_intersection_sort.py is a python script (written by myself, Micah Laing) that takes the data from intersection-database.csv and checks each intersection
against the parameters for a high priority intersection. The python script then returns two text files: one containing a list of high priority intersections
and the reason(s) they are considered so; and the second file containing the low priority intersections. Both files are included in this repository for
convenience.

is_rural.py is another python script written by me, which I used to assist myself in determining which intersections should be considered 'rural'. 
