'''
Background:
I didn't find any website that lists all the debentures currently listed in nepse with their latest traded price.
While some websites do list those debentures that have been traded the day before, they don't list them all out, which is a problem as debentures don't get traded very often.
So the only way I found was to search sharesansar.com for each of the scripts and extract the price from there, and I understand that searching website multiple times is very inefficient.
Chatgpt did most of the work so I don't really understand the code very well. I am looking to optimize the search time. 
'''

import requests
from bs4 import BeautifulSoup
import csv

scripts = [
  "NIBD84", "PBD85", "EBLD86", "GBILD86/87", "PBLD87", 
    "BOKD86", "SBID83", "SBD87", "NBLD87", "SDBD87", 
    "NMBD87/88", "NBLD85", "NIBD2082", "CCBD88", "NBLD82", 
    "ICFCD83", "CBLD88", "PBLD86", "SRD80", "PBD88", 
    "LBLD86", "SBIBD86", "GWFD83", "CIZBD86", "GBBD85", 
    "NMBD2085", "MFLD85", "MBLD2085", "NCCD86", "PBLD84", 
    "KBLD86", "SRBLD83", "HBLD83", "NICD83/84", "NIFRAUR85/86", 
    "ADBLD83", "SAND2085", "SBLD83", "SBLD2082", "NBBD2085", 
    "GBD80/81", "NICAD8283","NICAD8182"
  ]

results = []

for script in scripts:
    url = f"https://www.sharesansar.com/company/{script}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        comp_price_span = soup.find("span", class_="text-comp-red comp-price padding-second") or soup.find("span", class_="text-comp-green comp-price padding-second") or soup.find("span", class_="text-comp-blue comp-price padding-second")   
        if comp_price_span:
            share_price = comp_price_span.text.strip()
            results.append((script, share_price))
            print(script+" : "+share_price)
        else:
            results.append((script, "N/A"))
    else:
        results.append((script, "Failed to fetch"))

# Write results to a CSV file
with open("share_prices.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Script", "LTP"])
    csv_writer.writerows(results)

print("CSV file 'share_prices.csv' created.")
