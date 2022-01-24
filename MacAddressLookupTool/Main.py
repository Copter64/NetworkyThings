from encodings import utf_8
from mac_vendor_lookup import MacLookup
import csv
import os
import sys


macindex = None
vendorlist = []

#opens a CSV THAT MUST CONTAIN A COLUMN TITLE OF "MAC" in order to work correctly
with open(os.path.join(sys.path[0], 'macaddresses.csv'), newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)


mac = MacLookup()
mac.update_vendors()  # <- This can take a few seconds for the download

def find_mac(mac_address):
    # print(mac.lookup(mac_address))
    vendorname = mac.lookup(mac_address)
    return vendorname


#checks for the column title of "MAC" and sets the index for the for loop
if macindex is None:
        macindex = data[0].index('MAC')

#iterates over the list to output the mac vendor
for macaddr in data:
    #ignores the first row title to have a MAC lookup performed on it
    if macaddr[macindex] == "MAC":
        macaddr.append('Vendor')

    else:
        find_mac(macaddr[macindex])
        macaddr.append(str(find_mac(macaddr[macindex])))

#outputs to a CSV upon completion, vendors will be added with quotes to avoid conflicts with special characters
with open('output.csv', 'w', newline='') as foutput:
    writer = csv.writer(foutput, quoting=csv.QUOTE_ALL)
    writer.writerows(data)

#outputs all the appended data
print(data)
