class Date:
  def __init__(self, day, month, year):
    self.__day = day
    self.__month = month
    self.__year = year

  @property
  def year(self):
    return self.__year

  @property
  def day(self):
    return self.__day

  @property
  def month(self):
    return self.__month

  @day.setter
  def day (self, day):
    self.__day = day

  @month.setter
  def month (self, month):
    self.__month = month

  @year.setter
  def year (self, year):
    self.__year = year

  def isEven(self):
    return int (self.__day) % 2 == 0

  def what_time_of_year (self):
    seasons = {'Winter': (1,2,12),
               'spring': (3,4,5),
               'Summer': (6,7,8),
               'Autumn': (9,10,11)
              }
    for key in seasons:
      if int (self.__month) in seasons[key]:
        return key

  def isVisokosny (self):
    return int (self.__year) % 4 == 0

if __name__ == '__main__':
  date = Date ('8', '12', '2000')
  print(date.isEven())
  print(date.what_time_of_year())
  print(date.isVisokosny())