def split_date(date_str):
    day, month, year = date_str.split('-')
    return int(day), int(month), int(year)

def calculate_day(day1, month1, day2, month2) :
    result = 0
    if month1 < month2 : 
        result = 30 
    result = result + day2 - day1
    return result + 1

def holiday_day(month):
    days_in_month = [8, 10, 12, 11, 11, 12, 9, 12, 9, 9, 10, 10]
    if 1 <= month <= 12:
        return days_in_month[month - 1]
    else:
        print('have not month')
    
def working_month(month1, month2) : 
    working_days = 0
    for month in range(month1, month2 + 1):
        working_days += holiday_day(month)
    
    return working_days

# only for 2024 and day duration minimum 1 month
if __name__ == '__main__' : 
    date1 = "1-4-2024"
    a1, a2, a3 = split_date(date1)

    date2 = "30-4-2024"
    b1, b2, b3 = split_date(date2)

    if b2 < a2 : 
        print('invalid month input')
        exit()

    day = calculate_day(a1, a2, b1, b2)
    working_day_ = (day - working_month(a2 , b2))

    print('day calculate : ', day)
    print('working day : ', working_day_)
