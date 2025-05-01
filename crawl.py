import requests
from bs4 import BeautifulSoup
import json
filename = "data.json"
all_data = []
filename = "input_words.txt"
export = "exmp_results.txt"
# print("want to made file for flashcards?(y/n)")
# makefile = input()
# if(makefile == 'y'):
#     print()
file = open(filename)
r = file.read()
r = r.split("\n") #以換行分隔
f2 = open(export, "w", encoding = 'utf8')#開啟要存入的文件
f2.write('\ufeff')
for word in r:

    print('<' + str.upper(word) + '>')
    
    f2.write(str.upper(word) + '\n\n')
    url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/'
    full_url = url + word
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    headers = {'User-Agent': user_agent}
    web_request = requests.get(full_url, headers = headers)
    soup = BeautifulSoup(web_request.text, "html.parser")
    blocks = soup.find_all(class_ = "def-block ddef_block")
    j = 0

    for block in blocks:
        
        # print("詞性 : ")
        # print(block.find_parent(class_ = "pos-body").find_previous_sibling(class_ = "pos-header dpos-h").find(class_ = "pos dpos").text)
        pos = block.find_parent(class_ = "pos-body").find_previous_sibling(class_ = "pos-header dpos-h").find(class_ = "pos dpos").text
        f2.write("詞性 : " + pos + '\n')
        print("詞性:" + pos + '\n')
        if block.find_parent(class_ = "phrase-body dphrase_b"):
            continue
        j += 1
        word2 = str.upper(word) + "(" + str(j) + ")" 
        print("\n英文解釋 : " + block.find(class_= "ddef_h").find(class_= "def ddef_d db").text)#英文解釋
        eng_def = block.find(class_= "ddef_h").find(class_= "def ddef_d db").text
        eng_def2 = block.find(class_= "def-body ddef_b")
        f2.write("英文解釋 : " + block.find(class_= "ddef_h").find(class_= "def ddef_d db").text + '\n')
        # if(len(eng_def2.find(class_= "trans dtrans dtrans-se hdb break-cj")) == "None"):
        #         print("2222222222222222222222222222222222222222222222")
        #         break
        try:
            print("中文意思 : " + block.find(class_= "def-body ddef_b").find(class_= "dtrans").text)#中文意思
            chi_def = block.find(class_= "def-body ddef_b").find(class_= "dtrans").text
            f2.write("中文意思 : " + block.find(class_= "def-body ddef_b").find(class_= "dtrans").text + '\n\n')
        except:
            j -= 1
            continue
        exmps = block.find(class_= "def-body ddef_b").find_all(class_= "examp dexamp")#回傳list
        # chiexmps = block.find(class_= "def-body ddef_b").find_all(class_= "examp dexamp").find(class_= "trans dtrans dtrans-se hdb break-cj")
        print("\n例句 : ")
        # f2.write("\n例句 : \n")
        if(len(exmps) == 0):
            j -= 1
            print("none")
            f2.write("NONE\n")
            continue
        # if(len(exmps.find(class_ = "trans dtrans dtrans-se hdb break-cj")) == 0):
        #     print("has no chinese sentence")
        i = 0
        eng_sen = []
        chi_sen = []
        for exmp in exmps: #輸出例句
            # print(exmp.find(class_ = "eg deg").text)
            # print(i)
            i += 1
            if(str(exmp.find(class_= "trans dtrans dtrans-se hdb break-cj")) == "None"):
                continue
            print(exmp.text)
            f2.write("例句:" + exmp.find(class_ = "eg deg").text + '\n')
            eng_sen.append(exmp.find(class_ = "eg deg").text)
            f2.write("翻譯: " + exmp.find(class_ = "trans dtrans dtrans-se hdb break-cj").text + '\n\n')
            chi_sen.append(exmp.find(class_ = "trans dtrans dtrans-se hdb break-cj").text)
        data = {
        "word" : word2, #單字
        "POS" : pos, #詞性
        "eng_def" : eng_def, #英文釋義
        "chi_def" : chi_def, #中文釋義
        "eng_sen" : eng_sen, #英文例句的list
        "chi_sen" : chi_sen #中文例句 的list
        }
        all_data.append(data)
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)
