from pynput import mouse,keyboard
import time
m = mouse.Controller()

mpress = mouse.Button
n = keyboard.Controller()
'''''
while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
    if time_now == "06:30:00":  # 此处设置每天定时的时间
        m.position = (519, 1130)
        m.press(mpress.left)
        m.release(mpress.left)
        m.position = (717, 1067)
        time.sleep(1)
        m.press(mpress.right)
        m.release(mpress.left)
        n.press(keyboard.Key.enter)
        n.release(keyboard.Key.enter)
        # 此处3行替换为需要执行的动作
        print("hello")
        subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 定时发送测试"
        print(subject)
        break
'''''
#time.sleep(2)
from datetime import datetime
import time
import schedule
def job_run_once(*args):
    m.position = (519, 1130)
    m.press(mpress.left)
    m.release(mpress.left)
    m.position = (717, 1067)
    time.sleep(1)
    m.press(mpress.right)
    m.release(mpress.left)
    n.press(keyboard.Key.enter)
    n.release(keyboard.Key.enter)
    #
    return schedule.CancelJob


# 只执行一次任务
schedule.every().day.at('06:30:00').do(job_run_once)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)




#(754, 1058)