# Web-Crawler

Web Crawler for my android application, this scripts fetches movie details from internet and puts in the sql database.

## History

My Android application [Namma Mysuru](https://play.google.com/store/apps/details?id=com.project.raghavendra.nammamysore) gives information about the Movies being showed in Theaters (along with other details about [Mysore](https://en.wikipedia.org/wiki/Mysore). 

For this I wanted a crawler that can fetch that data from internet all by itself instead of me updating it every week. So went ahead and wrote a web crawler in python which collects data and puts it in SQL database after formatting it.

This Crawler uses [Beautiful Soup](https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)) HTML parser to parse the web pages. After formatting the data, I have used [Wikipedia](https://pypi.python.org/pypi/wikipedia/) Python package to get movie information from Wikipedia.

Then I use [SQLITE3](https://docs.python.org/3/library/sqlite3.html) python package to store the data into database. Since the theater details (address, gps co-ordinates etc..,) doesn't change, I have a table in my database named theater_detail that has all the information about theaters. When I run this python, I also have a sqlite database file called 'nammaMysuru.sqlite' which has this table.

## Installation

### Install the following dependencies

1. Beautiful Soup 
```shell
$ sudo apt-get install python-bs4
```

2. Wikipedia

```shell
## Install Python pip 
$ wget https://bootstrap.pypa.io/get-pip.py
$ chmod +x get-pip.py
$ python3 get-pip.py --user

## Install wikipedia using pip
$ pip install wikipedia --user
```

3. SQLITE 3
```shell
$ sudo apt-get install sqlite3
```

## Usage

```shell
$ python nammaMysuru.py
```
