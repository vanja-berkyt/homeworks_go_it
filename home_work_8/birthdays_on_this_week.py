from _datetime import datetime, timedelta
from collections import defaultdict

users = {
    "ivan": "1985.05.15",
    "oksana": "1985.08.03",
    "olena": "1985.08.02",
    "vasyl": "1985.08.02"
}

days_whith_birthday = defaultdict(list)


def write_berthday_into_day_selebration(name, day_of_week):
    if day_of_week == 1:
        days_whith_birthday["Tuesday"].append(name)
    elif day_of_week == 2:
        days_whith_birthday["Wednesday"].append(name)
    elif day_of_week == 3:
        days_whith_birthday["Thursday"].append(name)
    elif day_of_week == 4:
        days_whith_birthday["Friday"].append(name)
    else:
        days_whith_birthday["Monday"].append(name)


def days_from_begin_till_date(birthday):

    year = birthday.year
    year_today = datetime(year=year, month=1, day=1)
    days_from_start_year = birthday.toordinal() - year_today.toordinal()
    return days_from_start_year


def days_to_birthday_for_today(birthday):

    time_delta = timedelta(days=2)
    date_today = datetime.today() - time_delta
    days_to_birthday = days_from_begin_till_date(birthday) - days_from_begin_till_date(date_today)

    return days_to_birthday


def get_birthdays_per_week(users):

    for key, value in users.items():
        birthday = datetime.strptime(value, "%Y.%m.%d")
        birthday_day = birthday.weekday()
        days_to_birthday = days_to_birthday_for_today(birthday)
        if 0 <= days_to_birthday < 8:
            write_berthday_into_day_selebration(key, birthday_day)


get_birthdays_per_week(users)
print(days_whith_birthday)
