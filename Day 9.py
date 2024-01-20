# student_scores = {
#     "Ashish": 93,
#     "Hariom": 81,
#     "Mohit": 73,
#     "Abhishek": 68
# }
# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Excellent"
#     elif score > 70:
#         student_grades[student] = "Good"
#     elif score > 60:
#         student_grades[student] = "Average"
# print(student_grades)
#
# bids = {}
# bidding_finished = False
#
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
# while not bidding_finished:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: "))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)
#     #elif should_continue == "yes":
#         #clear()