###     			    			 	UPWORK PROJECT
# Importing all the required library 
import bs4
import requests
import time
import csv
import os
import pandas as pd

# Clearing the output on Terminal
clear_output = lambda : os.system('clear')

# Extracting data from All_postalCodes.xlsx
df = pd.read_excel("All_postalCodes .xlsx")

# Storing series of Postal code in postal_code variable  we will use this variable for later iteration 
postal_code = df["Postal code"]

# list of headers for tables
heading_list = ["Postal code","District", "Appartments", "Type of Building", "m2", "Debtfree price", "€/m2", 
    "Construction year", "Floor", "Elevator", "Condition", "Plot", "Energy class"
    ]

# Writing the headers
with open("output.csv", "w", newline = "") as csvfile:
            write = csv.writer(csvfile, delimiter = ",")
            write.writerow(heading_list)


# Function for extracting data and generating output and updating data in asuntojen.csv file
def table_generator(x):

    # Initializing page no for particular postal code 
    page = 1

    # Running loop for next page for paticular postal code (for safety runnig this block for 5 times )
    while page <= 5:

        try:

            # Common URL format
            url = requests.get(
                f"https://asuntojen.hintatiedot.fi/haku/?cr=1&ps={x}&t=3&l=2&z={page}&search=1&sf=0&so=a&renderType=renderTypeTable&submit=In+English"
                ).text

            # Intializing temporary list 
            row = [f"'{x:05}"]

            # Parsing the whole page
            soup = bs4.BeautifulSoup(url, "html.parser")

            # Parsing the all tbody tag and storing in table_body(temporary variable)
            table_body = soup.find_all("tbody")

            # Looping for all required tr tag in  particular tbody tag
            for table_row in range(2, len(table_body)-1):
    
                #if len(table_body)  == 3:
                    #break
                
                # Looping for all required td tag in  particular tr tag
                for tr in table_body[table_row].find_all("tr"):

                    # Append all the td tag content in row variable(temporary variable)
                    for td in tr.find_all("td"):

                        row.append(td.text)

                    # Appending the row in asuntojen.csv file  
                    with open("output.csv", "a", newline = "") as csvfile:
                        write = csv.writer(csvfile, delimiter = ",")
                        write.writerow(row)
                    
                    # Making row list same as in initial state for reuse
                    row = [f"'{x:05}"]

            # Delaying the loop for 1 sec sometimes sending many request at a same time can crash small websites 
            time.sleep(1)

            # Incrementing the value of the page so that we can go to next page in the next loop
            page += 1
        
        # If any error arises(it may break the code and stop further execution). It will come out of the loop
        except Exception as e:

            break


# Looping the postal code 
for x in postal_code:

    clear_output()
    print(f"processing (Scraping data from Postal code: {x:05}).....")

    # Calling the table_generator function and passing postal_code as a parameter 
    table_generator(x)

clear_output()
print("finish")
