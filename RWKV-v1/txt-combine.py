import os,chardet,shutil,sys

out=input('请输入要导入txt文件夹：')
inout='./合并.txt'
mis=input('请输入执行错误后存放的地方(也可以不输入直接回车就行):')
# mis=''
# out = "C:\\Users\\46045\\Desktop\\新建文件夹 (2)"
# inout="C:\\Users\\46045\\Desktop\\asd.txt"
dis=os.listdir(out)

c=3
b=int(len(dis))
for i in dis:
    c+=1
    try:
        t=len(dis)

        a=out+"\\"+i

        f = open(a, 'rb')
        r = f.read()
        f_charInfo = chardet.detect(r)
        f.close()

        if f_charInfo['encoding']!='None':
            with open(a, "r", encoding=f_charInfo['encoding']) as f1, \
                    open(inout, "a", encoding='utf-8') as f2:
                # print(f'正在导入  {i}')
                for line in f1:
                    f2.write("{}\n".format(line))
                f2.close()

        elif f_charInfo['encoding']!='gb2312':
            with open(a, "r", encoding="ansi") as f1, \
                    open(inout, "a", encoding='utf-8') as f2:
                # print(f'正在导入  {i}')
                for line in f1:
                    f2.write("{}\n".format(line))
                f2.close()

        else:
            with open(a, "r", encoding='utf-8') as f1, \
                    open(inout, "a", encoding='utf-8') as f2:
                # print(f'正在导入  {i}')
                for line in f1:
                    f2.write("{}\n".format(line))
                f2.close()

    except:   #总之是遇到错误用来存放的文件

        if mis=='':
            sys.stdout.write('\r发现错误文件: ' + i)
            sys.stdout.flush()
            continue

        else:
            print(f'发现错误文件   {i}   ！！！！！！')
            file_path  =  out + "\\" + i
            new_file_path = mis + '\\' + i
            shutil.move(file_path, new_file_path)

    sys.stdout.write('\r进度: ' + '%.2f%%' % (int(c) / int(b)))
    sys.stdout.flush()