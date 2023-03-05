import tkinter as tk
from db import db
from tkinter import ttk


# 录入类
class InputFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, stick=tk.W, pady=10)
        tk.Label(self, text="姓名:").grid(row=1, stick=tk.W, pady=10)
        # 单行文本框 entry，textvariable绑定变量
        tk.Entry(self, textvariable=self.name).grid(row=1, column=1, stick=tk.E)

        tk.Label(self, text="数学:").grid(row=2, stick=tk.W, pady=10)
        # 单行文本框 entry，textvariable绑定变量
        tk.Entry(self, textvariable=self.math).grid(row=2, column=1, stick=tk.E)

        tk.Label(self, text="语文:").grid(row=3, stick=tk.W, pady=10)
        # 单行文本框 entry，textvariable绑定变量
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=1, stick=tk.E)

        tk.Label(self, text="英语:").grid(row=4, stick=tk.W, pady=10)
        # 单行文本框 entry，textvariable绑定变量
        tk.Entry(self, textvariable=self.english).grid(row=4, column=1, stick=tk.E)

        tk.Button(self, text="录入", command=self.recode_student).grid(row=5, column=1, stick=tk.E, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=1, stick=tk.E, pady=10)

    # 录入成绩
    def recode_student(self):
        student = {
            "name": self.name.get(),
            "math": self.math.get(),
            "chinese": self.chinese.get(),
            "english": self.english.get(),
        }  # 一个学生的成绩
        db.insert(student)
        # get()得到值
        # set()设置值
        self.status.set("插入数据成功！")
        self._clear_data()
        db.save_data()

    # 清空文本数据
    def _clear_data(self):
        self.name.set("")
        self.math.set("")
        self.chinese.set("")
        self.english.set("")


# 查询类
class QuerryFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.create_page()

    # 创建查询界面
    def create_page(self):
        self.create_tree_view()
        self.show_data_frame()
        # grid()
        tk.Button(self, text="刷新数据", command=self.show_data_frame).pack(anchor=tk.E, pady=5)

    # Treeview
    def create_tree_view(self):
        # 表头
        columns = ("name", "chinese", "math", "english")
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column("name", width=80, anchor='center')
        self.tree_view.column("chinese", width=80, anchor='center')
        self.tree_view.column("math", width=80, anchor='center')
        self.tree_view.column("english", width=80, anchor='center')
        self.tree_view.heading("name", text='姓名')
        self.tree_view.heading("chinese", text='语文')
        self.tree_view.heading("math", text='数学')
        self.tree_view.heading("english", text='英语')
        self.tree_view.pack()

    # 显示数据
    def show_data_frame(self):
        # 删除原节点 map(int,值）
        for i in map(self.tree_view.delete, self.tree_view.get_children("")):
            pass
        # 拿到列表里面所有值、students[]
        students = db.all()
        # 同时拿到索引跟value值
        for index, stu in enumerate(students):
            self.tree_view.insert('', index, values=(stu["name"], stu["chinese"], stu
            ["math"], stu["english"]))


class DeleteFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        tk.Label(self, text='删除数据').pack()
        self.status = tk.StringVar()
        self.de_name = tk.StringVar()  # 获取删除学生的姓名
        self.create_page()

    # 创建界面
    def create_page(self):
        tk.Label(self, text="根据姓名删除信息").pack(anchor=tk.W, padx=20)
        e1 = tk.Entry(self, textvariable=self.de_name)
        e1.pack(side=tk.LEFT, padx=20, pady=5)

        tk.Button(self, text='删除', command=self._delete).pack(side=tk.RIGHT)
        tk.Label(self, textvariable=self.status).pack()

    # 删除
    def _delete(self):
        name = self.de_name.get()
        print(name)
        result = db.delete_by_name(name)
        if result:
            self.status.set(f'{name}已经被删')
            self.de_name.set("")
        else:
            self.status.set(f'{name}不存在')


class UpdateFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        tk.Label(self, text='修改界面').pack()
        self.change_frame = tk.Frame(self)
        self.change_frame.pack()
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self.change_frame).grid(row=0, stick=tk.W, pady=10)
        tk.Label(self.change_frame, text="姓名:").grid(row=1, stick=tk.W, pady=10)
        # 单行文本框 entry，textvariable绑定变量
        tk.Entry(self.change_frame, textvariable=self.name).grid(row=1, column=1, stick=tk.E)

        tk.Label(self.change_frame, text="数学:").grid(row=2, stick=tk.W, pady=10)
        # 单行文本框 entry，textvariable绑定变量
        tk.Entry(self.change_frame, textvariable=self.math).grid(row=2, column=1, stick=tk.E)

        tk.Label(self.change_frame, text="语文:").grid(row=3, stick=tk.W, pady=10)
        # 单行文本框 entry，textvariable绑定变量
        tk.Entry(self.change_frame, textvariable=self.chinese).grid(row=3, column=1, stick=tk.E)

        tk.Label(self.change_frame, text="英语:").grid(row=4, stick=tk.W, pady=10)
        # 单行文本框 entry，textvariable绑定变量
        tk.Entry(self.change_frame, textvariable=self.english).grid(row=4, column=1, stick=tk.E)

        # 按钮
        tk.Button(self.change_frame, text='查询', command=self._search).grid(row=6, column=0, stick=tk.W, pady=10)
        tk.Button(self.change_frame, text='修改', command=self._change).grid(row=6, column=1, stick=tk.E, pady=10)

        tk.Label(self.change_frame, textvariable=self.status).grid(row=7, column=1, stick=tk.E, pady=10)

    # 查询
    def _search(self):
        name = self.name.get()
        student = db.search_by_name(name)
        if student:
            self.math.set(student["math"])
            self.chinese.set(student["chinese"])
            self.english.set(student["english"])
            self.status.set(f'查询到{name}同学的信息')
        else:
            self.status.set(f'没有查询到{name}同学的信息')

    #  更改成绩
    def _change(self):
        name = self.name.get()
        math = self.math.get()
        chinese = self.chinese.get()
        english = self.english.get()
        stu = {
            "name": name,
            "math": math,
            "chinese": chinese,
            "english": english,
        }
        r = db.update(stu)
        if r:
            self.status.set(f"{name}同学的信息更新完毕")
        else:
            self.status.set(f"{name}同学的信息更新失败")


class AboutFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.create_page()

    def create_page(self):
        tk.Label(self, text="Made by Chen Yeguo").pack(anchor=tk.W)