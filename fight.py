from random import random, randint
from config import get_damage, get_accuracy, get_enchant_dmg
from math import ceil

modify = ['yes', 'no']
weights = [0.33, 0.77]


def sync_fight(player_id, username, db):
    boss = randint(1, 25)

    if boss != 20:

        mp = (random() * 1)
        enchant_dm = get_enchant_dmg(db.return_config_enh(player_id))

        player_stats = [get_damage(db.return_config_sword(player_id)), get_accuracy(db.return_config_sword(player_id)), 0.05]

        enemy_stats = [randint(1, 2 * db.return_lvl(player_id)), 0.5, 0.01]

        current_dmg = (player_stats[0] + enchant_dm)

        # определяем урон, наносимый игроком и врагом
        player_damage = ceil(current_dmg * mp * player_stats[1])
        enemy_damage = ceil(enemy_stats[0] * random() * enemy_stats[1])

        # определяем, был ли сделан критический удар
        if random() < player_stats[2]:
            player_damage *= 3

        reward_lvl = randint(1, 10)
        reward_coin = randint(5, 50)
        reward_coin_lose = randint(1, 20)

        #print(f"{player_damage} - total dmg player\n{player_stats} - player stats\n{mp} - multip\n{enchant_dm} - ench dmg\n{current_dmg} - current_dmg\n")

        # сравниваем урон, наносимый игроком и врагом

        if player_damage > enemy_damage:
            db.add_lvl(player_id, reward_lvl)
            db.add_coin(player_id, reward_coin)
            return f"⚔️ {username}, вы победили в битве! У вас был урон: {player_damage}. Вы получили: {reward_lvl} лвла и {reward_coin} монет!"

        elif player_damage < enemy_damage:
            db.add_coin(player_id, reward_coin_lose)
            return f"⚔️ {username}, вы проиграли в битве! У вас был урон: {player_damage}. Вы получили: {reward_coin_lose} монет"

        else:
            db.add_coin(player_id, reward_coin)
            return f"⚔️ {username}, ничья в битве! Вы получили: {reward_coin} монет!"

    elif boss == 20:

        mp = (random() * 1)
        enchant_dm = get_enchant_dmg(db.return_config_enh(player_id))

        player_stats = [get_damage(db.return_config_sword(player_id)), get_accuracy(db.return_config_sword(player_id)),
                        0.05]

        current_dmg = (player_stats[0] + enchant_dm)

        enemy_stats = [randint(current_dmg / 2, 2 * current_dmg), 0.9, 0.01]


        # определяем урон, наносимый игроком и врагом
        player_damage = ceil(current_dmg * mp * player_stats[1])
        enemy_damage = ceil(enemy_stats[0] * random() * enemy_stats[1])

        # определяем, был ли сделан критический удар
        if random() < player_stats[2]:
            player_damage *= 3

        reward_lvl = randint(100, 250)
        reward_coin = randint(500, 2500)
        reward_coin_lose = randint(100, 500)

        # print(f"{player_damage} - total dmg player\n{player_stats} - player stats\n{mp} - multip\n{enchant_dm} - ench dmg\n{current_dmg} - current_dmg\n")

        # сравниваем урон, наносимый игроком и врагом

        if player_damage > enemy_damage:
            db.add_lvl(player_id, reward_lvl)
            db.add_coin(player_id, reward_coin)
            return f"✨⚔️ {username}, вы победили в битве с БОССОМ! У вас был урон: {player_damage}, у босса: {enemy_damage}.\n Вы получили: {reward_lvl} лвла и {reward_coin} монет!"

        elif player_damage < enemy_damage:
            db.add_coin(player_id, reward_coin_lose)
            return f"✨⚔️ {username}, вы проиграли в битве с БОССОМ! У вас был урон: {player_damage}, у босса: {enemy_damage}.\n Вы получили: {reward_coin_lose} монет"

        else:
            db.add_coin(player_id, reward_coin)
            return f"✨⚔️ {username}, ничья в битве с БОССОМ! Вы получили: {reward_coin} монет!"


