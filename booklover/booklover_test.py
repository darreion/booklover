import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        
        bl = BookLover('Test User', 'test@email.com', 'Fantasy')
        
        bl.add_book('The Hobbit', 5)
        
        self.assertIn('The Hobbit', bl.book_list['book_name'].values)
        
    def test_2_add_book(self):
       
        bl = BookLover('Test User', 'test@email.com', 'Fantasy')
       
        bl.add_book('The Hobbit', 5)
        bl.add_book('The Hobbit', 5)
       
        self.assertEqual(sum(bl.book_list['book_name'] == 'The Hobbit'), 1)
                
    def test_3_has_read(self): 
        
        bl = BookLover('Test User', 'test@email.com', 'Fantasy')
        bl.add_book('The Hobbit', 5)
        
        self.assertTrue(bl.has_read('The Hobbit'))
        
    def test_4_has_read(self): 
        
        bl = BookLover('Test User', 'test@email.com', 'Fantasy')
    
        self.assertFalse(bl.has_read('1984'))
        
    def test_5_num_books_read(self): 
        
        bl = BookLover('Test User', 'test@email.com', 'Fantasy')
        bl.add_book('The Hobbit', 5)
        bl.add_book('The Lord of the Rings', 5)
        
        self.assertEqual(bl.num_books_read(), 2)
        
    def test_6_fav_books(self):
       
        bl = BookLover('Test User', 'test@email.com', 'Fantasy')
        bl.add_book('The Hobbit', 5)
        bl.add_book('The Silmarillion', 2)
        bl.add_book('The Lord of the Rings', 4)
        
        fav_books = bl.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
        self.assertIn('The Hobbit', fav_books['book_name'].values)
        self.assertIn('The Lord of the Rings', fav_books['book_name'].values)
        self.assertNotIn('The Silmarillion', fav_books['book_name'].values)

if __name__ == '__main__':
    unittest.main(verbosity=2)
