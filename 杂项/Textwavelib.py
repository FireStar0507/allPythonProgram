"""
在控制台中创建基于文本的波浪动画。
由 FireStar0507 编写
Creates a text-based wave animation in the console.
Written by FireStar0507
"""
import time, sys  # 导入 time 库控制时间，sys 库用于退出程序

def textwave(content= ["*", 1, 1, 10, 1], filler= [" ", 1, 1, 10, 1], interval=0.1):
"""
    参数：
        content（列表）：定义内容字符及其行为的列表：
                         - content[0]：用于波浪的字符（默认为“*”）。
                         - content[1]：初始方向（1 表示增加，0 表示减少）。
                         - content[2]：内容字符的初始计数。
                         - content[3]：内容字符的最大计数。
                         - content[4]：内容字符的最小计数。
        filler（列表）：定义空白填充物字符及其行为的列表（与“content”的结构相同）。
        interval （数值）：每个动画帧之间的时间间隔（以秒为单位）。
    Args:
        content (list): A list defining the content character and its behavior:
                         - content[0]: The character used for the wave (default "*").
                         - content[1]: Initial direction (1 for increasing, 0 for decreasing).
                         - content[2]: Initial count of the content character.
                         - content[3]: Maximum count of the content character.
                         - content[4]: Minimum count of the content character.
        filler (list):  A list defining the filler character and its behavior (same structure as 'content').
        interval (float): The time interval between each animation frame (in seconds).


"""
    try:
        print("Start!!!")
        while True:
            text = filler[0] * filler[2] + content[0] * content[2]
            print(text)
            time.sleep(interval)

            # Control content character count
            if content[1] == 1:
                content[2] += 1
                if content[2] == content[3]:
                    content[1] = 0
            elif content[1] == 0:
                content[2] -= 1
                if content[2] == content[4]:
                    content[1] = 1

            # Control filler character count (same logic as content)
            if filler[1] == 1:
                filler[2] += 1
                if filler[2] == filler[3]:
                    filler[1] = 0
            elif filler[1] == 0:
                filler[2] -= 1
                if filler[2] == filler[4]:
                    filler[1] = 1

    except KeyboardInterrupt:
        print("\nThe end")
        sys.exit()

