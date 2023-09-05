#assignment 10, web scraping
"""
I called the function with this line:
print(print_links("https://en.wikipedia.org/wiki/Drake_Bulldogs"))

The output:
['https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en', 
'https://de.wikipedia.org/wiki/Drake_Bulldogs', 'https://es.wikipedia.org/wiki/Drake_Bulldogs', 'https://fr.wikipedia.org/wiki/Bulldogs_de_Drake', 
'https://www.wikidata.org/wiki/Special:EntityPage/Q2927982#sitelinks-wikipedia', 'https://www.wikidata.org/wiki/Special:EntityPage/Q2927982', 
'https://commons.wikimedia.org/wiki/Category:Drake_University_athletics', 'http://www.Godrakebulldogs.com', 
'http://news.drake.edu/2015/10/08/drake-welcomes-new-live-mascot-griff/', 
'https://s3.amazonaws.com/sidearm.sites/mvc.sidearmsports.com/documents/2022/8/29/Style_Guide_Full_Version.pdf', 
'https://web.archive.org/web/20150915170401/http://www.mvc-sports.com/valleyinfo/default/#.VgQh-ctVhBc', 'http://www.mvc-sports.com/valleyinfo/default/#.VgQh-ctVhBc', 
'https://www.ncaa.com/schools/bradley', 'http://cfbdatawarehouse.com/data/active/d/drake/yearly_results.php?year=1893', 
'http://www.lib.drake.edu/heritage/bright/story/', 'http://cdm15183.contentdm.oclc.org/cdm/compoundobject/collection/p15183coll1/id/14097/rec/137', 
'http://www.godrakebulldogs.com', 'https://www.wikidata.org/wiki/Q2927982#P856', 'https://en.wikipedia.org/w/index.php?title=Template:Drake_University&action=edit', 
'https://en.wikipedia.org/w/index.php?title=Template:Missouri_Valley_Conference_navbox&action=edit', 
'https://en.wikipedia.org/w/index.php?title=Template:Metro_Atlantic_Athletic_Conference_navbox&action=edit', 
'https://en.wikipedia.org/w/index.php?title=Template:Summit_League_navbox&action=edit', 'https://en.wikipedia.org/w/index.php?title=Template:Iowa_Sports&action=edit',
 'https://en.wikipedia.org/w/index.php?title=Drake_Bulldogs&oldid=1141841555', 'https://foundation.wikimedia.org/wiki/Privacy_policy', 'https://developer.wikimedia.org', 
 'https://stats.wikimedia.org/#/en.wikipedia.org', 'https://foundation.wikimedia.org/wiki/Cookie_statement', 'https://wikimediafoundation.org/', 
 'https://www.mediawiki.org/']
 
"""

import requests
from bs4 import BeautifulSoup

def print_links(link):

    url = str(link)
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    links = []
    for link in soup.find_all("a"):
        href= link.get("href")
        if href and href.startswith("http"):
            links.append(href)

    return links

print(print_links("https://en.wikipedia.org/wiki/Drake_Bulldogs"))

