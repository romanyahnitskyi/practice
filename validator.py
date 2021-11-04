import re
from decimal import Decimal
class Validation:
    def valid_name(name):
        name_format=re.compile("[a-zA-Z_.+-]+$")
        if name_format.match(name):
            return name
        print("Incorect name fornat")
        return False

    def is_correct_price(str_price):
        dot_format = re.compile("[1-9][0-9]*.[0-9]{1,2}$")
        if  dot_format.match(str_price):
            return str_price
        return False