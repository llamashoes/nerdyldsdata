FROM ubuntu:16.04
RUN apt-get update;apt-get install -y python-scrapy less vim git jq
CMD /bin/bash
