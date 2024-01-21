
import numpy

def debug_print(instance, name="Debug", first_prefix="", second_prefix="", root = None, visited = None, equality = " = "):
    if visited == None:
        visited = []
    if instance is None:
        print(first_prefix, name + equality + "None")
        return
    if instance is root:
        print(first_prefix, name + equality + "Debug tree root", '('+instance.__class__.__name__+')')
    elif instance in visited:
        print(first_prefix, name + equality + "Already visited", '('+instance.__class__.__name__+')')
    else:
        if root is None:
            root = instance
        elif not(instance in visited or instance.__class__ in (int,float,complex,str,bool)):
            ## if instance isn't in visited  and  instance is an object
            visited.append(instance)
        if instance.__class__ in (list,tuple,numpy.ndarray):
            ## FIRST VERSION
            # simple = len(repr(instance)) < 30
            ## SECOND VERSION
            simple = True
            for item in instance:
                if not type(item) in (int,float,bool):
                    simple = False
            ## --
            if simple:
                print(first_prefix, name + equality + instance.__repr__())
            else:
                print(first_prefix, name, '('+instance.__class__.__name__+')')
                for i in range(len(instance)-1):
                    debug_print(instance[i], "", second_prefix+" ╠══", second_prefix+" ║  ", root, visited, "")
                debug_print(instance[-1], "", second_prefix+" ╚══", second_prefix+"    ", root, visited, "")
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
                        debug_print(dico[key], str(key), second_prefix+" ├──", second_prefix+" │  ", root, visited)
                    debug_print(dico[keys[-1]], str(keys[-1]), second_prefix+" └──", second_prefix+"    ", root, visited)
            except:
                print(first_prefix, name + equality + instance.__repr__())


class DebugCount:
    def __init__(self, name = "Debug") -> None:
        self.value = -1
        self.name = name
    
    def incr(self, add = 1):
        self.value += add
        print(' '+self.name, self.value)
    
    def reset(self):
        self.value = -1
    
    i = property(fget=incr)



def debug(*values, name = "Debug", separator = ' ', prefix=' ', repr=True):
    print(prefix+name, end=' ')
    for val in values:
        if repr:
            print(val.__repr__(), end=separator)
        else:
            print(val, end=separator)
    print()


