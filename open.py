from PIL import Image
import numpy as np

def open(imageName, r):
	im = Image.open(imageName)
	imarray=np.array(im)
	outarray=np.empty_like(imarray)
	sr=2*r-1
	mask=np.empty((sr,sr))
	for i in range(sr):
		for j in range(sr):
			mask[i,j]=((i-r+1)**2+(j-r+1)**2)<r**2
			#if(mask[i,j]):print("*",end=" ")
			#else:print(" ",end=" ")
		#print()
	for i in range(outarray.shape[0]):#erozja
		for j in range(outarray.shape[1]):
			temp=[]
			for k in range(sr):
				for l in range(sr):
					if(i-r+1+k<0 or i-r+1+k>=outarray.shape[0] or j-r+1+l<0 or j-r+1+l>=outarray.shape[1]):
						#temp.append(0)
						#print("temp.append(0)")
						continue
					elif(mask[k,l]):
						temp.append(imarray[i+k-r+1,j+l-r+1])
						#print("temp.append(imarray[i+k-r+1,j+l-r+1]*mask[k,l])")
						#print(i,j,k,l)
			#temp.sort()
			#outarray[i,j]=temp[0]
			outarray[i,j]=min(temp)
			#print("outarray[i,j]=temp[0]")

	outarray2=np.empty_like(imarray)
	for i in range(outarray.shape[0]):#dylacja
		for j in range(outarray.shape[1]):
			temp=[]
			for k in range(sr):
				for l in range(sr):
					if(i-r+1+k<0 or i-r+1+k>=outarray.shape[0] or j-r+1+l<0 or j-r+1+l>=outarray.shape[1]):
						#temp.append(0)
						#print("temp.append(0)")
						continue
					elif(mask[k,l]):
						temp.append(outarray[i+k-r+1,j+l-r+1])
						#print("temp.append(imarray[i+k-r+1,j+l-r+1]*mask[k,l])")
						#print(i,j,k,l)
			#temp.sort()
			#outarray2[i,j]=temp[-1]
			outarray2[i,j]=max(temp)
	wynik=Image.fromarray(outarray2)
	wynik.save("wynik.tif")
