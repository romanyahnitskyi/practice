class Logger:
    @staticmethod
    def log(events, file_name='out.txt'):
        f = open(file_name, 'a')
        f.write(str(events) + '\n')
        f.close