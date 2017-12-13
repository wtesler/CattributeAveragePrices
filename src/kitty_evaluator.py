import json
import urllib2
import cattribute_scraper


class KittyEvaluator:

    def __init__(self):
        self.cattributePriceAverageDict = cattribute_scraper.getCattributePriceAverages()

    def evaluateKittyInAuction(self, auction):
        url = 'https://api.cryptokitties.co/kitties/'
        ID = auction['kitty']['id']
        kitty = json.load(urllib2.urlopen(url + str(ID)))

        count = 0
        accumulatedWorth = 0
        cattributes = kitty['cattributes']
        for cattribute in cattributes:
            priceAverage = self.cattributePriceAverageDict[cattribute['description']]
            accumulatedWorth += priceAverage
            count += 1
        try:
            worth = accumulatedWorth / count
            kitty['worth'] = worth
        except ZeroDivisionError as e:
            print(str(e))
        return kitty
