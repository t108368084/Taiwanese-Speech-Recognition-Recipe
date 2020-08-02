import json
import os

name='condenser/json'
text=open('text','w')
for dir in os.listdir(name):
  for file in os.listdir(name+'/'+dir):
    jsons=name+'/'+dir+'/'+file
    file1=file.replace('.json','-03')
    id=dir+'_'+file1
    if jsons.endswith(".json"):
       with open(jsons, 'r', encoding='utf-8') as f:

         output = json.load(f)
         a=output['台羅數字調']
         a=a.replace('0','')
         a=a.replace('1','')
         a=a.replace('2','')
         a=a.replace('3','')
         a=a.replace('4','')
         a=a.replace('5','')
         a=a.replace('6','')
         a=a.replace('7','')
         a=a.replace('8','')
         a=a.replace('9','')
         a=a.replace('-',' ')
         a=a.replace("，"," ")
         a=a.replace(","," ")
         a=a.replace(".", " ")
         a=a.replace("?", " ")
         a=a.replace("﹖", " ")
         a=a.replace("!", " ")
         a=a.replace(":", " ")
         a=a.replace("”", " ")
         a=a.replace('“', ' ')
         a=a.replace(";", " ")
         a=a.replace("/", " ")
         a=a.replace("…", " ")
         a=a.replace("(", " ")
         a=a.replace(")", " ")
         a=a.replace("‘", " ")
         a=a.replace("’", " ")
         a=a.replace("／", " ")
         a=a.replace("⋯", " ")
         a=a.replace("~", " ")
         a=a.replace("（", " ")
         a=a.replace("）", " ")
         a=a.replace("「", " ")
         a=a.replace("」", " ")
         a=a.replace("％", " ")
         a=a.replace("｣", " ")
         a=a.replace("%", " ")
         a=a.replace("、", " ")
         a=a.replace("｢", " ")
         a=a.replace("--", " ")
         a=a.replace("！", " ")
         a=a.replace("：", " ")
         a=a.replace("。", " ")
         a=a.replace("—", " ")
         a=a.replace("？", " ")
         a=a.replace("──", " ")
         a=a.replace("  ", " ")
         a=a.strip()
         a=a.lower()
         b=a.split(' ')
         flag=True
         for _char in b:
            if '\u4e00' <= _char <= '\u9fa5':
              flag=False
              break
            e=_char.encode('utf-8').isalpha()
            if e==False:
              flag=False
              break
         if flag==True:
            text.write(id)
            text.write(' ')
            text.write(a)
            text.write('\n')

text.close()


