# from datetime import date
#
# date_list = [date.fromisoformat(input()) for i in range(2)]
# print(min(date_list).strftime("%d-%m (%Y)"))
import statistics
from calendar import month
# from datetime import date
#
# n = int(input())
# list_dates = [date.fromisoformat(input()) for _ in range(n)]
# for each in sorted(list_dates):
#     print(each.strftime("%d/%m/%Y"))

# from datetime import date
#
# def print_good_dates(dates):
#     interesting_dates = list(filter(lambda x: x, (map(lambda each: each if each.year == 1992 and each.month + each.day == 29 else None, dates))))
#     interesting_dates.sort(key=lambda each: each.month)
#     for each in interesting_dates:
#         print(each.strftime("%B %d, %Y"))
#
# print(print_good_dates([]))

# from datetime import date
#
# def is_correct(day, month, year):
#     try:
#         if date(year, month, day):
#             return True, 1
#     except:
#         return False
#
# input_date = input()
# count_correct = 0
# while input_date != "end":
#     day, month, year = map(int, input_date.split('.'))
#     if is_correct(day, month, year):
#         print("Корректная")
#         count_correct += 1
#     else:
#         print("Некорректная")
#     input_date = input()
# print(count_correct)

# from datetime import datetime
#
# my_datetime = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
# print(my_datetime)

# from datetime import datetime
#
# birthday = datetime(1992, 10, 6, 9, 48, 17)
#
# birthday = birthday.replace(year=1993, month=12)
#
# print(birthday)


# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)

# from datetime import datetime
#
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
#
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())

# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
#
# list_before = list(filter(lambda x: x.hour < 12, times_of_purchases))
# list_after = list(filter(lambda x: x.hour >= 12, times_of_purchases))
# print("До полудня") if len(list_before) > len(list_after) else print("После полудня")

# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
#
# zip_list = list(zip(dates, times))
# result_list = list(map(lambda x: datetime.combine(x[0], x[1]), zip_list))
# result_list = sorted(result_list, key=lambda x: x.second)
# for each in result_list:
#     print(each)

# from datetime import datetime
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
# list_ = [(i[0], datetime.strptime(i[1][1], '%d.%m.%Y %H:%M:%S') - datetime.strptime(i[1][0], '%d.%m.%Y %H:%M:%S')) for i in data.items()]
# print(min(list_, key=lambda x: x[1])[0])

# from datetime import datetime
#
# with open("files/diary.txt", encoding="UTF-8") as file:
#     list_ = file.read().split('\n')
#     main_list = list()
#     inner_list = list()
#
#     for each in list_:
#         if each != '':
#             inner_list.append(each)
#         elif each == '':
#             main_list.append(inner_list.copy())
#             inner_list.clear()
#     main_list.append(inner_list.copy())
#
#     main_list = list(map(lambda x: (datetime.strptime(x[0], "%d.%m.%Y; %H:%M"), *x[1:]), main_list))
#
#     main_list.sort(key=lambda x: x[0])
#     for i in range(len(main_list)):
#         for string in main_list[i]:
#             if type(string) == datetime:
#                 print(string.strftime("%d.%m.%Y; %H:%M"))
#             else:
#                 print(string)
#         print() if i < len(main_list) - 1 else None

# from datetime import datetime
#
# def is_available_date(booked_dates, date_for_booking):
#     reserved_dates = list()
#     required_dates = list()
#
#     def check_dates(date_string):
#         list_dates = date_string.split('-')
#         list_dates = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), list_dates))
#         return list(map(lambda x: x.toordinal(), list_dates))
#
#     for date_string in booked_dates:
#         if len(date_string) == 10:
#             date_ = datetime.strptime(date_string, '%d.%m.%Y')
#             reserved_dates.append(date_.toordinal())
#         else:
#             list_dates = check_dates(date_string)
#             reserved_dates.extend(list(range(list_dates[0], list_dates[-1] + 1)))
#
#     if len(date_for_booking) == 10:
#         required_dates.append(datetime.strptime(date_for_booking, '%d.%m.%Y').toordinal())
#     else:
#         list_dates = check_dates(date_for_booking)
#         required_dates.extend(list(range(list_dates[0], list_dates[-1] + 1)))
#
#     print(reserved_dates)
#     print(required_dates)
#
#     set_intersection = set(reserved_dates).intersection(required_dates)
#     if len(set_intersection) > 0:
#         return False
#     else:
#         return True
#
#
# dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
# some_date = '22.11.2021-25.11.2021'
# print(is_available_date(dates, some_date))

# from datetime import datetime, timedelta
# dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))

# from datetime import date, timedelta
#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days = (birthday - today).days
#
# print(days)

# from datetime import datetime, timedelta
#
# date_ = datetime.strptime(input(), '%d.%m.%Y')
# next_date = date_ + timedelta(days=1)
# previous_date = date_ - timedelta(days=1)
#
# print(next_date.strftime('%d.%m.%Y')
# print(previous_date.strftime('%d.%m.%Y')

# from datetime import datetime, timedelta
#
# time_ = datetime.strptime(input(), '%H:%M:%S')
# result = timedelta(hours=time_.hour, minutes=time_.minute, seconds=time_.second)
# print(int(result.total_seconds()))

# from datetime import datetime, timedelta
#
# current_time = datetime.strptime(input(), '%H:%M:%S')
# seconds = timedelta(seconds=int(input()))
# alarm = current_time + seconds
# print(alarm.strftime('%H:%M:%S'))
#
# from datetime import datetime, timedelta
#
# def num_of_sundays(year):
#     sundays = 0
#     date_ = datetime(year, 1, 1)
#     while date_.year == year:
#         if date_.weekday() == 6:
#             sundays += 1
#         date_ = date_ + timedelta(days=1)
#     return sundays
#
# print(num_of_sundays(2022))


# from datetime import datetime, timedelta
#
# date_ = datetime.strptime(input(), "%d.%m.%Y")
# key_day = [i for i in range(11) if i != 1]
# for i, day in zip(range(10), key_day):
#     date_ += timedelta(days=day)
#     print(date_.strftime("%d.%m.%Y"))

# from datetime import datetime
#
# list_dates = [datetime.strptime(i, '%d.%m.%Y') for i in input().split(' ')]
# main_list = list()
# for i in range(len(list_dates) - 1):
#     main_list.append(abs(list_dates[i+1] - list_dates[i]).days)
#
# print(main_list)

# from datetime import datetime, timedelta
#
# def fill_up_missing_dates(dates):
#     list_dates = [datetime.strptime(i, '%d.%m.%Y') for i in dates]
#     result_list = list()
#
#     add_date = min(list_dates)
#     while add_date <= max(list_dates):
#         result_list.append(add_date)
#         add_date += timedelta(days=1)
#
#     return list(map(lambda x: x.strftime('%d.%m.%Y'), result_list))
#
# dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
#
# print(fill_up_missing_dates(dates))

# from datetime import datetime, timedelta
#
# time_start = datetime.strptime(input(), '%H:%M')
# time_end = datetime.strptime(input(), '%H:%M')
#
# begin_time = time_start
# while begin_time + timedelta(minutes=45) <= time_end:
#     print(begin_time.strftime('%H:%M'), (begin_time + timedelta(minutes=45)).strftime('%H:%M'))
#     begin_time = begin_time + timedelta(minutes=45) + timedelta(minutes=10)

# from datetime import date, time, datetime, timedelta
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
#
# minutes = sum(list(map(lambda x: (datetime.strptime(x[1], '%H:%M') - datetime.strptime(x[0], '%H:%M')).seconds / 60, data)))
# print(int(minutes))

# from datetime import datetime, timedelta
#
# dict_ = dict(zip([i for i in range(1, 8)], [0 for i in range(7)]))
#
# start = datetime(1, 1, 1)
# end = datetime(9999, 12, 30)
#
# while start <= end:
#     if start.day == 13:
#         dict_[start.isoweekday()] += 1
#     start += timedelta(days=1)
#
# print(*dict_.values(), sep='\n')

# from datetime import datetime
#
# def checking_time(date):
#     date_ = datetime.strptime(date, "%d.%m.%Y %H:%M")
#     if date_.isoweekday() > 5:
#         if 10 <= date_.hour <= 17:
#             return int((datetime(date_.year, date_.month, date_.day, 18, 0) - date_).seconds / 60)
#         else:
#             return "Магазин не работает"
#     else:
#         if 9 <= date_.hour <= 20:
#             return int((datetime(date_.year, date_.month, date_.day, 21, 0) - date_).seconds / 60)
#         else:
#             return "Магазин не работает"
#
# print(checking_time('07.11.2021 10:00'))

# from datetime import datetime, timedelta
#
# start_date = datetime.strptime(input(), "%d.%m.%Y")
# end_date = datetime.strptime(input(), "%d.%m.%Y")
#
# if start_date.month + start_date.day % 2 == 0:
#     start_date = start_date + timedelta(days=1)
#     print(start_date)
#
# while start_date < end_date:
#
#     if start_date.isoweekday() != 1 or start_date.isoweekday() != 4:
#         print(start_date.strftime("%d.%m.%Y"), start_date.isoweekday())
#     start_date = start_date + timedelta(days=3)

# from datetime import datetime
#
# list_ = [[i for i in input().split(' ')] for j in range(int(input()))]
# list_ = list(map(lambda x: (x[0], x[1], datetime.strptime(x[2], "%d.%m.%Y")), list_))
#
# dict_ = dict()
# for each in list_:
#     dict_.setdefault(each[2], []).append(each[:2])
#
# key = max(dict_)
# print(type(key))

# from datetime import datetime
#
# list_ = [[i for i in input().split(' ')] for j in range(int(input()))]
# list_ = list(map(lambda x: (x[0], x[1], datetime.strptime(x[2], "%d.%m.%Y")), list_))
#
# dict_ = dict()
# for each in list_:
#     dict_.setdefault(each[2], []).append(each[:2])
#
# max_employee = len(max(list(dict_.values()), key=lambda x: len(x)))
#
# list_res = list(filter(lambda x: len(x[1]) == max_employee, list(dict_.items())))
# list_res.sort(key=lambda x: x[0])
#
# for each in list_res:
#     print(each[0].strftime("%d.%m.%Y"))

# from datetime import datetime, timedelta
#
# date_now = datetime.strptime(input(), "%d.%m.%Y")
# employees_list = [[j for j in input().split(' ')] for i in range(int(input()))]
# employees_list = list(map(lambda x: (x[0], x[1], datetime.strptime(x[2], "%d.%m.%Y")), employees_list))
# next_week = [date_now + timedelta(days=i) for i in range(1, 8)]
# next_week = list(map(lambda x: (x.day, x.month), next_week))
#
# next_birthdays = list()
# for each in employees_list:
#     if (each[2].day, each[2].month) in next_week:
#         next_birthdays.append(each)
#
# if len(next_birthdays) > 0:
#     print(*max(next_birthdays, key=lambda x: x[2])[:2])
# else:
#     print("Дни рождения не планируются")

# from datetime import datetime, timedelta
#
#
# def choose_plural(amount, declensions):
#     keys = list(range(10))
#     values_n = [declensions[2], declensions[0], declensions[1], declensions[1], declensions[1], declensions[2],
#                 declensions[2], declensions[2], declensions[2], declensions[2]]
#     values_m = [declensions[2] for i in range(10)]
#
#     num_dict_n = dict(zip(keys, values_n))
#     num_dict_m = dict(zip(keys, values_m))
#
#     if amount > 10 and str(amount)[-2] == '1':
#
#         return f'{amount} {num_dict_m.get(amount % 10)}'
#     else:
#         return f'{amount} {num_dict_n.get(amount % 10)}'
#
#
# release_date = datetime(2022, 11, 8, 12, 0)
# today = datetime.strptime(input(), "%d.%m.%Y %H:%M")
#
# if release_date > today:
#     result = release_date - today
#
# # print(result)
# # print(result.days)
# # print(result.seconds)
# try:
#     if result.days > 0 and result.seconds == 0:
#         # print(result.days)
#         print(f"До выхода курса осталось: {choose_plural(result.days, ('день', 'дня', 'дней'))}")
#     elif result.days > 0 and result.seconds > 0:
#         # print(result.days, result.seconds // 3600)
#         print(
#             f"До выхода курса осталось: {choose_plural(result.days, ('день', 'дня', 'дней'))} и {choose_plural(result.seconds // 3600, ('час', 'часа', 'часов'))}")
#     elif result.days < 1:
#         if result.seconds // 3600 > 0 and int(result.seconds % 3600 / 60) > 0:
#             # print(result.seconds // 3600, int(result.seconds % 3600 / 60))
#             print(
#                 f"До выхода курса осталось: {choose_plural(result.seconds // 3600, ('час', 'часа', 'часов'))} и {choose_plural(int(result.seconds % 3600 / 60), ('минута', 'минуты', 'минут'))}")
#         elif result.seconds // 3600 > 0:
#             # print(result.seconds // 3600)
#             print(f"До выхода курса осталось: {choose_plural(result.seconds // 3600, ('час', 'часа', 'часов'))}")
#         elif int(result.seconds % 3600 / 60) > 0:
#             # print(int(result.seconds % 3600 / 60))
#             print(
#                 f"До выхода курса осталось: {choose_plural(int(result.seconds % 3600 / 60), ('минута', 'минуты', 'минут'))}")
# except:
#     print("Курс уже вышел!")


# from datetime import date, timedelta
# import calendar
#
# def get_all_mondays(year):
#     dates = list()
#     date_ = date(year, 1, 1)
#     while date_.year == year:
#         dates.append(date_)
#         date_ = date_ + timedelta(days=1)
#
#     mondays = list()
#     for each in dates:
#         if calendar.weekday(each.year, each.month, each.day) == 0:
#             mondays.append(each)
#
#     return mondays
#
# print(get_all_mondays(2021))


# from datetime import date, timedelta
# import calendar
#
# year = int(input())
# if calendar.isleap:
#     days_year = [date(year, 1, 1) + timedelta(days=i) for i in range(366)]
# else:
#     days_year = [date(year, 1, 1) + timedelta(days=i) for i in range(365)]
#
# dict_thursdays = dict()
#
# for each in days_year:
#     if calendar.weekday(each.year, each.month, each.day) == 3:
#         dict_thursdays.setdefault(each.month, []).append(each)
#
# for dates_ in dict_thursdays.values():
#     print(dates_[2].strftime("%d.%m.%Y"))

# import csv
#
# with open("student_counts.csv", encoding="utf-8") as input_f, open("sorted_student_counts.csv", "w", encoding="utf-8", newline="") as output_f:
#     reader = csv.reader(input_f)
#     #print(list(reader))
#
#     list_ = list(reader)
#     headers = list_[0][1:]
#     headers = list(map(lambda x: x.split('-'), headers))
#     headers = list(map(lambda x: (int(x[0]), x[1]), headers))
#     print(headers)
#     print()
#     sorted_headers = sorted(headers, key=lambda x: (x[0], x[1]))
#     print(sorted_headers)
#
#     indexes = list()
#     for each in sorted_headers:
#         for index, every in enumerate(headers):
#             if each == every:
#                 print(index)
#                 indexes.append(index)
#
#     print()
#     main_list = list()
#     for each in indexes:
#         inner_list = list()
#         for i in range(len(list_)):
#            counts = list_[i][each + 1]
#            #print(counts)
#            inner_list.append(counts)
#         main_list.append(inner_list.copy())
#
#     years = list(range(2000, 2022))
#     years.insert(0, 'year')
#     main_list.insert(0, years)
#     print(main_list)
#     print()
#
#     # for each in main_list:
#     #     print(each)
#
#     writer = csv.writer(output_f)
#
#     for j in range(len(years)):
#         sub_list = list()
#         for i in range(len(main_list)):
#             sub_list.append(main_list[i][j])
#         writer.writerow(sub_list.copy())

import csv

with open("prices.csv", encoding="utf-8") as f_input:
    reader = csv.DictReader(f_input, delimiter=";")

    prices = list(reader)
    products = reader.fieldnames[1:]

    result_dict = dict()
    for product in products:
        inner_list = list()
        for row in prices:
            inner_list.append((f'{row["Магазин"]}', int(row[product])))
        min_price = min(inner_list, key=lambda x: x[1])
        result_dict[product] = min_price
    result = min(result_dict.items(), key=lambda x: (x[1][1], x[0]))
    print(f'{result[0]}: {result[1][0]}')