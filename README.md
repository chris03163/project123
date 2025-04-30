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
   
## How to Use
1. Web Crawler (visit3.py)
   
   1. Prepare your vocabulary list in input_words.txt (one word per line)
   
   2. Run the crawler:
      ```
      python visit3.py
      ```
   3. The crawler will generate:
      * result.json (structured data for the flashcard app)
      * exmp_results.txt (human-readable output)
2. Using the Flashcard App
   1.Run the application:
   ```
   python AR_helper.py
   ```
   2. Interface controls:
      * Previous/Next: Navigate through vocabulary
      * Show/Hide: Toggle definitions and translations
      * Got it: Remove mastered words from practice set
      * Save and Leave: Save progress and exit
## Features

1. Active Recall Practice: Hide/show translations to test your memory
   
2. Contextual Learning: Example sentences provide word usage in context
   
3. Progress Tracking: Remove mastered words from your practice set
   
4. Data Persistence: Save your progress between sessions

## Requirements

1. Python 3.x

2. Required packages:
   ```
   pip install requests beautifulsoup4 tkinter
   ```

## License

This project is for educational purposes only. Data is sourced from:

   * Cambridge Dictionary (https://dictionary.cambridge.org)
   * CEEC English Vocabulary List (https://www.ceec.edu.tw/)

Note: This program is for personal learning and research use only, with no commercial purpose.
