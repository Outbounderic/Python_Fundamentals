from art import logo

print(logo)
print("Welcome to the secret auction program.")

bid_list = {}
bidders_remaining = True

def auction_entry():
    bid_name = input("What is your name?: ")
    bid_amount = input("What's your bid?: ")
    bid_list[bid_name] = int(bid_amount)

while bidders_remaining:
    auction_entry()
    another_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if another_bid == 'yes':
        i = 1
        while i < 24:
            print("\n")
            i += 1
    elif another_bid == 'no':
        bidders_remaining = False
        highest_bidder = ""
        highest_bid = 0
        for bidder in bid_list:
            if bid_list[bidder] > highest_bid:
                highest_bidder = bidder
                highest_bid = bid_list[bidder]
        print(f"The winnder is {highest_bidder} with a bid of ${str(highest_bid)}.")

print(bid_list)



#TODO-1 input on if there are more bidders
# if yes gather name, key, and their bid, value
# if no loop over bidders and find highest bid
# display the largest bid
