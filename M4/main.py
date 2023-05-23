def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for minute in range(60):
        yield minute

def gen_hours():
    for hour in range(24):
        yield hour

def gen_years(start=2019):
    while True:
        yield start
        start += 1

def gen_months():
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    for day in range(1, days_in_month[month] + 1):
        yield day

def gen_date():
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for sec in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year:04d} {hour:02d}:{minute:02d}:{sec:02d}"

gen = gen_date()
counter = 0
while counter < 1000000:
    print(next(gen))
    counter += 1
