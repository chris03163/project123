# English Vocabulary Flashcard System

## Overview
This project is a comprehensive English vocabulary learning system that combines web scraping functionality with an interactive flashcard application for active recall practice. The system allows users to:

1. Crawl vocabulary data from Cambridge Dictionary

2. Store the data in a structured JSON format

3. Practice vocabulary through an interactive GUI with active recall features
## Components
1. Web Crawler (visit3.py)
   
   * Scrapes vocabulary data from Cambridge English-Chinese Dictionary
   
   * Extracts:
      * Word definitions (English and Chinese)
     
      * Part of speech (POS)
     
      * Example sentences (with translations)

   * Outputs results to both human-readable text file and structured JSON

3. Flashcard Application (AR_helper.py)
   
   * Tkinter-based GUI for vocabulary practice

   * Features:
      * Word display with part of speech
      
      * Toggleable English/Chinese definitions
      
      * Example sentences with hide/show translation functionality
      
      * Navigation through vocabulary list
      
      * "Got it" button to remove mastered words

   * Save progress functionality
3. Data Files
   
   * input_words.txt: Input vocabulary list
   
   * result.json: Structured vocabulary data (used by flashcard app)
   
   * exmp_results.txt: Human-readable output from crawler
   



再把此專案下載下來，點擊執行名為visit2.py的檔案，將會出現
```
enter filepath of word file:
```
的字樣，請輸入要爬取的單字文字檔的名稱，範例檔名是exmp_words.txt

註:單字文字檔的格式是以換行分隔的txt檔使用者可自行刪除或新增內容，範例如下
```
apple
banana
watermelon
...
```

接著會出現
```
enter filepath of destination:
```
這裡輸入要存取爬蟲結果的文字名稱，範例檔名是result_exmp.txt(若輸入不在資料夾內的檔名會自動創一個)



## 副功能

# 附錄

[大考中心英文單字表][1]

  [1]: https://www.ceec.edu.tw/xmdoc?xsmsid=0K213553204833715309        "游標顯示"
## 著作權聲明

單字表資料來源:大考中心 (https://www.ceec.edu.tw/)

爬蟲資料來源：劍橋英漢字典（https://dictionary.cambridge.org）

本程式僅供學習與研究使用，無任何商業用途。

###### This is a Heading h6

## Emphasis
