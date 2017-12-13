from bs4 import BeautifulSoup
import urllib2
import re


def getCattributePriceAverages(verbose=False):
    site = "http://cryptokittydex.com/cattributes"
    hdr = {
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'
    }

    req = urllib2.Request(site, headers=hdr)

    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
        exit(-1)

    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    avgPriceDict = dict()

    for li in soup.find("ul", { "class": "list-cattributes list-unstyled"}).findAll('li'):
        cattribute = li.find('strong')
        if cattribute is not None:
            cattributeString = cattribute.string
            avgPrice = li.find('span', { 'data-title': 'Average price paid for a kitty possessing this cattribute'})
            if avgPrice is not None:
                avgPriceString = avgPrice.string
                avgPriceNum = float(re.findall(r"[-+]?\d*\.\d+|\d+", avgPriceString)[0])
                avgPriceDict[cattributeString] = avgPriceNum
                if verbose:
                    print str(cattributeString) + ': ' + str(avgPriceNum)
    return avgPriceDict
