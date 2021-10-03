from PrintStyles import PrintStyles as ps
from matrix import Matrix, read_matrix
from menu_options import title, load_menu, end_program


def choice_option(option=int):
    a = read_matrix('A')
    b = None
    options = [lambda: a + b, lambda: a - b, lambda: a @ b, lambda: a * b, lambda: ~a, lambda: a.transpose, lambda: -a, lambda: a.diagonal, lambda: a.lower_triangular, lambda: a.upper_triangular, lambda: show_matrix_characteristics(a), lambda: a.determinant, lambda: a.sparse]
    if option == 4:
        b = float(input('Enter the number you want to multiply the matrix: '))
    elif option < 4:
        b = read_matrix('B')
    print(f'{ps.BOLD}Result:{ps.RESET}')
    print(options[option-1]())


def show_matrix_characteristics(matrix: Matrix):
    '''Shows the matrix characteristics'''
    characteristics = matrix.characteristics
    if True not in characteristics.values():
        r = f'{ps.YELLOW}this matrix has no special features!{ps.RESET}'
    else:
        r = ''
        for key, value in characteristics.items():
            if value:
                r += f"{ps.GREEN}It's a {key} matrix!{ps.RESET}\n"
    r += f'{ps.BGREEN}Sparsity: {ps.RESET}{ps.IGREEN}{matrix.sparsity:.2f}{ps.RESET}\n'
    r += f'{ps.BGREEN}Dimension: {ps.RESET}{ps.IGREEN}{matrix.dimension[0]} X {matrix.dimension[1]}{ps.RESET}'
    return r


if __name__ == '__main__':
    title('Matrix Calculator')
    while True:
        options = ['End the program', 'Addition between matrices', 'Subtraction between matrices', 'Multiplication between matrices', 'Matrix multiplication by scalar', 'Calculate inverse matrix', 'Calculate transposed matrix', 'Calculate opposite matrix', 'Calculate diagonal matrix', 'Calculate lower triangular matrix', 'Calculate upper triangular matrix', 'Show matrix characteristics', 'Calculate determinant', 'Calculate sparse matrix representation']
        option = load_menu(options,count_with_zero=True)
        if option == 0:
            break
        else:
            choice_option(option)
        input('Press enter to continue...\n')
    end_program()
