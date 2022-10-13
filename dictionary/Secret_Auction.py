from logo import logo
buyer_list = {}

# def Auction_list(buyer, cost):
#     buyer_list[buyer] = cost
#     print(buyer_list)

def whos_winner():
    max = 0

    for key in buyer_list:
        cost = buyer_list[key]
        if cost > max:
            max = buyer_list[key]
            main = key

    print(f"The winner is {main} with a bid of ${buyer_list[main]}.")

print(logo)
print("Welcome to the secret auction program")

on_off = True
while(on_off):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    # Auction_list(name, bid)
    buyer_list[name] = bid
    
    again = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if again == "no":
        on_off = False

whos_winner()

