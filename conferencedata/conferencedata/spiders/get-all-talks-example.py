import scrapy


class ConferenceSpider(scrapy.Spider):
    name = "conference"
    start_urls = [
        'https://www.lds.org/general-conference/2011/04?lang=eng',
    "https://www.lds.org/general-conference/2017/04?lang=eng",
    "https://www.lds.org/general-conference/2016/04?lang=eng",
    "https://www.lds.org/general-conference/2016/10?lang=eng",
    "https://www.lds.org/general-conference/2015/04?lang=eng",
    "https://www.lds.org/general-conference/2015/10?lang=eng",
    "https://www.lds.org/general-conference/2014/04?lang=eng",
    "https://www.lds.org/general-conference/2014/10?lang=eng",
    "https://www.lds.org/general-conference/2013/04?lang=eng",
    "https://www.lds.org/general-conference/2013/10?lang=eng",
    "https://www.lds.org/general-conference/2012/04?lang=eng",
    "https://www.lds.org/general-conference/2012/10?lang=eng",
    "https://www.lds.org/general-conference/2011/04?lang=eng",
    "https://www.lds.org/general-conference/2011/10?lang=eng",
    "https://www.lds.org/general-conference/2010/04?lang=eng",
    "https://www.lds.org/general-conference/2010/10?lang=eng",
    "https://www.lds.org/general-conference/2009/04?lang=eng",
    "https://www.lds.org/general-conference/2009/10?lang=eng",
    "https://www.lds.org/general-conference/2008/04?lang=eng",
    "https://www.lds.org/general-conference/2008/10?lang=eng",
    "https://www.lds.org/general-conference/2007/04?lang=eng",
    "https://www.lds.org/general-conference/2007/10?lang=eng",
    "https://www.lds.org/general-conference/2006/04?lang=eng",
    "https://www.lds.org/general-conference/2006/10?lang=eng",
    "https://www.lds.org/general-conference/2005/04?lang=eng",
    "https://www.lds.org/general-conference/2005/10?lang=eng",
    "https://www.lds.org/general-conference/2004/04?lang=eng",
    "https://www.lds.org/general-conference/2004/10?lang=eng",
    "https://www.lds.org/general-conference/2003/04?lang=eng",
    "https://www.lds.org/general-conference/2003/10?lang=eng",
    "https://www.lds.org/general-conference/2002/04?lang=eng",
    "https://www.lds.org/general-conference/2002/10?lang=eng",
    "https://www.lds.org/general-conference/2001/04?lang=eng",
    "https://www.lds.org/general-conference/2001/10?lang=eng",
    "https://www.lds.org/general-conference/2000/04?lang=eng",
    "https://www.lds.org/general-conference/2000/10?lang=eng",
    "https://www.lds.org/general-conference/1999/04?lang=eng",
    "https://www.lds.org/general-conference/1999/10?lang=eng",
    "https://www.lds.org/general-conference/1998/04?lang=eng",
    "https://www.lds.org/general-conference/1998/10?lang=eng",
    "https://www.lds.org/general-conference/1997/04?lang=eng",
    "https://www.lds.org/general-conference/1997/10?lang=eng",
    "https://www.lds.org/general-conference/1996/04?lang=eng",
    "https://www.lds.org/general-conference/1996/10?lang=eng",
    "https://www.lds.org/general-conference/1995/04?lang=eng",
    "https://www.lds.org/general-conference/1995/10?lang=eng",
    "https://www.lds.org/general-conference/1994/04?lang=eng",
    "https://www.lds.org/general-conference/1994/10?lang=eng",
    "https://www.lds.org/general-conference/1993/04?lang=eng",
    "https://www.lds.org/general-conference/1993/10?lang=eng",
    "https://www.lds.org/general-conference/1992/04?lang=eng",
    "https://www.lds.org/general-conference/1992/10?lang=eng",
    "https://www.lds.org/general-conference/1991/04?lang=eng",
    "https://www.lds.org/general-conference/1991/10?lang=eng",
    "https://www.lds.org/general-conference/1990/04?lang=eng",
    "https://www.lds.org/general-conference/1990/10?lang=eng",
    "https://www.lds.org/general-conference/1989/04?lang=eng",
    "https://www.lds.org/general-conference/1989/10?lang=eng",
    "https://www.lds.org/general-conference/1988/04?lang=eng",
    "https://www.lds.org/general-conference/1988/10?lang=eng",
    "https://www.lds.org/general-conference/1987/04?lang=eng",
    "https://www.lds.org/general-conference/1987/10?lang=eng",
    "https://www.lds.org/general-conference/1986/04?lang=eng",
    "https://www.lds.org/general-conference/1986/10?lang=eng",
    "https://www.lds.org/general-conference/1985/04?lang=eng",
    "https://www.lds.org/general-conference/1985/10?lang=eng",
    "https://www.lds.org/general-conference/1984/04?lang=eng",
    "https://www.lds.org/general-conference/1984/10?lang=eng",
    "https://www.lds.org/general-conference/1983/04?lang=eng",
    "https://www.lds.org/general-conference/1983/10?lang=eng",
    "https://www.lds.org/general-conference/1982/04?lang=eng",
    "https://www.lds.org/general-conference/1982/10?lang=eng",
    "https://www.lds.org/general-conference/1981/04?lang=eng",
    "https://www.lds.org/general-conference/1981/10?lang=eng",
    "https://www.lds.org/general-conference/1980/04?lang=eng",
    "https://www.lds.org/general-conference/1980/10?lang=eng",
    "https://www.lds.org/general-conference/1979/04?lang=eng",
    "https://www.lds.org/general-conference/1979/10?lang=eng",
    "https://www.lds.org/general-conference/1978/04?lang=eng",
    "https://www.lds.org/general-conference/1978/10?lang=eng",
    "https://www.lds.org/general-conference/1977/04?lang=eng",
    "https://www.lds.org/general-conference/1977/10?lang=eng",
    "https://www.lds.org/general-conference/1976/04?lang=eng",
    "https://www.lds.org/general-conference/1976/10?lang=eng",
    "https://www.lds.org/general-conference/1975/04?lang=eng",
    "https://www.lds.org/general-conference/1975/10?lang=eng",
    "https://www.lds.org/general-conference/1974/04?lang=eng",
    "https://www.lds.org/general-conference/1974/10?lang=eng",
    "https://www.lds.org/general-conference/1973/04?lang=eng",
    "https://www.lds.org/general-conference/1973/10?lang=eng",
    "https://www.lds.org/general-conference/1972/04?lang=eng",
    "https://www.lds.org/general-conference/1972/10?lang=eng",
    "https://www.lds.org/general-conference/1971/04?lang=eng",
    "https://www.lds.org/general-conference/1971/10?lang=eng"
    ]

    def parse(self, response):
        for talk in response.css('div.lumen-tile'):
            yield {
                'link': talk.css('a::attr(href)').extract(),
            }