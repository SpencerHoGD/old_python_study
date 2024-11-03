import os
import time


def main():
    """走马灯效果"""
    # content = "走马灯效果……"
    content = "张居正还有一个错误，则是他忽视了文官集团的双重性格......"
    while True:
        # 清理屏幕上的输出
        os.system("clear")
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
