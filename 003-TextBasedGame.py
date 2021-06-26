from random import choice, randint
from time import sleep

'''
The main ideia is to develop a text-based game, with three routes.
however, I decided to create a larger game, with attributes and dice rolls.
My inspiration was to create something old school for my sister to play.
That said, the game's dialogues will be in Portuguese.

Disclaimer: this will be a mess, because I am not trying to make a clean 
code, but a cool game that my sister can enjoy and be proud of.
'''

'''Attributes'''
#player's dexterity, handling, stealth, precision and aim.
style = 0
#strenght, player's constitution, endurance and intimidation.
power = 0
#something like persuasion, deception and player's appearance.
charm = 0
#player's intellect, wisdom, knowledge and perception
brain = 0

def dice_roll(attribute):
    if attribute < 0:
        print(f'\nRolando 2d6 {attribute}', end = '')
    else:
        print(f'\nRolando 2d6 +{attribute}', end = '')
    sleep(0.8); print('.', end='')
    sleep(0.8); print('.', end='') 
    sleep(0.8); print('.')
    result = randint(1, 6) + randint(1, 6) + attribute
    sleep(1); print(f'Você rolou {result}.')
    if result >= 12:
        print('Um sucesso crítico!')
    return result

print('Após dias de viagem ', end=''); sleep(2); 
print('você finalmente chegou à ilha perdida.')
sleep(2)
print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\\
 \_/__________________________________________________________________/
''')
sleep(3); print('A Ilha do Tesouro Perdido.\n\n')
sleep(2)
print('Mas', end='')
sleep(0.8); print('.', end='')
sleep(0.8); print('.', end='') 
sleep(0.8); print('.', end='')
sleep(0.8); print(' Quem é você?')
sleep(2); print('0 - Um charlatão que conquistou o mapa em uma aposta.')
sleep(2); print('1 - Um nobre soldado à serviço de um rei em uma expedição.')
sleep(2); print('2 - Um estudioso historiador que investiga mitos antigos.')
sleep(2); print('3 - Um viajante destemido que recebeu este mapa de seu avô.')


'''Playbooks'''
player_playbook = int(input('Digite o número de seu personagem: '))

if player_playbook == 0:
    style = 3; power = 0; charm = 1; brain = -1
elif player_playbook == 1:
    style = 0; power = 3; charm = -1; brain = 1
elif player_playbook == 2:
    style = 1; power = -1; charm = 0; brain = 3
elif player_playbook == 3:
    style = -1; power = 1; charm = 3; brain = 0
else:
    player_playbook = 7
    print('Que misterioso, espero que tenha sorte em sua jornada.')
    style = 1; power = 1; charm = 1; brain = 1


#algoritm for dice rolls
if dice_roll(style) >= 7:
    print('A primeira rolagem foi um sucesso')

