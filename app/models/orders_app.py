from app.models.order import *
from datetime import date

order1 = Order("Frank Booth", date(2020, 5, 17), 5)
order2 = Order("Jack booth", date(2020, 12, 3), 19)
order3 = Order("Jeffrey Dahmer", date(1977,6,7),25)
order4 = Order("Mary Beth", date (2020, 8, 5) ,32)

orders = [order1, order2, order3, order4]