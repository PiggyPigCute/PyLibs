

class poly:
    def __init__(self, *args):
        self.coeff = args[0] if len(args) == 1 and isinstance(args[0], list) else list(args)
    
    def __call__(self, value):
        return sum([self[i]*value**i for i in range(len(self))])
    
    def __str__(self) -> str:
        return (len(self)!=0)*''.join([(self[i] != 0)*(str(self[i])*(self[i]!=1 or i==0) + (i!=0)*('X' + (i!=1)*''.join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[int(n)] for n in str(i)])) + " + ") for i in range(len(self)-1, -1, -1)])[:-3]+(len(self)==0)*'0'
    
    def __repr__(self) -> str:
        return "poly(" + ','.join(str(i) for i in self.coeff) + ")"

    def __getitem__(self, i:int|slice):
        return (0 if i >= len(self) else self.coeff[i]) if isinstance(i, int) else self.coeff[i.start:min(len(self),0 if i.stop==None else i.stop)]+(i.stop==None or i.stop>=len(self))*([0 for i in range((len(self) if i.stop==None else i.stop)-max(len(self),i.start))])
    
    def __setitem__(self, i, coeff):
        while i >= len(self): self.coeff.append(0)
        self.coeff[i] = coeff
        return self
    
    def __len__(self) -> int:
        while self.coeff[-1] == 0: self.coeff.pop()
        return len(self.coeff)
    
    def __add__(self, other):
        return poly([self[i]+other[i] for i in range(max(len(self),len(other)))]) if isinstance(other,poly) else poly([self[0]+other]+self[1:len(self)]) # type: ignore
    
    def __iadd__(self, other):
        self.coeff = [self[i]+other[i] for i in range(len(self))]

    def __radd__(self, other):
        return self+other

    def __mul__(self, other):
        return poly([sum([self[k]*other[i-k] for k in range(i+1)]) for i in range(max(len(self), len(other))+1)]) if isinstance(other, poly) else poly([other*coeff for coeff in self.coeff])
    
    def __imul__(self, other):
        self.coeff = (self*other).coeff
    
    def __rmul__(self, other):
        return self*other
    
    def __pow__(self, other:int):
        return (poly(1),self.copy,self*self)[other] if other<=2 else (self**((other-1)//2))**2*((other%2==0) + (other%2!=0)*self)
    
    def __eq__(self, other) -> bool:
        return self.coeff == other.coeff
    
    def __neq__(self, other) -> bool:
        return not self == other

    def get_deg(self) -> int|float:
        return len(self)-1 if len(self)>0 else float('-inf')
    
    def get_max(self):
        return self[self.deg]
    
    def get_copy(self):
        return poly(self.coeff.copy())

    deg = property(get_deg)
    max = property(get_max)
    copy = property(get_copy)


X = poly(0,1)
X2 = poly(0,0,1)
X3 = poly(0,0,0,1)