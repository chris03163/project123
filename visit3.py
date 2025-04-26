import requests
from bs4 import BeautifulSoup
import json
filename = "data.json"
all_data = []
print("enter filename of word file:")
filename = "input_words.txt"
print("enter filename of destination:")
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
    
    # f2.write(str.upper(word) + '\n')
    url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/'
    full_url = url + word
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    headers = {'User-Agent': user_agent}
    web_request = requests.get(full_url, headers = headers)
    soup = BeautifulSoup(web_request.text, "html.parser")
    blocks = soup.find_all(class_ = "def-block ddef_block")
    j = 0

    for block in blocks:
        if block.find_parent(class_ = "phrase-body dphrase_b"):
            continue
        j += 1
        wword = str.upper(word) + "(" + str(j) + ")"
        print("\n英文解釋 : " + block.find(class_= "ddef_h").find(class_= "def ddef_d db").text)#英文解釋
        eng_def = block.find(class_= "ddef_h").find(class_= "def ddef_d db").text
        eng_def2 = block.find(class_= "def-body ddef_b")
        # f2.write(block.find(class_= "ddef_h").find(class_= "def ddef_d db").text)
        # if(len(eng_def2.find(class_= "trans dtrans dtrans-se hdb break-cj")) == "None"):
        #         print("2222222222222222222222222222222222222222222222")
        #         break
        try:
            print("\n中文意思 : " + block.find(class_= "def-body ddef_b").find(class_= "dtrans").text)#中文意思
            chi_def = block.find(class_= "def-body ddef_b").find(class_= "dtrans").text
            # f2.write(block.find(class_= "def-body ddef_b").find(class_= "dtrans").text)
        except:
            j -= 1
            continue
        exmps = block.find(class_= "def-body ddef_b").find_all(class_= "examp dexamp")#回傳list
        # chiexmps = block.find(class_= "def-body ddef_b").find_all(class_= "examp dexamp").find(class_= "trans dtrans dtrans-se hdb break-cj")
        print("\n例句 : \n")
        # f2.write("\n例句 : \n")
        if(len(exmps) == 0):
            j -= 1
            print("hello")
            # f2.write("NONE\n")
            continue
        # if(len(exmps.find(class_ = "trans dtrans dtrans-se hdb break-cj")) == 0):
        #     print("has no chinese sentence")
        i = 0
        eng_sen = []
        chi_sen = []
        for exmp in exmps: #輸出例句
            # print(exmp.find(class_ = "eg deg").text)
            print(i)
            i += 1
            if(str(exmp.find(class_= "trans dtrans dtrans-se hdb break-cj")) == "None"):
                continue
            print(exmp.text)
            f2.write("eng sentence: " + exmp.find(class_ = "eg deg").text + '\n')
            eng_sen.append(exmp.find(class_ = "eg deg").text)
            f2.write("ch sentence: " + exmp.find(class_ = "trans dtrans dtrans-se hdb break-cj").text + '\n')
            chi_sen.append(exmp.find(class_ = "trans dtrans dtrans-se hdb break-cj").text)
        datum = {
        "word" : wword, 
        "eng_def" : eng_def, 
        "chi_def" : chi_def, 
        "eng_sen" : eng_sen, 
        "chi_sen" : chi_sen
        }
        all_data.append(datum)
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)