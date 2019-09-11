def five_strategy(active_roll):

    score_bucket = []
    qualify_bucket = []
    active_bucket = active_roll
    is_score_full = False

    fives = active_roll.count(5)
    sixes = active_roll.count(6)
    spots_remain = 4 - sixes - fives

    if spots_remain == 0:
        is_score_full = True

    # if active_dice contains a 6, then add it to the score_bucket, otherwise choose highest value
    if sixes >= 1:
        for n in active_bucket[:len(active_bucket)]:
            if (n == 6 and n== 5) and (active_roll.count(6) >= 2):
                counter = 0
                while counter <= 3:
                    score_bucket.append(n)
                    print(active_roll.count(6))
                    sixes -= 1
                    active_bucket.sort()
                    active_bucket.pop()
                    counter += 1    
                    print("The Active roll is: %s" % active_bucket,"The Qualifiers are: %s" % qualify_bucket, "The Score is: %s" % score_bucket, "The counter is: %s" % counter)           
                else:
                    print("While loop ended")
                    
            else:
                print("Inside If ended")
    else:
        print("Outside if ended")
        
    # print("The Active roll is: %s" % active_bucket,"The Qualifiers are: %s" % qualify_bucket, "The Score is: %s" % score_bucket, "The counter is: %s" % counter)           

active_dice_list = [1,6,6,6,6,6]
six_strategy(active_dice_list)