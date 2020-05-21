import json 
from difflib import get_close_matches 

data = json.load(open('data.json'))

search = input("Search Something: ")

if search.upper() in data.keys():

    for x in range(len(data[search.upper()])):
        print(data[search.upper()][x])

elif search.lower() in data.keys():

    for x in range(len(data[search.lower()])):
        print(data[search.lower()][x])

elif search.title() in data.keys():

    for x in range(len(data[search.title()])):
        print(data[search.title()][x])

else:

    search = get_close_matches(search,data.keys(), cutoff = 0.7)

    if len(search) == 0:

        print('Sorry no result!')

    else: 

        print(f'Did you mean {search[0]}')

        if input('Enter yes or no: ').lower() == 'yes':

            for x in range(len(data[search[0]])):
                print(data[search[0]][x])

        else:
            
            exit()
            
        


