class Date:
   def __init__(self, d, m, y):
      self.validate_month(m)
      self._month = m

      self.validate_day(d)
      self._day = d

      self.validate_year(y)
      self._year = y

   def validate_year(self, year):
      if year < 0:
         raise ValueError("Invalid Year: " + str(year))

   def validate_month(self, month):
      if month < 1 or month > 12:
         raise ValueError("Invalid Month: " + str(month))

   def validate_day(self, day):
      if day < 1 or day > self.days_in_month():
         raise ValueError("Invalid Day: " + str(day))

   @property
   def year(self):
      return self._year

   @year.setter
   def year(self, year):
      self.validate_year(year)
      self._year = year

   @property
   def month(self):
      return self._month

   @month.setter
   def month(self, month):
      self.validate_month(month)
      self._month = month

   @property
   def day(self):
      return self._day

   @day.setter
   def day(self, day):
      self.validate_day(day)
      self._day = day

   def __str__(self):
      return str(self._month) + "/" + str(self._day) + "/" + str(self._year)

   def __eq__(self, other):
      if self._month == other.month and self._day == other.day and self._year == other.year:
         return True
      else:
         return False

   def __gt__(self, other):
      if self._year > other.year:
         return True
      elif self._year < other.year:
         return False

      if self._month > other.month:
         return True
      elif self._month < other.month:
         return False
         
      if self._day > other.day:
         return True
      return False

   def days_in_month(self):
      if self._month in (4, 6, 9, 11):
         return 30
      elif self._month == 2:
         return 28
      else:
         return 31

   def advance(self):
      self._day += 1
      if self._day > self.days_in_month():
         self._day = 1
         self._month += 1

         if self._month > 12:
            self._month = 1
            self._year += 1