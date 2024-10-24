import pyperclip
import re
import time

# 正则表达式匹配 \ 和 ()
pattern_square = r'\\\[(.*?)\\\]'
pattern_parenthesis = r'\\\((.*?)\\\)'

# 上次的剪贴板内容
previous_clipboard = ''

def process_clipboard():
    # 读取剪贴板内容
    clipboard_content = pyperclip.paste()

    global previous_clipboard
    if clipboard_content != previous_clipboard:
        # 匹配并替换\和()内容
        processed_content = re.sub(pattern_square, r'$\1$', clipboard_content)
        processed_content = re.sub(pattern_parenthesis, r'$\1$', processed_content)

        # 如果内容有变化，更新剪贴板
        if processed_content != clipboard_content:
            print(f"检测到剪贴板内容变化")
            pyperclip.copy(processed_content)
            print(f"更新剪贴板内容")

        previous_clipboard = clipboard_content

if __name__ == "__main__":
    print("正在监控剪贴板内容...")
    while True:
        process_clipboard()
        time.sleep(1)  # 每秒检测一次剪贴板内容
