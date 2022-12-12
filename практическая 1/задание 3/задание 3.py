age=int(input())
name=input()
if (age>0) and (age<75):
  if (name!='Иван'):
    if (age >= 16): 
      print('Поздравляем вы поступили в ВГУИТ')
    else:
      z=16-age
      print('Сначала нужно окончить школу. Вам осталось учиться:',z)
  else:
    print('Вас зовут Иван, вы нам не подходите')  
else:
  print('Ваш возраст вне рамок')