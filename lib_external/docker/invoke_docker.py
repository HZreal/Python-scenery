"""
invoke docker daemon with Docker Engine SDK for Python
doc: https://docker-py.readthedocs.io/en/stable/
"""
import docker

# macOS上 ssl 基于 LibreSSL 2.8.3 编译的，与 urllib3 v2.0 不兼容
# 参考: https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modu
# 降级 urllib3 v2.0 到 1.26.6 解决 ssl 兼容性问题

# docker desktop for macOS 理解在macoOS上使用的权限问题 ！！
# https://docs.docker.com/desktop/mac/permission-requirements/


# 创建 Docker 客户端对象，默认连接到本机的 Docker 守护进程
# 每次启动Docker Desktop for Mac（除非安装时已设置）, 设置软连接： sudo ln -s -f /Users/huang/.docker/run/docker.sock /var/run/docker.sock
# client = docker.from_env()  # 读取 DOCKER_HOST 环境变量
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

images = client.images.list()
for image in images:
    print(image)

containers = client.containers.list()
for container in containers:
    print(container)
