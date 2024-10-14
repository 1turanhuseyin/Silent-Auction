import art
print(art.logo)

bidders = {}
is_there_other_bidder = True

while is_there_other_bidder:
    name = input("What is your name? : ")
    price = float(input("What is your bid? $"))
    bidders[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "no":
        is_there_other_bidder = False
    print("\n" * 100)


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner_name = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner_name = bidder

    print(f"The winner is {winner_name} with a bid of {highest_bid}")


find_highest_bidder(bidders)


