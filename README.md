# Nerd Stuff

The end goal is to index all of general conference talks in elasticsearch. This is a start.

Scrapy is used to crawl lds.org and grab data.

Here are my thoughts on how I would do this:

* Dynamically reate a list of all the urls of conference talks.
* Crawl each talk from the list, grabbing the data and exporting it in json to elasticsearch with proper tags etc. 

The scrapy python file is in /conferencedata/conferencedata/scripts.

To run it (from /conferencedata/conferencedata)

`scrapy crawl conference -o conf.json`

That will output a list of all the conference talks on lds.org and their href. Thats as far as I have gotten at this point.

TODO:

* Scrape the urls to grab the data from each talk
* Output in json to an elk stack somewhere 
