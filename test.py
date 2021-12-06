import unittest
from unittest.main import main
from copy import deepcopy
import Collection
from caretaker import CareTaker

class Test_Receipt(unittest.TestCase):
    def setUp(self):
        file = 'data.txt'
        self.col = Collection.collection.read_file(file)

    def test_search(self):
        self.assertIsNotNone(self.col.search('1'))
        self.assertFalse(self.col.search("//"))

    def test_remove(self):
        tempcol = deepcopy(self.col)
        tempcol.remove('5', "test.txt")
        self.assertNotEqual(self.col.col, tempcol.col)

    def test_add(self):
        tempcol = deepcopy(self.col)
        tempcol.add_new("test.txt")
        self.assertNotEqual(self.col.col, tempcol.col)

    def test_sort(self):
        tempcol = deepcopy(self.col)
        self.col.sort(0, 'test.txt')
        self.assertNotEqual(self.col.col, tempcol.col)


    def test_search_id(self):
        self.assertIsNotNone(self.col.search_id("1"))
    def test_read_file(self):
        new_cole=Collection.collection.read_file("data.txt")
        self.assertIsNotNone(new_cole)
    def test_edit1(self):
        tempcol = deepcopy(self.col)
        tempcol.col[0].edit_id()
        self.assertNotEqual(self.col.col, tempcol.col)
    def test_edit2(self):
        tempcol = deepcopy(self.col)
        tempcol.col[0].edit_name()
        self.assertNotEqual(self.col.col, tempcol.col)
    def test_edit3(self):
        tempcol = deepcopy(self.col)
        tempcol.col[0].edit_bank()
        self.assertNotEqual(self.col.col, tempcol.col)
    def test_edit4(self):
        tempcol = deepcopy(self.col)
        tempcol.col[0].edit_iban()
        self.assertNotEqual(self.col.col, tempcol.col)
    def test_edit5(self):
        tempcol = deepcopy(self.col)
        tempcol.col[0].edit_amount()
        self.assertNotEqual(self.col.col, tempcol.col)
    def test_edit6(self):
        tempcol = deepcopy(self.col)
        tempcol.col[0].edit_datetime()
        self.assertNotEqual(self.col.col, tempcol.col)
    def test_edit(self):
        tempcol = deepcopy(self.col)
        tempcol.col[0].edit_payment_type()
        self.assertNotEqual(self.col.col, tempcol.col)
    def test_updatefile(self):
        self.assertFalse(self.col.update_file("ste"))
    def test_memento(self):
        tempcol = deepcopy(self.col)
        c=CareTaker(self.col)
        c.save()
        self.col.remove("1","data.txt")
        c.undo("data.txt")
        self.assertNotEqual(self.col.col, tempcol.col)
    def test_memento2(self):
        tempcol = deepcopy(self.col)
        c=CareTaker(self.col)
        c.save()
        self.col.remove("1","data.txt")
        c.save()
        c.undo("data.txt")
        c.redo("data.txt")
        c.undo("data.txt")
        self.assertNotEqual(self.col.col, tempcol.col)
if __name__ == '__main__':
    unittest.main()
