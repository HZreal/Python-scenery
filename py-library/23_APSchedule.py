# 调度器
from apscheduler.schedulers.base import BaseScheduler
from apscheduler.schedulers.blocking import BlockingScheduler                    # 阻塞主线程
from apscheduler.schedulers.background import BackgroundScheduler                # 不会阻塞主线程，以子线程在后台运行
# from apscheduler.schedulers.asyncio import AsyncIOScheduler                    # 当程序使用 asyncio 框架时使用
# from apscheduler.schedulers.gevent import GeventScheduler                      # 当程序使用 gevent 框架时使用
# from apscheduler.schedulers.tornado import TornadoScheduler                    # 当构建 Tornado 程序时使用
# from apscheduler.schedulers.qt import QtScheduler                              # 当构建 Qt 程序时使用
# from apscheduler.schedulers.twisted import TwistedScheduler                    # 当构建 Twisted 程序时使用

# 触发器
from apscheduler.triggers.base import BaseTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger                                # 仅cron为一个python包，其他为单个文件
from apscheduler.triggers.combining import BaseCombiningTrigger

# 作业存储：用于job数据的持久化。默认 job 存储在内存中，还可以存储在各种数据库中
from apscheduler.jobstores.base import BaseJobStore                              # 抽象基类
# from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.jobstores.memory import MemoryJobStore
# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.rethinkdb import RethinkDB                          # 使用 rethinkdb 存储
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore                # 使用 ORM 框架 SQLAlchemy，后端可以是 sqlite、mysql、PoatgreSQL 等数据库
# from apscheduler.jobstores.zookeeper import ZooKeeperJobStore                  # 使用 zookeeper 存储

# 执行器：负责处理 job。通常使用线程池（默认）或者进程池来运行 job
from apscheduler.executors.base import BaseExecutor
from apscheduler.executors.pool import BasePoolExecutor, ProcessPoolExecutor, ThreadPoolExecutor    # 进程池线程池常用
# from apscheduler.executors.gevent import GeventExecutor
# from apscheduler.executors.tornado import TornadoExecutor
# from apscheduler.executors.twisted import TwistedExecutor
# from apscheduler.executors.asyncio import AsyncIOExecutor
# from apscheduler.executors.debug import DebugExecutor
# from apscheduler.executors.base_py3 import run_coroutine_job



import datetime, time


# 阻塞式调度
# schedule = BlockingScheduler()
# 后台非阻塞式调度(主线程退出会导致子线程销毁而不执行)
schedule = BackgroundScheduler()

# 创建调度器时的配置
jobstores = {
    # 'mongo': MongoDBJobStore(),
    # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
# 创建调度器时就指定jobstores、executors、job_defaults
scheduler3 = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)


class CustomJobStore(MemoryJobStore):
    """
    自定义Jobstore
    """
    def custom_func(self):
        pass


custom_job_store = CustomJobStore()
# 动态添加jobstore(可自定义)
schedule.add_jobstore(MemoryJobStore(), 'default')
schedule.add_jobstore(custom_job_store, 'custom')
# 添加executor(可自定义)
# schedule.add_executor()


def task1():
    print('任务一执行时间-------->', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 静态添加任务(此方式声明在应用程序运行时不再更改的作业)
@schedule.scheduled_job('cron', second='*/2', id='cron_task2')
def task2():
    print('任务二执行时间-------->', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def task3(params, params1, params2):
    print('任务三执行时间-------->', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('task3的参数是：%s, %s, %s' % (params, params1, params2))




if __name__ == '__main__':

    # 动态添加任务(此方式返回job实例，后续可动态操作)
    # 触发器date：作业任务只会执行一次。它表示特定的时间点触发。参数run_date (datetime 或 str)
    schedule.add_job(task1, 'date', run_date=datetime.date(2021, 11, 24), jobstore='default', id='date_task1')
    # job = schedule.add_job(task1, 'date', run_date=datetime.datetime(2021, 11, 24, 11, 38, 59))
    # schedule.add_job(task1, 'date', run_date='2021-12-13 14:09:47')
    
    # 触发器interval：固定时间间隔触发。参数weeks(int)、days(int)、minutes(int)、start_date(datetime或str)、end_date(datetime或str) 等
    # schedule.add_job(task1, 'interval', seconds=2)
    job_task1 = schedule.add_job(task1, 'interval', seconds=5, start_date='2020-11-22 12:24:47', end_date='2021-11-24 16:34:47', id='interval_task1', jobstore='custom')
    
    # 触发器cron：在特定时间周期性地触发，和Linux crontab格式兼容。它是功能最强大的触发器。参数year(int或str)、hour(int或str)、start_date(datetime或str) 等
    schedule.add_job(task1, 'cron', day_of_week='1-5', hour='6-18', minute='*', id='cron_task1')
    # schedule.add_job(task1, 'cron', month='1-3,7-9', day='0, tue', hour='0-3')                # 在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行任务
    schedule.add_job(task3, 'cron', second='*/3', id='cron_task3', args=('hello', ), kwargs={'params1': 'huang', 'params2': 'zhen'})
    
    # 获取任务列表(若指定jobstore，则返回指定jobstore下的任务)
    job1 = schedule.get_job(job_id='date_task1', jobstore='default')                            # 根据id返回指定job实例
    job2 = schedule.get_job(job_id='interval_task1', jobstore='custom')                         # 根据id返回指定job实例
    default_job_list = schedule.get_jobs(jobstore='default')                                    # 返回所有的job实例列表
    custom_job_list = schedule.get_jobs(jobstore='custom')                                      # 返回所有的job实例列表
    print('job1=======>%s' % job1, 'job2=======>%s' % job2, 'default_job_list=======>%s' % default_job_list, 'custom_job_list=======>%s' % custom_job_list, sep='\n')

    # 修改、暂停、恢复、移除任务均两种方式：调度器通过id操作job 或者 job实例自我操作
    # 修改任务
    # schedule.modify_job(job_id='interval_task1', jobstore='')
    # job_task1.modify(minutes=5)
    # 暂停任务
    # schedule.pause_job(job_id='interval_task1', jobstore='')
    # job_task1.pause()
    # 恢复任务
    # schedule.resume_job(job_id='interval_task1', jobstore='')
    # job_task1.resume()
    # 移除任务
    # schedule.remove_job('interval_task1', jobstore='')
    # job_task1.remove()

    schedule.start()

    # 关闭调度器  默认情况下调度器会等待所有正在运行的作业完成后，关闭所有的调度器和作业存储。如果你不想等待，可以将wait选项设置为False
    # schedule.shutdown()
    # schedule.shutdown(wait=False)

    try:
        while True:
            # 保持主线程一直运行
            print('keep the main thread alive, or the children thread will not run for the destruction by the main exited thread')
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        print('the main thread exit with unknown reason !')
        schedule.shutdown()


