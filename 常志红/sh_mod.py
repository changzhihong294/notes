# import  shutil
# f1 = open('/etc/passwd','rb')
# f2 = open('/tmp/xxx','wb')
#
# shutil.copyfileobj(f1,f2)
#
# f1.close()
# f2.close()
#
# shutil.copyfile('/etc/passwd','/tmp/xyz')    #拷贝文件
# shutil.copy('/etc/passwd','/tmp')
# shutil.copy('/etc/passwd','/tmp/aabb')
# shutil.copy2('/etc/passwd','/tmp/aabbcc')   #copy2 权限拷贝，相当于cp  -p

# import  shutil
#
# shutil.copytree('/etc/security','/tmp/anquan')
# shutil.rmtree(/tmp/anquan)   #删除
#

# 变量赋值
# a =10
# b = 20
# a,b = b, a
#
# import keyword
#
# keyword.kwlist  # 查看定义的关键字
# keyword.iskeyword('pass')  # 查看是否为关键字
#
#
# import  os
# os.path.exists('/tmp')   #判断文件是否存在
#

# 1.思考一下，程序的运行场景
# 2.构思程序的结构，把每一个功能
#
# import os
#
#
# def get_fname():
#     while True:
#         fname = input('请输入一个文件名:')
#         if not os.path.exists(fname):
#             break
#         print('文件以存在,请从新输入')
#         # print('%s 文件以存在，请从新输入' % fname)
#     return fname
#
#
# def get_content():
#     content = []
#     print('请输入正文，end结束')
#     while True:
#         line = input('>')
#         if line == 'end':
#             break
#         content.append(line)
#     return content
#
#
# def wfile(fname, content):
#     with open(fname, 'w') as fobj:
#         fobj.writelines(content)
#
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n' % line for line in content]
#     wfile(fname, content)

#
# fib = [0,1]
# aa = int(input('请输入一个数:'))
# for  i in range(aa):
#  fib.append(fib[-1] + fib[-2])
#
# print(fib)
#
# for i  in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s' % (j,i , i*j),end=' ')
#     print()


# aa = open('/bin/ls','rb')
# bb = open('/root/ls','wb')
#
# data=aa.read()
# bb.write(data)
#
# aa.close()
# bb.close()
#
# import shutil
# aa = open('/etc/passwd','rb')
# bb = open('/tmp/aaa','wb')
#
# shutil.copyfileobj(aa,bb)
# aa.close()
# bb.close()


#字符串

# users = ['bob','alice','john']
#
# for i  in range(len(users)):
#     print('#%s :%s' % (i,users[i]))
#
# list(enumerate(users))    #>>> list(enumerate(users)) [(0, 'bob'), (1, 'alice'), (2, 'john')]

# for item in enumerate(users):   #应用时不必替换
#     print('#%s : %s' % (item[0],item[1]))
#
# for ind,user in enumerate(users):
#     print('#%s : %s' % (ind,user))


# for u in reversed(users):    #反序
#     print(u)
#
# sorted(users)   #排序


#字符编码 ：ASCII

#
# from string import  ascii_letters,digits
# from  keyword import  iskeyword
#
# first_chs = ascii_letters + '_'   #首字母可以使用大小写字母和下划线
# other_chs = first_chs + digits    #其他可以使用大小写字母和下划线、数字
#
# def check_id(idt):
#     if iskeyword(idt ):     #输入的是否为关键字
#         return  '%s is keyword'  % idt
#
#     if idt[0] not in first_chs:    #当输入的第一个字没有first_chs中的值的话
#         return '1st invalid'
#
#     for ind, ch in enumerate(idt[1:]):
#         if ch not in other_chs:
#             return '第%s个字符不合法'  % (ind + 2)
#
#     return '%s是合法的'  % idt
#
# if __name__ == '__main__':
#     idt = input('代检查的标示符:')
#     print(check_id(idt))

####################常用############
# '%s is %s years old'  % ('bob',25)
# '%s is %d years old'   % ('bob',25)
# '%12s%8s'  % ('name','age')    #右对齐
# '%-12s%8s' % ('name','age')
# '%-12s%-8s'  % ('bob',25)     #左对齐
#
# #############不常用####################
# '%c' % 98
# '#%o' % 30   #8进制数

#############################


# import subprocess    #调用shell
# subprocess.call('ls /root' shell=True)
############################################
#创建用户
# 1.  编写一个程序,实现创建用户的功能
# 2.  提示用户输入用户名
# 3.  随机生成8位密码
# 4.  创建用户并设置密码
# 5.  将用户相关信息写入指定文件

# import sys
# import subprocess
# from  randpass import  randpass
#
# def adduser(username,password,fname):
#
#   subprocess.call('useradd %s' % username,shell=True)
#   subprocess.call('echo %s | passwd --stdin %s' % (password,username),shell=True)
#
#   user_info = '''user information:
# 用户名: %s
# 密码：  %s
# '''% (username,password)
#
#   with open(fname,'a') as fobj:
#       fobj.write(user_info)
#
# if __name__ == '__main__':
#     username = sys.argv[1]
#     password = randpass()
#     adduser(username,password,'/tmp/users.txt')
# #
# win_path = 'c: \temp\newdir'
#
# win_path = 'c: \\temp\\newdir'
# wpath = r'c:\temp\newdir'
#
#
#
# print('+%s+'  % ('*'))


# astr = '\thello'
# astr.split()   #去除两端空白字符
# astr.lstrip()  #去除左端空白字符
# astr.rsplit()  #去除右端空白字符
# 'hello.tar.gz'.split('.')   #以点切割
#
# hi = 'hello world'
# hi.title()    #首写字母大写
# hi.upper()    #大写
# hi.lower()    #
# hi.islower()  #有一个大写或着小写，不统一，返回false
# 'hao123'.isdigit()   #不统一，返回false
# hi.isdigit()
# hi.center(50)
# hi.center(50,'#')
# hi.ljust(50)
# hi.rjust(50)
# hi.startswith('he')
# hi.endswith('d')    #查看hi中是否有d
# ##################更新列表
# alist = [1,50,60,100]
# alist[0] =10
# alist[1:3] = [30,40]
# alist[3:3] = [50,60,70,80,90]
# alist.append(30)   #追加
# alist.sort()  #排序
# alist.reverse()   #反序
# alist.remove(30)
# alist.pop()   #默认弹出最后一项
# alist.pop(2)
# alist.extend('abc')   #字符串
# alist.extend(['abc','xyc'])   #列表
# alist.index(50)   #50的下表
# alist.insert(3,1000)     #把1000放到下标为3的位置
#


#######################用列表构建栈结构
# 1.  栈是一个后进先出的结构
# 2.  编写一个程序,用列表实现栈结构
# 3.  需要支持压栈、出栈、查询功能
# stack = [] #全局变量，从定义开始到程度结束都可见可用
# def push_it():
#     item = input('上传项目 item to push:')
#     stack.append(item)
#     #print('push_it')
#
# def pop_it():
#     if stack:
#         print('pop:\033[31;1m %s\033[0m' % stack.pop())
#     #print('pop_it')
# def view_it():
#     print('\033[032;1m%s\033[0m' % stack)
#
# def show_menu():
#   cmds = {'0':push_it,'1':pop_it,'2':view_it}
#   prompt = '''(0) push it
# (1) pop it
# (2) view it
# (3) exit
# 请输入序号(0/1/2/3): '''
#
#   while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '0123':
#             print('无效输入，请重新输入')
#             continue
#         if choice == '3':
#             break
#         cmds[choice]()
#         # if choice == '0':
#         #     push_it()
#         # elif choice == '1':
#         #     pop_it()
#         # else:
#         #     view_it()
#
#
# if __name__ == '__main__':
#     show_menu()





