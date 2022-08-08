import pyautogui
import time
import win32gui

if __name__ == '__main__':
    print('开始自动钓鱼')
    hwnd = win32gui.FindWindow('GLFW30',None) #找到窗口并赋给hwnd(这个hwnd的名字自己可以随便改，但改了之后下面所有的hwnd都要一起改) 括号内 逗号前面的是窗口的类名，逗号后面是窗口的名字。
    win32gui.SetForegroundWindow(hwnd) #将hwnd的窗口激活到窗口的最前方
    print(win32gui.GetClassName(hwnd)) #获得hwnd的窗口的类名，因为窗口的名字有时候会变，所以获取类名知道窗口的类名后，用类名会比较好。
    left, top, right, bottom = win32gui.GetWindowRect(hwnd) #获得hwnd窗口在整个电脑画面中的坐标
    print('窗口位置',left, top, right, bottom) #打印出来上一行获得的坐标值
    ex_w=int(0.25*(right-left)) #下面要用的截图宽度，这里用小学数学来计算，因为我根本不会算法。int()是将数值变成整数，不然有小数点的话下面会用不了报错。
    ex_h=int(0.5*(bottom-top)) #下面要用的截图高度
    ex_x=int(right-ex_w) #下面要用的截图起始X坐标
    ex_y=int(bottom-ex_h) #下面要用的截图起始Y坐标
    time.sleep(1) #等待1秒
    pyautogui.click('back2game.png') #识别项目根目录下的一张图片并点击
    pyautogui.click(button='right') #点击鼠标右键
    mis=0 #暂时没用到
    suc=0 #成功钓鱼的次数，初始是0
    #result = pyautogui.locateOnScreen('wt.png', region=(ex_x,ex_y,ex_w,ex_h))
    while(True):
        result= pyautogui.locateOnScreen('wt.png', region=(ex_x,ex_y,ex_w,ex_h)) #识别屏幕的(ex_x,ex_y,ex_w,ex_h)区域画面中是否有项目根目录下的一张叫wt.png的图片，没有识别到就返回None，赋值给result。
        if result !=None: #如果result不等于None，执行↓
            pyautogui.click(button='right') #点鼠标右键
            time.sleep(1)
            pyautogui.click(button='right') #点鼠标右键
            #print('等待时间约为:%ds' %())
            #mis=0
            suc+=1 #成功次数+1
            print("成功次数%d"%(suc)) #打印成功次数suc的值
            time.sleep(2)
        else: #result等于None时，执行↓
            mis+=1
            time.sleep(0.5)

