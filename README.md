# 🎬 Subtitle Tool / 字幕工具集 

[English version](https://github.com/HungryNeko/Subtitle_tool/blob/main/README_EN.md)

一个用于管理与处理字幕文件的多功能 Python 工具集。
## 功能概览 
### 字幕重命名 — 自动将字幕文件名改为与视频文件一致，方便播放器自动匹配。

使用方法

    在命令行运行 renamefiles.py
    
    将包含视频和字幕文件的文件夹拖入终端窗口
    
    脚本会自动根据视频文件名（自然顺序）重命名对应字幕文件（自然顺序）
    
    示例
    [vid1.mp4, vid2.mp4, sub1.ass, sub2.ass] 
    → [vid1.mp4, vid2.mp4, vid1.ass, vid2.ass]

### 简繁转换 - 自动将繁体字幕转换为简体字幕

使用方法

    在命令行运行tra_sim.py

    选择源文件夹以及输出文件夹

    脚本会自动将繁体字母转换为简体字幕
