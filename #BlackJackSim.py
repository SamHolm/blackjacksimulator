#Black Jack
import random
#Rules:
stand = "S17" #S17 or H17 #doesnt work
blackjack = 1 #3:2 or 6:5 #works
decks = 2 #1, 2, 4, 6, 8 #works
double_all_hands = True #doesnt work
das = True #double after split #doesnt work
rsa = True #resplit aces #doesnt work
peek10 = True #dealer peeks when his up card is 10 #works
surrender = False #You can take half of your bet back #doesnt work

# Basic Strategy
#Dealer      2    3    4    5    6    7    8    9    10   A   player total
hard_total=[["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"] , #4
            ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"] , #5
            ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"] , #6
            ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"] , #7
            ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"] , #8
            ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"] , #9
            ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"] , #10
            ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"] , #11
            ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"] , #12
            ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"] , #13
            ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"] , #14
            ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"] , #15
            ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"] , #16
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"] , #17
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"] , #18
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"] , #19
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"] , #20
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]] #21
soft_total=[["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"] , #A2
            ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"] , #A3
            ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"] , #A4
            ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"] , #A5
            ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"] , #A6
            ["D", "D", "D", "D", "D", "H", "H", "H", "H", "H"] , #A7
            ["S", "S", "S", "S", "D", "S", "S", "S", "S", "S"] , #A8
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"] , #A9
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]] #A10
split_hand=[["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"] , #22
            ["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"] , #33
            ["N", "N", "N", "Y", "Y", "N", "N", "N", "N", "N"] , #44
            ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"] , #55
            ["Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N", "N"] , #66
            ["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"] , #77
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"] , #88
            ["Y", "Y", "Y", "Y", "Y", "N", "Y", "Y", "N", "N"] , #99
            ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"] , #TT
            ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"]] #AA

def player_choice():
    times = int(input("How many times do you want to play?"))
    new_balence = float(input("How much money do you have?")) 
times = 5000000
new_balence = 1000
start_balence = new_balence
print("bal: "+str(new_balence))
# Deck Creation

shoe = []
for i in range(1,10):
    for j in range(0,(4*decks)):
        shoe.append(i)
for i in range(10,14):
    for j in range(0,(4*decks)):
        shoe.append(10)
print(shoe)
shuffle = list(shoe)
print(shuffle)
random.shuffle(shoe)
print(shuffle)

print("")
print("")


def hand(balence, shoe):
    
    while True:
        bet = 20
        if bet > balence or bet < 0:
            '''
            print("You cannot bet over your balence or lower than 1")
            '''
        else:
            break
    balence = balence - bet
    
    # Deal
    one_card = shoe[0]
    shoe.pop(0)
    down_card = shoe[0]
    shoe.pop(0)
    two_card = shoe[0]
    shoe.pop(0)
    up_card = shoe[0]
    shoe.pop(0)
    player_hand = [one_card,two_card] 
    dealer_hand = [up_card,down_card]
    player_aces = 0
    dealer_aces = 0
    player_hands = 1
    player_side = [[],[],[],[]] #Needed for splits , most of the game they will be empty spots
    splits = 0 #tracking of splits
    for i in range(2):
        if player_hand[i] == 1:
            player_aces += 1
        if dealer_hand[i] == 1:
            dealer_aces += 1
    '''
    print("Dealer has "+str(dealer_hand[1]))
    print("You have "+str(player_hand[0])+", "+str(player_hand[1]))
    '''
    # player blackjack
    if player_aces == 1:
        if player_hand[0] + player_hand[1] == 11:
            '''
            print("Black Jack!")
            '''
            balence = balence + bet*(1+blackjack)
            return balence

    # dealer blackjack
    if dealer_hand[1] == 1:
        insurance = "no"
        if dealer_hand[0] == 10:
            '''
            print("Dealer has Blackjack")
            '''
            if insurance == "yes":
                balence = balence + bet
            return balence
        else:
            '''
            print("Dealer doesn't have Blackjack")
            '''
            if insurance == "yes":
                balence = balence - (bet/2)
    if peek10 == True:
        if dealer_hand[0] == 10:
            if dealer_hand[1] == 1:
                return balence

    #player choice
    current_hands = 0
    player_side[0] = player_hand
    '''
    print(player_side[0])
    '''
    for i in range(4):
        while True:
            if len(player_side[i]) > 1:
                '''
                print("Your hand" + str(player_side[i]))
                '''
                choice = "N"
                if player_side[i][0] == player_side[i][1] and len(player_side[i]) == 2 and splits < 1:
                    if player_side[i][0] == 1:
                        choice = "Y"
                    else:
                        choice = (split_hand[((player_side[i][0])-2)][up_card-2])
                elif player_side[i][0] == 1 or player_side[i][1] == 1:
                    if len(player_side[i]) == 2:
                        choice = (soft_total[(sum(player_side[i])-3)][up_card-2])
                if choice == "N":
                    choice = (hard_total[(sum(player_side[i])-4)][up_card-2])
                

                if choice == "H" or choice == "D":
                    if choice == "D" and balence > bet:
                        balence = balence - bet
                        bet = bet*2
                    new_card = shoe[0]
                    player_side[i].append(new_card)
                    shoe.pop(0)
                    '''
                    print("You drawn "+str(player_side[i][-1]))
                    if player_aces > 0 and sum(player_side[i]) <= 11:
                        print("Your hand is: "+str(sum(player_side[i])+10))
                    else:
                        print("Your hand is: "+str(sum(player_side[i])))
                    '''
                    if sum(player_side[i]) > 21:
                        '''
                        print("You bust")
                        '''
                        player_side[i] = [0,0]
                        break
                    if choice == "D":
                        break
                elif choice == "S":
                    '''
                    print("You stand.")
                    '''
                    break
                elif choice == "Y":
                    if player_side[i][0] == player_side[i][1] and balence >= bet:
                        balence = balence - bet
                        player_side[i+2-splits].append(player_side[i][1]) 
                        new_card = shoe[0]
                        player_side[i][1] = new_card
                        '''
                        print(player_side[i])
                        '''
                        if new_card == 1:
                            player_aces += 1
                        shoe.pop(0)
                        new_card = shoe[0]
                        player_side[i+2-splits].append(new_card)
                        '''
                        print(player_side[i+2-splits])
                        '''
                        if new_card == 1:
                            player_aces += 1
                        shoe.pop(0)
                        splits += 1
                    else:
                        bet = bet
            else:
                break
                            
                            

    # dealer choice
    dealer_value = sum(dealer_hand)
    '''
    print("Dealer has "+str(sum(dealer_hand)))
    '''
    while True:
        dealer_value = sum(dealer_hand) #Value including aces to make choices. Needed due to S17 vs H17 rules.
        if dealer_aces > 0 and (sum(dealer_hand)+10) <= 21:
            dealer_value = (sum(dealer_hand)+10)
            
        if dealer_value < 17: #hit
            new_card = shoe[0]
            dealer_hand.append(new_card)
            shoe.pop(0)
            '''
            print("Dealer drawn "+str(dealer_hand[-1]))
            '''
            if dealer_hand[-1] == 1:
                dealer_aces += 1
            if (dealer_value + dealer_hand[-1] - (dealer_aces*10)) > 21:
                '''
                print("Dealer bust!")
                '''
                balence = balence + bet*2
                dealer_bust = True
                break
        if dealer_value >= 17: #stand
            '''
            print("Dealer stands")
            '''
            dealer_bust = False
            break
            
            
    #who wins?

    for i in range(4):
        if len(player_side[i]) > 1:
            if dealer_aces > 0 and sum(dealer_hand) <= 11:
                dealer_hand.append(10)
            if player_aces > 0 and sum(player_hand) <= 11:
                player_side[i].append(10)
            if dealer_bust == False:
                if sum(player_side[i]) > sum(dealer_hand):
                    balence = balence + bet*2
                elif sum(player_side[i]) == sum(dealer_hand):
                    balence = balence + bet
            elif dealer_bust == True:
                if sum(player_side[i]) > 2:
                    balence = balence + bet
    return balence
            
            
            
for i in range(1,times+1):
    new_balence = hand(new_balence, shoe)
    '''
    print("You now have "+str(new_balence)+" dollars")
    print("")
    print("")
    '''
    if i % 13 == 0:
        '''
        print("Shuffling")
        '''
        shoe = list(shuffle)
        random.shuffle(shoe)
    if new_balence == 0:
        print("You have no money. Game Over.")
        break
        
        
print("You started with "+str(start_balence))
print("You played "+str(times)+" hands.")
print("You end with "+str(new_balence))
avg_per_hand = (new_balence-start_balence)/times
print("Average per hand  "+str(avg_per_hand))