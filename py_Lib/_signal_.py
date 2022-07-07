import signal


def _handle_timeout(signum, frame):
    # err_msg = f'Function {func.__name__} timed out after {sec} seconds'
    # device_status = get_redis_connection('default')
    # device_status.set('handing', 'fail')
    # raise TimeoutError(err_msg)
    pass

signal.signal(signal.SIGALRM, _handle_timeout)
signal.alarm(1)