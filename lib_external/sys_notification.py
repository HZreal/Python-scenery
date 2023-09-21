from plyer import notification


def notice():
    """
    desc: eye care notification
    :return:
    """
    notification.notify(
        title='Eye Care',
        message='have an relaxing for your eye !',
        app_icon=None,
        timeout=10,
    )





if __name__ == '__main__':
    notice()


