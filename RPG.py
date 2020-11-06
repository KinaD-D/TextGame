import random
level = 1
HP = maxHP = 25
armorend = armor = sword = kolvoheal = enemykills = gold = XP = shop = XPcount = 0 
XPneed = 15
heal = atack = 3
healing = 5
print('Изначально у вас максимум 25 HP, атака у вас 3, при атаке она колеблится от -2 до +2\nУ вас в наличии 3 пачки лечебных трав, они восстанавливают по 5 хп\nДля следующего уровня вам необходимо 15 XP\nВаша цель набрать 5 уровень и сразить босса\nдля битвы с боссом рекомендую купить в магазине броню, введя 5 и оружие введя 6\n После того как вы победили босса для завершения игры необходимо купить в магазине ,хорошее будущее, введя 10')
while level != 1000:
	shop = int(input('Хотите купить лечебные травы? 0 - нет, 1 - да, 2 - подробнее '))
	if shop == 2:
		print('Лечебные травы продаются по цене 1 к 1, если у вас не хватает денег вы получите максимум который можно купить\nСейчас у вас', gold, 'золотых монет ')
		print('Вы можете купить броню за ')
		shop = input('Хотите зайти в магазин? ( 1 - да, 0 - нет ) ')
	if shop == 1:
		kolvo = int(input('Сколько лечебных трав купить хотите? (Если хотите узнать цену и и кол-во денег читайте подробнее) '))
		gold -= 1 * kolvo
		heal += 1 * kolvo
		while gold < 0:
			gold += 1
			heal -= 1
		print('Теперь у вас', heal, 'пачек лечебных трав и', gold, 'золотых монет ')
		shop -= 1
	if shop == 5 and gold > 1000 and armor != 1:
		armor += 1
		gold -= 1000
	if shop == 6 and gold > 1000:
		atack += 9
		gold -= 1000
		sword = 1
	if shop == 10 and gold > 10000:
		print('Поздравляю, хорошее будущее вам обеспеченно')
		print('YOU WIN!!!')
		input('')
		break
	XPcount = int(input('Введите до скольки вы будете качаться? (введите XP) '))
	while XP < XPcount:
		enemyescape = 0
		print('\nУ вас', HP, 'HP')
		timetoheal = int(input('Хотите ли вы полечится? (0 - нет, 1 - да) '))
		if timetoheal == 1:
			kolvoheal = int(input('Сколько лечебных пачек трав использовать? '))
			if heal >= kolvoheal:
				HP = HP + healing * kolvoheal
				heal -= kolvoheal
				if HP > maxHP:
					print('\nВы восстановили на', HP - maxHP, 'HP больше неообходимого, теперь у вас ', maxHP, ' HP\n')
					HP = maxHP
				else:
					print('\nВы восстановили', healing * kolvoheal, ' HP, теперь у вас', HP, 'HP\n')
		print('Вам необходимо ещё', XPcount - XP, 'XP')
		a = random.randint(1, 3)

		if a == 1:
			enemy = 'Волк'
			enemyatack = 4
			enemyHP = 10
			enemyXP = 5
			enemygold = 100
			enemygoldn2 = 200
			if armor == 1:
				enemyatack -= 2
		# Тут всё связвнное с волком

		elif a == 2:
			enemy = 'Лиса'
			enemyatack = 2
			enemyHP = 5
			enemyXP = 2
			enemygold = 50
			enemygoldn2 = 100
		# Тут всё связанное с лисой

		elif a == 3:
			enemy = 'Медведь'
			enemyatack = 7
			enemyHP = 30
			enemyXP = 15
			enemygold = 300
			enemygoldn2 = 500
			if armor == 1:
				enemyatack -= 3
		# Тут всё связвнное с медведем

		if level == 5:
			enemy = 'Голем'
			enemyatack = 11
			enemyHP = 100
			enemyXP = 75
			enemygold = 10000
			enemygoldn2 = 15000
			if armor == 1:
				enemyatack -= 5
		# Тут всё связанное с боссом големом

		if a == 1 or a == 2 or a == 3:
			print('''\nВы столкнулись с врагом''', enemy, '''\nОн имеет''', enemyHP, '''HP, а так же атаку ''', enemyatack,'\n')
			if a == 3 and level < 3:
				print('\nЛучшее решение будет бежать\n')
			while enemyHP > 0:
				x = int(input('\nЧто будете делать? 1 - атаковать, 2 - лечится, 3 - бежать, 4 - бежать и досрочно закончить тренировку\n'))
				if x == 1:
					damage = random.randint(atack - 2, atack + 2)
					enemyHP -= damage
					print('\nВы нанесли', damage, 'урона, теперь у существа', enemy, ',', enemyHP, 'здоровья\n')
					if enemyHP <= 0:
						print('\nПоздравляем вы победили существо', enemy, ', вы заработали', enemyXP, 'XP!\n')
						break
				elif x == 2 and heal > 0:
					HP += healing
					if HP > maxHP:
						print('\nВы восстановили на', HP - maxHP, 'HP больше неообходимого, теперь у вас ', maxHP, ' HP\n')
						HP = maxHP
					else:
						print('\nВы восстановили', healing, ' HP, теперь у вас', HP, 'HP\n')
					input('')
					heal -= 1
				elif x == 3 or x == 4:
					input('\nВы сбежали\n')
					XP -= enemyXP
					break
				if enemyescape == 1:
					print('\nВраг сбежал\n')
					print('\nВы заработали 0 XP\n')
					break
					XP -= enemyXP
				input('\nНастал ход противника\n')
				if enemyHP > 3:
					print('\nОн решает атаковать вас\n')
					damage = random.randint(enemyatack - 2, enemyatack + 2)
					HP -= damage
					print('\nОн нанёс', damage, 'урона, теперь у вас', HP, 'HP\n')
					if HP <= 0:
						print('\nВы умерли\n')
						print('\nВаш итоговый счёт\n', level, 'Уровень', gold, 'золотых монет', XP, 'XP, а так же вы убили', enemykills, 'сушеств\n')
						input('')
				elif enemyHP > 0:
					print('\nВраг хочет сбежать, у вас есть 1 ход что бы это предотвратить\n')
					enemyescape = int(1)
			XP += enemyXP
			enemykills += 1
			if XP >= XPneed:
				atack += 2
				maxHP += 5
				level += 1
				healing += 3
				XPneed += 2.5
				XP -= XPneed
				print('\nПоздравляем, теперь у вас', level, 'уровень\n')
				print('\nТуперь у вас атака больше на 2, всего атака', atack, '\nHP увеличено на 5, всего HP', HP, '\nВаш навык лечения повышен, вы восстанавливаете теперь', healing, '\n')
				print('\nДля следующего уровня вам необходимо', XPneed, 'XP\n')
			if x != 3 and x != 4:
				goldup = random.randint(enemygold, enemygoldn2)
				gold += goldup
				print('\nВы получили', goldup, 'золотых монет, всего у вас', gold, 'золотых монет\n')
			if x == 4:
				break

print('\nВаш итоговый счёт\n', level, 'Уровень', gold, 'золотых монет', XP, 'XP, а так же вы убили', enemykills, 'сушеств\n')
input('')