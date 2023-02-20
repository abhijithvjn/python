#Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to find sum of 2 time
class time:
    def __init__(self):
        self.__hour=int(input("Enter the hour:"))
        self.__minute=int(input("Enter the minute:"))
        self.__second=int(input("Enter the second:"))
    def __add__(self,t2):
        hours=self.__hour+t2.__hour
        print("sum of hours",hours)
        minutes=self.__minute+t2.__minute
        print("sum of minutes",minutes)
        seconds=self.__second+t2.__second
        print("sum of seconds",hours)
        if minutes>=60:
            hours=hours+1
            minutes=minutes-60
        if seconds>=60:
            minutes=minutes+1
            seconds=seconds-60
        return hours,minutes,seconds
print("Enter the time of first object:")
ob1=time()
print("Enter the time of second object:")
ob2=time()
print(ob1+ob2)