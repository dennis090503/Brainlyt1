from datetime import datetime, timedelta
def get_tues_and_fri(month,year):
    #Start from the first day of the month
    start_date = datetime(year,month,1)
    #Calculate the first day of the next month
    if month == 12:
        next_month=datetime(year+1,1,1)
    else:
        next_month=datetime(year,month+1,1)
    #Initialize an empty list to store the dates
    result=[]
    current_date=start_date
    while current_date<next_month:
        if current_date.weekday() in [1, 4]:  #1 for Tuesday, 4 for Friday
            result.append(current_date.strftime("%Y-%m-%d"))
        current_date +=timedelta(days=1)
    return result
month=int(input("Enter month:"))
print(get_tues_and_fri(month,year=2024))