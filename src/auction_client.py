import json
import urllib2

# https://api.cryptokitties.co/auctions?
# offset=0
# &limit=12
# &type=sale
# &status=open
# &search=gen:1
# &sorting=cheap
# &orderBy=current_price
# &orderDirection=asc
# &parents=false


def getAuctions(
        offset=0,
        limit=12,
        theType='sale',
        status='open',
        search='gen:1',
        sorting='cheap',
        orderBy='currentPrice',
        orderDirection='asc',
        parents=False):
    url = 'https://api.cryptokitties.co/auctions?'
    url.join([
        'offset=' + str(offset),
        '&limit=' + str(limit),
        '&type=' + str(theType),
        '&status=' + str(status),
        '&search=' + str(search),
        '&sorting=' + str(sorting),
        '&orderBy=' + str(orderBy),
        '&orderDirection=' + str(orderDirection),
        '&parents=' + str(parents),
        ])
    auctionResponse = json.load(urllib2.urlopen(url))
    return auctionResponse['auctions']


def getCurrentAuctionPrice(auction):
    multiplier = 0.000000000000000001
    startPrice = int(auction['start_price']) * multiplier
    endPrice = int(auction['end_price']) * multiplier

    startTime = int(auction['start_time'])
    endTime = int(auction['end_time'])

    duration = auction['duration']

    rise = startPrice - endPrice
    run = endTime - startTime
    progress = float(duration) / run
    velocity = rise / run

    currentPrice = int(auction['current_price']) * multiplier

    endDiscount = endPrice - currentPrice

    return currentPrice

