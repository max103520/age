driving = input("請問有沒有開過車:")
age =  input("請問你的年紀:")
age = int(age)
if driving == '有' :
	if age >=18 :
		print('通過測驗了')
	else:
		print('奇怪 你怎麼會有開過車')
elif driving == '沒有' :
	if age >=18 :
		print('你可以考駕照')
	else:
		print('很好')