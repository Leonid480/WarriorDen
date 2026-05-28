class MyTime:
    
    def __init__(self, *args):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        if len(args) == 0:
            return
        elif len(args) == 3:
            h, m, s = args
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                parts = arg.split(':')
                h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
            elif isinstance(arg, MyTime):
                h, m, s = arg.hours, arg.minutes, arg.seconds
            else:
                raise TypeError("Неверный тип аргумента")
        else:
            raise ValueError("Неверное количество аргументов")

        self._set_time(h, m, s)

    def _set_time(self, h, m, s):
        total_seconds = h * 3600 + m * 60 + s
        
        self.seconds = total_seconds % 60
        total_minutes = total_seconds // 60
        

        self.minutes = total_minutes % 60
        self.hours = total_minutes // 60

    

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __repr__(self):
        return self.__str__()


    def _to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __eq__(self, other):
        if not isinstance(other, MyTime):
            return NotImplemented
        return self._to_seconds() == other._to_seconds()

    def __ne__(self, other):
        if not isinstance(other, MyTime):
            return NotImplemented
        return self._to_seconds() != other._to_seconds()

    def __lt__(self, other):
        if not isinstance(other, MyTime):
            return NotImplemented
        return self._to_seconds() < other._to_seconds()

    def __le__(self, other):
        if not isinstance(other, MyTime):
            return NotImplemented
        return self._to_seconds() <= other._to_seconds()

    def __gt__(self, other):
        if not isinstance(other, MyTime):
            return NotImplemented
        return self._to_seconds() > other._to_seconds()

    def __ge__(self, other):
        if not isinstance(other, MyTime):
            return NotImplemented
        return self._to_seconds() >= other._to_seconds()


    def __add__(self, other):
        if not isinstance(other, MyTime):
            return NotImplemented
        new_seconds = self._to_seconds() + other._to_seconds()
        return MyTime(0, 0, new_seconds)

    def __sub__(self, other):
        if not isinstance(other, MyTime):
            return NotImplemented
        new_seconds = self._to_seconds() - other._to_seconds()
        return MyTime(0, 0, new_seconds)

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return NotImplemented
        new_seconds = int(self._to_seconds() * number)
        return MyTime(0, 0, new_seconds)
if __name__ == "__main__":
    t1 = MyTime(12, 65, 83)  
    t2 = MyTime("12:65:83")  
    t3 = MyTime(t1)          
    t4 = MyTime()           

    print(f"t1: {t1}")  


    print(f"t1 == t2: {t1 == t2}")  
    print(f"t1 > t3: {t1 > t3}")    


    t5 = t1 + MyTime(1, 0, 0)
    print(f"t1 + 1 час: {t5}")     

    t6 = t1 * 2
    print(f"t1 * 2: {t6}")  

