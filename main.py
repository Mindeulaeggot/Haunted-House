####################### import libraries #########################################################################################
import random 
import os
import sys 
import time 
import DemonImages as Image

Player_information = {'player_name': '', 'player_health': 1000 , 'player_manapoint' : 100, 'current_stage': 1}
skillset = {'1.Sword Attack': 300, '2.Fire Magic': 450, '3.Ice Magic': 530} # Skill name : Damage given
skill_set = ['', '1.Sword Attack', '2.Fire Magic', '3.Ice Magic'] # index 0 does not count
skill_set_mana = [0, 30, 50, 60] # index 0 does not count
mana_show = {'Sword Attack': 30, 'Fire Magic': 50, 'Ice Magic': 60}
Stage_information = {'Stage1_health' : 1500, 'Stage2_health' : 2500, 'Stage3_health' : 4000, 'Stage4_health' : 7000}
item = {'1.A sword of Amenadiel': 2500}
PlayerAttack = 100 
r = random.Random(); seed = int(input('Before starting the game, please press any positive integar number for your gameplay!: ')); os.system('clear')
if seed != -1: r.seed(seed)

def gameintro():
    global Player_information
    print("############################\n#  *THE HERO'S ADVENTURE*  #\n#1. Game Start             #\n#2. Quit Game              #\n############################")
    if '1' == input('Press 1 or 2 to play! '):
        name = input('How can I call you..? ')
        os.system('clear')
        board(f'{name}, your journey starts now!'.center(len(f'{name}, your journey starts now!')))
        time.sleep(3)
        Player_information['player_name'] = name
        main()
    else:
        exit()

def board(text: str):
    show = {'1':'------------------------------------------------', '2':'', '3':'------------------------------------------------'}
    show['2'] = text.center(48)
    for v in show.values():
        print(v)

def move_next(): # allows to move to the next stage
    if Player_information['current_stage'] == 2: Stage2().printStage()
    if Player_information['current_stage'] == 3: Stage3().printStage()
    if Player_information['current_stage'] == 4: Stage4().printStage()
    if Player_information['current_stage'] == 5: os.system('clear'); Image.Print_Princess(); text = 'You have saved the princess!'.center(48); print(text); board('You have completed the game!'); exit()


def attack_next(): # allows to run next Stage nth attack()
    if Player_information['current_stage'] == 1: return Stage1().attack()
    if Player_information['current_stage'] == 2: return Stage2().attack()
    if Player_information['current_stage'] == 3: return Stage3().attack()
    if Player_information['current_stage'] == 4: return Stage4().attack()

def Defend():
    if Player_information['current_stage'] == 1: return Stage1().Defend()
    if Player_information['current_stage'] == 2: return Stage2().Defend()
    if Player_information['current_stage'] == 3: return Stage3().Defend()
    if Player_information['current_stage'] == 4: return Stage4().Defend()

def Print():
    if Player_information['current_stage'] == 1: return Image.Print_Demograth()
    if Player_information['current_stage'] == 2: return Image.Print_Adramalech()
    if Player_information['current_stage'] == 3: return Image.Print_Mammon()
    if Player_information['current_stage'] == 4: return Image.Print_Lucifer()

class Player:
    def __init__(self):
        self.name = Player_information['player_name']
        
    def show(self, damage):
        board(f'You gave {damage} damage!\n'+attack_next()+'\nYour health: {}'.format(Player_information['player_health'])+'\nYour mana: {}'.format(Player_information['player_manapoint']))
        PlayerAttack = 100

    def show_def(self, text):
        board(text +'\nYour health: {}'.format(Player_information['player_health'])+'\nYour mana: {}'.format(Player_information['player_manapoint']))
        PlayerAttack = 100
    
    def attack(self):
        global PlayerAttack # basic damage is 100 but if you use 2.Defend your damage increases by 450 
        stage = int(Player_information['current_stage'])
        Stage_information[f'Stage{stage}_health'] = int(Stage_information[f'Stage{stage}_health']) - PlayerAttack
        if Stage_information[f'Stage{stage}_health'] <= 0:
            Stage_information[f'Stage{stage}_health'] = 0
        os.system('clear'); Player().show(PlayerAttack)

    def Defendfrom(self):
        os.system('clear')
        Defend()

    def skillsuse(self):
        print('Your skills: {}'.format(skillset)); print('MP cost of your skills: {}'.format(mana_show)); cho = input('Choose your skill! (write the number of the skill, e.g. 1): '); stage = int(Player_information['current_stage'])
        if cho in '1234' and int(cho) <= len(skill_set)-1: 
            cho = int(cho)
            if int(Player_information['player_manapoint']) >= int(skill_set_mana[cho]):
                Player_information['player_manapoint'] = int(Player_information['player_manapoint']) - int(skill_set_mana[cho])
                Stage_information[f'Stage{stage}_health'] = int(Stage_information[f'Stage{stage}_health']) - skillset[(skill_set[cho])]
                if Stage_information[f'Stage{stage}_health'] <= 0:
                    Stage_information[f'Stage{stage}_health'] = 0
                os.system('clear'); Player().show(skillset[skill_set[cho]])
            else: os.system('clear'); Print(); board('Invalid move! Not enough Mana Points!')
        else:
            os.system('clear'); Print(); board('Invalid input!')

    def itemuse(self):
        turn = Player_information['current_stage'] 
        print('Your item: {}'.format(item)); cho = int(input('Choose your item (write the number of your item): '))
        if cho == 1:
            if turn == 3:
                os.system('clear')
                Print(); stage = Player_information['current_stage']; Stage_information['Stage3_health'] = Stage_information['Stage3_health'] - item["1.A sword of Amenadiel"]
                if Stage_information[f'Stage{stage}_health'] <= 0: Stage_information[f'Stage{stage}_health'] = 0
                text = "The use of the item was effective"+"\nMammon's HP: {}".format(Stage_information['Stage3_health'])+'\nMammon cannot make move for this turn!'+f'\nYou received 0 damage!'
                board(text)
            if turn == 4:
                os.system('clear')
                Print(); stage = Player_information['current_stage']; Stage_information['Stage4_health'] = Stage_information['Stage4_health'] - item["1.A sword of Amenadiel"]
                if Stage_information[f'Stage{stage}_health'] <= 0: Stage_information[f'Stage{stage}_health'] = 0
                text = "The use of the item was effective."+"\nLucifer's HP: {}".format(Stage_information['Stage4_health'])+'\nLucifer cannot make move for this turn.'+f'\nYou received 0 damage!'
                board(text)
        else:
            message = 'Invalid move! Please write the number of the existing item.'.center(48); print(message)

    def decision(self, item):
        if item == 0:
            board('1. Attack  **  2. Defend  **  3. Skill')
            cho = input('What are you going to do? ')
            if cho == '1':
                Player().attack() 
            if cho == '2':
                Player().Defendfrom()
            if cho == '3':
                Player().skillsuse() 
            if cho not in '123':
                os.system('clear'); Print(); board('Invalid input!')
        else:
            board('1. Attack * 2. Defend * 3. Skill * 4. Items')
            cho = input('What are you going to do? ')
            if cho == '1':
                Player().attack() 
            if cho == '2':
                Player().Defendfrom()
            if cho == '3':
                Player().skillsuse() 
            if cho == '4':
                Player().itemuse()
            if cho not in '1234':
                os.system('clear'); Print(); board('Invalid input!')
        

class Stage1:
    def __init__(self):
        self.name = 'Demograth'
    
    def printStage(self):
        os.system('clear')
        text1 = 'There was a princess named Rose. ' 
        text2 = 'However, the king of Hell Lucifer took her to his own castle. ' 
        text3 = 'Your job is to find her and take her back to your kingdom. ' 
        text4 = "On the way to Lucifer's castle, you feel a sense of strangeness. "
        text5 = "You have encountered {}! ".format(self.name)
        text6 = "Your battle begins now.\n"

        for character in text1: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text2: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text3: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text4: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text5: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text6: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)

        os.system('clear')
        Print()


    def Defend(self):
        Print()
        board('You defended the attack from Demograth.\nYou did not take any damage from Demograth!')

    def attack(self):
        stage = int(Player_information['current_stage'])
        attack_1 = 45 # First stage has only one move
        if Stage_information[f'Stage{stage}_health'] <= 0:
            attack_1 = 0
        else:
            Player_information['player_health'] = int(Player_information['player_health']) - attack_1
        if Player_information['player_health'] <= 0: Player_information['player_health'] = 0
        text = 'Demograth HP: {}'.format(Stage_information['Stage1_health'])+'\nDemograth makes a move!'+f'\nYou received {attack_1} damage!'
        Print()
        return text

class Stage2:
    def __init__(self):
        self.name = 'Adramalech'
    
    def printStage(self):
        os.system('clear')
        Player_information['player_health'] = Player_information['player_health'] + 3000 
        skillset.update({'4.Dark Magic' : 800}); skill_set.append('4.Dark Magic'); mana_show.update({'Dark Magic': 100}); skill_set_mana.append(100) # adding a new skill
        text1 = 'Another demon called Adramalech appeared on your way. ' 
        text2 = 'Because you killed Demograth, your skills are enforced and your HP and MP are restored. ' 
        text3 = 'Kill Adramalech and find the key that opens the gate of Hell. ' 
        text4 = "According to the Adventure Guild, Adramalech has special attack that deals signficiant damage but has a lower chance of attack. "
        text5 = "You have encountered {}! ".format(self.name)
        text6 = "Your battle begins now.\n"

        for character in text1: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text2: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text3: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text4: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text5: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text6: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)

        os.system('clear')
        Print()

    def Defend(self):
        global PlayerAttack
        stage = int(Player_information['current_stage'])
        attack_1 = 0
        randnum = r.randrange(1,7)
        if randnum == (2 or 3 or 4 or 5 or 6): attack_1 += 100
        else: attack_1 += 200
        if Stage_information[f'Stage{stage}_health'] <= 0:
            attack_1 = 0
        else:
            Player_information['player_health'] = int(Player_information['player_health']) - attack_1 + 50
        Print()
        text = "Adramalech's HP: {}".format(Stage_information['Stage2_health'])+'\nAdramalech makes a move!'+f"\nEnemy's damage is reduced by 50.\nYou attack is enforced by 100."
        PlayerAttack += 100
        Player().show_def(text)

    def attack(self):
        stage = int(Player_information['current_stage'])
        attack_1 = 0
        randnum = r.randrange(1,7)
        if randnum == (2 or 3 or 4 or 5 or 6): attack_1 += 100
        else: attack_1 += 200
        if Stage_information[f'Stage{stage}_health'] <= 0:
            attack_1 = 0
        else:
            Player_information['player_health'] = int(Player_information['player_health']) - attack_1
        if Player_information['player_health'] <= 0: Player_information['player_health'] = 0
        text = "Adramalech's HP: {}".format(Stage_information['Stage2_health'])+'\nAdramalech makes a move!'+f'\nYou received {attack_1} damage!'
        Print()
        return text
    
class Stage3:
    def __init__(self):
        self.name = 'Mammon'
    
    def printStage(self):
        os.system('clear')
        Player_information['player_health'] = Player_information['player_health'] + 3000 
        text1 = "After Adramalech's death Mammon was summoned in front of you. "
        text2 = "Mammon says, 'How dare you kill my beloved freind. I shall grant you the cycle of pain.' " 
        text3 = 'Because you killed Adramalech, you gained a special item called The Sword of Amenadiel. ' 
        text4 = 'You now can use this item. '
        text5 = "You have encountered {}! ".format(self.name)
        text6 = "Your battle begins now.\n"

        for character in text1: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text2: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text3: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text4: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text5: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text6: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)

        os.system('clear')
        Print()

    def Defend(self):
        global PlayerAttack
        stage = int(Player_information['current_stage'])
        attack_1 = 0
        randnum = r.randrange(1,7)
        if randnum == (2 or 3 or 4 or 5 or 6): attack_1 += 100
        else: attack_1 += 200
        if Stage_information[f'Stage{stage}_health'] <= 0:
            attack_1 = 0
        else:
            Player_information['player_health'] = int(Player_information['player_health']) - attack_1 + 10
        text = "Mammon's HP: {}".format(Stage_information['Stage3_health'])+'\nMammon makes a move!'+f"\nEnemy's damage is reduced by 100.\nYou attack is enforced by 450."
        PlayerAttack += 450
        Print()
        Player().show_def(text)

    def attack(self):
        stage = int(Player_information['current_stage'])
        attack_1 = 0
        randnum = r.randrange(1,7)
        if randnum == (2 or 3 or 4 or 5): attack_1 += 200
        else: attack_1 += 300
        if Stage_information[f'Stage{stage}_health'] <= 0:
            attack_1 = 0
        else:
            Player_information['player_health'] = int(Player_information['player_health']) - attack_1
        if Player_information['player_health'] <= 0: Player_information['player_health'] = 0
        text = "Mammon's HP: {}".format(Stage_information['Stage3_health'])+'\nMammon makes a move!'+f'\nYou received {attack_1} damage!'
        Print()
        return text
   
class Stage4:
    def __init__(self):
        self.name = 'Lucifer'
    
    def printStage(self):
        os.system('clear')
        Player_information['player_health'] = Player_information['player_health'] + 1000 
        #skillset.update({'5.Self Heal' : 1000}); skill_set.append('5.Self Heal'); skill_set_mana.append(200) # adding a new skill
        text1 = 'You obtained the key from Mammon. Now You can unlock the gate of Hell. You entered the realm of Hell after opening the gate of Hell. ' 
        text2 = "Because you killed three of Lucifer's servants, Lucifer is about to rage. "
        text3 = 'You see princess Rose locked in the jail of the Hell. ' 
        text4 = "Exterminate Lucifer and save princess Rose! "
        text5 = "You have encountered {}! ".format(self.name)
        text6 = "Your battle begins now.\n"

        for character in text1: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text2: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text3: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text4: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text5: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        for character in text6: 
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)

        os.system('clear')
        Print()

    def Defend(self):
        global PlayerAttack
        stage = int(Player_information['current_stage'])
        attack_1 = 0
        randnum = r.randrange(1,7)
        if randnum == (2 or 3 or 4 or 5): attack_1 += 300
        else: attack_1 += 500
        if Stage_information[f'Stage{stage}_health'] <= 0:
            attack_1 = 0
        else:
            Player_information['player_health'] = int(Player_information['player_health']) - attack_1
        text = 'Lucifer is too powerful to make such move.\nYou cannot defend his attack.'+"\nLucifer's HP: {}".format(Stage_information['Stage4_health'])+'\nLucifer makes a move!'+f'\nYou received {attack_1} damage!'
        Print()
        Player().show_def(text)

    def attack(self):
        stage = int(Player_information['current_stage'])
        attack_1 = 0
        randnum = r.randrange(1,7)
        if randnum == (2 or 3 or 4 or 5 or 6 or 7): attack_1 += 300
        else: attack_1 += 700
        if Stage_information[f'Stage{stage}_health'] <= 0:
            attack_1 = 0
        else:
            Player_information['player_health'] = int(Player_information['player_health']) - attack_1
        if Player_information['player_health'] <= 0: Player_information['player_health'] = 0
        text = "Lucifer's HP: {}".format(Stage_information['Stage4_health'])+'\nLucifer makes a move!'+f'\nYou received {attack_1} damage!'
        Print()
        return text

def main():
    global PlayerAttack
    GameStatus = 1
    Stage1().printStage()
    while GameStatus != 0:
        stage = int(Player_information['current_stage'])
        if Stage_information[f'Stage{stage}_health'] <= 0:
            board('You have defeated the monster!')
            time.sleep(5)
            os.system('clear')
            Player_information['current_stage'] = int(Player_information['current_stage']) + 1
            Player_information['player_health'] = 1000; Player_information['player_manapoint'] = 150; PlayerAttack = 100
            move_next() 
        if Player_information['player_health'] <= 0:
            os.system('clear')
            board('You are eliminated... Game Over!'); exit()
        else:
            if stage <= 2: Player().decision(0)
            else: Player().decision(1)

gameintro()
