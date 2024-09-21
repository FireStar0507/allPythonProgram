import time

def loading(nums, sleeptime=0.5, step=1, loaded="#", noloaded="-"):
    """
    显示一个简单的加载进度条动画。

    参数：
        nums (int): 进度条的总长度，即显示的 '#' 字符的数量。
        sleeptime (float, optional): 每次迭代之间的睡眠时间（秒）。默认值为 0.5 秒。
        step (int, optional): 每次迭代的步长，表示每次增加的 '#' 字符数量。默认值为 1。
        loaded (str, optional): 用于代表已加载部分的字符。默认值为 '#'。
        noloaded (str, optional): 用于代表未加载部分的字符。默认值为 '-'。

    示例：
        loading(18, 0.5, 2, "$", "!") 将会创建一个长度为 18 的进度条，每过0.5秒钟增加 2 个 '$' 字符，未加载部分用 '!' 表示。
    """
    for i in range(0, nums + 1, step):
        # 构建进度条字符串
        text = loaded * i + noloaded * (nums - i) + " " + str(round(i / nums * 100)) + "%"
        # 打印进度条并覆盖同一行
        print(text, end="\r")
        # 暂停一段时间以创建动画效果
        time.sleep(sleeptime)
