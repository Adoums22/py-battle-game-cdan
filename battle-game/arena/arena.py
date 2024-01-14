
from characters.character import Character


class Arena:

    def __init__(self, first_character: Character, second_character: Character):
        self.first_character = first_character
        self.second_character = second_character

    def fight(self):
        print("Let the battle begin!")
        round_number = 1

        while self.first_character.is_alive() and self.second_character.is_alive():
            print(f"\nRound {round_number}:")

            # Premier personnage attaque le deuxième
            self.first_character.attack(self.second_character)
            print(f"{self.first_character.name} attacks {self.second_character.name}.")
            self.print_mini_bilan()

            # Deuxième personnage attaque le premier
            if self.second_character.is_alive():  # Vérifie si le deuxième personnage est encore en vie
                self.second_character.attack(self.first_character)
                print(f"{self.second_character.name} attacks {self.first_character.name}.")
                self.print_mini_bilan()

            round_number += 1

        # Affichage du bilan final
        self.print_final_bilan()

    def print_mini_bilan(self):
        print(f"{self.first_character.name} HP: {self.first_character.get_hp()} | SHIELD: {self.first_character.get_armor()} "
              f"{self.second_character.name} HP: {self.second_character.get_hp()} | SHIELD: {self.second_character.get_armor()}")

    def print_final_bilan(self):
        if self.first_character.is_alive():
            print(f"\n{self.first_character.name} wins!")
        elif self.second_character.is_alive():
            print(f"\n{self.second_character.name} wins!")
        else:
            print("\nIt's a draw!")
