rm -rf corpus
rm -rf models
rm -rf cleaned
python3 scraper.py
python3 parser.py
python3 build.py
