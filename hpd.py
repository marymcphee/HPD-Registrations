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

def parse_registrations(filepath):
    registrations = []
    with open(filepath, 'r') as f:
        reg_reader = csv.reader(f, delimiter='|')
        reg_reader.next()
        for row in reg_reader:
            if len(row) == 16:
                row_as_dict = {'RegistrationID': row[0], 'BuildingID': row[1], 'BoroID': row[2], 'Boro': row[3], 'HouseNumber': row[4], 'LowHouseNumber': row[5], 'HighHouseNumber': row[6], 'StreetName': row[7], 'StreetCode': row[8], 'Zip': row[9], 'Block': row[10], 'Lot': row[11], 'BIN': row[12], 'CommunityBoard': row[13], 'LastRegistrationDate': row[14], 'RegistrationEndDate': row[15]}
                registrations.append(row_as_dict)
            else:
                print 'Error with Row length: ' + row[0]
    return registrations


if __name__ == "__main__":
    print len(parse_contact('data/RegistrationContact20150331.txt'))    

