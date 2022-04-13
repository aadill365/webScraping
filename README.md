## Web scraper to read articles

`python` `sqlite3`

- Make sure you install following packages and have a internet connection while running the script.

```python
pip install requests
pip install BeautifulSoup4
pip install html5lib
```
After installing the above mentioned packages, run main.py script which will scrape the data and save it to both csv file and sqlite3 database.   

```python
python main.py or python3 main.py
```

Database connection logic is implemented in config.py file and scraping logic is implemented in scrape.py file.
