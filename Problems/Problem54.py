# ProblemURL: https://projecteuler.net/problem=67
cardIndex = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}


def pokerhand(arg1):
    def straight(hand):
        shifted_hand = [(x+5) % 12 for x in hand]
        shifted_hand.sort(reverse=True)
        for x in range(len(hand)-1):
            if hand[x] != hand[x+1] + 1:
                for x in range(len(hand)-1):
                    if shifted_hand[x] != shifted_hand[x + 1] - 1:
                        return False
        return True

    def flush(hand):
        if len(set(hand)) == 1:
            return True
        else:
            return False

    def pairs(hand):
        pair = [[], [], []]  # [[2pairs], [3pairs], [4pairs]]
        unique_numbers = set(hand)
        for x in unique_numbers:
            if hand.count(x) == 2:
                pair[0].append(x)
            elif hand.count(x) == 3:
                pair[1].append(x)
            elif hand.count(x) == 4:
                pair[2].append(x)
        return pair

    def highcard(hand):
        return hand[0]

    # Handling Data
    simple_hand_num = [cardIndex[x[0]] for x in arg1]
    simple_hand_num.sort(reverse = True)
    simple_hand_suit = [x[1] for x in arg1]

    # Checking for patterns
    is_straight = straight(simple_hand_num)
    is_flush = flush(simple_hand_suit)
    p = pairs(simple_hand_num)
    h = highcard(simple_hand_num)
    score = 0

    # Giving score
    if is_straight and is_flush and simple_hand_num[0] == 14 and simple_hand_num[4] == 8:  # Royal Flush
        score = 9
    elif is_straight and is_flush:  # Straight Flush
        score = 8
    elif len(p[2]) == 1:  # Four of a kind
        score = 7 + p[2][-1]/10**2
    elif len(p[0]) == 1 and len(p[1]) == 1:  # Full house
        score = 6 + p[1][-1]/10**4 + p[0][-1]/10**6
    elif is_flush:  # Flush
        score = 5
    elif is_straight:  # Straight
        score = 4
    elif len(p[0]) == 0 and len(p[1]) == 1:  # Three of a kind
        score = 3 + p[1][-1]/10**2
    elif len(p[0]) == 2 and len(p[1]) == 0:  # Two pair
        score = 2 + p[0][-1]/10**4
    elif len(p[0]) == 1 and len(p[1]) == 0:  # One pair
        score = 1 + p[0][-1]/10**6
    return score, h


f = open('Problem54data.txt', 'r')
content = f.read().split("\n")
f.close()
hands = [y.split() for y in content]
player1Wins = 0
for n in range(len(hands)):
    hand1 = hands[n][0:5]
    hand2 = hands[n][5:10]
    hand1Score, hand1HighCard = pokerhand(hand1)
    hand2Score, hand2HighCard = pokerhand(hand2)
    if hand1Score > hand2Score or hand1Score == hand2Score and hand1HighCard > hand2HighCard:
        player1Wins += 1
print(player1Wins)
