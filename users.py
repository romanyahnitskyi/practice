
import json
import Validation
class user:
    def __init__(self,id,first_name,last_name,email,password,is_admin=0):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.is_admin=is_admin
    def __str__(self):
        out = ""
        for atrib, val in vars(self).items():
            out += str(atrib) + ": " + str(val) + "\n"
        out+="\n"
        return out
    @classmethod
    def read_json(cls, inf_l):
        r_obj = user(**json.loads(inf_l))
        return r_obj

    def data_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
class users:
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
            a = users()
            with open(file) as f:
                for i in f:
                    print(i)
                    a.col.append(user.read_json(str(i)))

                return a
    def search_id(self, id):
        for i in range(len(self.col)):
            if str(id) == str(self.col[i].id):
                return i
        return False

    def add_new(self, file,id,first_name,last_name,email,password):
        for i in range(len(self.col)):
            if self.col[i].email==email:
                return False
        self.col.append(user(id,first_name,last_name,email,password))
        if Validation.Validation.valid_file_name(file):
            self.update_file(file)

    def search_email(self, email):
        for i in range(len(self.col)):
            if str(email) == str(self.col[i].email):
                return i
        return False