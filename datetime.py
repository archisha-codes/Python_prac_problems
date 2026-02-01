from atetime import datetime
print(datetime.now())
d=datetime.today()
print(d)
print(d.year)
print(d.month)
print(d.day)

ANS=d.strftime("%Y%m%d and %H%M%S")
print(ANS)

