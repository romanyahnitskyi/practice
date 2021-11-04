from enum import Enum
class cars(Enum):
    Audi_A3="Audi A3"
    BMW_X1="BMW X1"
    Toyota_Yaris="Toyota Yaris"
    Volkswagen_T_Roc="Volkswagen T-Roc"
    Ford_Fiesta="Ford Fiesta"
    Honda_Civic="Honda Civik"
    Volkswagen_Golf="Volkswagen Golf"
class CarReservation:
    id_counter=0
    def __init__(self,car,start_datatime,end_datatime,name,price):
        self.id=CarReservation.id_counter
        self.car=cars(car)
        self.start_datatime=start_datatime
        self.end_datatime=end_datatime
        self.name=name
        self.price=price
        CarReservation.id_counter+=1
    def set_car(self,car):
        self.car=cars(car)
    def set_start(self,start_datatime):
        self.start_datatime=start_datatime
    def set_end(self,end_datatime):
        self.end_datatime=end_datatime
    def set_name(self,name):
        self.name=name
    def set_price(self,price):
        self.price=price
