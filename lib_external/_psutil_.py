# psutil是一个跨平台库(http://pythonhosted.org/psutil/)能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。
# 它主要用来做系统监控，性能分析，进程管理。它实现了同等命令行工具提供的功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。目前支持32位和64位的Linux、Windows、OS X、FreeBSD和Sun Solaris等操作系统.
# 运维库
import psutil


# print(psutil.cpu_times())


def NetIfAddr():
    r""" 打印多网卡 mac 和 ip 信息 """
    adaptersInfo = []
    NICs_dict = psutil.net_if_addrs()
    # print('NICs_dict ---->  ', NICs_dict)
    for adapter in NICs_dict:
        if adapter == 'lo':
            continue
        snicList = NICs_dict[adapter]
        mac = '无 mac 地址'
        ipv4 = '无 ipv4 地址'
        ipv6 = '无 ipv6 地址'
        for snic in snicList:
            if snic.family.name in {'AF_LINK', 'AF_PACKET'}:
                mac = snic.address
            elif snic.family.name == 'AF_INET':
                ipv4 = snic.address
            elif snic.family.name == 'AF_INET6':
                ipv6 = snic.address
        adaptersInfo.append({
            "adapter": adapter,
            "mac": mac,
            "ipv4": ipv4,
            "ipv6": ipv6,
        })
    return adaptersInfo


if __name__ == '__main__':
    print(NetIfAddr())
