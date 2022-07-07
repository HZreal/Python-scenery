# logging日志

import logging
import logging.config
from python_log.log_conf import logging_config


# Logger 即记录器，Logger提供了日志相关功能的调用接口。
# Handler 即处理器，将（记录器产生的）日志记录发送至合适的目的地。
# Filter 即过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
# Formatter 即格式化器，指明了最终输出中日志记录的格式。


# 设置logging日志的配置信息
# level表示设置日志级别
#           DEBUG：排查故障时使用的低级别系统信息，通常开发时使用
#           INFO：一般的系统信息，并不算问题
#           WARNING：描述系统发生小问题的信息，但通常不影响功能
#           ERROR：描述系统发生大问题的信息，可能会导致功能不正常
#           CRITICAL：描述系统发生严重问题的信息，应用程序有崩溃的风险
#           在配置文件中配置好日志等级后，智慧输出等级高于配置等级的日志。
# format表示输出格式：
#            %(asctime)s表示当前时间
#            %(filename)s表示程序文件名
#            %(lineno)d表示行号
#            %(levelname)s表示日志级别
#            %(message)s表示日志信息

# 加载基本配置
# logging.basicConfig(
#     filename='logging.log',
#     filemode='a',
#     format='%(asctime)s-%(filename)s[lineno:%(lineno)d]-%(levelname)s-%(message)s',
#     level=logging.DEBUG,
# )

# 简单调用
# 默认创建一个root logger，并应用默认的日志级别(WARN)、默认的处理器Handler(StreamHandler，即将日志信息打印输出在标准输出上)，和默认的格式化器Formatter(默认的格式即为第一个简单使用程序中输出的格式)。
# logging.debug('调试日志信息')
# logging.info('普通日志信息')
# logging.warning('警告日志信息')
# logging.error('错误日志信息')
# logging.critical('严重错误日志信息')


# 加载更详细的配置
logging.config.dictConfig(logging_config)       # 通过字典加载配置
# logging.config.fileConfig('log_conf.ini')           # 通过 .conf 或 .ini 文件加载配置


# 获取某个logger记录器
logger1 = logging.getLogger('FileLogger')
logger2 = logging.getLogger('StreamLogger')

# 设置部分组件
# logger1.setLevel()
# logger1.addHandler()
# logger1.addFilter()

# 使用
logger1.info('info log')


