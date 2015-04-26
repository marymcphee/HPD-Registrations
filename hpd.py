import csv

# string (filepath) -> [{}]
def parse_contact(filepath):
    contact_list = []
    with open(filepath, 'r') as f:
        contact_reader = csv.reader(f, delimiter='|')
        contact_reader.next()
        for row in contact_reader:
            if len(row) == 15:
                row_as_dict = {'RegistrationContactID': row[0], 'RegistrationID': row[1], 'Type': row[2], 'ContactDescription': row[3], 'CorporationName': row[4], 'Title': row[5], 'FirstName': row[6], 'MiddleInitial': row[7], 'LastName': row[8], 'BusinessHouseNumber': row[9], 'BusinessStreetName': row[10], 'BusinessApartment': row[11], 'BusinessCity': row[12], 'BusinessState': row[13], 'BusinessZip': row[14]}
                contact_list.append(row_as_dict)
            else:
                print 'Error with Row length: ' + row[0]
    return contact_list

def say_hi():
    return 'hello ziggy'


if __name__ == "__main__":
    print parse_contact('data/RegistrationContact20150331.txt')[0:2]

