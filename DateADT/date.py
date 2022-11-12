# Date(12-12-1234)
# Date(12/12/1234)
class BaseException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'--Error {self.msg}'

class Date:
    def __init__(self, cur_date, delimeter='-'):
        self.cur_date = cur_date.split(delimeter)
        self.day = self.cur_date[0]
        self.month = self.cur_date[1]
        self.year = int(self.cur_date[2])

        self._validGreagorian()

    def __str__(self):
        return f'Day: {self.day}\nMonth: {self.month}\nYear: {self.year}'

    def monthName(self):
        """
        This function returns the name of month
        """
        months = {'01': 'January',
                  '02': 'February',
                  '03': 'March',
                  '04': 'April',
                  '05': 'May',
                  '06': 'June',
                  '07': 'July',
                  '08': 'August',
                  '09': 'September',
                  '10': 'October',
                  '11': 'November',
                  '12': 'December'}

        for i in months.keys():
            if i == self.month:
                return months[i]

    def isLeapYear(self):
        """
        Provides us to check leap year or not
        """
        if self.year % 4 == 0 and self.year % 400 == 0:
            return f'{self.year} is a leap year'

        else: 
            return f'{self.year} is not a leap year'


    def _validGreagorian(self):
        try:
            if self.day > '31' or self.day < '0' or self.month > '12':
                raise BaseException("Invalid day or month value!")

            if self.year < 0 or self.year > 9999:
                raise BaseException("Invalid year!")
            
        except:
            raise BaseException('Check the date')

    def dayOfWeek(self):
        # Referance year : 2000
        """
        F=k+ [(13*m-1)/5] +D+ [D/4] +[C/4]-2*C where

        k is  the day of the month.
        m is the month number.
        D is the last two digits of the year.
        C is the first two digits of the year.
        pass
        """

    def dayOfYear(self):
        pass

    def isWeekDay(self):
        pass


date = Date('17-04-2003')
print(date)
print(date.monthName())
print(date.isLeapYear())
