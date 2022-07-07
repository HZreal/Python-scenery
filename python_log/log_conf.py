logging_config = {
    'version': 1,
    'disable_existing_loggers': False,  # 不使其他日志失效
    'formatters': {  # 日志格式化器
        'default': {
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        'verbose': {                           # 描述详细
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {                            # 描述简单
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    # 'filters': {                               # 对日志进行过滤
    #     'require_debug_true': {                # django在debug模式下才输出日志
    #         '()': 'django.utils.log.RequireDebugTrue',
    #     },
    # },
    'handlers': {  # 日志处理器
        'console': {  # 标准输出输出
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file': {  # 输出到文件
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 所使用的处理类，这个类可以固定时间开始新的日志，保存原来的日志
            'maxBytes': 300 * 1024 * 1024,                       # 每个日志文件的大小
            'backupCount': 10,                                   # 日志文件个数(一个文件存满自动生成下一个)
            'formatter': 'verbose',
            'filename': 'logs/stdout.log'
        }
    },
    'loggers': {  # 日志记录器
        'StreamLogger': {
            'handlers': ['console'],  # 所使用的处理器
            'level': 'DEBUG',
        },
        'FileLogger': {
            'handlers': ['console', 'file'],   # 既有 console Handler，还有 file Handler
            'level': 'DEBUG',
        },
        'django': {                                             # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],                    # 可以同时向终端与文件中输出日志
            'propagate': True,                                  # 是否继续传递日志信息
            'level': 'INFO',                                    # 日志器接收的最低日志级别
        },
    }
}

