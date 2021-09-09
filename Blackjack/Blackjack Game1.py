#Set the suits&ranks&values 
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
#Class definitions
#Card class
class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
        
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
#Deck class
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
   
        

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
         return self.deck.pop()
#Hand class
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value=values[card.rank]+self.value
        if card.rank=='Ace':
            self.aces+=1
        
    
    def adjust_for_ace(self):
        if self.value>21 and self.aces!=0:
            self.value-=10
            self.aces-=1
#Chips class
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
        
    
    def lose_bet(self):
        self.total-=self.bet
#Function Defintions
#Function for taking bets
def take_bet(Chips):
    while True:
        try :
            bet=int(input('please make a bet: '))
            if bet<=Chips.total:
                return bet
                     
            else:
                print('you dont have enough chips')
        except:
            print('wrong input please enter a number')
#Function for taking hits
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
#Function prompting the Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    choise='w'
    while choise not in ['H','S']:
        choise=input('do you want to Hit or Stand(H or S): ')
        if choise not in ['H','S']:
            print('wrong input ')
        elif choise=='H':
            hit(deck,hand)
        elif choise=='S':
            playing=False
#Functions to display cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
    
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
#Functions to handle end of game scenarios
def player_busts(player,chips):
    print('player busts')
    chips.lose_bet()
    return False
    
    

def player_wins(player,chips):
    print ('player win')
    chips.win_bet()
    return False

    
def dealer_busts(player,chips):
    print ('dealer busts')
    chips.win_bet()
    return False
      
def dealer_wins(player,chips):
    print('dealer win')
    chips.lose_bet()
    return False
    
def push():
    print("it's a tie ! push")
    return False
#Main
while playing==True:
    # Print an opening statement
    print('Welcome to Blackjack game')
    
    # Create & shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffle()
    player=Hand()
    dealer=Hand()
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
        
    # Set up the Player's chips
    player_chips=Chips()
    
    
    # Prompt the Player for their bet

    player_chips.bet=take_bet(player_chips)
    # Show cards (but keep one dealer card hidden)
    
    show_some(player,dealer)
    
    while playing==True: 
        # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
 
        show_some(player,dealer)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            playing=player_busts(player,player_chips)
            break 
            
            

            

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if  player.value <= 21:
        
        while dealer.value<17:
            
            dealer.add_card(deck.deal())
                
                
            
    
        # Show all cards
        show_all(player,dealer)
        
    
        # Run different winning scenarios
        if dealer.value>21 :
            playing=dealer_busts(player,player_chips)
            
        elif dealer.value>player.value:
            playing=dealer_wins(player,player_chips)
            
        elif dealer.value<player.value:
            playing=player_wins(player,player_chips)
            
        else:
            playing = push()
            
            
            
        
    
    # Inform Player of their chips total 
    print(f'you have {player_chips.total} chips')
    
    # Ask to play again
    a='w'
    while a not in ['Y','N']:
        a=input('do you want to play again?(Y or N): ')
        if a == 'Y':
            
            playing = True
            continue
        elif a == 'N':
            playing = False
            break
        else:
            print('wrong input')

        

    