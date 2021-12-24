from art import logo

print(logo)
print("Welcome to the secret auction program.")

bid_list = {}

def auction_entry():
    bid_name = input("What is your name?: ")
    bid_amount = input("What's your bid?: ")
    bid_list[bid_name] = int(bid_amount)

#TODO-1 input on if there are more bidders
# if yes gather name, key, and their bid, value
# if no loop over bidders and find highest bid
# display the largest bid

auction_entry()
print(bid_list)