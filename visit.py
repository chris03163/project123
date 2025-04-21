import requests
from bs4 import BeautifulSoup
print("enter filename of word file:")
filename = input()
print("enter filename of destination:")
export = input()
file = open(filename)#"words_exmp.txt"
r = file.read()
r = r.split("\n") #以換行分隔
f2 = open(export, "w", encoding = 'utf8')#開啟要存入的文件 "results_exmp.txt"
f2.write('\ufeff')
# f2.write("welcome\n")
for word in r:
    print('<' + str.upper(word) + '>')
    f2.write('\n<' + str.upper(word) + '>\n')
    url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/'
    full_url = url + word
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    headers = {'User-Agent': user_agent}
    web_request = requests.get(full_url, headers = headers)
    soup = BeautifulSoup(web_request.text, "html.parser")
    blocks = soup.find_all(class_ = "def-block ddef_block")
    i = 0
    for block in blocks:
        i += 1
        print("\n英文解釋 : " + block.find(class_= "ddef_h").find(class_= "def ddef_d db").text)#英文解釋
        f2.write("\n英文解釋" + str(i) + " : " + block.find(class_= "ddef_h").find(class_= "def ddef_d db").text)
        try:
            print("\n中文意思 : " + block.find(class_= "def-body ddef_b").find(class_= "dtrans").text)#中文意思
            f2.write("\n中文意思 : " + block.find(class_= "def-body ddef_b").find(class_= "dtrans").text)
        except:
            continue
        exmps = block.find(class_= "def-body ddef_b").find_all(class_= "examp dexamp")#回傳list
        print("\n例句 : \n")
        f2.write("\n例句 : \n")
        if(len(exmps) == 0):
            print("hello")
            f2.write("NONE\n")
            continue
        for exmp in exmps: #輸出例句
            print(exmp.text)
            f2.write(exmp.text)
        