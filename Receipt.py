from Validation import Validation
import json
import ast

class receipt:
    def __init__(self, id, recipient_name, recipient_iban, bank, payment_type, amount, payment_datetime):
        self.id = id
        self.recipient_name = recipient_name
        self.recipient_iban = recipient_iban
        self.bank = bank
        self.payment_type = payment_type
        self.amount = amount
        self.payment_datetime = payment_datetime

    def __str__(self):
        out = ""
        for atrib, val in vars(self).items():
            out += str(atrib) + ": " + str(val) + "\n"
        out += "\n"
        return out

    @property
    def recipient_name(self):
        return self.recipient_name

    @recipient_name.setter
    @Validation.valid_name
    def recipient_name(self, name):
        self.__recipient_name = name

    @property
    def recipient_iban(self):
        return self.__recipient_iban

    @recipient_iban.setter
    @Validation.valid_iban
    def recipient_iban(self, recipient_iban):
        self.__recipient_iban = recipient_iban

    @property
    def bank(self):
        return self.__bank

    @bank.setter
    @Validation.valid_bank
    def bank(self, bank):
        self.__bank = bank

    @property
    def payment_type(self):
        return self.__payment_type

    @payment_type.setter
    @Validation.valid_paymant_type
    def payment_type(self, payment_type):
        self.__payment_type = payment_type

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    @Validation.positive_amm
    def amount(self, amount):
        self.__amount = amount

    @property
    def payment_datetime(self):
        return self.__recipient_name

    @payment_datetime.setter
    @Validation.valid_time
    def payment_datetime(self, payment_datetime):
        self.__payment_datetime = payment_datetime

    @classmethod
    def read_json(cls, inf_l):
        r_obj = receipt(**json.loads(inf_l))
        return r_obj

    def data_to_json(self):
        out=dict()
        for atrib, val in vars(self).items():
            if atrib!="id":
                new_atrib=atrib[10:]
                out.update({new_atrib:val})
            else:
                out.update({atrib: val})
        return (json.dumps(out))

    def edit_id(self):
        self.id = input()

    def edit_name(self,name="1"):
        self.recipient_name = name

    def edit_iban(self,iban="1"):
        self.recipient_iban = iban

    def edit_bank(self,bank="a"):
        self.bank = bank

    def edit_payment_type(self,payment_type="1"):
        self.payment_type = payment_type

    def edit_amount(self,amm="aa"):
        self.amount = amm

    def edit_datetime(self,q=1):
        self.payment_datetime = q

    def edit_r(self, key):
        dictionarySets = {"1": self.edit_id,
                          "2": self.edit_name,
                          "3": self.edit_iban,
                          "4": self.edit_bank,
                          "5": self.edit_payment_type,
                          "6": self.edit_amount,
                          "7": self.edit_datetime}
        try:
            dictionarySets[str(key)]()
        except KeyError:
            print("Key not found")
