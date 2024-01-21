
# Classes
class Vector:
	"""Mathematical Vector"""
	
	def __init__(self,*values):
		if len(values) == 1 and values[0].__class__ in LISTABLE_CLASSES:
			self.val = list(values[0])
		else:
			for value in values:
				assert value.__class__ in NUMBER_CLASSES, "Unsupported type in Vector initialisation "+value.__class__
			self.val = list(values)
			while len(self) > 0 and self.val[-1] == 0:
				self.val.pop()

	def __repr__(self):
		if len(self.val) == 0:
			return "Vector(0)"
		s = 'Vector('
		for i in self.val:
			s += str(i) + ', '
		return s[:-2] + ')'
	
	def __eq__(self,other):
		if other.__class__ != Vector: return False
		return self.val == other.val
	
	def __ne__(self,other):
		if other.__class__ != Vector: return True
		return self.val != other.val

	def __list__(self):
		return self.val

	def __len__(self):
		return len(self.val)
	
	def __abs__(self):
		s = 0
		for val in self.val:
			s += val**2
		return s**0.5

	def __add__(self,other):
		assert other.__class__ == Vector, "unsupported operand type(s) for +: 'Vector' and '"+other.__class__.__name__+"'"
		s = []
		for i in range(max(len(self),len(other))):
			s.append(0)
			if i < len(self): s[i] += self.val[i]
			if i < len(other): s[i] += other.val[i]
		while len(s) > 0 and s[-1] == 0:
			s.pop()
		return Vector(s)

	def __iadd__(self,other):
		assert other.__class__ == Vector, "unsupported operand type(s) for +=: 'Vector' and '"+other.__class__.__name__+"'"
		for i in range(max(len(self),len(other))):
			if i < len(other):
				self.val[i] += other.val[i]
		return self
	
	def __sub__(self,other):
		s = []
		for i in range(max(len(self),len(other))):
			s.append(0)
			if i < len(self): s[i] += self.val[i]
			if i < len(other): s[i] -= other.val[i]
		return Vector(s)
	
	def __isub__(self,other):
		assert other.__class__ == Vector, "unsupported operand type(s) for -=: 'Vector' and '"+other.__class__.__name__+"'"
		for i in range(max(len(self),len(other))):
			if i < len(other):
				self.val[i] -= other.val[i]
		return self
	
	def __mul__(self,x):
		assert x.__class__ in NUMBER_CLASSES + (Vector,), "unsupported operand type(s) for *=: 'Vector' and '"+x.__class__.__name__+"'"
		if isinstance(x, Vector): # If x is a Vector
			s = 0
			for i in range(min(len(self),len(x))):
				s += self.val[i] * x.val[i]
			return s
		else: 					  # If x is a NUMBER
			if not(x): # IF x = 0
				return(VEC0)
			s = []
			for i in range(self.dim):
				s.append(self.val[i]*x)
			return Vector(s)

	def __imul__(self,x):
		assert x.__class__ != Vector, 'Operand *= with vectors can only be used as "vector *= number". To use scalar product, use the * operand not the *= one.'
		assert x.__class__ in NUMBER_CLASSES, "unsupported operand type(s) for *=: 'Vector' and '"+x.__class__.__name__+"'"
		for i in range(self.dim):
			self.val[i] *= x
		return self
	
	def __rmul__(self,x):
		s = []
		for i in range(self.dim):
			s.append(self.val[i]*x)
		return Vector(s)
	
	def __matmul__(self,other):
		if len(self) * len(other) == 0:
			return VEC0
		assert self.dim == other.dim == 3, "Vector product needs two 3D vectors"
		a = self[1]*other[2]-self[2]*other[1]
		b = self[2]*other[0]-self[0]*other[2]
		c = self[0]*other[1]-self[1]*other[0]
		return Vector(a,b,c)

	def __imatmul__(self,other):
		self = self @ other
		return self

	def __div__(self,x):
		s = []
		for i in range(self.dim):
			s.append(self.val[i]/x)
		return Vector(s)
	
	def __idiv__(self,x):
		for i in range(self.dim):
			self.val[i] /= x
		return self

	def __pow__(self,x):
		assert x.__class__ == int, "unsupported operand type(s) for **=: 'Vector' and '"+x.__class__.__name__+"'"
		assert x in [1,2], "Vector can only be upped to 2 or 1"
		if x == 1:
			return self
		s = 0
		for val in self.val:
			s += val**2
		return s

	def __getitem__(self,i):
		return self.val[i]
	
	def __setitem__(self,i,value):
		self.val[i] = value
	
	def get_copy(self):
		return Vector(self.val)
	
	copy = property(fget=get_copy, doc="Return a copy of the instance.")
	magnitude = property(fget=__abs__, doc="Return the magnitude of the vector.")
	dim = property(fget=__len__, doc="Return the dimension of the vector")


class Point:
	"""Mathematical Point"""
	
	def __init__(self,*values):
		if len(values) == 1 and values[0].__class__ in LISTABLE_CLASSES:
			self.val = list(values[0])
		else:
			for value in values:
				assert value.__class__ in NUMBER_CLASSES, "Unsupported type in Vector initialisation "+value.__class__
			self.val = list(values)

	def __str__(self):
		s = '('
		for i in self.val:
			s += str(i) + ' ; '
		return s[:-3] + ')'

	def __repr__(self):
		s = 'Point('
		for i in self.val:
			s += str(i) + ', '
		return s[:-2] + ')'
	
	def __eq__(self,other):
		if other.__class__ != Vector: return False
		return self.val == other.val
	
	def __ne__(self,other):
		if other.__class__ != Vector: return True
		return self.val != other.val

	def __list__(self):
		return self.val

	def __len__(self):
		return len(self.val)
	
	def __sub__(self,other):
		assert other.__class__ == Vector, "unsupported operand type(s) for -: 'Point' and '"+other.__class__.__name__+"'"
		assert self.dim == other.dim, "Points substraction needs two point with the same dimension"
		s = []
		for i in range(self.dim):
			s.append(self.val[i]-other.val[i])
		return Vector(s)
	
	# def translate(self, vecotr:Vector):
	# 	assert self.dim == vecotr.dim, "Point translation needs a vector with same"

	def __getitem__(self,i):
		return self.val[i]
	
	def __setitem__(self,i,value):
		self.val[i] = value
	
	def get_copy(self):
		return Vector(self.val)
	
	def get_is_zero(self):
		return len(self.val) == 0
	
	copy = property(fget=get_copy, doc="Return a copy of the instance.")
	dim = property(fget=__len__, doc="Return the dimension of the point")
	is_zero = property(fget=get_is_zero, doc="Return True if the coordinates of the points are null")



# Consts
LISTABLE_CLASSES = (list, tuple, set, Vector, Point)
NUMBER_CLASSES = (int,float,bool,complex)
POINT0 = Point()
VEC0 = Vector(0)
