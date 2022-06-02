# coding: utf-8

from concurrent.futures import ThreadPoolExecutor
import imghdr
import os
import threading
import tinify
import oss2
from urllib.parse import unquote, urlparse
"""
https://tinypng.com/developers/reference/python
设置本地或远程图片后，通过 tinypng 在线压缩后，再上传到阿里云 OSS。

https://zetcode.com/python/pillow/
https://github.com/janbodnar/pillow-examples
https://github.com/aliyun/aliyun-oss-python-sdk
"""


class AliyunOss:
    """
    https://help.aliyun.com/document_detail/88426.html
    """

    def __init__(self, accessKeyID, accessKeySecret, endpoint, bucket):
        self._accessKeyID = accessKeyID
        self._accessKeySecret = accessKeySecret
        self._endpoint = endpoint
        self._bucket = bucket

    def upload(self, file_path: str, file_name: str = None) -> str:
        """上传图片到阿里云 OSS

        Args:
            file_path (str): 要上传的本地图片路径
            file_name (str, optional): 上传后的图片名称. Defaults to None.

        Returns:
            str: 远程图片地址
        """

        # 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
        auth = oss2.Auth(self._accessKeyID, self._accessKeySecret)
        # yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
        # 填写Bucket名称。
        bucket = oss2.Bucket(auth, self._endpoint, self._bucket, connect_timeout=15)

        # name if (not (file_name is None)) else path.basename(file_path)
        result = bucket.put_object_from_file((file_name, os.path.basename(file_path))[file_name is None], file_path)
        result_url = result.resp.response.url
        # https://my-android.oss-cn-shanghai.aliyuncs.com/aaa%2Fbbb%2Foptimized_file.jpeg 转换为
        # https://my-android.oss-cn-shanghai.aliyuncs.com/aaa/bbb/optimized_file.jpeg
        url_parse = urlparse(result_url)
        convert_url = f'''{url_parse.scheme}://{url_parse.netloc}{unquote(url_parse.path, 'utf-8')}'''
        return convert_url


class TinypngCompressor:
    """
    curl --user api:API_KEY \
        --data-binary @unoptimized.png -i https://api.tinify.com/shrink
    """

    def __init__(self, tinypng_api_key):
        tinify.key = tinypng_api_key

    def compress_from_file(self, unoptimized_img_file: str, optimized_img_file: str):
        """压缩本地图片

        Args:
            unoptimized_img_file (str): 本地图片文件路径
            optimized_img_file (str): 压缩后的图片文件路径
        """
        source = tinify.from_file(unoptimized_img_file)
        source.to_file(optimized_img_file)

    def compress_from_url(self, unoptimized_img_url: str, optimized_img_file: str, log=True):
        """压缩网络图片

        Args:
            unoptimized_img_url (str): 网络图片地址
            optimized_img_file (str): 压缩后的图片文件路径
        """
        source = tinify.from_url(unoptimized_img_url)
        source.to_file(optimized_img_file)
        if log:
            print(f'图片压缩完成。图片地址：{unoptimized_img_url} 压缩后的图片路径：{optimized_img_file}')

    def _resize_file(source, width: int, height: int, optimized_img_file: str, method='fit'):
        """调整图片

        Args:
            source (_type_): 原文件
            width (int): 图片宽度
            height (int): 图片高度
            optimized_img_file (str): 转换后的图片文件路径
            method (str, optional): 图片调整模式：scale fit cover thumb. Defaults to 'fit'.
        """
        resized = source.resize(method=method, width=width, height=height)
        resized.to_file(optimized_img_file)


def sampel_compress(unoptimized: str, optimized: str):
    TINYPNG_API_KEY = "TINYPNG_API_KEY"
    compressor = TinypngCompressor(TINYPNG_API_KEY)
    compressor.compress_from_file(unoptimized, optimized)


def sample_upload(optimized_file: str, bucket_path: str):
    accessKeyID = 'accessKeyID'
    accessKeySecret = 'accessKeySecret'
    endpoint = 'endpoint'
    bucket = 'bucket'
    oss = AliyunOss(accessKeyID, accessKeySecret, endpoint, bucket)
    # 可以指定 Bucket 下面的目录。参考 https://tech.antfin.com/docs/2/39630
    result_url = oss.upload(optimized_file, bucket_path)
    # https://my-android.oss-cn-shanghai.aliyuncs.com/aaa/bbb/optimized_file.jpeg
    print(f"图片 url: {result_url}")


def sampel_compress_upload(unoptimized: str, optimized: str, bucket_path: str):
    sampel_compress(unoptimized, optimized)
    sample_upload(optimized, bucket_path)


def sampel_compress_thread():
    thread = threading.Thread(target=sampel_compress, args=['/home/vance/图片/abstract-fraktal.jpeg', '/home/vance/图片/optimized.jpeg'])
    thread.start()


def sampel_compress_threadpool():
    pool = ThreadPoolExecutor(max_workers=3, thread_name_prefix='tinypng')
    # future = pool.submit(compressor.compress_from_file, '/home/vance/图片/abstract-fraktal.jpeg', '/home/vance/图片/optimized.jpeg')
    # result = future.result()
    # print(f'result: {result}')

    dir = '/home/vance/aaa/'
    file_list = next(os.walk(dir))[2]
    for file in file_list:
        # https://docs.python.org/3/library/imghdr.html
        ext = imghdr.what(dir + file)
        if ext:
            pool.submit(sampel_compress, dir + file, f'{dir}{file}_optimized.{ext}')


def sampel_compress_upload_thread():
    thread = threading.Thread(target=sampel_compress_upload,
                              args=('/home/vance/aaa/veer-140775274.jpg', '/home/vance/aaa/ccc.jpg', 'aaa/bbb/hello.png'))
    thread.start()


def sampel_compress_upload_threadpool():
    pool = ThreadPoolExecutor(max_workers=3, thread_name_prefix='tinypng')

    dir = '/home/vance/aaa/'
    file_list = next(os.walk(dir))[2]
    for file in file_list:
        # https://docs.python.org/3/library/imghdr.html
        ext = imghdr.what(dir + file)
        if ext:
            pool.submit(sampel_compress_upload, dir + file, f'{dir}{file}_optimized.{ext}', f'aaa/bbb/{file}_optimized.{ext}')


if __name__ == '__main__':
    # sampel_compress_thread()
    # sampel_compress_threadpool()
    # sampel_compress_upload_thread()
    sampel_compress_upload_threadpool()
