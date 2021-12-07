import Receipt
import Validation
from Receipt import receipt
import json


class collection:
    def __init__(self):
        self.col = []

    def __str__(self):
        out = ""
        for i in range(len(self.col)):
            out += str(self.col[i])
        return out

    @classmethod
    def read_file(cls, file):
        if Validation.Validation.valid_file_name(file):
            a = collection()
            with open(file) as f:
                for i in f:
                    print(i)
                    a.col.append(Receipt.receipt.read_json(str(i)))

                return a

    def update_file(self, file):
        if Validation.Validation.valid_file_name(file):
            str = ""
            for i in range(len(self.col)):
                str += self.col[i].data_to_json()
                if i != len(self.col) - 1:
                    str += "\n"
            with open(file, mode="w") as f:
                f.write(str)

    def search_id(self, id):
        for i in range(len(self.col)):
            if str(id) == str(self.col[i].id):
                return i
        return False

    def remove(self, id,file):
        if self.search_id(str(id)) != False:
            self.col.pop(self.search_id(str(id)))
        if Validation.Validation.valid_file_name(str(file)):
            self.update_file(str(file))


    def add_new(self,file):
        self.col.append(Receipt.receipt(None, None, None, None, None, None, None))
        if Validation.Validation.valid_file_name(file):
            self.update_file(file)

    def sort(self, key,file):
        if Validation.Validation.positive_num(key) and key < 8:
            n = 1
            for keys, values in vars(self.col[0]).items():
                if key == n:
                    self.col = sorted(self.col, key=lambda product: str(getattr(product, keys)).lower())
                n += 1
        if Validation.Validation.valid_file_name(file):
            self.update_file(file)

    def search(self, val):
        find_in_keys = []
        for i in range(len(self.col)):
            n=0
            for atr, value in vars(self.col[i]).items():
                if str(val) in str(value):
                    if n==0:
                        find_in_keys.append(i)
                        n+=1
        return find_in_keys
    def edit(self, id, key,file):
        if self.search_id(id)!=False:
            self.col[self.search_id(str(id))].edit_r(str(key))
        self.update_file(file)
    def all_data_to_json(self):
        out=""
        for i in range(len(self.col)):
            out+=str(self.col[i].data_to_json()) +"\n"
        return out
