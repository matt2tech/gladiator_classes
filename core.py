from random import randint
from time import sleep

# balanced gladiator: Gladiator(name, 100, 100, 0, 100, 5, 15, 15, 65)
# name, health, maximum health, total rage, maximum rage, lowest damage, highest damage, evasion percentage


# berserker class: Gladiator(name, 100, 100, 0, 150, 15, 20, 15, 15)
# bladedancer class: Gladiator(name, 85, 85, 40, 100, 10, 10, 65, 65)
# vanguard class: Gladiator(name, 150, 150, 0, 100, 10, 15, 25, 25)
class Gladiator():
    '''Represents a gladiator.

    Each gladiator has a name, health, maximum health, rage, maximum rage, a range of damage, evasion, base evasion.
    '''

    def __init__(self, name, health, maximum_health, rage, maximum_rage,
                 damage_low, damage_high, evasion, base_evasion):
        self.name = name
        self.health = health
        self.maximum_health = maximum_health
        self.rage = rage
        self.maximum_rage = maximum_rage
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.evasion = evasion
        self.base_evasion = base_evasion

    def __str__(self):
        ''' (Gladiator) -> str

        Returns a string representation of a Gladiator showing their
        name, health, and rage.
        '''

        return '{}: {} HP ||| {} Rage'.format(self.name, self.health,
                                              self.rage)

    def __repr__(self):
        ''' (Gladiator) -> str

        Returns a string representation of this Gladiator.
        '''

        return 'Gladiator(\'{}\', {}, {}, {}, {}, {}, {}, {}, {})'.format(
            self.name, self.health, self.maximum_health, self.rage,
            self.maximum_rage, self.damage_low, self.damage_high, self.evasion,
            self.base_evasion)

    def attack(self, defender):
        ''' (Gladiator, Gladiator) -> NoneType

        Attacker attacks defender which results in the attack hitting and 
        taking health from the defender, or the attack missing
        '''

        attack = randint(self.damage_low, self.damage_high)
        accuracy = randint(1, 100)
        if accuracy > defender.evasion:
            if self.rage >= randint(1, 100):
                print(
                    '{} rages, slings the controller and hits {} in the head'.
                    format(self.name, defender.name))
                print('"{} dealt {} DMG"'.format(self.name, attack * 2))
                print('( -_-)つ -=≡~B(҂T-T)')
                defender.health = max(defender.health - attack * 2, 0)
                self.rage = 0
            else:
                defender.health = max(defender.health - attack, 0)
                self.rage = min(self.rage + self.maximum_rage // 10,
                                self.maximum_rage)
                print('{} hit {}'.format(self.name, defender.name))
                print('"{} dealt {} DMG"'.format(self.name, attack))
                print('( ಠ_ಠ)⊃o-|===>(ಠ╭╮ಠ )')

        else:
            print('{} evaded'.format(defender.name))
            print('( ÒДÓ)⊃o-|===> ε=ε=ε=┌( ^-^)ﾉ')

    def heal(self):
        ''' (Gladiator) -> NoneType

        Attacker will use their rage to recover health. Health recovered
        is 80% of the total rage.
        '''
        if self.rage > 0:
            self.health = min(self.health + int(self.rage * 0.8),
                              self.maximum_health)
            self.rage -= self.rage
            print('{} drunk a potion'.format(self.name))
            print('(* .*)=[HP^]')
        else:
            print(
                '{} attempted to drink a potion but couldn\'t stomach it\n"Rage required"'.
                format(self.name))
            print('(°Д°)')

    def rampage(self, defender):
        ''' (Gladiator, Gladiator) -> NoneType

        Attacker uses all their rage for a chance to deal 50 points
        of damage to the defender.
        '''

        if self.rage >= 100:
            attack = randint(self.damage_low, self.damage_high)
            accuracy = randint(1, 100)
            if accuracy > defender.evasion + 20:
                defender.health = max(defender.health - attack * 3, 0)
                self.rage = 0
                print(
                    '{} unleashed built-up rage, went on a rampaged and severely injured {}'.
                    format(self.name, defender.name))
                print('"{} dealt {} DMG"'.format(self.name, attack * 3))
                print("（╯°□ °）╯︵（ .o.）")
            else:
                self.rage = 0
                print(
                    '{} attempted to go on a rampage but tripped and faceplanted'.
                    format(self.name))
                print('(#;-;)')

        else:
            print(
                '{} attempted to go on a rampage but wasn\'t angry enough\n"100 Rage required"'.
                format(self.name))
            print('¯\_(o-o)_/¯')

    def is_dead(self):
        ''' (Gladiator) -> NoneType

        Checks if the Gladiator is dead.
        '''

        return self.health == 0

    def evading(self):
        ''' (Gladiator) -> NoneType

        Attacker will use 20 rage to add 10 points of evasion to their evasion stat.
        '''

        if self.rage >= 20:
            self.evasion += 10
            self.rage -= 20
            print('{} is evading'.format(self.name))
            print('ε=ε=ε=┌( o-o)ﾉ')
        else:
            print(
                '{} attempted to evade but tripped over a pebble\n"20 Rage required'.
                format(self.name))
            print('.︵ /(.□ . \)')

    def evading_reset(self):
        ''' (Gladiator) -> NoneType

        Gladiator evasion stat will reset back to base after both players' turns end.
        '''

        self.evasion = self.base_evasion

    def waiting(self):
        ''' (Gladiator) ->

        Gladiator will do nothing for their turn but will gain more rage than from attacking.
        '''

        self.rage = min(self.rage + self.maximum_rage // 5, self.maximum_rage)
        print('{} is waiting'.format(self.name))
        print('(ง-_-)ง')


class Scene():
    '''Represents all the scenes.
    '''

    def __init__(self, name):
        self.name = name

    def start_menu():
        while True:
            sleep(0.1)
            print('\n')
            sleep(0.1)
            print(
                '--------------------------------------------------------------------------'
            )
            sleep(0.1)
            print('\n')
            sleep(0.1)
            print('\n')
            sleep(0.1)
            print('  ___       _   _   _            __   _   _            _')
            sleep(0.1)
            print(
                ' | _ ) __ _| |_| |_| |___   ___ / _| | |_| |_  ___    /_\  __ _ ___ ___'
            )
            sleep(0.1)
            print(
                ' | _ \/ _` |  _|  _| / -_) / _ \  _| |  _| \' \/ -_)  / _ \/ _` / -_|_-<'
            )
            sleep(0.1)
            print(
                ' |___/\__,_|\__|\__|_\___| \___/_|    \__|_||_\___| /_/ \_\__, \___/__/'
            )
            sleep(0.1)
            print(
                '                                                          |___/'
            )
            sleep(0.1)
            print('\n')
            sleep(0.1)
            print('\n')
            sleep(0.1)
            print(
                '--------------------------------------------------------------------------'
            )
            sleep(0.1)
            print('\n')
            sleep(0.1)
            text = input('{:<37}{:>37}\n>>> '.format('1 - Start Game',
                                                     '2 - Quit Game'))
            sleep(0.1)
            print('\n')
            if text == '1':
                break

            elif text == '2':
                sleep(0.1)
                print('Quitting game...')
                sleep(2)
                print(
                    '--------------------------------------------------------------------------'
                )
                exit()

            else:
                sleep(0.1)
                print('Invalid choice')
                sleep(2)
                print('\n')
                sleep(0.1)

    def loading_screen():
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print(
            '--------------------------------------------------------------------------'
        )
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('Loading Battle of the Ages...')
        sleep(2)
        print('\n')
        sleep(0.1)
        print("                  [\\")
        sleep(0.1)
        print("                  |\)                                ____")
        sleep(0.1)
        print("                  |                               __(_   )__")
        sleep(0.1)
        print("                  Y\          ___               _(          )")
        sleep(0.1)
        print("                 T  \       __)  )--.          (     )-----`")
        sleep(0.1)
        print("                J    \   ,-(         )_         `---'")
        sleep(0.1)
        print("               Y/T`-._\ (     (       _)                 __")
        sleep(0.1)
        print("               /[|   ]|  `-(__  ___)-`  |\          ,-(  __)")
        sleep(0.1)
        print("               | |    |      (__)       J'         (     )")
        sleep(0.1)
        print("   _           | |  ] |    _           /;\          `-  '")
        sleep(0.1)
        print("  (,,)        [| |    |    L'         /;  \\")
        sleep(0.1)
        print("             /||.| /\ |   /\         /.,-._\        ___ _")
        sleep(0.1)
        print("            /_|||| || |  /  \        | |{  |       (._.'_)")
        sleep(0.1)
        print("  L/\       | \| | '` |_ _ {|        | | U |   /\\")
        sleep(0.1)
        print(" /v^v\/\   `|  Y | [  '-' '--''-''-\"-'`'   | ,`^v\ /\,`\\")
        sleep(0.1)
        print("/ ,'./  \.` |[   |       [     __   L    ] |      /^v\  \\")
        sleep(0.1)
        print(",'     `    |    |           ,`##Y.   ]    |___Y Y____,_,,_,,_")
        sleep(0.1)
        print(
            "--   -----.-(] [ |   ]     o/####U|o      ]|| /`-, Y   _   Y  Y")
        sleep(0.1)
        print("   Y Y  --;`~T   |      }   \####U|[\ _,.-(^) ,-'  _  (^)__  _")
        sleep(0.1)
        print("  Y  YY   ;'~~l  |   L     [|\###U'E'\  \ \Y-` _  (^) _Y  _")
        sleep(0.1)
        print(" Y  Y Y   ;\~~/\{| [      _,'-\`= = '.\_ ,`   (^)(^) (^) (^)")
        sleep(0.1)
        print("     --   ;\~~~/\|  _,.-'`_  `.\_..-'\"  _ . ,_ Y_ Y_ _Y  _Y__")
        sleep(0.1)
        print("    _    _; \~~( Y``   Y (^) / `,      (^)      _   (^) (^)")
        sleep(0.1)
        print("   (^)  (^)`._~ /  L \  _.Y'`  _  ` --  Y - - -(^) - Y - Y -")
        sleep(0.1)
        print("    Y    Y    `'--..,-'`      (^)   _  -    _   Y ____")
        sleep(0.1)
        print("      --           _    _ --   Y   (^)   _ (^)  ===   ----")
        sleep(0.1)
        print("          __   -  (^)  (^)      --- Y   (^) Y")
        sleep(0.1)
        print("      _            Y    Y                Y             ")
        sleep(0.1)
        print('Initializing...')
        sleep(2)

    def sign_up():
        print('\n')
        sleep(0.1)
        print(
            '--------------------------------------------------------------------------'
        )
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('\t(\ ')
        sleep(0.1)
        print('\t\\\'\\ ')
        sleep(0.1)
        print('\t \\\'\\      __________  ')
        sleep(0.1)
        print('\t / \'|    ()_________)')
        sleep(0.1)
        print('\t \\ \'/    \\  𝓢𝓘𝓖𝓝-𝓤𝓟 \\')
        sleep(0.1)
        print('\t   \\      \\ ~~~~~~~~ \\')
        sleep(0.1)
        print('\t   ==).    \\__________\\')
        sleep(0.1)
        print('\t  (__)    ()__________)')
        sleep(0.1)
        print('\n')
        sleep(0.5)

    def trophy():
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('                                  ___________')
        sleep(0.1)
        print('                             .---\'::\'        `---.')
        sleep(0.1)
        print('                            (::::::\'              )')
        sleep(0.1)
        print('                            |`-----._______.-----\'|')
        sleep(0.1)
        print('                           /￣             ::::::￣\\')
        sleep(0.1)
        print('                          / _               ::::::_ \\')
        sleep(0.1)
        print('                         / /|               ::::::|\\ \\')
        sleep(0.1)
        print('                        | | |               ::::::| | |')
        sleep(0.1)
        print('                        | | |      𝓒𝓗𝓐𝓜 𝓟𝓘𝓞𝓝 :::::| | |')
        sleep(0.1)
        print('                         \ \|    𝓞𝓕 𝓣𝓗𝓔 𝓐𝓡𝓔𝓝𝓐 ::::|/ /')
        sleep(0.1)
        print('                          \ ￣               ::::￣ /')
        sleep(0.1)
        print('                           \_              .::::::_/')
        sleep(0.1)
        print('                            |              :::::::|')
        sleep(0.1)
        print('                             \            :::::::/')
        sleep(0.1)
        print('                              `.        .:::::::\'')
        sleep(0.1)
        print('                                `-._  .:::::;-\'')
        sleep(0.1)
        print(
            '____________________________________|  """|"______________________________'
        )
        sleep(0.1)
        print('                                    |  :::|')
        sleep(0.1)
        print('                                    |   ::|')
        sleep(0.1)
        print('                                   /     ::\\ ')
        sleep(0.1)
        print('                              __.-\'      :::`-.__')
        sleep(0.1)
        print('                             (_           ::::::_)')
        sleep(0.1)
        print('                               `"""---------"""\'')
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print(
            '--------------------------------------------------------------------------'
        )
        sleep(0.1)
        print('\n')
        sleep(2)

    def credits(self, other):
        sleep(0.5)
        print('Developer:')
        sleep(0.5)
        print('Matthew Lipsey\n')
        sleep(0.5)
        print('World Artwork:')
        sleep(0.5)
        print('ASCII Art Archive\n')
        sleep(0.5)
        print('Character Artwork:')
        sleep(0.5)
        print('Unicode\n')
        sleep(0.5)
        print('Testers:')
        sleep(0.5)
        print('Henry Moore')
        sleep(0.5)
        print('Cody van der Poel\n')
        sleep(0.5)
        print('Coding Language:')
        sleep(0.5)
        print('Python\n')
        sleep(0.5)
        print('Text Editor:')
        sleep(0.5)
        print('Visual Studio Code\n')
        sleep(0.5)
        print('Special Thanks:')
        sleep(0.5)
        print('Base Camp Coding Academy')
        sleep(0.5)
        print('Player 1: {}'.format(self.name))
        sleep(0.5)
        print('Player 2: {}'.format(other.name))
        sleep(0.5)
        print('Terminals and command prompts everywhere')
        sleep(2)
        print('\n')
        sleep(0.1)
        print(
            '--------------------------------------------------------------------------'
        )
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('\t     ___________')
        sleep(0.1)
        print('\t._____l_______l_____.')
        sleep(0.1)
        print('\t||_____/  |  \_____||')
        sleep(0.1)
        print('\t      /   |   \\')
        sleep(0.1)
        print('\t     /    |    \\')
        sleep(0.1)
        print('\t    /     |     \\')
        sleep(0.1)
        print('\t   /      |      \\')
        sleep(0.1)
        print('\t  /       |       \\')
        sleep(0.1)
        print('\t /        |        \\')
        sleep(0.1)
        print('\t|         |         |')
        sleep(0.1)
        print('\t \        |        /')
        sleep(0.1)
        print('\t   \      |      /')
        sleep(0.1)
        print('\t     \    |    /')
        sleep(0.1)
        print('\t       \  |  /')
        sleep(0.1)
        print('\t         \|/')
        sleep(0.1)
        print('\t          `')
        sleep(0.1)
        print('Thanks for playing Battle of the Ages')
        sleep(2)

    def battle_announce(self, other):
        sleep(2)
        print('\n')
        sleep(0.1)
        print(
            '--------------------------------------------------------------------------'
        )
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('\t     |\                 /)')
        sleep(0.1)
        print('\t   /\_\\\__           (_//')
        sleep(0.1)
        print('\t  |   `>\-`   _._     //`)')
        sleep(0.1)
        print('\t   \ /` \\\_.-`:::`-._//')
        sleep(0.1)
        print('\t    `   |`    :::    `|')
        sleep(0.1)
        print('\t        |     :::     |')
        sleep(0.1)
        print('\t        |.....:::.....|')
        sleep(0.1)
        print('\t        |:::::::::::::|')
        sleep(0.1)
        print('\t        |     :::     |')
        sleep(0.1)
        print('\t        \     :::     /')
        sleep(0.1)
        print('\t         \    :::    /')
        sleep(0.1)
        print('\t          `-. ::: .-\'')
        sleep(0.1)
        print('\t            //\:/\\\\')
        sleep(0.1)
        print('\t           //  \'  \\\\')
        sleep(0.1)
        print('\t          |/       \\\\')
        sleep(0.1)
        print('\n')
        sleep(2)
        print('WELCOME TO THE BATTLE OF THE AGES\n'.center(50))
        sleep(2)
        print('From zero to hero, the legendary {}\n'.format(
            self.name).center(51))
        sleep(2)
        print('From unknown to famous, the all-star {}\n'.format(other.name)
              .center(51))
        sleep(2)
        print('{} vs. {}! Let the battle begin!'.format(self.name,
                                                        other.name).center(50))
        sleep(2)
        print('\n')
        sleep(0.1)
        print(
            '--------------------------------------------------------------------------\n'
        )
        sleep(1)

    def __str__(self):
        return self.name
