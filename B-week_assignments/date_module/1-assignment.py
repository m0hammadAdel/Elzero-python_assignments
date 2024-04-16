import datetime

my_date = datetime.datetime(2021, 6, 25)
cur_date = datetime.datetime.now()

print(f"Days from {my_date} to {cur_date} Is => {(cur_date - my_date).days}")