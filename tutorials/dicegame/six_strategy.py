import itertools

def six_strategy(active_roll):

    score_bucket = []
    qualify_bucket = []
    active_bucket = active_roll
    is_score_full = False

    total_fives = active_roll.count(5)
    total_sixes = active_roll.count(6)
    spots_remain = 4 - total_sixes - total_fives
    sixes_index = [] 

    for die in active_bucket:
        if die == 6:
            index_pos = active_bucket.index(6)
            sixes_index.append(index_pos)
            active_bucket.remove(n)
            print(sixes_index)

    if spots_remain == 0:
        is_score_full = True

    # if active_dice contains a 6, then add it to the score_bucket, otherwise choose highest value
    if total_sixes > 0:
        for n in active_bucket[:len(active_bucket)]:
            if (n == 6) and (active_roll.count(6) >= 1):
                counter = 0
                while n == 6:
                    print(active_roll.count(6))
                    print("The Active roll is: %s" % active_bucket,"The Qualifiers are: %s" % qualify_bucket, "The Score is: %s" % score_bucket, "The counter is: %s" % counter)
                    score_bucket.append(n)
                    active_bucket.remove(n)
                    total_sixes -= 1
                    counter += 1
    # print("The Active roll is: %s" % active_bucket,"The Qualifiers are: %s" % qualify_bucket, "The Score is: %s" % score_bucket, "The counter is: %s" % counter)           

active_dice_list = [1,5,5,3,6,6]
six_strategy(active_dice_list)