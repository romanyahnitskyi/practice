import re
import datetime
import os
import enums


class Validation:
    @staticmethod
    def positive_num(num):
        if num != None:
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
    def positive_amm(func):
        def wrapper(self, num):
            if num != None:
                while True:
                    try:
                        int(num)
                        if int(num) <= 0:
                            print("Must be positive")
                            num = input()
                        else:
                            break
                    except ValueError:
                        num = input("Incorrect amount")
            return func(self, num)

        return wrapper

    @staticmethod
    def input_positive_num():
        do_it = False
        while do_it == False:
            str = input()
            do_it = Validation.positive_num(str)
            if do_it:
                str = int(str)
        return str

    @staticmethod
    def valid_name(func):
        def wrapper(self, name):
            name_format = re.compile("[a-zA-Z_.+-]+$")
            if name==None:
                name="1"
            if name != None:
                while True:
                    if name_format.match(name):
                        break
                    else:
                        name = input("Incorrect name")

            return func(self, name)

        return wrapper

    @staticmethod
    def valid_time(func):
        def wrapper(self, date):
            while True:
                try:
                    datetime.datetime.strptime(str(date), '%Y-%m-%d')
                    break
                except ValueError:
                    date = input("Incorrect time")
            return func(self, date)

        return wrapper

    @staticmethod
    def valid_iban(func):
        def wrapper(self, iban):
            iban_format = re.compile("[A-Z]{2}[0-9]{27}")
            while True:
                if iban != None:
                    if len(iban) == 29:
                        if iban_format.match(iban):
                            break

                iban = input("Incorrect iban")
            return func(self, iban)

        return wrapper

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
    def valid_bank(func):
        def wrapper(self, bank):
            while True:
                if str(bank).lower() not in enums.bank.__members__:
                    bank = input("Incorrect bank")
                else:
                    break
            return func(self, bank)

        return wrapper

    @staticmethod
    def valid_paymant_type(func):
        def wrapper(self, type_):
            while True:
                if str(type_).lower() not in enums.payment_type.__members__:
                    type_ = input("Incorrect payment type")
                else:
                    break
            return func(self, type_)

        return wrapper
