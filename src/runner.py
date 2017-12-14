import auction_client
from kitty_evaluator import KittyEvaluator
import book_keeper

VERBOSE = True

kittyEvaluator = KittyEvaluator()

auctions = auction_client.getAuctions(limit=2)

for auction in auctions:
    kitty = kittyEvaluator.evaluateKitty(auction['kitty']['id'])
    worth = kitty['worth']
    auctionPrice = auction_client.getCurrentAuctionPrice(auction)
    currentBalance = book_keeper.getCurrentBalance()

    if VERBOSE:
        print("Evaluating kitty " + str(kitty['id']))
        print("Worth: " + str(worth))
        print("Selling At: " + str(auctionPrice))
        print('Considered' if worth > auctionPrice else 'Ignored')
        print(('Sufficient' if currentBalance > auctionPrice else 'Insufficient') + ' funds')
        print('')


