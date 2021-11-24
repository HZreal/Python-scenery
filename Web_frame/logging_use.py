# logging日志

import logging

# 设置logging日志的配置信息
# level表示设置级别
# format表示输出格式： %(asctime)s表示当前时间
#                      %(filename)s表示程序文件名
#                      %(lineno)d表示行号
#                      %(levelname)s表示日志级别
#                      %(message)s表示日志信息
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(filename)s[lineno:%(lineno)d]-%(levelname)s-%(message)s',
                    filename='log.txt',
                    filemode='a'
                    )


logging.debug('调试日志信息')      #输出日志信息
logging.info('普通日志信息')
logging.warning('警告日志信息')
logging.error('错误日志信息')
logging.critical('严重错误日志信息')
# 默认是warning级别的，只有大于等于warning级别的日志才会输出显示