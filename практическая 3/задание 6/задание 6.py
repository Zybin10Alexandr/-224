print("Введите год")
god=int(input())
if god%4==0 and god%100!=0 and god%400!=0:
    print("да")
else:
    print("нет")
