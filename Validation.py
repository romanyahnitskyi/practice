import re
import datetime
import os
import enums
class Validation:
    @staticmethod
    def positive_num(num):
        if num!=None:
            try:
                int(num)
                if int(num) <= 0:
                    print("Must be positive")
                    return False
            except ValueError:
                print("Incorrect type")
                return False
            return True
        return False

    @staticmethod
    def input_positive_num():
        do_it=False
        while do_it==False:
            str=input()
            do_it=Validation.positive_num(str)
            if do_it:
                str=int(str)
        return  str



    @staticmethod
    def valid_name(name):
        name_format = re.compile("[a-zA-Z_.+-]+$")
        if name!=None:
            if name_format.match(name):
                return True
            print("Incorect name fornat")
        return False
    @staticmethod
    def input_name():
        do_it = False
        while do_it == False:
            str = input()
            do_it=Validation.valid_name(str)
        return str

    @staticmethod
    def valid_time(date):
        try:
            datetime.datetime.strptime(str(date),'%Y-%m-%d')
            return True
        except ValueError:
            if date!=None:
                print("Incorrect format")
            return  False

    @staticmethod
    def input_time():
        do_it = False
        while do_it == False:
            date = input()
            do_it = Validation.valid_time(date)
        return date

    @staticmethod
    def valid_iban(iban):
        iban_format = re.compile("[A-Z]{2}[0-9]{27}")
        if iban!=None:
            if len(iban) == 29:
                if iban_format.match(iban):
                    return True
            print(f'! Incorrect transaction_number format in {str(iban)} !')
        return False

    @staticmethod
    def input_iban():
        do_it = False
        while do_it == False:
            iban = input()
            do_it = Validation.valid_iban(iban)
        return iban
    @staticmethod
    def valid_file_name(name):
        if os.path.isfile(name) and name.endswith(".txt"):
            return True
        print("incorrect file name")
        return False
    @staticmethod
    def input_file():
        do_it = False
        while do_it == False:
            name = input()
            do_it = Validation.valid_file_name(name)
        return name
    @staticmethod
    def valid_bank(bank):
        if str(bank).lower() not in enums.bank.__members__:
            return False
        return True

    @staticmethod
    def input_bank():
        do_it = False
        while do_it == False:
            bank = input()
            do_it = Validation.valid_bank(bank)
        return bank

    @staticmethod
    def valid_paymant_type(type_):
        if str(type_).lower() not in enums.payment_type.__members__:
            return False
        return True

    @staticmethod
    def input_payment_type():
        do_it = False
        while do_it == False:
            type_ = input()
            do_it = Validation.valid_paymant_type(type_)
        return type_


