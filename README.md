# Light-Novel-JLPT
Read Japanese light novels and have Japanese Language Proficiency Test (JLPT).



- To scrape corpus from [](https://yomou.syosetu.com):

  `$ python3 scraper.py`


- To clean and parse corpus:

  `$ python3 parser.py`


- To build and save N-gram language model:

  `$ python3 build.py `

- To do things above:

  `$ ./build_all.sh `

  ​


- If you don't want to do things above by yourself,

  you can download the N-gram language model and unzip it:

  **Warning: The language model is large. (About 254MB)**

  `$ wget https://gitlab.com/Kikokushijo/Light-Novel-JLPT_models/raw/master/models.zip `

  `$ unzip models.zip `



- To test questions by user's input:

  **Warning: The language model is large and you will need about 6GB RAM to load it.**

  `$ python3 test.py online`

- To test questions from data:

  `$ python3 test.py txt`
  
  The data should be saved in `problems/q.txt`,
  and be saved with the format `problem, option1, option2, option3, option4, ans`.
  
  There is an example below:
  `台風が来るから、%sほうがいい。, 帰った, 帰る, 帰って, 帰り, 1`
  
  The blank should be represented by `%s`, and the answer is 1-based (the answer of the problem above is `帰った`)
