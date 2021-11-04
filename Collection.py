import datetime

import validator
from CarReservation import CarReservation
from CarReservation import cars
from validator import Validation
def input_datas():
    while True:
        start_date = input("Input the start date as dd-mm-yyyy")
        end_date = input("Input the end date as dd-mm-yyyy")
        if not Validation.is_valid_date(start_date) or not Validation.is_valid_date(end_date) or \
                not Validation.is_valid_time_interval(start_date, end_date):
            print("! Enter again !")
            continue
        return start_date, end_date
    class Collection:
        def __init__(self):
            self.array=[]
        def add_elem(self):
            a=CarReservation
            try:
                a.set_car(input())
                start_date,end_date=input_datas()
                a.set_start(start_date)
                a.set_end(end_date)
                b=Validation.valid_name(input())
                if b!=False:
                    a.set_name(b)
                b = Validation.valid_price(input())
                if b != False:
                    a.set_price(b)
            except:
                print("Smth wrong")
