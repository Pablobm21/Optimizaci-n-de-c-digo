class Optimizar:
    array= []
    
    def inp(self):
        print("Introduce un número:")
        return int(input())
    def add(self,n):
        self.array.append(n)

    def media(self):
        suma=0
        for i in self.array:
            suma+=i
        print(suma/len(self.array))
        return suma/len(self.array)