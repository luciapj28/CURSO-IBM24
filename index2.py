#Se genera una lista de 100 millones de números aleatorios

x=list(np.random.randint(low=1,high=500000, size=99999999))
#Complejidad constante O(k)

def constante(x:list) -> list:
    return x
constante(x)
