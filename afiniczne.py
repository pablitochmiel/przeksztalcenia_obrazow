from PIL import Image
import numpy as np

def afiniczne(imageName):
	im = Image.open(imageName)
	imarray=np.array(im)
	#af=[[1.2, 0],[0,0.6]]
	#af=[[0.707,-0.707],[0.707,0.707]]
	#af=[[1,8],[3,5]]
	af=[[1.2,-0.7],[1.3,0.4]]
	#outshape=(round(args[0]*imarray.shape[0]),round(args[1]*imarray.shape[1]))
	#outshape=imarray.shape
	wys=[0,round(imarray.shape[1]*af[0][1]),round(imarray.shape[0]*af[0][0]),round(imarray.shape[0]*af[0][0]+imarray.shape[1]*af[0][1])]
	szer=[0,round(imarray.shape[1]*af[1][1]),round(imarray.shape[0]*af[1][0]),round(imarray.shape[0]*af[1][0]+imarray.shape[1]*af[1][1])]
	outshape=(max(wys)-min(wys),max(szer)-min(szer))
	det=float(af[0][0]*af[1][1]-af[0][1]*af[1][0])
	if(det==0):
		print("nie mozna wykonac operacji")
		return
	afin=[[af[1][1]/det,-af[0][1]/det],[-af[1][0]/det,af[0][0]/det]]
	outarray=[]
	for i in range(outshape[0]):
		temp=[]
		for j in range(outshape[1]):
			x=round(imarray.shape[0]/2+(i-outshape[0]/2)*afin[0][0]+(j-outshape[1]/2)*afin[0][1])
			y=round(imarray.shape[1]/2+(i-outshape[0]/2)*afin[1][0]+(j-outshape[1]/2)*afin[1][1])
			if(x>=imarray.shape[0] or x<0 or y>=imarray.shape[1] or y<0):
				temp.append(np.zeros_like(imarray[0,0]))
			else:
				temp.append(imarray[x,y])
		outarray.append(temp)
	outarray=np.array(outarray)
	wynik=Image.fromarray(outarray)
	wynik.save("wynik.tif")
