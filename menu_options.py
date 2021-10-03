from PrintStyles import PrintStyles as ps


def title(title:str):
    print(f'\n{ps.BYELLOW}{ps.UNDERLINE}{title}{ps.RESET}\n')


def load_menu(options: list, utterance: str = 'Choose:',count_with_zero: bool = False):
    show_utterance(utterance)
    options_range = show_options(options, count_with_zero)
    option = int(input(f'{ps.VIOLET}Enter the number of the option you want: {ps.RESET}'))
    valid_option(option, options_range)
    return option


def show_utterance(utterance: str = 'Choose:'):
    print(f'{ps.VIOLET}{utterance}{ps.RESET}')


def show_options(options: list, count_with_zero: bool = False):
    c = 0 if count_with_zero else 1
    for i in range(len(options)+c):
        print(f'{ps.CYAN}{i+c:2}. {ps.BLUE}{options[i]}')
    options_range = (c,len(options)+c)
    return options_range


def valid_option(option: int, options_range: tuple):
    if option<options_range[0] or option>options_range[1]:
        raise ValueError('Invalid Option/Operation!')


def end_program(text: str = 'END OF THE PROGRAM...'):
    print(f'{ps.BWHITE_REDBG}{text}{ps.RESET}')