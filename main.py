import pyperclip
import re
import time

# 正则表达式匹配 \[ \] (包括换行) 和 \( \) 之间的内容
pattern_square = r'\\\[\r\n\s*([\s\S]*?)\r\n\s*\\\]'
pattern_parenthesis = r'\\\(\s*(.*?)\s*\\\)'
pattern_fix = r'\$\s*([\s\S]*?)\s*\$'

# 上次的剪贴板内容
previous_clipboard = ''

def process_clipboard():
    # 读取剪贴板内容
    clipboard_content = pyperclip.paste()

    global previous_clipboard
    if clipboard_content != previous_clipboard:
        # 匹配并替换 LaTeX 数学公式块内容
        processed_content = re.sub(pattern_square, r'$\1$', clipboard_content)
        processed_content = re.sub(pattern_parenthesis, r'$\1$', processed_content)
        processed_content = re.sub(pattern_fix, r'$\1$', processed_content)

        # 如果内容有变化，更新剪贴板
        if processed_content != clipboard_content:
            print(f"检测到剪贴板内容变化")
            pyperclip.copy(processed_content)
            print(f"更新剪贴板内容")

        # 将剪贴板内容更新到previous_clipboard，避免重复处理
        previous_clipboard = clipboard_content

if __name__ == "__main__":
    print("正在监控剪贴板内容...")
    while True:
        process_clipboard()
        time.sleep(1)  # 每秒检测一次剪贴板内容
