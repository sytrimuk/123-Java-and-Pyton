try:
	years_old = int(input('Введите ваше полное количество лет:\n'))
	print('\nПоздравляем! Вы прожили более', years_old * (365 * 24), 'часов')
	input()
except ValueError:
	print('\nОшибка! Вы ввели не число. Перезапустите программу и попробуйте ещё раз.')
	input()