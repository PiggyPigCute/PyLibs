
inf = 1e+310

closed = True
opened = False


class nset:
	"""Numerical Mathematical Set"""

	def __init__(self,input_set = "empty"):

		typ = type(input_set)

		if typ == nset:
			self.values = input_set.values
			self.inters = input_set.inters
			self.all = input_set.all
			self.int_all = input_set.int_all
			self.uint_all = input_set.uint_all
			return

		self.values = set()
		self.inters = []
		self.all = False
		self.int_all = False
		self.uint_all = False
		
		if typ == list:
			a = input_set[0]
			b = input_set[1]
			if len(input_set) == 2:
				c,d = True,True
			elif len(input_set) == 3:
				c = bool(input_set[2])
				d = c
			else:
				c = bool(input_set[2])
				d = bool(input_set[3])
			if (a,b) == (-inf,inf):
				self.all = True
				return
			if a == b and c and d:
				self.values = {input_set[0]}
				return
			if a < b:
				self.inters = [(a,b,c,d)]
			return
		
		if typ == set:
			self.values = input_set
			return
		
		if typ in (int,float):
			self.values = [input_set]

		if typ == str:
			input_set = input_set.lower()

			if input_set == 'r':
				self.all = True
				return
			if input_set == 'n':
				self.uint_all = True
				return
			if input_set == 'z':
				self.int_all = True
				return

	def __repr__(self):
		
		if self.all:
			return 'ℝ'
		
		s = ''

		if self.uint_all: s += "ℕ ∪ "

		if self.int_all: s += "ℤ ∪ "

		for inter in self.inters:
			a,b,c,d = inter
			if a == -inf: a = "-∞"
			if b == inf: b = "∞"
			c = '['*c + ']'*(not(c))
			d = ']'*d + '['*(not(d))
			s += c + str(a) + '; ' + str(b) + d + ' ∪ '

		
		if self.values:
			K = list(self.values)
			K.sort()
			s += '{'
			for value in K:
				s += str(value) + '; '
			return s[:-2] + '}'
		
		if self.int_all or self.uint_all or self.inters:
			return s[:-3]
		
		return 'Ø'
	
	def __contains__(self,value):
		if self.all:
			return True
		
		if self.int_all and value % 1 == 0:
			return True
		
		elif self.uint_all and value % 1 == 0 and value >= 0:
			return True
		
		if value in self.values:
			return True
		
		for inter in self.inters:
			if inter[0] < value < inter[1]:
				return True
			if inter[0] == value and inter[2]:
				return True
			if inter[1] == value and inter[3]:
				return True

		return False
	
	def __add__(self,other):
		K = self.copy
		K += other
		return K
	
	def __iadd__(self,other):
		if type(other) != nset:
			other = nset(other)


		if self.all or other.all: return RSET

		self.int_all = self.int_all or other.int_all
		self.uint_all = not(self.int_all) and (self.uint_all or other.uint_all)

		
		for inter in other.inters:
			modification = False
			for i in range(len(self.inters)):
				if self.inters[i][1] > inter[0] or (self.inters[i][1] == inter[0] and (self.inters[i][3] or inter[2])):
					modification = True
					a = min(self.inters[i][0],inter[0])
					c = self.inters[i][2] and inter[0] != a or (self.inters[i][2] or inter[2]) and self.inters[i][0] == inter[0] or inter[2] and self.inters[i][0] != a
					last_bound, last_opening = inter[1], inter[3]
					while self.inters[i][0] <= inter[1]:
						last_bound = self.inters[i][1]
						last_opening = self.inters.pop(i)[3]
						if i == len(self.inters):
							break
					b = max(last_bound,inter[1])
					if (a,b) == (-inf,inf):
						return RSET
					d = last_opening and inter[1] != b or (last_opening or inter[3]) and last_bound == inter[1] or inter[3] and last_bound != b
					self.inters.append((a,b,c,d))
					break
			if not(modification):
				self.inters.append(inter)
		
			self.inters.sort()

		if self.int_all or self.uint_all:
			for i in range(len(self.inters)):
				if self.inters[i][2] and self.inters[i][0]%1 == 0 and not(self.uint_all and self.inters[i][0]<0):
					self.inters[i] = (self.inters[i][0],self.inters[i][1],False,self.inters[i][3])
				if self.inters[i][3] and self.inters[i][1]%1 == 0 and not(self.uint_all and self.inters[i][1]<0):
					self.inters[i] = (self.inters[i][0],self.inters[i][1],self.inters[i][2],False)


		values = []
		for val in set.union(self.values,other.values):
			if val%1 != 0 or not self.int_all and not(self.uint_all and val>=0):
				appending = True
				for i in range(len(self.inters)):
					a,b,c,d = self.inters[i]
					if a < val < b:
						appending = False
					if a == val:
						appending = False
						self.inters[i] = (a,b,True,d)
					if b == val:
						appending = False
						self.inters[i] = (a,b,c,True)
				if appending:
					values.append(val)

		self.values = set(values)

		return self
	
	def __sub__(self,other):
		K = self.copy
		K -= other
		return K
	
	def __isub__(self,other):
		if type(other) != nset:
			other = nset(other)

		# On ne peut pas soustraire par ℕ ou ℤ
		other.int_all, other.uint_all = False, False
		
		if abs(other) == 0:
			return self
		
		if other.all:
			return nset()
		
		if self.all:
			self.all = False
			self.inters.append((-inf,inf,False,False))

		
		for o_inter in other.inters:
			new_inters = []
			for i in range(len(self.inters)):
				a,b,c,d = self.inters[i]
				modif = False
				if b == o_inter[0] and d and o_inter[2]:
					d = False
					modif = True
				elif b > o_inter[0]:
					if b <= o_inter[1] and not(b == o_inter[1] and d and not(o_inter[3])):
						if a >= o_inter[0] and not(a == o_inter[0] and c and not(o_inter[2])):
							self.inters[i] = ()
						else:
							b = o_inter[0]
							d = not(o_inter[2])
							modif = True
					else:
						if a < o_inter[0] or a == o_inter[0] and c and not(o_inter[2]):
							new_a = o_inter[1]
							new_c = not(o_inter[3])
							new_inters.append((new_a,b,new_c,d))
							b = o_inter[0]
							d = not(o_inter[2])
							modif = True
						elif a <= o_inter[1] and not(a == o_inter[1] and c and not(o_inter[3])):
							a = o_inter[1]
							c = not(o_inter[3])
							modif = True
				elif a > o_inter[1]:
					break
				if modif:
					self.inters[i] = (a,b,c,d)
			i = 0
			while i < len(self.inters):
				if self.inters[i] == ():
					self.inters.pop(i)
				else:
					i += 1
			self.inters += new_inters
			self.inters.sort()

		i = 0
		while i < len(self.inters):
			a,b = self.inters[i][:2]
			if a == b:
				self.values.add(a)
				self.inters.pop(i)
			else:
				i += 1
		
		for val in other.values:
			new_inters = []
			for i in range(len(self.inters)):
				a,b,c,d = self.inters[i]
				modif = False
				if a == val and c:
					c = False
					modif = True
				elif a < val < b:
					new_inters.append((val,b,False,d))
					b = val
					d = False
					modif = True
				elif b == val and d:
					d = False
					modif = True
				if modif:
					self.inters[i] = (a,b,c,d)
			self.inters += new_inters
			self.inters.sort()
		
		
		for value in list(self.values):
			if value in other:
				self.values.remove(value)
		
		return self
	
	def __mul__(self,other):
		return self - (RSET - other)
	
	def __imul__(self,other):
		return self - (RSET - other)

	def __abs__(self):
		if self.all or self.int_all or self.uint_all or len(self.inters):
			return inf
		return len(self.values)
	
	def __eq__(self,other):
		if type(other) != nset:
			other = nset(other)
		return self.__dict__ == other.__dict__

	def __ne__(self,other):
		if type(other) != nset:
			other = nset(other)
		return self.__dict__ != other.__dict__
	
	def __list__(self):
		return len(self.values)

	def get_copy(self):
		s = nset()
		s.values = self.values.copy()
		s.inters = self.inters.copy()
		s.all = self.all
		s.int_all = self.int_all
		s.uint_all = self.uint_all
		return s

	copy = property(fget=get_copy)





RSET = nset('r')
ZSET = nset('z')
NSET = nset('n')

