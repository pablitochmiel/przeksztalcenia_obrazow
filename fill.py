from PIL import Image
import numpy as np

def fill(imageName):
	im = Image.open(imageName)
	imarray=np.array(im)
	inverse=np.invert(imarray)
	outarray=np.zeros_like(imarray)
	outarray[0,:]=1
	outarray[outarray.shape[0]-1,:]=1
	outarray[:,0]=1
	outarray[:,outarray.shape[1]-1]=1
	outarray2=np.zeros_like(imarray)
	while(1):
		for i in range(outarray.shape[0]):#dylacja
			for j in range(outarray.shape[1]):
				outarray2[i,j]=False
				if(inverse[i,j]):
					if(outarray[i,j]):
						outarray2[i,j]=True
						continue
					if(i-1>=0 and outarray[i-1,j]):
						outarray2[i,j]=True
						continue
					if(i+1<outarray.shape[0] and outarray[i+1,j]):
						outarray2[i,j]=True
						continue
					if(j-1>=0 and outarray[i,j-1]):
						outarray2[i,j]=True
						continue
					if(j+1<outarray.shape[1] and outarray[i,j+1]):
						outarray2[i,j]=True
						continue
		if(np.array_equal(outarray,outarray2)):break
		outarray=np.array(outarray2)
	outarray2=np.invert(outarray2)
	wynik=Image.fromarray(outarray2)
	wynik.save("wynik.tif")
