def something(cheese_count,boxes_of_crackers):
    print "You have %d cheesess!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
something(20,30)

print "OR, we can used variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

something(amount_of_cheese,amount_of_crackers)

print "We can even use variables from our script:"
something(10+20,5+6)

print "And we can combine the two, variables and math:"
something(amount_of_cheese + 100, amount_of_crackers + 1000)
