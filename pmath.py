

def id_fun(x):
	return x

def psum(a=0,b=id_fun,c=id_fun):

	if isinstance(b,int):
		if a > b:
			return 0
		
		S = 0
		for i in range(a,b+1):
			S += c(i)
		return S
	
	if a < 1:
		return 0
	
	S = 0
	for i in range(0,a+1):
		S += b(i)
	return S

	

def pprod(a=1,b=id_fun,c=id_fun):

	if isinstance(b,int):
		if a > b:
			return 1
			
		P = 1
		for i in range(a,b+1):
			P *= c(i)
		return P
	
	if a < 1:
		return 1
	
	P = 1
	for i in range(1,a+1):
		P *= b(i)
	return P



