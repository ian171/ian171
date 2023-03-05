import tkinter as tk
from view import *


class MenuPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (600, 400))
        self.create_page()
        self.input_page = InputFrame(self.root)
        self.query_page = QuerryFrame(self.root)
        self.delete_page = DeleteFrame(self.root)
        self.update_page = UpdateFrame(self.root)
        self.about_page = AboutFrame(self.root)
        self.input_page.pack()

    def create_page(self):
        # 创建菜单对象
        menubar = tk.Menu(self.root)
        # add_command 添加
        menubar.add_command(label="录入", command=self.input_data)  # label
        menubar.add_command(label="查询", command=self.query_data)  # label
        menubar.add_command(label="删除", command=self.delete_data)  # label
        menubar.add_command(label="修改", command=self.update_data)  # label
        menubar.add_command(label="关于", command=self.about_data)  # label
        # 设置菜单栏
        self.root.config(menu=menubar)

    # 切换界面
    def input_data(self):
        self.input_page.pack()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.about_page.pack_forget()
        self.query_page.pack_forget()

    def query_data(self):
        self.input_page.pack_forget()
        self.query_page.pack()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.about_page.pack_forget()

    def update_data(self):
        self.input_page.pack_forget()
        self.update_page.pack()
        self.delete_page.pack_forget()
        self.about_page.pack_forget()
        self.query_page.pack_forget()

    def delete_data(self):
        self.input_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack()
        self.about_page.pack_forget()
        self.query_page.pack_forget()

    def about_data(self):
        self.input_page.pack_forget()
        self.update_page.pack_forget()
        self.delete_page.pack_forget()
        self.about_page.pack()
        self.query_page.pack_forget()