
mydice = [1,2,3,4,5,6]
myit = iter(mydice)
score_bucket = []

def six_strategy(active_bucket):

    qualify_bucket = []
    active_bucket = []

    if myit == 6:
        score_bucket.append(myit)

    print("The Active roll is: %s" % active_bucket,"The Qualifiers are: %s" % qualify_bucket, "The Score is: %s" % score_bucket)
    # print("The Active roll is: %s" % active_bucket,"The Qualifiers are: %s" % qualify_bucket, "The Score is: %s" % score_bucket, "The counter is: %s" % counter)           


one = next(six_strategy(myit))
print(one)
two = six_strategy(next(myit))
print(two)




