##Tests for pipeline
import sys,os,traceback
import numpy as np
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import pyParz

def par_func1(x):
	return(x**2)
def par_func2(args):
	x,y=args
	return(x**2+y)
def test_pyparz():
	failed=0
	total=0
	indata=np.arange(0,1000,1)
	try:   
		total+=1 
		res=pyParz.foreach(indata,par_func1,args=None)
		print('Passed!')
	except Exception as e:
		print('Failed')
		print(traceback.format_exc())
		
		failed+=1

	try:   
		total+=1 
		indata2=1
		res=pyParz.foreach(indata,par_func2,args=[indata2])
		print('Passed!')
	except Exception as e:
		print('Failed')
		print(traceback.format_exc())
		
		failed+=1	

	print('Passed %i/%i tests.'%(total-failed,total))

	return

if __name__ == '__main__':
	test_pyparz()
