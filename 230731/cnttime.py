import datetime

now = datetime.datetime.now()

_ = input("Press Enter to continue...")

now2 = datetime.datetime.now()

print(now2 - now)

if now2 - now > datetime.timedelta(seconds=5):
    print("You were thinking too long!")
