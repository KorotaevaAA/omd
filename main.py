# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print('Пошел дождь, утка идет под зонтом и встречает промокшего зайца. '
          'Заяц просится к утке под зонт. Пустить его?'
          )
    option = ''
    options_hare = {'Пустить и проводить домой': 0, 'Пустить и предложить пойти в бар': 1,
                    'Не пускать': 2}
    while option not in options_hare:
        print('Выберите: {}/{}/{}'.format(*options_hare))
        option = input()

    if options_hare[option] == 0:
        print('Утка проводила зайца, и он пригласил ее домой пить чай с печеньками.')
    elif options_hare[option] == 1:
        print('Заяц составил утке компанию, они прекрасно провели время!')
    else:
        print('Утка пришла в бар, но оказалась там одна, все испугались дождя(')

def step2_no_umbrella():
    print('Пошел дождь, утка видит кота с зонтом, но стесняется подойти. Что ей делать?')
    option = ''
    options_cat = {'Не стесняться, кот добрый': True, 'Не подходить, вдруг он кусается': False}
    while option not in options_cat:
        print('Выберите: {}/{}'.format(*options_cat))
        option = input()

    if options_cat[option]:
        print('Кот с радостью пустил утку под зонт, и они вместе пошли в бар!')
    else:
        print('Утка сильно промокла, замерзла и вернулась домой смотреть сериал и пить какао')


if __name__ == '__main__':
    step1()
