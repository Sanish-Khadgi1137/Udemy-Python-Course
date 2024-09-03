#alternative of thonny to check the flow of the code https://pythontutor.com/render.html#mode=display

#from replit import clear   #replet module was not availabe
#HINT: You can call clear() to clear the output in the console

from art import gavel
print(gavel)




def find_hightest_bidder(bidding_record):
#bidding_record = {"Angela": 123, "James": 321}
    
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] #here "bidder" is key to get "value i.e. bid_amount"
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")


#a empty dictionary
bids = {}
bidding_finished = False


#this while loop runs only if "bidding is not finish or bidding_finished = False"
while not bidding_finished:
    name  = input("What is your name? ")
    price = int(input("Wht is your bid? $"))

    #addint to "bids= {}" dictionary
    bids[name] = price

    should_continue = input("Are there any other bidders? Type yes or no.")
    if should_continue == "no":
        bidding_finished = True

        #above function called 
        find_hightest_bidder(bids)
    #elif should_continue == "yes":
     #   clear()