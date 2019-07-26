import random

"""basis for my game idea. quick pvp spirelike"""
class Deck:
    def __init__(self, deck_list, hand_limit):#change to take tuple
        """generates deck, requires decklist and hand limit"""
        self.deck_list = deck_list
        self.hand_limit = hand_limit#safeguard
    
    def new_future(self):
        """shuffles deck"""
        self.future = self.deck_list.copy()
        random.shuffle(self.future)

    def draw(self):
        """checks if enough cards in future, may shuffle then draws"""
        if len(self.future) < self.hand_limit:
            self.new_future()
        self.hand = []
        for amt in range(0,self.hand_limit):
            self.hand.append(self.future.pop(0))

    def read_future(self):
        """still needs to alphabetize, reads future"""
        print(self.future)

testDeck = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']

class Ghost:
    def __init__(self,name):
        """generates health and a player name"""
        self.name = name
        self.maxhp = 15
        self.block = 0
        self.dead = False
        self.damage = 0

    def hp_delta(self, change):
        """gains or loses damage based on int given, checks for 'death'. Positive #s = hurt"""
        self.damage += int(change)
        if self.damage >= self.maxhp:
            self.dead = True

    def rez(self):
        """undos death"""
        self.damage = (self.maxhp - 1)
        self.dead = False

    def murderize(self):
        """sets Ghost to dead, and sets damage to max hp via hp_delta just to make sure"""
        self.dead = True
        self.hp_delta(self.maxhp - self.damage)

    def attacked(self, dmg):
        self.block += -(dmg)
        if self.block <= 0:
            self.hp_delta(abs(self.block))
            self.block = 0
        
class Persona:
    def __init__(self, persona_name, maxhp, deck_list, hand_size, ghost_var):
        self.name = persona_name
        ghost_var['ghost'].maxhp = maxhp
        ghost_var['deck'] = Deck(deck_list, hand_size)
    

class PersonaClashDuel:
    def __init__(self, playerA_name, playerA_persona, playerB_name, playerB_persona):
        """starts up a duel"""
        player1 = {}
        player1['ghost'] = Ghost(playerA_name)

class BaseDeck:
    def __init__(self):
        """Base Deck Info for testing"""
        pass

    def strike(target):
        """Deal 5 Damage to target"""
        dmg = 5
        target.attacked(5)

    def defend(owner):
        """Blocks for 5 Damage"""
        owner.block += 5

    def guarded_stab(owner, target):
        """Blocks 4 Attacks 2"""
        owner.block += 4
        target.attacked(2)

    def crush(target):
        """Damages armor for 5 then deals 4 Damage"""
        if target.block <= 5: 
            target.block = 0
        else:
            target.block += -5
        target.attacked(4)

    def full_guard(owner):
        """Blocks for 10"""
        owner.block += 10

    def norm_deck_gen():
        list = {'Strike':None}
        
