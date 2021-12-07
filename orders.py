import json
import Validation
class order:
    def __init__(self,user_email,orders_id):
        self.user_email=user_email
        self.orders_id=orders_id
    def __str__(self):
        out=""
        out+=str(self.user_email)
        for i in range(len(self.orders_id)):
            out+=str(self.orders_id[i])+' '
        return out
    @classmethod
    def read_json(cls, inf_l):
        r_obj = order(**json.loads(inf_l))
        return r_obj

    def data_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
class orders:
    def __init__(self):
        self.col = []

    def __str__(self):
        out = ""
        for i in range(len(self.col)):
            out += str(self.col[i])
        return out

    def update_file(self, file):
        if Validation.Validation.valid_file_name(file):
            str = ""
            for i in range(len(self.col)):
                str += self.col[i].data_to_json()
                if i != len(self.col) - 1:
                    str += "\n"
            with open(file, mode="w") as f:
                f.write(str)
    def all_data_to_json(self):
        out=""
        for i in range(len(self.col)):
            out+=str(self.col[i].data_to_json()) +"\n"
        return out

    @classmethod
    def read_file(cls, file):
        if Validation.Validation.valid_file_name(file):
            a = orders()
            with open(file) as f:
                for i in f:
                    print(i)
                    a.col.append(order.read_json(str(i)))

                return a

    def add_new(self,file,email,orders_id):
        if len(self.col)>0:
            for i in range(len(self.col)):
                if self.col[i].user_email==email:
                    for j in range(len(orders_id)):
                        self.col[i].orders_id.append(orders_id[j])
                        if Validation.Validation.valid_file_name(file):
                            self.update_file(file)
                    return True
        self.col.append(order(email,orders_id))
        if Validation.Validation.valid_file_name(file):
            self.update_file(file)

    def search_email(self, email):
        for i in range(len(self.col)):
            if str(email) == str(self.col[i].user_email):
                return i
        return False