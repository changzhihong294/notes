list = ['电脑', '显示器', '笔记本', '机械键盘']
num_list = '''
(0)电脑
(1)显示器
(2)笔记本
(3)机械键盘
请输入(0/1/2/3)：'''
aa = int(input(num_list))
print(list[aa])

bb = input('是否要添加商品:(y/n) ')
if bb == 'y':
    cc = input('写出你要添加的商品:')
    list.append(cc)
    print(list)
