import csv


class Utilities():

    def parse_user_list(filename):
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames=fields)
            
            users = []
            for row in reader:
                user = {}
                if not row['name']:
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
        return users

    def parse_book_list(filename):
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames=fields)
            
            books = []
            for row in reader:
                book = {}
                if not row['name']:
                    continue 
                
                book['title'] = row['Title']
                book['author'] = row['Author']
                book['genre'] = row['Genre']
                book['rating'] = row['Rating']
                book['best_seller'] = row['Best Seller']
                book['checked_out'] = row['Checked Out']
                book['renewed'] = row['Renewed']
                book['reference'] = row['Reference']
                book['returned'] = row['Returned']

                books.append(book)
            f.close()
        return books

    def parse_audio_list(filename):
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames=fields)
            
            audios = []
            for row in reader:
                audio = {}
                if not row['title']:
                    continue 
                
                audio['title'] = row['Title']
                audio['genre'] = row['Genre']
                audio['rating'] = row['Rating']
                audio['duration'] = row['Duration']
                audio['checked_out'] = row['Checked Out']
                audio['renewed'] = row['Renewed']
                audio['returned'] = row['Returned']

                audios.append(audio)
            f.close()
        return audios

    def parse_video_list(filename):
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames=fields)
            
            videos = []
            for row in reader:
                video = {}
                if not row["title"]:
                    continue 
                
                video['title'] = row['Title']
                video['genre'] = row['Genre']
                video['rating'] = row['Rating']
                video['duration'] = row['Duration']
                video['checked_out'] = row['Checked Out']
                video['renewed'] = row['Renewed']
                video['returned'] = row['Returned']
                
                videos.append(video)
            f.close()
        return videos

    def update_user_csv(filename):
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames=fields) 
            writer = csv.DictWriter(f, fieldnames=fields)

            for user in users:
                for row in reader:
                    if row['Name'] == user['name']:
                        row['Name'] = user['name']
                        row['Address'] = user['address']
                        row['Age'] = user['age']
                        row['Phone Number'] = user['phone_number']
                        row['Card Number'] = user['card_number']
                        row['Checked Out'] = user['checked_out']
                        row['Items Amount'] = user['items_amount']

                    row = {
                    'Name': row['Name'],
                    'Address': row['Address'],
                    'Age': row['Age'],
                    'Phone Number': row['Phone Number'],
                    'Card Number': row['Card Number'],
                    'Checked Out': row['Checked Out'],
                    'Items Amount': row['Items Amount'],
                    }
                    writer.writerow(row)

            f.close()
        return

    def update_books_csv(filename):
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames=fields) 
            writer = csv.DictWriter(f, fieldnames=fields)

            for book in books:
                for row in reader:
                    if row['Title'] == book['title']:
                        row['Title'] = book['name']
                        row['Author'] = book['address']
                        row['Genre'] = book['age']
                        row['Rating'] = book['rating']
                        row['Best Seller'] = book['best_seller']
                        row['Checked Out'] = book['checked_out']
                        row['Renewed'] = book['renewed']
                        row['Referenced'] = book['referenced']
                        row['Returned'] = book['returned']

                    row = {
                    'Title': row['Title'],
                    'Author': row['Author'],
                    'Genre': row['Genre'],
                    'Rating': row['Rating'],
                    'Best Seller': row['Best Seller'],
                    'Checked Out': row['Checked Out'],
                    'Renewed': row['Renewed'],
                    'Referenced': row['Referenced'],
                    'Returned': row['Returned'],
                    }
                    writer.writerow(row)
                    
            f.close()
        return
    
    def update_audio_csv(filename):
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames=fields) 
            writer = csv.DictWriter(f, fieldnames=fields)

            for audio in audios:
                for row in reader:
                    if row['Title'] == audio['title']:
                        row['Title'] = audio['title']
                        row['Genre'] = audio['Genre']
                        row['Rating'] = audio['rating']
                        row['Duration'] = audio['duration']
                        row['Checked Out'] = audio['checked_out']
                        row['Renewed'] = audio['renewed']
                        row['Returned'] = audio['returned']

                    row = {
                    'Title': row['Title'],
                    'Genre': row['Genre'],
                    'Rating': row['Rating'],
                    'Duration': row['Duration'],
                    'Checked Out': row['Checked Out'],
                    'Renewed': row['Renewed'],
                    'Returned': row['Returned'],
                    }
                    writer.writerow(row)

            f.close()
        return

    def update_video_csv(filename):
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames=fields) 
            writer = csv.DictWriter(f, fieldnames=fields)

            for video in videos:
                for row in reader:
                    if row['Title'] == video['title']:
                        row['Title'] = video['title']
                        row['Genre'] = video['Genre']
                        row['Rating'] = video['rating']
                        row['Duration'] = video['duration']
                        row['Checked Out'] = video['checked_out']
                        row['Renewed'] = video['renewed']
                        row['Returned'] = video['returned']

                    row = {
                    'Title': row['Title'],
                    'Genre': row['Genre'],
                    'Rating': row['Rating'],
                    'Duration': row['Duration'],
                    'Checked Out': row['Checked Out'],
                    'Renewed': row['Renewed'],
                    'Returned': row['Returned'],
                    }
                    writer.writerow(row)

            f.close()
        return
