aa = ['电脑','显示器','笔记本','机械键盘']
while True :
    bb = """
请选择(1/2)
(1)列出商品:
(2)添加商品:"""
    cc = int(input(bb))

    if cc == 1:
        print(aa)
        lc = int(input('请输入序号:'))
        print(aa[lc])
        break
    elif cc == 2:
        add  = input('请写出你要添加的商品:')
        aa.append(add)
        print(aa)
        break
    else:
        print('不在范围之内,请选择(1/2)')
