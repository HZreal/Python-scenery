"""
invoke Docker Daemon with Docker Engine SDK for Python
doc: https://docker-py.readthedocs.io/en/stable/
"""
import sys

import docker
import logging

# 默认目录映射
VOLUME_BINDING = {
    '/Users/huang/Desktop/tmp/': {
        'bind': '/data',
        'mode': 'rw'
    }
}


class DockerProxy:
    logger = logging.getLogger('docker')

    client = None

    volume_binding = None

    def __init__(self, base_url: str = 'unix://var/run/docker.sock', auto_config: bool = True):
        """

        Args:
            base_url (str): The base URL to connect to Docker Engine
            auto_config (bool): if True, set_config will be invoked automatically, otherwise must invoke set_config
        """
        self.client = docker.DockerClient(base_url=base_url)
        print('Engine Version is ', self.client.version())

        if auto_config:
            self.set_config()
        else:
            self.logger.warning('Please specify the config for DockerProxy, or invoke Docker Engine will be failed')

    def set_config(self, volume_binding=None):
        """

        Args:
            volume_binding ():

        Returns:

        """
        self.volume_binding = volume_binding or VOLUME_BINDING

    def run(self, image: str, cmd: str, **kwargs):
        """

        Args:
            image ():
            cmd ():
            **kwargs ():

        Returns:

        """
        try:
            container = self.client.containers.run(image, cmd, self.volume_binding, **kwargs)
            # 等待容器运行结束
            result = container.wait()
            if result['StatusCode'] == 0:
                print(f"Container ran successfully: {container.logs().decode()}")
            else:
                print(f"Container exited with error code {result['StatusCode']}: {container.logs().decode()}")
            return container.logs().decode()

        except docker.errors.ContainerError as e:
            print(f"ContainerError: {e}")
        except docker.errors.ImageNotFound as e:
            print(f"ImageNotFound: {e}")
        except docker.errors.APIError as e:
            print(f"APIError: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def ctb_publish(self, input_path, output_path, **kwargs):
        """

        Args:
            input_path ():
            output_path ():
            **kwargs ():

        Returns:

        """
        image = 'homme/cesium-terrain-builder'
        cmd = f"ctb-tile --output-dir {output_path} {input_path}"
        self.run(image, cmd, **kwargs)


def invoke():
    args = sys.argv

    if len(args) != 3:
        raise Exception("the length of parameter must be 3")

    input_path = args[1]
    output_path = args[2]

    proxy = DockerProxy()
    proxy.ctb_publish(input_path=input_path, output_path=output_path)


if __name__ == '__main__':
    # test1
    proxy = DockerProxy()
    proxy.ctb_publish(input_path='/data/ctb_result/', output_path='/data/aa.tif')

    # test2
    # invoke()
