
"""

@author: ASUS
"""
teacher={'admin1':'123456','admin2':'987654321','mm':'123'}

student={'BZB':100,'bzb':80,'Bzb':95}

from tkinter import*
from tkinter import messagebox

top=Tk()
top.title('学生管理系统登录页面')

label1=Label(top,text='用户名:')
label2=Label(top,text='密码:')

textbox1=Text(top,height=1,width=12)
textbox2=Text(top,height=1,width=12)


label1.grid_configure(column=1,row=1,columnspan=1,rowspan=1)
label2.grid_configure(column=1,row=2,columnspan=1,rowspan=1)