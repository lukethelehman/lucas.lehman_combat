import tbc

def main():
    hero = tbc.character("Hero", 10, 50, 5, 2)
    monster = tbc.character("Monster", 10, 50, 5, 2)

    hero.printStats()
    monster.printStats()

    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()