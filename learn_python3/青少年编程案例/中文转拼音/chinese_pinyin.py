import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from xpinyin import Pinyin
import win32clipboard as wcb
import win32con as wc

def transfer_to_pinyin():
    """左功能区->`转换为拼音`按钮"""
    pinyin = Pinyin()
    chinese_str = chinese_txt.get('1.0', tk.END)
    # 删除多余的Text组件产生换行符
    chinese_str = chinese_str.removesuffix('\n')
    # 拼音使用小写，显示字符声调，拼音之间使用空格
    pinyin_str = pinyin.get_pinyin(chinese_str, tone_marks='marks', splitter=' ', convert='lower')
    pinyin_txt.delete('1.0', tk.END)
    pinyin_txt.insert('1.0', pinyin_str)


def clear_txt():
    """右功能区->`清除`按钮"""
    chinese_txt.delete('1.0', tk.END)
    pinyin_txt.delete('1.0', tk.END)


def copy_pinyin():
    """右功能区->`复制结果`按钮"""
    # 打开复制粘贴板
    wcb.OpenClipboard()
    # 清空剪切板
    wcb.EmptyClipboard()
    # 将内容写入复制粘贴板,第一个参数win32con.CF_TEXT
    # 关键第二个参数，就是我们要复制的内容，一定要传入字节
    pinyin_str = pinyin_txt.get('1.0', tk.END)
    wcb.SetClipboardData(wc.CF_TEXT, pinyin_str.encode('gbk'))  # Windows中文操作系统默认使用gbk编码
    # 关闭复制粘贴板
    wcb.CloseClipboard()


def main():
    # 需要被其他函数来访问, 因此需要变成global变量
    global chinese_txt, pinyin_txt

    root_win = tk.Tk()
    root_win.title('中文转拼音')
    root_win.resizable(0, 0)
    # ==== 左半部分功能
    left_frame = ttk.Frame(root_win)
    left_frame.grid(row=0, column=0)
    chinese_lbl = ttk.Label(left_frame, text='待转化的内容')
    chinese_lbl.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)  # 靠左对齐
    chinese_txt = ScrolledText(left_frame)
    chinese_txt.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)  # 靠左对齐
    transfer_btn = ttk.Button(left_frame, text='转换为拼音', command=transfer_to_pinyin)
    transfer_btn.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)  # 靠左对齐

    # ==== 右半区的功能
    right_frame = tk.Frame(root_win)
    right_frame.grid(row=0, column=1)

    pinyin_lbl = ttk.Label(right_frame, text='拼音转换结果')
    pinyin_lbl.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)  # 靠左对齐
    pinyin_txt = ScrolledText(right_frame)
    pinyin_txt.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)  # 靠左对齐
    right_btn_frame = ttk.Frame(right_frame)

    right_btn_frame.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)  # 靠左对齐
    copy_btn = ttk.Button(right_btn_frame, text='复制结果', command=copy_pinyin)
    copy_btn.grid(row=0, column=0, sticky=tk.W)  # 靠左对齐
    clear_btn = ttk.Button(right_btn_frame, text='清空', command=clear_txt)
    clear_btn.grid(row=0, column=1, sticky=tk.W)  # 靠左对齐

    # ==== 消息处理循环
    root_win.mainloop()


if __name__ == '__main__':
    main()
