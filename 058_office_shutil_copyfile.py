import os, stat, time
import shutil
# import shutil
from shutil import copytree, ignore_patterns

start = time.time()
src = r'd:\read_write_test'
dst = r'd:\read_write_test_copytree'
copytree(src, dst, ignore=ignore_patterns('*.pyc', 'tmp*'))
print('tree has been copy')

# copytree('folder1', 'folder2', ignore=ignore_patterns('*.pyc', 'tmp*'))

# copytree('f1', 'f2', symlinks=True, ignore=ignore_patterns('*.pyc', 'tmp*'))

shutil.make_archive(dst, "zip",  base_dir=dst)
print('zip has been made')

def remove_readonly(func, path, _):
    "去除文件的只读属性，尝试再次删除"
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree(dst, onerror=remove_readonly)
end = time.time()
print('copy tree has been remove')
print('Took %.3f seconds.' % (end - start))