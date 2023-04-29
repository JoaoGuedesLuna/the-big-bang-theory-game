import os
from random import randint


class Game:

    RULES = {
        'PEDRA': ['TESOURA', 'LAGARTO'],
        'PAPEL': ['PEDRA', 'SPOCK'],
        'TESOURA': ['PAPEL', 'LAGARTO'],
        'LAGARTO': ['PAPEL', 'SPOCK'],
        'SPOCK': ['PEDRA', 'TESOURA']
    }

    VALID_OPTIONS = {
        '1': 'PEDRA',
        '2': 'PAPEL',
        '3': 'TESOURA',
        '4': 'LAGARTO',
        '5': 'SPOCK'
    }

    WIDTH = 38

    def __init__(self):
        self.playing = False
        self.user_score = 0
        self.machine_score = 0

    # Inicia o jogo
    def start(self):
        self.playing = True
        Util.clear_screen()
        self.show_rules_menu()
        while self.playing:
            self.show_dispute_menu()
        self.show_bye_bye_menu()

    # Exibe a primeira linha padrão dos menus
    def show_first_line(self):
        print(f'🌌🪐🌍 {Color.bold}THE BIG BANG THEORY GAME{Color.reset} 🌍🪐🌌\n')

    # Exibe a última linha padrão dos menus
    def show_end_line(self):
        print('\n🌌 🌌 🌌 🌌 🌌 🌌 🌌 🌌 🌌 🌌 🌌 🌌 🌌')

    # Exibe um menu onde o usuário pode visualizar as regras do jogo
    def show_rules_menu(self):
        self.show_first_line()
        print(f'{"REGRAS DO JOGO".center(self.WIDTH)}\n')
        self.draw_list(self.get_rules_list())
        print('\n' + ('-' * self.WIDTH))
        print(f'{"[Pressione ENTER]".center(self.WIDTH)}')
        print('-' * self.WIDTH)
        self.show_end_line()
        input()
        Util.clear_screen()

    # Exibe os dados de uma lista centralizando-os na tela
    def draw_list(self, any_list):
        for line in any_list:
            print(f'{line.center(self.WIDTH)}')

    # Retorna uma lista contendo as instruções das regras do jogo
    def get_rules_list(self):
        return [
            "✊ Pedra quebra Tesoura ✌️ ",
            "✊ Pedra esmaga Lagarto 🤏  ",
            "🤚 Papel envolve Pedra ✊   ",
            " 🤚 Papel desautoriza Spock 🖖",
            "✌️ Tesoura corta Papel 🤚  ",
            "   ✌️ Tesoura decapita Lagarto 🤏",
            "🤏 Lagarto devora Papel 🤚  ",
            "🤏 Lagarto envenena Spock 🖖",
            "🖖 Spock vaporiza Pedra ✊ ",
            "🖖 Spock quebra Tesoura ✌️ "
        ]

    # Exibe um menu de disputa do jogo
    def show_dispute_menu(self):
        self.show_first_line()
        print('-' * self.WIDTH)
        self.draw_scores()
        print(('-' * self.WIDTH) + '\n')
        self.draw_list(self.get_options_list())
        user_option = self.get_user_option()
        if user_option in self.VALID_OPTIONS:
            machine_option = self.get_machine_option()
            print(('-' * self.WIDTH) + '\n')
            self.show_result(self.VALID_OPTIONS[user_option], self.VALID_OPTIONS[machine_option])
            self.playing = self.continue_game()
        elif user_option.upper() == 'X':
            self.playing = False
        else:
            self.show_invalid_input_message()
            print('-' * self.WIDTH)
            input()
        Util.clear_screen()

    # Exibe a pontuação do jogador e o da máquina
    def draw_scores(self):
        print(f'🎮: {str(self.user_score).ljust(3)} | 🤖: {str(self.machine_score).ljust(3)}'.center(self.WIDTH))

    # Retorna uma lista com as opções de jogadas
    def get_options_list(self):
        return [
            "[1] - ✊ Pedra ",
            "[2] - 🤚 Papel ",
            "  [3] - ✌️ Tesoura",
            "  [4] - 🤏 Lagarto",
            "[5] - 🖖 Spock ",
            "[x] - 🔚 Sair  "
        ]

    # Retorna a jogada do usuário
    def get_user_option(self):
        print('\n' + ('-' * self.WIDTH))
        user_option = input("🎮 Jogador: ")
        return user_option

    # Retorna a jogada da máquina
    def get_machine_option(self):
        machine_option = randint(1, len(self.VALID_OPTIONS))
        print('-' * self.WIDTH)
        print(f'🤖 Máquina: {machine_option}')
        return str(machine_option)

    # Exibe o resultado da partida
    def show_result(self, user_option, machine_option):
        result = self.get_result(user_option, machine_option)
        print(f'{result.center(self.WIDTH)}\n')
        if user_option == machine_option:
            return
        for rule in self.get_rules_list():
            rule = rule.upper()
            if user_option in rule and machine_option in rule:
                print(f'{rule.center(self.WIDTH)}\n')
                return

    # Verifica qual foi o resultado da disputa e retorna uma string com o resultado
    def get_result(self, user_option, machine_option):
        if user_option == machine_option:
            return "🥉      EMPATE      🥉"
        if machine_option in self.RULES[user_option]:
            self.user_score += 1
            return "🥇    VOCÊ VENCEU    🥇"
        self.machine_score += 1
        return "🥈    VOCÊ PERDEU    🥈"

    # Retorna se o jogador deseja jogar novamente
    def continue_game(self):
        while True:
            player_input = input("Jogar novamente [s/n]? ").upper()
            if player_input == "S":
                return True
            if player_input == "N":
                return False
            self.show_invalid_input_message()

    # Exibe uma mensagem caso o jogador tenha entrado com um valor inválido
    def show_invalid_input_message(self):
        print(f'{"❌ Opção Inválida ❌".center(self.WIDTH)}')

    # Exibe o menu de despedida do jogo
    def show_bye_bye_menu(self):
        self.show_first_line()
        print(f'\n\n\n\n{"Até mais 👋".center(self.WIDTH)}\n\n\n\n')
        self.show_end_line()


# Essa classe contém atributos que representam uma cor
class Color:

    black = '\x1b[90m'
    orange = '\x1b[94m'
    cyan = '\x1b[96m'
    green = '\x1b[92m'
    magenta = '\x1b[95m'
    red = '\x1b[91m'
    white = '\x1b[97m'
    yellow = '\x1b[93m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\x1b[00m'


# Classe utilitária para métodos auxiliares à aplicação
class Util:

    # Limpa a tela do console
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


the_big_bang_theory_game = Game()
the_big_bang_theory_game.start()
