import datetime
import time

# 一、datetime模块里的datetime类
t = datetime.datetime.now()           # 返回当前日期及时间
print(t)
print(t.strftime('%Y-%m-%d %H:%M:%S'))
print(t.time())                   # 返回当前时间的日期
print(t.date())                  # 返回当前的时间对象

print('-----------------------------------------------------------\n')


# 二、datetime模块里的date类
# date对象是日期的专属对象，语法格式如下：
# datetime.date(year,month,day)，参数分别代表年月日
current_date = datetime.date.today()          # 返回了当前的日期对象
print(type(current_date), current_date)
datetime.date.fromtimestamp(time.time())              # 返回当前时间戳对应的日期

print('-----------------------------------------------------------\n')


# 三、datetime模块里的time类
# time类中包含了一整天的信息，语法结构如下:
# datetime.time(hour, minute, second, microsecond, tzinfo=None)      # 自定义初始化time类
init_time = datetime.time(15, 22, 58, 24)
print(init_time)

print('-----------------------------------------------------------\n')


# 四、datetime模块里的timedelta类
timedelta = datetime.timedelta(hours=2, minutes=10, seconds=52)
print(timedelta)

print('-----------------------------------------------------------\n')


# 时间戳：格林尼治时间自1970年1月1号至当前时间的总秒数，唯一地标识某一刻的时间
timestamp = time.time()    # 返回当前的时间戳
print(timestamp)