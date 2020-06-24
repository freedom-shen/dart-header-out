import os
from datetime import datetime

black_list = ['.g.dart']
head = '''// create by freedom's script
// time: {time}
// git: http://gitlab.108sq.org/flutter_app/flutter_tool_kit/tree/master/lib_export 

'''.format(time=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))


class LibManager(object):
    def __init__(self, localPath=None, libName=None):
        self.localPath = localPath or os.getcwd()
        path_list = list(filter(lambda x: x != '', self.localPath.split('/')))
        self.libName = libName or path_list[-1]
        self.output = head + 'library {};\n'.format(self.libName)

    # 判断当前工程是否满足要求
    def verify_programe(self):
        return os.path.dirname(os.path.join(self.output, 'lib'))

    # 循环loop
    def loop_walk(self, path=None):
        path = path or os.path.join(self.localPath, 'lib')
        for root, dirs, files in os.walk(path):
            relativePath = self._filter_path(root)
            self._insert_output(files, relativePath)
            for filePath in dirs:
                self.loop_walk(filePath)

    # 创建文件
    def make_file(self):
        filePath = os.path.join(self._lib_path, self.libName + '.dart')
        with open(filePath, 'w+') as f:
            f.write(self.output)
            f.close()

    # 插入数据
    def _insert_output(self, files: list, filterPath: str):
        if len(files) == 0:
            return
        self.output += '\n// {note}\n'.format(note=filterPath[1:] or 'lib')
        for name in files:
            if name == self.libName + '.dart':
                # 自己
                continue
            if '.dart' not in name:
                continue
            if self._in_black_list(name):
                continue

            tem = os.path.join(filterPath or '/', name)
            self.output += "export '{tem}';\n".format(tem=tem[1:])

    # 删选
    def _filter_path(self, path: str):
        return path.replace(self._lib_path, '')

    # 是否在黑名单
    def _in_black_list(self, name: str):
        tem = False
        for black in black_list:
            if black in name:
                tem = True
                break
        return tem

    @property
    def _lib_path(self):
        return os.path.join(self.localPath, 'lib')


if __name__ == "__main__":
    # path = '/Users/freedom/Documents/108/code/ChangShuo/flutter/changshuo_logic/changshuo_logic_mixed/'
    path = None
    libManger = LibManager(localPath=path)
    if libManger.verify_programe() == False:
        print('❌ 工程目录错误')
        os._exit(0)
    libManger.loop_walk()
    libManger.make_file()
    print(libManger.output)
