from Validation import Validation
import json


class receipt:
    def __init__(self, id, recipient_name, recipient_iban, bank, payment_type, amount, payment_datetime):
        self.id = receipt.id = id
        self.recipient_name = recipient_name
        self.recipient_iban = recipient_iban
        self.bank = bank
        self.payment_type = payment_type
        self.amount = amount
        self.payment_datetime = payment_datetime
        self.validator()

    def __str__(self):
        out = ""
        for atrib, val in vars(self).items():
            out += str(atrib) + ": " + str(val) + "\n"
        out+="\n"
        return out

    def validator(self):
        while self.id==None or self.id=='':
            print("input correct id")
            self.id=input()
        if not Validation.valid_bank(self.bank):
            print("Input correct bank")
            self.bank = Validation.input_bank()
        if not Validation.valid_iban(self.recipient_iban):
            print("Input correct iban")
            self.recipient_iban = Validation.input_iban()
        if not Validation.valid_time(self.payment_datetime):
            print("Input correct date")
            self.payment_datetime = Validation.input_time()
        if not Validation.valid_name(self.recipient_name):
            print("Input correct name")
            self.recipient_name = Validation.input_name()
        if not Validation.valid_paymant_type(self.payment_type):
            print("Input correct payment type")
            self.payment_type = Validation.input_payment_type()
        if not Validation.positive_num(self.amount):
            print("Input correct amount")
            self.amount = Validation.input_positive_num()

    @classmethod
    def read_json(cls, inf_l):
        r_obj = receipt(**json.loads(inf_l))
        return r_obj

    def data_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def edit_id(self):
        self.id = input()
        self.validator()

    def edit_name(self):
        self.recipient_name = Validation.input_name()

    def edit_iban(self):
        self.recipient_iban = Validation.input_iban()

    def edit_bank(self):
        self.bank = Validation.input_bank()

    def edit_payment_type(self):
        self.payment_type = Validation.input_payment_type()

    def edit_amount(self):
        self.amount = Validation.input_positive_num()

    def edit_datetime(self):
        self.payment_datetime = Validation.input_time()

    def edit_r(self,key):
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