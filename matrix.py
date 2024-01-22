from random import randint


class Matrix:

	def __init__(self,*args) -> None:
		if len(args) == 1 and isinstance(args[0],list) and len(args[0]) > 0 and isinstance(args[0][0],list): # Matrix from matrix
			# If :
			#	There is only one argument
			#	The argument is a list
			# 	This list isn't empty
			# 	This list contains lists
			dim_x = len(args[0][0])
			equal_rows = True
			for row in args[0]:
				if len(row) != dim_x:
					equal_rows = False
			if equal_rows:
				self.val = args[0].copy()
				self.dim_x = dim_x
				self.dim_y = len(args[0])
				return
		if len(args) == 1 and isinstance(args[0],Graph) and len(args[0]) > 0: # Matrix from Graph
			# If :
			#	There is only one argument
			#	The argument is a Graph
			# 	This Graph isn't empty
			self = args[0].matrix.copy
			return
		elif len(args) >= 1 and isinstance(args[0],int): # Matrix creation
			if len(args) == 1:
				dim_y, dim_x, value = args[0], args[0], 0
				value = 0
			elif len(args) == 2:
				dim_y, dim_x, value = args[0], args[1], 0
			else:
				dim_y, dim_x, value = args[0], args[1], args[2]
			if dim_x > 0 and dim_y > 0:
				val = []
				for i in range(dim_y):
					val.append([])
					for j in range(dim_x):
						val[i].append(value)
				self.val = val
				self.dim_x = dim_x
				self.dim_y = dim_y
				return
		self.val = []
		self.dim_x = 0
		self.dim_y = 0
	
	def __str__(self) -> str:
		if self.dim_y == 0:
			return "┌  ┐\n└  ┘"

		max = []
		for i in self.val[0]:
			max.append(0)
		for i in self.val:
			for j in range(0,len(i)):
				if max[j] < len(str(i[j])):
					max[j] = len(str(i[j]))
			
		S = ""
		line_size = 0
		for i in range(0,len(self.val)):
			for j in range(0,len(self.val[i])):
				element = str(self.val[i][j])
				S += element
				S += ' '*(max[j]-len(element)+1)
			if i==0:
				line_size = len(S)+1
			S += "│\n│ "

		return "┌" + " "*line_size + "┐\n│ " + S[:-2] + "└" + " "*line_size + "┘"
	
	def __repr__(self) -> str:
		if self.val == []:
			return "Matrix()"
		return "Matrix(" + self.val.__repr__() + ")"

	def get_line(self,n) -> list:
		return self.val[n]

	def get_column(self,n) -> list:
		s = []
		for i in self.val:
			s.append(i[n])
		return s

	def insert_line(self,n:int,content:list) -> None:
		self.val = self.val[0:n] + [content] + self.val[n:]
		self.dim_x += 1

	def insert_column(self,n:int,content:list) -> None:
		for i in range(0,len(self.val)):
			self.val[i] = self.val[i][0:n] + [content[i]] + self.val[i][n:]
		self.dim_y += 1

	def __getitem__(self, position:tuple[int,int]):
		return self.val[position[0]][position[1]]

	def __setitem__(self, position:tuple[int,int], value):
		self.val[position[0]][position[1]] = value

	def __add__(self,other):
		K = self.copy
		K += other
		return K
	
	def __iadd__(self,other):
		for i in range(self.dim_y):
			for j in range(self.dim_x):
				self[i,j] += other[i,j]
		return self

	def __mul__(self,other):
		K = self.copy
		K *= other
		return K

	def __imul__(self,other):
		if isinstance(other, Matrix):
			self = Matrix([[sum(self[i,k]*other[k,j] for k in range(self.dim_x)) for j in range(other.dim_x)] for i in range(self.dim_y)])
		else:
			for i in range(self.dim_y):
				for j in range(self.dim_x):
					self[i,j] *= other
		return self

	def __rmul__(self,other):
		return self*other

	def __neg__(self,other):
		K = self.copy
		K *= -1
		return K

	def __list__(self) -> list:
		return self.val

	def __len__(self) -> int:
		return self.dim_y

	def __invert__(self):
		return (1/self.det)*self.comatrix.T

	def __pow__(self,other:int):
		if other == 0: return id_mat(self.dim_y)
		if other == 2: return self*self
		if other < 0: return ~(self**-other)
		return (self**(other//2)).square*((other%2==0) + (other%2!=0)*self)

	def __eq__(self, other) -> bool:
		return isinstance(other, Matrix) and self.val == other.val
		
	def __neq__(self, other) -> bool:
		return not self == other

	def column_shear(self,i,j,value):
		self.val = (self*shear_mat(self.dim_x, i, j, value)).val
		return self
	
	def column_expand(self,i,value):
		self.val = (self*expansion_mat(self.dim_x, i, value)).val
		return self
	
	def column_permutate(self,i,j):
		self.val = (self*permutation_mat(self.dim_x, i, j)).val
		return self
	
	def line_shear(self,i,j,value):
		self.val = (shear_mat(self.dim_y, i, j, value)*self).val
		return self
	
	def line_expand(self,i,value):
		self.val = (expansion_mat(self.dim_y, i, value)*self).val
		return self
	
	def line_permutate(self,i,j):
		self.val = (permutation_mat(self.dim_y, i, j) * self).val
		return self
	
	def get_copy(self):
		copy = Matrix(self.dim_y,self.dim_x)
		for i in range(self.dim_y):
			for j in range(self.dim_x):
				copy[i,j] = self[i,j]
		return copy

	def get_dims(self):
		return (self.dim_x, self.dim_y)

	def get_square(self):
		return self*self

	def get_transpo(self):
		return Matrix([[self[j,i] for j in range(self.dim_y)] for i in range(self.dim_x)])

	def get_det(self):
		if self.dim_y == 2:
			return self[0,0]*self[1,1]-self[0,1]*self[1,0]
		S = 0
		for k in range(self.dim_y):
			sub = Matrix([[self[i,j-(j-1<k)] for j in range(1,self.dim_y)] for i in range(1,self.dim_y)])
			S += self[0,k] * sub.get_det() * (-1)**k
		return S

	def get_comatrix(self):
		return Matrix([[self[1,1],-self[1,0]],[-self[0,1],self[0,0]]]) if len(self)==2 else Matrix([[(-1)**(i+j)*Matrix([[self[ii+(ii>=i),jj+(jj>=j)] for jj in range(self.dim_x-1)] for ii in range(self.dim_y-1)]).det for j in range(self.dim_x)] for i in range(self.dim_y)])

	copy = property(fget=get_copy)
	dims = property(fget=get_dims)
	det = property(fget=get_det)
	square = property(fget=get_square)
	transpo = property(fget=get_transpo)
	T = property(fget=get_transpo)
	comatrix = property(fget=get_comatrix)


class Graph:
	"Mathematicl Graph"

	def __init__(self, verteces:list = [], matrix:Matrix|None = None) -> None:
		self.verteces = verteces
		if matrix is None or matrix.dim_y != len(verteces) or matrix.dim_x != len(verteces):
			self.matrix = Matrix(len(verteces))
		else:
			self.matrix = matrix
		
	
	def __len__(self):
		return len(self.verteces)
	
	def __repr__(self) -> str:
		if len(self) == 0:
			return "Graph()"
		s = "Graph ("
		for vertex in self.verteces:
			s += repr(vertex) + ", "
		return s[:-2] + ')'
	
	def __getitem__(self, index):
		return self.verteces[index]
	
	def __setitem__(self, index, vertex):
		self.verteces[index] = vertex
	
	def append(self, vertex):
		self.verteces.append(vertex)
	
	def edge(self, vertex1, vertex2, weight=1, directed=False):
		self.matrix[self.verteces.index(vertex1),self.verteces.index(vertex2)] += weight
		if not directed:
			self.matrix[self.verteces.index(vertex2),self.verteces.index(vertex1)] += weight






def id_mat(n:int) -> Matrix:
	"""Return the identity matrix n-sized"""
	m = Matrix(n)
	for i in range(n):
		m[i,i] = 1
	return m

def elem_mat(n:int, i:int, j:int) -> Matrix:
	"""Return the Elementary matrix (i,i) with a size of n
	
	The Elementary matrix (i,j) is the matrix filled with 0 with only a 1 at position (i,j)"""
	m = Matrix(n)
	m[i,j] = 1
	return m

def diag_mat(*args) -> Matrix:
	"""Return the diagonal matrix with given values"""
	m = Matrix(len(args))
	for i in range(len(args)):
		m[i,i] = args[i]
	return m

def line_mat(*args) -> Matrix:
	"""Return the Line matrix with given values"""
	return Matrix([list(args)])

def column_mat(*args) -> Matrix:
	"""Return the Column matrix with given values"""
	m = Matrix(len(args),1)
	for i in range(len(args)):
		m[i,0] = args[i]
	return m

def scalar_mat(n:int, value) -> Matrix:
	"""Return the diagonal matrix n-sized filled with the given value"""
	m = Matrix(n)
	for i in range(n):
		m[i,i] = value
	return m

def shear_mat(n:int,i:int,j:int,value) -> Matrix:
	"""Return the Matrix of the transvection Lᵢ ← Lᵢ + value*Lⱼ"""
	m = id_mat(n)
	m[i,j] = value
	return m

def expansion_mat(n:int,i:int,value) -> Matrix:
	"""Return the Matrix of the expansion Lᵢ ← value*Lᵢ"""
	m = id_mat(n)
	m[i,i] = value
	return m

def permutation_mat(n:int, i:int, j:int) -> Matrix:
	"""Return the Matrix of the permutation Lᵢ ←→ Lⱼ"""
	m = id_mat(n)
	m[i,j] = 1
	m[j,i] = 1
	m[i,i] = 0
	m[j,j] = 0
	return m

def rand_mat(n:int,p:int,min=0,max=9)->Matrix:
	"""Return a random matrix of size n,p filled with random integers between min and max (including both)"""
	return Matrix([[randint(min,max) for j in range(p)] for i in range(n)])

def print_mat(mat:Matrix,start="Matrix",end='\n',start_line='',line_prefix=False,dimensions=True,printed=True) -> str:
		# affiche une matrice

		if mat.val == []:
			S = "Empty Matrix" + end
			if printed: print(S)
			return S

		S = ""

		if dimensions:
			start += (" "*(start!=''))+str(mat.dim_y)+"*"+str(mat.dim_x)

		if start != '':
			S += start + '\n'

		max = []
		for i in mat.val[0]:
			max.append(0)
		for i in mat.val:
			for j in range(0,len(i)):
				if max[j] < len(str(i[j])):
					max[j] = len(str(i[j]))
			
		for i in range(0,len(mat.val)):
			if line_prefix:
				S += str(i)
			S += start_line
			for j in range(0,len(mat.val[i])):
				element = str(mat.val[i][j])
				S += element
				S += ' '*(max[j]-len(element)+1)
			S += '\n'
		S = S[:-1] + end

		if printed: print(S)
		return S


