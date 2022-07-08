import requests
from requests.utils import dict_from_cookiejar

url = 'https://www.baidu.com'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"

}

# 查询参数
query_params = {
    'wd': 'python requests'
}

# cookie
cookies = {

}
# proxy
proxies = {
    "http": "http://12.34.56.79:9527",
    "https": "https://12.34.56.79:9527"
}

# GET请求
response = requests.get(url=url, params=query_params, headers=header, cookies=cookies, proxies=proxies, verify=False, timeout=3)

# 响应处理
status_code = response.status_code
text = response.text
content = response.content

cookie_obj = response.cookies
cookie_dict = dict_from_cookiejar(cookie_obj)    # return dict


# POST请求
post_data = {}
json_data = {}
f = open('', 'rb')
res = requests.post(url=url, data=post_data, json=json_data, files=f)


# 其他请求方式
# requests.put()
# requests.patch()
# requests.delete()


# session:
# 自动处理cookie，即 **下一次请求会带上前一次的cookie**
# 自动处理连续的多次请求过程中产生的cookie
session = requests.session()
session.get(url='')
session.post(url='')