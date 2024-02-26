
from email.mime import image
import shutil

from colorama import Fore, Style
from characters.character import Character


class Arena:

    def __init__(self, first_character: Character, second_character: Character):
        self.first_character = first_character
        self.second_character = second_character
        self.round_number = 1
    def print_centered(self, text):  
        term_width = shutil.get_terminal_size().columns  # obtenir la largeur de la console
        frame_width = term_width - 2  # largeur du cadre, moins les bords

        # imprimer le cadre supérieur
        print("\033[94m╔" + "═" * (frame_width - 8) + "╗\033[0m")

        # imprimer le texte centré avec "BattleGame" au milieu
        text_width = len(text)
        padding_width = (frame_width - text_width) // 2
        print("\033[94m║\033[0m" + " " * padding_width + text + " " * (frame_width - text_width - padding_width) + "\033[94m║\033[0m")

        # imprimer le cadre inférieur
        print("\033[94m╚" + "═" * (frame_width - 8) + "╝\033[0m")

    def fight(self):
        # Affichage du texte centré avec encadrement
        self.print_centered("\033[1mLet the Battle Begin!\033[0m")

        while self.first_character.is_alive() and self.second_character.is_alive():
            print(f"\n\033[1mRound {self.round_number}:\033[0m")  # Titre en gras

            # Premier personnage attaque le deuxième
            print(f"\033[94m{self.first_character.name}\033[0m attacks \033[95m{self.second_character.name}\033[0m.")  # Bleu pour le premier personnage, magenta pour le deuxième
            self.first_character.attack(self.second_character)

            # Vérifie si le deuxième personnage est encore en vie après l'attaque du premier
            if self.second_character.is_alive():
                print(f"\033[95m{self.second_character.name}\033[0m attacks \033[94m{self.first_character.name}\033[0m.")  # Magenta pour le deuxième personnage, bleu pour le premier
                self.second_character.attack(self.first_character)
                self.print_mini_bilan()

            self.round_number += 1

            input("Press Enter to continue...")

        # Affichage du bilan final
        self.print_final_bilan()


    def print_mini_bilan(self):

        # Titre en gras et en bleu
        title = f"--- Round Summary {self.round_number} ---"
        formatted_title = f"{Style.BRIGHT}{Fore.BLUE}{title}{Style.RESET_ALL}"
        self.print_centered(formatted_title)

        # Informations sur le premier personnage (bleu)
        print(f"{Fore.BLUE}{self.first_character.name}{Style.RESET_ALL} HP: {Fore.BLUE}{self.first_character.get_hp()}{Style.RESET_ALL} | SHIELD: {Fore.BLUE}{self.first_character.get_armor()}{Style.RESET_ALL}")


        # Informations sur le deuxième personnage (magenta)
        print(f"{Fore.MAGENTA}{self.second_character.name}{Style.RESET_ALL} HP: {Fore.MAGENTA}{self.second_character.get_hp()}{Style.RESET_ALL} | SHIELD: {Fore.MAGENTA}{self.second_character.get_armor()}{Style.RESET_ALL}")


    def print_final_bilan(self):
        if self.first_character.is_alive():
            print(f"\n\033[94m{self.first_character.name}\033[0m wins!")  # Bleu pour le premier personnage
            print(f"\033[94m{self.first_character.name}\033[0m HP: \033[94m{self.first_character.get_hp()}\033[0m | SHIELD: \033[94m{self.first_character.get_armor()}\033[0m ")
            print(f"\033[95m{self.second_character.name}\033[0m HP: \033[95m{self.second_character.get_hp()}\033[0m | SHIELD: \033[95m{self.second_character.get_armor()}\033[0m")
        elif self.second_character.is_alive():
            print(f"\n\033[91m{self.second_character.name}\033[0m wins!")  # Rouge pour le deuxième personnage
            print(f"\033[94m{self.first_character.name}\033[0m HP: \033[94m{self.first_character.get_hp()}\033[0m | SHIELD: \033[94m{self.first_character.get_armor()}\033[0m ")
            print(f"\033[95m{self.second_character.name}\033[0m HP: \033[95m{self.second_character.get_hp()}\033[0m | SHIELD: \033[95m{self.second_character.get_armor()}\033[0m")
        else:
            print("\nIt's a draw!")  # Cas d'égalité
            print(f"\033[94m{self.first_character.name}\033[0m HP: \033[94m{self.first_character.get_hp()}\033[0m | SHIELD: \033[94m{self.first_character.get_armor()}\033[0m ")
            print(f"\033[95m{self.second_character.name}\033[0m HP: \033[95m{self.second_character.get_hp()}\033[0m | SHIELD: \033[95m{self.second_character.get_armor()}\033[0m")
