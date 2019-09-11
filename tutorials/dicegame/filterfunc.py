
score_bucket = []
qualify_bucket = []
active_roll = [1,2,6,6,6,6,6]
is_score_full = False
counter = 0

def count_sixes(listofdice):
    while counter <= 2:
        if listofdice == 6:
            counter += 1
            print(counter)
            return True
        return False
     
qty_sixes = filter(count_sixes, active_roll)

for item in qty_sixes:
    score_bucket.append(item)
print(score_bucket)

