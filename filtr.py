from PIL import Image
import numpy as np

def filtr(imageName, bok):
	im = Image.open(imageName)
	imarray=np.array(im,dtype='float')
	imarray/=255
	outarray=np.zeros((imarray.shape[0],imarray.shape[1]),dtype='float')
	if(len(imarray.shape)==2):
		for i in range(outarray.shape[0]):
			for j in range(outarray.shape[1]):
				temp=[]
				for k in range(i-round((bok-1)/2),i+round((bok-1)/2)+1):
					for l in range(j-round((bok-1)/2),j+round((bok-1)/2)+1):
						if(k<0 or k>=outarray.shape[0] or l<0 or l>=outarray.shape[1]):
							#temp.append(0)
							#print"temp.append(0)")
							continue
						else:
							temp.append(imarray[k,l])
							#print("temp.append(imarray[i+k-r+1,j+l-r+1]*mask[k,l])")
							#print(i,j,k,l)
				sr=sum(temp)/len(temp)
				temp-=sr
				temp**=2
				outarray[i,j]+=(sum(temp)/len(temp))**0.5
	else:#len(shape)==3 -> RGB
		for warstwa in range(3):
			for i in range(outarray.shape[0]):
				for j in range(outarray.shape[1]):
					temp=[]
					for k in range(i-round((bok-1)/2),i+round((bok-1)/2)+1):
						for l in range(j-round((bok-1)/2),j+round((bok-1)/2)+1):
							if(k<0 or k>=outarray.shape[0] or l<0 or l>=outarray.shape[1]):
								#temp.append(0)
								#print"temp.append(0)")
								continue
							else:
								temp.append(imarray[k,l,warstwa])
								#print("temp.append(imarray[i+k-r+1,j+l-r+1]*mask[k,l])")
								#print(i,j,k,l)
					sr=sum(temp)/len(temp)
					temp-=sr
					temp**=2
					outarray[i,j]+=(sum(temp)/len(temp))**0.5
	outarray-=np.amin(outarray)
	outarray/=np.amax(outarray)
	#outarray*=255
	wynik=Image.fromarray(outarray)
	wynik.save("wynik.tif")
