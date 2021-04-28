###########################################
#创建类，计算任意两个日期之间的天数、周数
###########################################

import datetime
from dateutil import rrule

class BetDate:
    def __init__(self, start_date, stop_date):
        self.start = datetime.datetime.strptime(start_date, "%Y, %m, %d")
        self.stop = datetime.datetime.strptime(stop_date, "%Y, %m, %d")
    
    def days(self):
        d = self.stop - self.start
        return d.days if d.days > 0 else False
    
    def weeks(self):
        weeks = rrule.rrule(rrule.WEEKLY, dtstart=self.start, until=self.stop)
        return weeks.count()

fir_twe = BetDate("2021, 4, 14", "2022, 6, 18")
d = fir_twe.days()
w = fir_twe.weeks()

print("Between 2021-4-14, 2022-6-18:")
print("Days is:", d)
print("Weeks is:", w)