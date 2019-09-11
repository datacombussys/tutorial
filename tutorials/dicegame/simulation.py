import random

class PlayGame():

    def __init__(self, die_list=None):
        if die_list:
            if len(die_list) != 6:
                raise Exception("You need to have exactly 6 dice.")
        self.active_roll = die_list or self.roll_all_dice()
        self.active_roll_counter = 6
        self.qualify_bucket = []
        self.score_bucket = []
        self.total_rolls = 0 # Need to fix
        self.perfect_game = [1,4,6,6,6,6]
        self.total_score = 0
        self.play()

    def rolldice(self):
        dice1 = random.randint(1,6)
        return dice1

    def roll_all_dice(self):
        #This is the active_roll_bucket
        #player rolls all dice
        dice = []
        for die in range(6):
            dice.append(self.rolldice())
        print("This is the roll_all_dice FUNCTION", dice)
        return dice   
    
    def roll_all_dice_again(self):
        #This is the active_roll_bucket
        #player rolls all dice
        dice2 = []
        # print("this is the activerollcounter", self.active_roll_counter)
        for die in range(self.active_roll_counter):
            dice2.append(self.rolldice())
        print("This is the roll_all_dice_again FUNCTION", dice2)
        return dice2 

    def play(self):
        while self.do_turn():
            self.qualify_rules()
            self.strategy_sixes()
            self.update_active_roll()
            self.roll_all_dice_again()
            #Clear Active_Roll and update with new dice
            print("This is the PLAY loop active roll", self.active_roll)
        self.results()
        #player must place a minimum of one dice in either bucket on each roll
        #The bucket placement depends on qualify_rules and score_rules
        #Display the results of each roll and the corresponding buckets
        print("The Active roll is: %s" % self.active_roll,"The Qualifiers are: %s" % self.qualify_bucket, "The Score is: %s" % self.score_bucket, "The total rolls were: %s" % self.total_rolls)

    def do_turn(self):
        if self.active_roll_counter == 0:
            return False
        else:
            return True
        #test if we should do another turn

    def update_active_roll(self):
        self.active_roll.clear()
        self.active_roll = self.roll_all_dice_again()
        # return self.active_roll

    def qualify_rules(self):
        #Add dice to qualify_bucket
        #Must be 1 and a 4 not two 1's or two 4's
        #No more than two dice in this bucket
        for die in self.active_roll:
            if self.is_qualified():
                break
            if die in [1,4] and not die in self.qualify_bucket:
                self.qualify_bucket.append(die)
                self.active_roll.remove(die)
                self.active_roll_counter -= 1
                self.total_rolls += 1
                print("This is the qualify bucket", self.qualify_bucket)
        return self.qualify_bucket, self.active_roll
        #can occur within six different rolls
        

    def is_qualified(self):
        if 1 in self.qualify_bucket and 4 in self.qualify_bucket:
            return True

    def strategy_sixes(self):
        # only pick 6 when available
        #Must be four dice only, no more, no less
        #Must put a minimum of one dice per roll in the score_bucket and roll the rest according to strategy used
        is_found = False
        for die in self.active_roll:
            if len(self.score_bucket) == 4:
                return
            if die == 6:
                is_found = True
                self.score_bucket.append(die)
                self.active_roll.remove(die)
                self.active_roll_counter -= 1
                self.total_rolls += 1
                print("This is the score bucket", self.score_bucket)
        if is_found == False and len(self.score_bucket) < 4:
            die_max = max(self.active_roll)
            self.score_bucket.append(die_max)
            self.active_roll.remove(die_max)
            self.active_roll_counter -= 1
            self.total_rolls += 1
            print("This is the score bucket", self.score_bucket)
    # def strategyfives_and_sixes(self):
    #     #Pick 5 or 6 when available
        return self.score_bucket, self.active_roll
    
    def sum_score(self):
        self.total_score = sum(self.score_bucket)

    def results(self):
        if self.is_qualified():
            self.sum_score()
            # print("You are Qualified!, and your score is {}".format(self.total_score))
        else:
            print("Sorry, you did not qualify. Your score does not count.")

for x in range(1):
    game1 = PlayGame()
    print(game1.total_score )

