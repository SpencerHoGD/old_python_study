import time

def get_time(f):

    def inner(*arg,**kwarg):
        s_time = time.time()
        res = f(*arg,**kwarg)
        e_time = time.time()
        print('耗时：{:.3f}秒'.format(e_time - s_time))
        return res
    return inner

# @get_time
# def test():
#     time.sleep(2)  # 模拟运行2s

# test()