# coding: utf-8
# license: GPLv3
from hero import Hero
from enemies import *


def annoying_input_int(message: str = '') -> Union[Optional[float], str]:
    '''
    Function, which need to create int-type restriction on input
    from keyboard.
    :param message: user input text
    '''
    answer = None
    first_answer = input(message)
    if first_answer != Hero().lvl_up_key and first_answer not in cheat_list:
        try:
            answer = float(first_answer)
        except ValueError:
            while answer == None:
                try:
                    answer = float(input(message))
                except ValueError:
                    print('Вы ввели недопустимые символы')
    else:
        return first_answer
    return answer


def game_tournament(hero, dragon_list) -> None:
    '''
    Main process of the game. Let enemies out from there cages.
    :param hero: Hero class object. Used by the user.
    :param dragon_list: Randomly created list of enemies.
     '''
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'противник!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if answer == hero.lvl_up_key:
                hero.level_up()
                print("Теперь, введите ваш ответ:")
                answer = annoying_input_int("Ответ:")

            elif answer == dragon.cheat:
                dragon._health = -1
                print("O боже!!! Читерить очень плохо:(")
                break

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')

        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')
        print("Легчайшие 50 XP для величайшего!!")
        print("Несите следующего очередняру!!!!")
        hero._experience += 50
    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт: ', hero._experience)
        print("Ваш уровень: ", hero.level)
    else:
        print('К сожалению, Вы проиграли...  Но ничего, ждем вас снова!')


def start_game() -> None:
    '''
    Process needed for testing.
    '''

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end='')
        hero = Hero(input())
        print("ВАЖНО!!! так как автору игры 0 лет, пожалуйста вводите ответы в виде float")
        print(("Бинд для проверки возможности повысить левел: {}".format(hero.lvl_up_key)))
        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert (len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
