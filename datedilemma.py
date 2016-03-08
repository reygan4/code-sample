def get_date(date):
    date = date.replace('/','-').replace(' ','-').split('-')
    
    if len(date[0]) == 4: year, month, day = date[0], date[1], date[2]
    else: year, month, day = date[2], date[0], date[1]
    if len(str(year)) < 4: year = '20%s' %year
    if len(str(month)) < 2: month = '0%s' %month
    if len(str(day)) < 2: day = '0%s' %day
    date = '-'.join([year, month, day])
    return date
datelist = ['2/13/15','1-21-10', '5 10 2015','2012 3 17', '2001-01-01', '2008/01/07']
for date in datelist:
    print get_date(date)
