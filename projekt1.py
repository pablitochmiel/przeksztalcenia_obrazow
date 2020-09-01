import fill
import afiniczne
import open
import filtr

b=input("Podaj ścierzkę do pliku: ")
a=int(input("Wybierz operację: \n1)Przekształcenie afiniczne,\n2)Filtracja odchylenia stangardowego,\n3)Otwarcie elementem kołowym,\n4)Wypełnienie dziur.\n"))
#b="onion.png"
#a=2
if(a==1):
	afiniczne.afiniczne(b)
elif(a==2):
	c=int(input("Podaj rozmiar maski: "))
	#c=3
	filtr.filtr(b,c)
elif(a==3):
	c=int(input("Podaj promień: "))
	open.open(b,c)
elif(a==4):
	fill.fill(b)
else:
	print("błędna cyferka")
