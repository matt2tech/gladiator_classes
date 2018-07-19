from core import Gladiator
from time import sleep
from core import Scene


def get_name_1():
    name = input('Contestant #1\'s name? ').strip()
    name = Scene(name)
    return name


def get_name_2():
    sleep(1)
    name = input('Contestant #2\'s name? ').strip()
    name = Scene(name)
    return name


def player(name):
    player = Gladiator(name, 100, 0, 5, 15, 15)
    return player


def player_turn(attacker, defender):
    while True:
        text = input(
            'It is {}\'s move.\n1 - attack\n2 - wait\n3 - heal\n4 - rampage\n5 - evade\n>>> '.
            format(attacker.name))
        if text == '1':
            attacker.attack(defender)
            break
        elif text == '2':
            Battle.waiting(attacker)
            break
        elif text == '3':
            attacker.heal()
            break
        elif text == '4':
            attacker.rampage(defender)
            break
        elif text == '5':
            attacker.evading()
            break
        else:
            print('Invalid move\n"The crowd is not pleased"')
            print('(-(-_(-_-)_-)-)')
            sleep(1)
            print(
                '\n--------------------------------------------------------------------------\n'
            )


def battle(player_1, player_2):
    while True:
        player_1.evading_reset()
        print(player_1)
        print(player_2)
        player_turn(player_1, player_2)
        sleep(1)
        print(
            '\n--------------------------------------------------------------------------\n'
        )
        if player_2.is_dead() == True:
            print('{} has fallen\n{} wins'.format(player_2.name,
                                                  player_1.name))
            print('ᕦ(ˇò_ó)ᕤ (✖╭╮✖ )')
            sleep(2)
            break
        player_2.evading_reset()
        print(player_1)
        print(player_2)
        player_turn(player_2, player_1)
        sleep(1)
        print(
            '\n--------------------------------------------------------------------------\n'
        )
        if player_1.is_dead() == True:
            print('{} has fallen\n{} wins'.format(player_1.name,
                                                  player_2.name))
            print('( ✖╭╮✖) ᕦ(ò_ó^)ᕤ')
            sleep(2)
            break


def main():
    Scene.start_menu()
    Scene.loading_screen()
    Scene.sign_up()
    name_1 = get_name_1()
    name_2 = get_name_2()
    player_1 = player(name_1)
    player_2 = player(name_2)
    name_1.battle_announce(name_2)
    battle(player_1, player_2)
    Scene.trophy()
    name_1.credits(name_2)
    main()


if __name__ == '__main__':
    main()
