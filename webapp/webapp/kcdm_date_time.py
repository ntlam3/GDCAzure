from calendar import weekday
import datetime
#from datetime import datetime
from datetime import date

def get_kcdm_datetime():

    today=date.today()
    #today=datetime.date(2022,9,21)
    print(today)
    #mydate=datetime.date(2022,4,20)
    #print(mydate)
    #first=mydate.replace(day=1)
    #lastmonth=first-datetime.timedelta(days=1)
    #myfirstdate=mydate.replace(day=1)


    #print(myweekday)
    #def last_day_of_month(anyday):
        #nextmonth=anyday.replace(day=28)+datetime.timedelta(days=4)
        
        #return nextmonth-datetime.timedelta(days=nextmonth.day)
    mylastdate=today.replace(day=1)-datetime.timedelta(days=1)
    myfirstdate=mylastdate.replace(day=1)
    print('My first date: ' + myfirstdate.strftime("%Y-%m-%d"))
    print('My last date: ' + mylastdate.strftime("%Y-%m-%d"))
    fromurl=myfirstdate
    tourl=myfirstdate
    url1=[]
    print(type(myfirstdate))
    print(type(mylastdate))
    print(mylastdate>myfirstdate)

    while(myfirstdate<=mylastdate):
        myweekday=date.weekday(myfirstdate)
        delta=(mylastdate-myfirstdate).days
        if (delta>5):
            print(delta)
            if myweekday==0:
                fromurl1=myfirstdate
                tourl1=fromurl1+datetime.timedelta(days=3)
                str1="from="+fromurl1.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl1.strftime("%Y-%m-%d")
                url1.append(str1)
                fromurl2=fromurl1+datetime.timedelta(days=4)
                tourl2=fromurl2+datetime.timedelta(days=2)
                str2="from="+fromurl2.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl2.strftime("%Y-%m-%d")
                url1.append(str2)
                myfirstdate=tourl2+datetime.timedelta(days=1)
            elif myweekday==1:
                fromurl1=myfirstdate
                tourl1=myfirstdate+datetime.timedelta(days=2)
                str1="from="+fromurl1.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl1.strftime("%Y-%m-%d")
                url1.append(str1)
                fromurl2=fromurl1+datetime.timedelta(days=3)
                tourl2=fromurl2+datetime.timedelta(days=2)
                str2="from="+fromurl2.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl2.strftime("%Y-%m-%d")
                url1.append(str2)
                myfirstdate=tourl2+datetime.timedelta(days=1)
            elif myweekday==2:
                fromurl1=myfirstdate
                tourl1=fromurl1+datetime.timedelta(days=1)
                str1="from="+fromurl1.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl1.strftime("%Y-%m-%d")
                url1.append(str1)
                fromurl2=fromurl1+datetime.timedelta(days=2)
                tourl2=fromurl2+datetime.timedelta(days=2)
                str2="from="+fromurl2.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl2.strftime("%Y-%m-%d")
                url1.append(str2)
                myfirstdate=tourl2+datetime.timedelta(days=1)
            elif myweekday==3:
                fromurl1=myfirstdate
                tourl1=fromurl1+datetime.timedelta(days=0)
                str1="from="+fromurl1.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl1.strftime("%Y-%m-%d")
                url1.append(str1)
                fromurl2=fromurl1+datetime.timedelta(days=1)
                tourl2=fromurl2+datetime.timedelta(days=2)
                str2="from="+fromurl2.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl2.strftime("%Y-%m-%d")
                url1.append(str2)
                myfirstdate=tourl2+datetime.timedelta(days=1)
            elif myweekday==4:
                fromurl2=myfirstdate+datetime.timedelta(days=0)
                tourl2=myfirstdate+datetime.timedelta(days=2)
                str2="from="+fromurl2.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl2.strftime("%Y-%m-%d")
                url1.append(str2)
                myfirstdate=tourl2+datetime.timedelta(days=1)
            elif myweekday==5:
                fromurl2=myfirstdate+datetime.timedelta(days=0)
                tourl2=myfirstdate+datetime.timedelta(days=1)
                str2="from="+fromurl2.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl2.strftime("%Y-%m-%d")
                url1.append(str2)
                myfirstdate=tourl2+datetime.timedelta(days=1)
            elif myweekday==6:
                fromurl2=myfirstdate+datetime.timedelta(days=0)
                tourl2=myfirstdate+datetime.timedelta(days=0)
                str2="from="+fromurl2.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl2.strftime("%Y-%m-%d")
                print(str2)
                url1.append(str2)
                myfirstdate=tourl2+datetime.timedelta(days=1)
        else:
            
            if delta <=3: 
                print(delta)
                fromurl1=myfirstdate
                tourl1=fromurl1+datetime.timedelta(days=delta)
                str1="from="+fromurl1.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl1.strftime("%Y-%m-%d")
                url1.append(str1)
                break
                
            else:
                print(delta)
                fromurl1=myfirstdate
                tourl1=fromurl1+datetime.timedelta(days=3)
                str1="from="+fromurl1.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl1.strftime("%Y-%m-%d")
                url1.append(str1)
                fromurl2=fromurl1+datetime.timedelta(days=4)
                tourl2=fromurl2+datetime.timedelta(delta-4)
                str2="from="+fromurl2.strftime("%Y-%m-%d")+"%2000%3A00%3A00&to="+tourl2.strftime("%Y-%m-%d")
                print(str2)
                url1.append(str2)
                break

    return url1

    #url1=http://azure.thezabbix.com/zabbix/chart2.php?graphid=4251&screenid=128&width=500&height=100&legend=1&profileIdx=web.screens.filter&profileIdx2=128&from=2022-05-02%2000%3A00%3A00&to=2022-05-05%2023%3A59%3A00&_=vidjh3iu
print(get_kcdm_datetime())

#first=today.replace(day=1)
#lastmonth=first-datetime.timedelta(days=1)
#print(lastmonth.strftime("%Y-%m"))
#date_time_obj=datetime.datetime.strptime('2022-06-26',"%Y-%m-%d")
#print(date_time_obj)
#print(date.weekday(date_time_obj))
#print(date.weekday(today))
