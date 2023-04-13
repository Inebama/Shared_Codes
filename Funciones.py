from numpy import *
from time import *
from matplotlib.pyplot import *
from decimal import *
#-------------------------------------------------

#_______________________________________________________
#-----Sub-section-AREAS----------

#Esta funcion entrega un array con los diferenciales de una lista o un array
def dif(x):
    x=array(x)
    y=list(x[1:len(x)]-x[:len(x)-1]) #restamos los elementos n+1,n 
    y.insert(0,x[0])                 #agregamos el primer termino
    return(array(y))

def promH(x):
    x=array(x)
    y=list((x[1:len(x)]+x[:len(x)-1])/2.) #sumamos los n+1,n terminos
    y.insert(0,x[0])                      #agregamos el primero de estos
    return(array(y))

#advertencia: al elegir rango de x1,x2 asegurarse que x1>=x[0]
def area(x,y,x1,x2):    #funcion para calcular el area bajo la curva en rangos especificos 
   if x[0]<=x1:
     x,y=array(x),array(y)              
     j,k=dif(x),promH(y)   #diferrencia entre un punto y el siquiente #promedios la altura entre estos dos puntos
     h=(x<=x2)&(x>x1)      #acotamos los datos
     j,k=j[h],k[h]
     f=j*k                #obtenemos el area de cada 'rectangulo'
     return(sum(f))       #obtenemos el valor del area total 
   else:
     print('el rango debe ser mayor que el primer valor (para evitar errores de medida)')
     
     
def aumento_de_puntos(x,n=4): #donde el n representa la cantidad de veces que la cantidad de datos (-2 (los extremos)) se multiplicara por 2
      #print(len(x))  
      i=1
      while i<=n:
          X=list(promH(x))
          X.pop(0)
          x=list(x)
          for m in range(len(X)-1,-1,-1):
              x.insert(m+1,X[m])         #tendremos 2**n -1 puntos entre cada punto original
          #print(len(x))
          i+=1
      return(array(x))  

#_______________________________________________________

############################################################################################
def suav(x,n=7):  #suavizar curvas promediando datos 
    n=int(n)      #esto y las condiciones es solo para asegurarse que funcione corectamente
    x=array(x)    #requiere el paquete numpy
    if n%2==1 and n>1 and len(x)>=n:  #si el numero es impar lo consideramos como valor central +-n/2
       y=[]
       L=int((n-1)/2)                      #rango alrededor de cada elemento
       y.extend(x[:L])                     #agregamos los primeros elementos
       for i in range(L,len(x)-L):         #seleccionamos cada elemento posea elemento aledaños suficientes
           y.append(sum(x[(i-L):(i+L)])/n) #suavisamos promediando 
       y.extend(x[(len(x)-L):])            #agregamos los ultimos valores
       return(array(y))
    elif n%2==0 and n>1 and len(x)>=n: #si el numero es par tomaremos n/2 como el rango alrededor de cada valor central
       y=[]
       L=int(n/2)
       y.extend(x[:L])                         #agregamos los primeros elementos
       for i in range(L,len(x)-L):             #seleccionamos cada elemento posea elemento aledaños suficientes
           y.append(sum(x[(i-L):(i+L)])/(n+1)) #suavisamos promediando 
       y.extend(x[(len(x)-L):])                #agregamos los ultimos valores
       return(array(y)) 
    else:
       print('Revisa tus datos o el n')
############################################################################################
#entrega una fecha entrando la suma o una resta de dias con respecto a una fecha 
def Fecha(x=0,d=int(strftime("%d")),n=int(strftime("%m")),Q=int(strftime("%Y"))):  # requiere saber el dia, el mes y el year donde se parte     
    s={1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
    S=array([31,28,31,30,31,30,31,31,30,31,30,31])
    x,d,n,Q=int(x),int(d),int(n),int(Q)
    if any(array([d,n])<1) or n>12 or S[n-1]<d:
        return('Wrong Date, please enter a valid Date')
    D=x+d
    if (Q%4==0 and Q%100!=0) or Q%400==0:
       S[1]=S[1]+1
    if x>=0 and n>0 and n<13: #nos aseguramos que n sea un valor de un mes
       while n<=12:
           if D-S[n-1]>0:   
              D=D-S[n-1]
              n+=1
           else: #aqui termina el ciclo si es que D es negativo o 0
              return(str(D)+' '+s[n]+' '+str(Q)) 
       if n==13:
           return(Fecha(D-1,1,1,Q+1))
    elif x<0 and n>0 and n<13:  # esto pretende ir descontando dias a partir de una fecha
       while n>=1:
           if D<=0:
              n-=1
              D=D+S[n-1]
           else: #aqui termina el ciclo si es que D es + 
              return(str(D)+' '+s[n]+' '+str(Q)) 
       if n==0:
           return(Fecha(D-31,31,12,Q-1))

#print(Fecha(58993,17,11,1858)) #sirve por ejemplo para MJD
#24 de marzo 2020
#print(Fecha())  #entrega la fecha del dia
#sirve para aprox +- 995 years en torno a una fecha => Fecha(-363226),Fecha(363301)
################################################################################
def distancias(x,y,z): #distancias entre todos los elementos de una lista de 3 dimensiones
    if len(x)==len(y)==len(z):
       R=[]
       for i in range(0,len(x)-1):
           R.extend(list((sqrt((x[i]-x[i+1:])**2+(y[i]-y[i+1:])**2+(z[i]-z[i+1:])**2))))
       return(array(R))
################################################################################
#funcion de regresion lineal metodo minimos cuadrados y maxima verosimilitud
def Regresion_lineal(x,y,Met=None):  #Met se refiere a los metodos solo hay dos opciones
    n,x,y=len(x),array(x),array(y)
    if len(x)==len(y):
       X,Y=sum(x)/n,sum(y)/n #los respectivos promedios
       if type(Met)==type(None): #metodo de minimos cuadrados
            B2=(sum((x-X)*y))/(sum((x-X)**2))
            B1=Y-B2*X
            J=B2*x+B1
            print('La pendiente es ',B2)
            print('El coeficiente de posicion es',B1)
            V=sum((y-J)**2)/(n-2) #varianza
            print('La varianza es ',V)
            print('La desviacion estandar es',sqrt(V))
            p=sum((x-X)*(y-Y))/sqrt((sum((x-X)**2))*(sum((y-Y)**2))) 
            print('El coeficiente de correlacion es ',p)
            print('El coeficiente de determinacion es ',p**2)
            return(J) #devuelve el y(x) calculado
       elif type(Met)!=type(None): #metodo de maxima verosimilitud
            B2=(sum(x*y)-(n*X*Y))/(sum(x**2)-(n*(X**2)))
            B1=Y-B2*X
            J=B2*x+B1
            print('La pendiente es ',B2)
            print('El coeficiente de posicion es',B1)
            V=sum((y-J)**2)/(n-2) #varianza
            print('La varianza es ',V)
            print('La desviacion estandar es',sqrt(V))
            p=(sum(x*y)-(n*Y*X))/sqrt((sum(x**2)-(n*(X**2)))*(sum(y**2)-(n*(Y**2)))) 
            print('El coeficiente de correlacion es ',p)
            print('El coeficiente de determinacion es ',p**2)
            return(J) #devuelve el y(x) calculado
#################################################################################

#la funcion tiene un limite "funcional" cercano a un numero de 16 digitos (aprox 5993912977177733) (cuando este es primo, con multiplos muy altos este valor es menor), con numeros a los que puede detectar un multiplo temprano esta funcion puede calcular a mayores digitos de manera eficaz
#funcion para verificar numeros primos y si no lo son entrega los numeros que al multiplicarlos dan este numero

def primos(h,L=[],O=[],original=None):
    h=abs(int(h))
    if h>2: #En tanto el numero
      Answer=True  
      if original==None:
          globals()[getcontext().prec] = len(str(h))
          print('Esta funcion esta pensada para enteros por ende se convirtio (o mantuvo) el input al entero ',h)
          original=h
      elif original!=None:
          Answer=False  
      i=2
      l=[]
      other=[1]
      other.extend(O)
      if h%2==0:
         Answer=False
         q=h
         n=1
         while q%(i**n)==0:       #vemos la multiplicidad del numero 2 (si es que es divisor)
              other.append(i**n)
              n+=1
         if (n-1)==1:             # en caso de multiplicidad 1 solo agregamos este valor
              l.append(i)
         elif (n-1)!=1:
              l.append(str(i)+'^('+str(n-1)+')') #en caso de mayor multiplicidad aparecera el divisor x^(multiplicidad)
              #l.append(i**(n-1))                #en caso de necesitar la lista de los numeros como numeros (puesto que la linea superior entrega un string)
         q=int(Decimal(q)/Decimal(i**(n-1)))
         if q!=1:
             return(primos(q,l,other,original))
         else:
             H=1
      else:
         q=h
         H=int(h**0.5)  # Para usar la criba de Eratostenes
      i=3
      while i<=H:     # mientras el divisor sea menor que el cuadrado de nuestro numero seguiremos buscando
           if h%i==0: # Si es divisible por algun numero
              Answer=False
              while q!=1 and i<=int(q**0.5): #buscando el minimo común multiplo
                   if q%i==0 and i not in set(other):
                      n=1
                      while q%(i**n)==0:       #vemos la multiplicidad del numero que es divisor
                            other.append(i**n)
                            n+=1
                      if (n-1)==1:             # en caso de multiplicidad 1 solo agregamos este valor
                         l.append(i)
                      elif (n-1)!=1:
                         l.append(str(i)+'^('+str(n-1)+')') #en caso de mayor multiplicidad aparecera el divisor x^(multiplicidad)
                         #l.append(i**(n-1))                #en caso de necesitar la lista de los numeros como numeros (puesto que la linea superior entrega un string)
                      q=int(Decimal(q)/Decimal(i**(n-1)))                   #se divide nuestro numero para buscar mas componentes
                   i+=2
              if i>int(q**0.5) and q!=1:
                   l.append(q) 
              break
           elif h%i!=0:        #se continua buscando numeros que sean divisores de h
              i+=2
      L.extend(l)
      if q==h:
          L.append(h)
      if Answer==True:         #devuelve un valor True si es que es un primo
           return('¿'+str(original)+' es un primo? ',Answer)
      else:                    #entrega un false en caso de no ser primo y una lista con los factores que dan la cantidad h ingresada
           print('¿'+str(original)+' es un primo? ',Answer)
           print('Puede ser obtenido mediante la multiplicacion de ')
           return(L)
    elif h==2:
      Answer=True
      original=2
      return('¿'+str(original)+' es un primo? ',Answer) 
    else:
      return('necesita ser un numero mayor o igual a 2') # en caso de entregar un numero menor que 2 advertimos
