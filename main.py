import json
import ctypes, sys
from collections import OrderedDict

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
# 由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中

# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLACK = 0x00  # black.
FOREGROUND_DARKBLUE = 0x01  # dark blue.
FOREGROUND_DARKGREEN = 0x02  # dark green.
FOREGROUND_DARKSKYBLUE = 0x03  # dark skyblue.
FOREGROUND_DARKRED = 0x04  # dark red.
FOREGROUND_DARKPINK = 0x05  # dark pink.
FOREGROUND_DARKYELLOW = 0x06  # dark yellow.
FOREGROUND_DARKWHITE = 0x07  # dark white.
FOREGROUND_DARKGRAY = 0x08  # dark gray.
FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_SKYBLUE = 0x0b  # skyblue.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_PINK = 0x0d  # pink.
FOREGROUND_YELLOW = 0x0e  # yellow.
FOREGROUND_WHITE = 0x0f  # white.

# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_BLUE = 0x10  # dark blue.
BACKGROUND_GREEN = 0x20  # dark green.
BACKGROUND_DARKSKYBLUE = 0x30  # dark skyblue.
BACKGROUND_DARKRED = 0x40  # dark red.
BACKGROUND_DARKPINK = 0x50  # dark pink.
BACKGROUND_DARKYELLOW = 0x60  # dark yellow.
BACKGROUND_DARKWHITE = 0x70  # dark white.
BACKGROUND_DARKGRAY = 0x80  # dark gray.
BACKGROUND_BLUE = 0x90  # blue.
BACKGROUND_GREEN = 0xa0  # green.
BACKGROUND_SKYBLUE = 0xb0  # skyblue.
BACKGROUND_RED = 0xc0  # red.
BACKGROUND_PINK = 0xd0  # pink.
BACKGROUND_YELLOW = 0xe0  # yellow.
BACKGROUND_WHITE = 0xf0  # white.

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


# reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


###############################################################

# 暗蓝色
# dark blue
def printDarkBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKBLUE)
    sys.stdout.write(mess)
    resetColor()


# 暗绿色
# dark green
def printDarkGreen(mess):
    set_cmd_text_color(FOREGROUND_DARKGREEN)
    sys.stdout.write(mess)
    resetColor()


# 暗天蓝色
# dark sky blue
def printDarkSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
    sys.stdout.write(mess)
    resetColor()


# 暗红色
# dark red
def printDarkRed(mess):
    set_cmd_text_color(FOREGROUND_DARKRED)
    sys.stdout.write(mess)
    resetColor()


# 暗粉红色
# dark pink
def printDarkPink(mess):
    set_cmd_text_color(FOREGROUND_DARKPINK)
    sys.stdout.write(mess)
    resetColor()


# 暗黄色
# dark yellow
def printDarkYellow(mess):
    set_cmd_text_color(FOREGROUND_DARKYELLOW)
    sys.stdout.write(mess)
    resetColor()


# 暗白色
# dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(mess)
    resetColor()


# 暗灰色
# dark gray
def printDarkGray(mess):
    set_cmd_text_color(FOREGROUND_DARKGRAY)
    sys.stdout.write(mess)
    resetColor()


# 蓝色
# blue
def printBlue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    sys.stdout.write(mess)
    resetColor()


# 绿色
# green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()


# 天蓝色
# sky blue
def printSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()


# 红色
# red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()


# 粉红色
# pink
def printPink(mess):
    set_cmd_text_color(FOREGROUND_PINK)
    sys.stdout.write(mess)
    resetColor()


# 黄色
# yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()


# 白色
# white
def printWhite(mess):
    set_cmd_text_color(FOREGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()


##################################################

# 白底黑字
# white bkground and black text
def printWhiteBlack(mess):
    set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()


# 白底黑字
# white bkground and black text
def printWhiteBlack_2(mess):
    set_cmd_text_color(0xf0)
    sys.stdout.write(mess)
    resetColor()


# 黄底蓝字
# white bkground and black text
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()


##################################################################################


recipes = json.load(open(r'basic.json', 'r', encoding='utf-8'))
advanced_recipes = json.load(open('Formula.json', 'r', encoding='utf-8'))
built_by = json.load(open('built_by.json', 'r', encoding='utf-8'))

#
igo = ["处理器", "硫酸"]


def advanced_recipes(name):
    recipes[name] = advanced_recipes[name]


advanced_recipes("碳纳米管")
advanced_recipes("石墨烯")
advanced_recipes("硫酸")
advanced_recipes("有机晶体")


def search_recipe(name, pcs, result, parent):
    if name in recipes:
        entry = recipes[name]
        if name not in result:
            result[name] = dict()
            result[name]["pcs"] = 0
            result[name]["dest"] = set()
        result[name]["pcs"] += pcs
        result[name]["dest"].add(parent)
        if "end" in entry or name in igo:
            return
        else:
            for i,j in entry["req_item"].items():
                search_recipe(i, pcs * j, result, name)
            return
    printYellowRed("⚠输入字符非法，请重新输入⚠")


def depend(parent_name, child_name):
    result = dict()
    search_recipe(parent_name, 1, result, "")
    return (child_name in result)



def main():
    printDarkSkyBlue("输入要计算的材料:\n")
    req = input().split(",")
    printRed('输入所需产量，单位为个/秒:\n')
    gen_speed = float(input())
    req_name = req[0]
    req_pcs = 1 if len(req) != 2 else float(req[1])
    result = dict()
    search_recipe(req_name, req_pcs, result, "")
    result = OrderedDict(sorted(result.items(), key=lambda x: x[1]["pcs"]))
    print(f"【目标产量 = {gen_speed:1.2f} 份/秒】")
    printDarkGreen(
        '************************************************************************************************************************\n')
    print(f"| {'材料名称':^28} | {'材料数':>6} | {'制造方式'}| {'机器数量'} ||{'目的产物'}| ")
    consumption = 0
    for name, d in result.items():
        e = recipes[name]
        temp = e["制造方式"]
        pcs = d["pcs"]
        if "sec" in e:
            n = pcs * e["sec"] * gen_speed
            consumption += e["sec"] * built_by[temp]["work"] * pcs
        else:
            n = pcs * 1 / built_by[temp]["speed"] * gen_speed
        dep = ""
        dest = list(d["dest"])
        print(f"| {name:^29} |", f" {pcs:>6.2f} ", f"| {temp:^5} | ", f"{n:>5.2f} |", dest[0])
    printDarkGreen(
        '************************************************************************************************************************\n')
    print('\n')
    print(f"|{'能量消耗':^28}| {consumption / 1000} MJ / 份材料 = {consumption / 1000 * gen_speed} MW / s".center(10))


if __name__ == '__main__':
    printDarkYellow('''
    ____                            _____       __                      ______      __           __      __            
   / __ \__  ___________  ____     / ___/____  / /_  ___  ________     / ____/___ _/ /______  __/ /___ _/ /_____  _____
  / / / / / / / ___/ __ \/ __ \    \__ \/ __ \/ __ \/ _ \/ ___/ _ \   / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
 / /_/ / /_/ (__  ) /_/ / / / /   ___/ / /_/ / / / /  __/ /  /  __/  / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
/_____/\__, /____/\____/_/ /_/   /____/ .___/_/ /_/\___/_/   \___/   \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
      /____/                         /_/                                                                               

''')
while (True):
    main()
