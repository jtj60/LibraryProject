from library import Library
import csv
import unittest

class SimpleTest(unittest.TestCase):
    # Returns True. Just to test if unit test is working or not
    def test(self):        
        self.assertTrue(True)

# test data file path, the fils is a csv file.
test_data_file_path = './user.csv'

# test data file object
test_data_file_object = None

def load_test_data():
    global test_data_file_object
    # open test data csv file.
    test_data_file_object = open(test_data_file_path, 'r')
    # read the csv file and return the text line list.
    csv_reader = csv.reader(test_data_file_object, delimiter=',')
    print('open and load data from test_data.csv complete.')

# close and release the test data file object.
def close_test_data_file():
    global test_data_file_object
    if test_data_file_object is not None:
        test_data_file_object.close()
        test_data_file_object = None
        print('close file test_data.csv complete.')

class testImportCSV(unittest.TestCase):
    '''Tests for importing a CSV file'''

    def testImportAudioCSV(self):
        ''' Test a good file and make sure importCSV returns a csv reader object     '''
        readerObject = csv.reader("audio")
        self.assertTrue(str(type(readerObject)), "_csv.reader")
  
    def testImportBooksCSV(self):
        ''' Test a good file and make sure importCSV returns a csv reader object     '''
        readerObject = csv.reader("books")
        self.assertTrue(str(type(readerObject)), "_csv.reader")
    
    def testImportUserCSV(self):
        ''' Test a good file and make sure importCSV returns a csv reader object     '''
        readerObject = csv.reader("user")
        self.assertTrue(str(type(readerObject)), "_csv.reader")

    def testImportVideoCSV(self):
        ''' Test a good file and make sure importCSV returns a csv reader object     '''
        readerObject = csv.reader("video")
        self.assertTrue(str(type(readerObject)), "_csv.reader")

class testReturnCSV(unittest.TestCase):
    def string_from_audio_csv(audio):
        """Return the contents of file as a string"""
        with open(audio) as f:
            file_contents = f.read()
        return file_contents

    def string_from_books_csv(books):
        """Return the contents of file as a string"""
        with open(books) as f:
            file_contents = f.read()
        return file_contents
        
    def string_from_user_csv(user):
        """Return the contents of file as a string"""
        with open(user) as f:
            file_contents = f.read()
        return file_contents

    def string_from_video_csv(video):
        """Return the contents of file as a string"""
        with open(video) as f:
            file_contents = f.read()
        return file_contents

if __name__ == '__main__':
    unittest.main()