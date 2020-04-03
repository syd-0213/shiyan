
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

var_name=StringVar()
textbox1=Entry(top,textvariable=var_name)
textbox1.grid_configure(column=2,row=1,columnspan=3,rowspan=1)

var_password=StringVar()
textbox2=Entry(top,textvariable=var_password)
textbox2.grid_configure(column=2,row=2,columnspan=3,rowspan=1)

button1=Button(top,text='登录',command=lambda:Login()).grid(column=3,row=4,columnspan=3,rowspan=1)
button2=Button(top,text='退出',command=lambda:quit_()).grid(column=5,row=4,columnspan=3,rowspan=1)

def quit_():
    top.destroy()

def Login():
    s1=textbox1.get()
    s2=textbox2.get()
    if s1 in teacher and s2==teacher[s1]:
        messagebox.showinfo('登陆成功','欢迎')
        top.destroy()
        top_=Tk()
        top_.title=('学生管理系统')
        
        button4=Button(top_,text='添加成绩',command=lambda:add()).place(x=100,y=50)
        button5=Button(top_,text='查看成绩',command=lambda:search()).place(x=100,y=100)
        button6=Button(top_,text='退出系统',command=lambda:quit1()).place(x=100,y=150)
    
    else:
        messagebox.showinfo('登陆失败','用户名或密码错误')
    def quit1():    #定义退出系统按钮
        top_.destroy()
    def add():     #定义添加成绩按钮
        window1=Tk()
        window1.title('提示')
        lab1=Label(window1,text='请输入学生姓名').place(x=20,y=10)
        
        
        name1=StringVar()
        tex1=Entry(window1,textvariable=name1)
        tex1.place(x=20,y=50)

        
        
        
        but1=Button(window1,text='OK',command=lambda:OK_()).place(x=20,y=80)
        but2=Button(window1,text='Cancel',command=lambda:Cancel_()).place(x=60,y=80)

    
        def Cancel_():
            window1.destroy()
        def OK_():   #真正的添加成绩
            n1=tex1.get()
            if n1 in student:
                messagebox.showinfo('错误','该学生已经存在')
            else:
                window1.destroy()
                window2=Tk()
                
                lab2=Label(window2,text='请输入学生成绩').place(x=20,y=10)
                name2=StringVar()
                tex2=Entry(window2,textvariable=name2)
                tex2.place(x=20,y=50)
                
                but3=Button(window2,text='OK',command=lambda:OK2()).place(x=20,y=80)
                but4=Button(window2,text='Cancel',command=lambda:Cancel2()).place(x=60,y=80)
                
                def Cancel2():
                    window2.destroy()
                def OK2():
                    n2=tex2.get()
                    student[n1]=n2
                    window2.destroy()


    def search(): #定义查询成绩
        window3=Tk()
        lab4=Label(window3,text='请输入学生姓名').place(x=20,y=10)
        name4=StringVar()
        tex4=Entry(window3,textvariable=name4)
        tex4.place(x=20,y=50)
        but5=Button(window3,text='查询',command=lambda:search_()).place(x=20,y=80)
        def search_():
            name_=tex4.get()
        
            if name_ not in student:
                messagebox.showinfo('错误','该学生不存在')
            else:
                print('姓名：',name_,'成绩',student[name_])

            window3.destroy()



top.mainloop()