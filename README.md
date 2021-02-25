<p align="center">
    <img src="https://raw.githubusercontent.com/dafeigy/image/master/20210131233350.jpg" alt="logo"  />
</p>
<h1 align="center">戴森球计划产量计算器</h1>
<p align="center">
    <em>平白无奇的游戏菜鸡 又菜又爱玩</em>
</p>
<p align="center">
    <a href="https://www.mathworks.com/">
        <img src="https://img.shields.io/badge/Platform-steam-blue.svg" alt="Platform">
    </a>
    <a href="https://github.com/Dafeigy/Wireless-Calculator-based-on-2FSK">
        <img src="https://img.shields.io/badge/Version-0.6.15-red.svg" alt="Version">
    </a>
    <a href="https://github.com/Dafeigy/DysonSphere_Calculator/blob/main/README.md">
        <img src="https://img.shields.io/badge/Readme-Clickhere-yellow.svg" alt="README">
    </a>
    <a href="http://cybercolyce.cn/">
        <img src="https://img.shields.io/badge/Contact-Homepage-brightgreen.svg" alt="Contact">
    </a><p align="center">
    <a href="https://github.com/me-shaon/GLWTPL/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/Build-passing-purple.svg" alt="Build">
    </a>
    <a href="https://github.com/Dafeigy">
        <img src="https://img.shields.io/badge/Contribution-Wel♂cum-blue.svg" alt="contribution">
    </a>
    <a href="https://github.com/me-shaon/GLWTPL/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/License-GLWT-critical.svg" alt="License">
    </a>
</p>

# ❓这是什么&What Is This

这是一款模拟经营类游戏的辅助工具，用于帮助玩家计算产量所需的素材、能源以及机器数。**但是很遗憾的是现在仅支持用中文输入**😭

# 🌠我该怎么用

有两种办法：

## 1.如果你是python学习者👉

在你的IDE中运行`main.py`文件即可，懂的都懂👍

## 2.如果你和我一样懒:👉

**可以直接运行dist文件夹里的main.exe文件**。但是请注意：



<p align="center" style="font-size:40px">
   ❗那三个json文件不要删掉❗
</p>

## 运行截图：

![image-20210222212328132](https://raw.githubusercontent.com/dafeigy/image/master/20210222212328.png)



# 🙋‍后续有更新怎么办

问得好，本懒狗把数据保存在三个json文件里，更新的时候分别更新即可。

* `basic.json`:zap:这个文件保存了**基本**的合成公式、素材关系以及各自的常量信息
* `Formula.json`:cl:这个文件保存了高阶的合成公式，用于更快速的合成，官方应该在后续会有给新的
* `built_by.json`:zzz:这个文件保存了制作材料的方式，一般来讲不会更新吧...

# 🐟Todo List

- [x] ~~面向对象编程~~（json也算半个面向对象了是吧...）
- [ ] 递归结构实现（有点意思，可能会做，但意义不大）
- [ ] GUI页面设计（~~Excel也算GUI~~打算PyQT5做）
- [ ] 多语言（随缘,英文翻译比较麻烦）

# ❌错误修复

2021.2.25 修复分解部分的问题、补全宇宙矩阵的公式。