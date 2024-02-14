
from numpy import ndarray

def debug_print(instance, name = "Debug", first_prefix = "", second_prefix = "", root = None, visited = None, line=0, equality = " = "):
    if visited == None:
        visited = []
    if instance is None:
        print(first_prefix, name + equality + "None")
        return
    if instance is root:
        print(first_prefix, name + equality + "Debug tree root", '('+instance.__class__.__name__+')')
        return
    visit = -1
    for obj_pos in visited:
        if instance is obj_pos[0]:
            visit = obj_pos[1]
    if visit > -1:
        print(first_prefix, name + equality + "Already visited", '('+instance.__class__.__name__+', line ' + str(visit) + ')')
    else:
        if root is None:
            root = instance
        elif not instance.__class__ in (int,float,complex,str,bool):
            ## instance is an object, then add to visited
            visited.append((instance,line))
        if instance.__class__ in (list,tuple,ndarray):
            ## FIRST VERSION
            # simple = len(repr(instance)) < 30
            ## SECOND VERSION
            simple = True
            for item in instance:
                if not type(item) in (int,float,bool):
                    simple = False
            ## --
            if simple:
                print(first_prefix, name + equality + repr(instance))
            else:
                print(first_prefix, name, '('+instance.__class__.__name__+')')
                for i in range(len(instance)-1):
                    debug_print(instance[i], "", second_prefix+" ╠══", second_prefix+" ║  ", root, visited, line+1, "")
                debug_print(instance[-1], "", second_prefix+" ╚══", second_prefix+"    ", root, visited, line+1, "")
        else:
            try:
                if isinstance(instance, dict):
                    dico = instance
                else:
                    dico = instance.__dict__
                keys = tuple(dico.keys())
                if len(keys) == 0:
                    print(first_prefix, name + equality + "Empty " + instance.__class__.__name__)
                else:
                    print(first_prefix, name, '('+instance.__class__.__name__+')')
                    for key in keys[:-1]:
                        debug_print(dico[key], str(key), second_prefix+" ├──", second_prefix+" │  ", root, visited, line+1)
                    debug_print(dico[keys[-1]], str(keys[-1]), second_prefix+" └──", second_prefix+"    ", root, visited, line+1)
            except:
                print(first_prefix, name + equality + repr(instance))


class DebugCount:
    def __init__(self, name = "Debug") -> None:
        self.value = -1
        self.name = name
    
    def __call__(self, add = 1):
        self.value += add
        print(' '+self.name, self.value)
        return self.value
    
    def reset(self):
        self.value = -1
    
    i = property(fget=__call__)



def debug(*values, name = "Debug", separator = ' ', prefix = ' ', repr=True):
    print(prefix+name, end=' ')
    for val in values:
        if repr:
            print(val.__repr__(), end=separator)
        else:
            print(val, end=separator)
    print()


