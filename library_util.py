import csv

def parse_user_list(filename):
    with open(filename) as f:
        reader = csv.DictReader( f )
        
        users = []
        for row in reader:
            user = {}
            if not row["name"]:
                continue 
            
            user['name'] = row['Name']
            user['address'] = row['Address']
            user['age'] = row['Age']
            user['phone_number'] = row['Phone Number']
            user['card_number'] = row['Card Number']
            user['checked_out'] = row['Checked Out']
            user['items_amount'] = row['Items Amount']

            users.append(user)
        f.close()
    return
