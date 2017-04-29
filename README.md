# Nerd Stuff

The end goal is to index all of general conference talks in elasticsearch. This is a start.

Scrapy is used to crawl lds.org and grab data.

Here are my thoughts on how I would do this:

* Dynamically create a list of all the urls of conference talks.
* Crawl each talk from the list, grabbing the data and exporting it in json to elasticsearch with proper tags etc. 

The scrapy python file is in /conferencedata/conferencedata/scripts.

To run it from scrapy (from /conferencedata/conferencedata)

`scrapy crawl conference -o conf.json`

That will output a list of all the conference talks on lds.org and their href. Thats as far as I have gotten at this point.


Run in Docker:

If you want to get a quick scrapy install up and running in docker there is an included Dockerfile you can build an image from. You can also do the following to run a prebuild image:

`docker run -it llamashoes/scrapy`

From there you can clone this repo somewhere are run scrapy like a boss. 

TODO:

* Scrape the urls to grab the data from each talk
 * Author - DONE
 * Title - DONE
 * URL - DONE
 * Date - TODO - put in a date format for indexing
 * Content - DONE
* Output in json to an elk stack somewhere 

