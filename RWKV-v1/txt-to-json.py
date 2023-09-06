import os


import re

#input dir
indir="D:\倒生树\书\A赫尔曼黑塞训练集"
#output dir
file_n=os.listdir(indir)
print(file_n)
outdir="D:\倒生树\书\A赫尔曼黑塞训练集\output.txt"
f2=open(outdir,"a",encoding="utf-8")
f2.write("[")
def not_empty(s):
    return s and s.strip()
 

for i in file_n:
    filepath=indir+"\\"+i
    print(i)
    #f=open("D:\倒生树\书\A赫尔曼黑塞训练集\给所有人的黑塞童话.txt", "r",encoding="utf-8")
    
    with open(filepath, "r", encoding="utf-8-sig") as f1:
        
        # print(f'正在导入  {i}')
        content=f1.read()
        content.strip()
        content=content.replace("本书由“ePUBw.COM”整理ePUBw.COM 提供最新最全的优质电子书下载\
","")
 
            
        clist=re.split("目录\n|译本序\n",content)

        
        #删除注释和xx章
        chapter="第.*章.*\n"
        annote="\[\d*\] .*\n"
        enter="(\n)+"
        repl=''
    
        for c in clist:
            
           
            c=re.sub(enter, "\n", c)
            c=re.sub(chapter, repl, c)
            c=re.sub(annote,repl,c)
            f2.write("\"{}\",".format(c))


    print("ok")
f2.write("\"\"]")

f2.close()

        


