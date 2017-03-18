# Web-Crawler

Web Crawler for my android application, this scripts fetches movie details from internet and puts in the sql database.

## Installation

### Install the following dependencies

1. Beautiful Soup 
```shell
$ apt-get install python-bs4
```

2. Wikipedia
```shell
$ pip install wikipedia
```

## Usage

```shell
$ python nammaMysuru.py
```

## History

My Android application [Namma Mysuru](https://play.google.com/store/apps/details?id=com.project.raghavendra.nammamysore) gives information about the Movies being showed in Theaters (along with other details about [Mysore](https://en.wikipedia.org/wiki/Mysore). For this I wanted a crawler that can fetch that data from internet all by itself instead of me updating it every week. So went ahead and wrote a web crawler in python which collects data and puts it in SQL database after formatting it.
