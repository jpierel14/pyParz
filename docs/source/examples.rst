***************************
Parallelization with PyParz
***************************

No arguments
============
		
.. code-block:: python     

  import pyParz
  import numpy as np
  import time
  indata=np.arange(0,1000,1)
  def par_func1(x):
    return(x**2)
  start = time.time()
  res=[par_func1(x) for x in indata]
  end = time.time()
  print(end - start)
  start = time.time()
  res=pyParz.foreach(indata,par_func1,args=None)
  end = time.time()

Out::
  
  Testing


With Arguments
==============  

.. code-block:: python

  import pyParz
  import numpy as np
  import time
  indata=np.arange(0,1000,1)
  indata2=1
  
  def par_func2(args):
    x,y=args
    return(x**2+y)
  start = time.time()
  res=[par_func2(x,indata2) for x in indata]
  end = time.time()
  print(end - start)
  start = time.time()
  res2=pyParz.foreach(indata,par_func2,args=[indata2])
  end = time.time()
  


Out::
  
  Test2
  