import datetime
import time
# 参考：https://blog.csdn.net/qq_40494873/article/details/120603382


# UTC时间      ------>  时间统一协调时间
# unix时间戳   ------>   自UTC1970年1月1号至当前时间的总秒数
# 当地时间     ------>  如北京时间，比UTC时间快8小时


# 一、datetime模块里的date类
# date对象是日期的专属对象，语法格式如下：
# datetime.date(year, month, day)，参数分别代表年月日
current_date = datetime.date.today()                  # 返回了当前的日期对象
print('当前日期对象 ---->  ', current_date, type(current_date))
year = current_date.year
month = current_date.month
day = current_date.day
print(year, month, day)
_date_ = current_date.fromtimestamp(time.time())              # 返回当前时间戳对应的日期
print(_date_)
print('-----------------------------------------------------------\n')



# 二、datetime模块里的time类
# time类中包含了一整天的信息: datetime.time(hour, minute, second, microsecond, tzinfo=None)
point_time = datetime.time(6, 22, 48, 24)                       # 创建某天的一个时间点对象
print('point_time ---->  ', point_time)
# 获取这个时间点的时间相关属性
hour = point_time.hour
minute = point_time.minute
second = point_time.second
microsecond = point_time.microsecond
tzinfo = point_time.tzinfo
print(hour, minute, second, microsecond, tzinfo)
print('时间点格式化成字符串 ---->  ', point_time.strftime('%H:%M:%S'))
print('-----------------------------------------------------------\n')



# 三、datetime模块里的datetime类，继承date类
now = datetime.datetime.now()                    # 返回当前日期及时间，在中国指当前中国北京时间
print('当前中国北京时间 ---->  ', now, type(now))
print('datetime格式化字符串 ---->  ', now.strftime('%Y-%m-%d %H:%M:%S'))         # 时间对象转字符串格式化输出
utcnow = datetime.datetime.utcnow()              # 当前unix时间，世界标准时间，此值+8就是北京时间
print('当前unix时间 ---->  ', utcnow, type(utcnow))
# utcnow.replace()

print('date object ---->  ', now.date())                                # 返回一个date实例(datetime模块)
print('time object ---->  ', now.time())                                # 返回一个time实例(datetime模块)
# now 与 today 几乎没什么区别 。。。
print(now.today(), type(now.today()))
print(datetime.datetime.today(), type(datetime.datetime.today()))
print('-----------------------------------------------------------\n')



# 四、datetime模块里的timedelta类        ----> 即持续时间duration
timedelta = datetime.timedelta(weeks=1, days=2, hours=3, minutes=10, seconds=52, milliseconds=200, microseconds=100)
print('timedelta ---->  ', timedelta, type(timedelta))

days = timedelta.days                               # 时间戳包含的天数                  9
seconds = timedelta.seconds                         # 时间戳包含的hour及以后的整秒数      (3*60+10)*60+52=11452
total_seconds = timedelta.total_seconds()           # 时间戳包含的总秒数(保留四位)        789052.2001
microseconds = timedelta.microseconds               # 时间戳不足一秒的微秒数              200100
print(days, seconds, total_seconds, microseconds)

time_in_2_hours_later = datetime.datetime.now() + datetime.timedelta(hours=2)
print('当前时间 + 2小时 ---->  ', time_in_2_hours_later)
print('-----------------------------------------------------------\n')



# 五、时间戳：格林尼治时间自1970年1月1号至当前时间的总秒数，唯一地标识某一刻的时间
timestamp = time.time()                # 返回当前的时间戳
print('timestamp ---->  ', timestamp)
print('-----------------------------------------------------------\n')



# timezone时区
# 创建时区对象，里面参数可由 和 timedelta() 提供
# timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
china_tz = datetime.timezone(datetime.timedelta(hours=8), name='Asia/Shanghai')

beijing_tz = datetime.timezone(datetime.timedelta(hours=8))
print(f'1、北京时区为：{beijing_tz}')
Tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
print(f'2、东京时区为：{Tokyo_tz}')
New_York_tz = datetime.timezone(datetime.timedelta(hours=-4))
print(f'3、纽约时区为：{New_York_tz}')
utc_tz = datetime.timezone.utc
print(f'4、世界标准时区为：{utc_tz}')

# timezone的类属性
print(datetime.timezone.utc)         # utc 时区
print(datetime.timezone.min)         # UTC-23:59
print(datetime.timezone.max)         # UTC+23:59

# 时区的方法
dt = datetime.datetime.now(tz=china_tz)
print(china_tz.tzname(dt))           # Asia/Shanghai
print(china_tz.utcoffset(dt))        # 8:00:00
print(china_tz.dst(dt))              # None
print(china_tz.fromutc(dt))          # 2022-04-27 22:19:37.935747+08:00
print('-----------------------------------------------------------\n')



# localtime
localtime = time.localtime()             # struct_time对象
print(localtime)                         # TODO tm_wday=4, tm_yday=140, tm_isdst=0指的是？
tm_year = localtime.tm_year
tm_mon = localtime.tm_mon
tm_mday = localtime.tm_mday
tm_hour = localtime.tm_hour
tm_min = localtime.tm_min
tm_sec = localtime.tm_sec
print(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec)
print('-----------------------------------------------------------\n')



# calendar
import calendar
# calendar 基于datetime date实现的

ca_isleap = calendar.isleap(2020) # 返回是否瑞年
print(ca_isleap)

ca_isleaps = calendar.leapdays(2020, 2030) # 返回瑞年数量
print(ca_isleaps)

ca_weekday = calendar.weekday(2021, 10, 6) # 返回星期几
print(ca_weekday)

ca_monthrange =  calendar.monthrange(2021, 10) # 返回当前月份有几个星期&当月天数
print(ca_monthrange)

ca_setfirstweekday = calendar.setfirstweekday(1) # 0 = Monday, 6 = Sunday
print(ca_setfirstweekday)

print(calendar.firstweekday())

ca_obj = calendar.TextCalendar(firstweekday=0)
ca_text = ca_obj.monthdayscalendar(2021,10)
print(ca_text)
print(calendar.monthcalendar(2021, 10)) # 当月星期数

ca_prmonth = ca_obj.prmonth(2021, 10, l=2, w=6)
print(ca_prmonth)
print(calendar.prmonth(2021, 10, l=2, w=5)) # 返回当月日历

ca_month = ca_obj.formatmonth(2021, 10, w=12, l=2)
print(ca_month)
print(calendar.month(2021, 10, w=5, l=2)) # 返回当月日历

ca_prcal = calendar.prcal(2021, w=3, l=0, c=12, m=3) # w:日期列宽、l:日期行高、c:每个月之间的间隔宽度 、m:显示列
print(ca_prcal)

ca_calendar = calendar.calendar(2021, c=12, l=0, w=3)
print(ca_calendar)

# year, month, day, hour, minute, second = tuple[:6]
ca_timegm = calendar.timegm((2021, 10, 6, 0, 59, 30)) # 返回时间戳
print(ca_timegm)

ca_month_name = calendar.month_name # 输出月份名字
for ca in ca_month_name:
    print(ca)

ca_month_abbr = calendar.month_abbr # 输出月份简称
for ca in ca_month_abbr:
    print(ca)

ca_day_name = calendar.day_name # 输出星期名称
for ca in ca_day_name:
    print(ca)

ca_day_abbr = calendar.day_abbr # 输出星期简称
for ca in ca_day_abbr:
    print(ca)






