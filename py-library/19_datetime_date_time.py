import datetime
import time


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
now = datetime.datetime.now()                    # 返回当前日期及时间，指当前中国北京时间
print('当前中国北京时间 ---->  ', now, type(now))
print('datetime格式化字符串 ---->  ', now.strftime('%Y-%m-%d %H:%M:%S'))         # 时间对象转字符串格式化输出
utcnow = datetime.datetime.utcnow()              # 当前unix时间，+8就是北京时间
print('当前unix时间 ---->  ', utcnow, type(utcnow))

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


# 时间戳：格林尼治时间自1970年1月1号至当前时间的总秒数，唯一地标识某一刻的时间
timestamp = time.time()                # 返回当前的时间戳
print('timestamp ---->  ', timestamp)

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



