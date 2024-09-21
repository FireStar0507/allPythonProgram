import os, sys


class grammarCheck:
    def __init__(self, fileName):
        self.fileName = fileName
        self.text = ""

    def rewrite(self, text):
        self.text = text
        with open(self.fileName, "w") as f:
            f.write(text)

    def ccm(self, symbol=(", ", " "), isRewrite=True):
        with open(self.fileName, "r", encoding="gbk") as file:
            textLists = file.readlines()
        
        for i in range(len(textLists)):
            text = textLists[i]
            newText = ""
            j = 0
            while j < len(text):
                if text[j] == symbol[0]:
                    newText += symbol[0]
                    if j + 1 < len(text) and text[j + 1] != symbol[1]:
                        newText += symbol[1]
                else:
                    newText += text[j]
                j += 1
            textLists[i] = newText
        
        alls = "".join(textLists)
        if isRewrite:
            self.rewrite(alls)
        else:
            self.text = alls


def adapter(path="."):
    for f in os.listdir(path):
        if f != sys.argv[0]:
            grammarCheck(f).ccm()
            print(f"{f}已经重写")


# 使用实例
adapter()

