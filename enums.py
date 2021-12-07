from enum import Enum
class bank(Enum):
    privatbank = 1
    universal_bank = 2
class payment_type(Enum):
    monthly = 1
    yearly = 2
class status(Enum):
    user=1
    admin=2
