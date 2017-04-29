h1. Nerd Stuff

The end goal is to index all of general conference talks in elasticsearch. This is a start.

Scrapy is used to crawl lds.org and grab data.

Here are my thoughts on how I would do this:

* Dynamically reate a list of all the urls of conference talks.
* Crawl each talk from the list, grabbing the data and exporting it in json to elasticsearch with proper tags etc. 
