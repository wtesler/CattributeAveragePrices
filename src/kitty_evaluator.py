import json
import urllib2
import cattribute_scraper


class KittyEvaluator:

    def __init__(self):
        self.cattributePriceAverageDict = cattribute_scraper.getCattributePriceAverages()

    def evaluateKitty(self, kittyId):
        """
            Returns a kitty with it's worth determined.
        """
        url = 'https://api.cryptokitties.co/kitties/'
        kitty = json.load(urllib2.urlopen(url + str(kittyId)))

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
            print(str(e) + " due to " + kitty)
            kitty['worth'] = 0
        return kitty

    def evaluateKittyWorth(self, kittyId):
        """
            Convenience method for when you just want the worth.
        """
        return self.evaluateKitty(kittyId)['worth']
