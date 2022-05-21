import os

from os.path import join, getsize
from heapq import nlargest


def walk_files_and_sizes(start_at: str):
    for root, _, files in os.walk(start_at):
        for file in files:
            path = join(root, file)
            try:
                size = getsize(path)  # bytes
                yield path, size
            except OSError:
                continue


def largest_files(n: int, start_at: str):
    MB = 1024 * 1024
    largest = nlargest(n, walk_files_and_sizes(start_at), key=lambda x: x[1])
    for path, size in largest:
        print(f'{size/MB} MB {path}')


def test_os_walk(dir_path: str):
    """
    https://docs.python.org/zh-cn/3/library/os.html#os.walk
    os.walk(file_path) 返回生成器类型，三元组; dirpath: 根目录路径; dirnames: 目录下所有的文件夹; filenames: 目录下所有的文件夹
    """
    dir = os.walk(dir_path)
    print(type(dir))
    for dirpath, dirnames, filenames in dir:
        print(f'root: {dirpath}, dirnames: {dirnames}, files: {filenames}')


if __name__ == '__main__':
    """ start = time.perf_counter()
    largest_files(10, "C:/Windows")
    elapsed = time.perf_counter() - start
    print(f'{elapsed} seconds elapsed') """
    test_os_walk('/home/vance/Android/AndroidProjects/PythonLearn/')
