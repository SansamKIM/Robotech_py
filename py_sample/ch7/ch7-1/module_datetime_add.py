import datetime

now = datetime.datetime.now()

# Add a time delta to current time
print("# Add using datetime.timedelta")
after = now + datetime.timedelta(
    weeks=1,
    days=1,
    hours=1,
    minutes=1,
    seconds=1,
)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

# Replace specific time element
print("# Add 1 year using now.replace()")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
