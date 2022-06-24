import pandas as pd
datos =        [["Jose",22],
                ["Jorge",24],
                ["Oscar",29],
                ["Adriana",27],
                ["Ernesto", 25],
                ["Rodrigo", 24],
                ["Fany", 25],
                ["Fernando", 28],
                ["Bryan", 23],
                ["Arturo",22]]
columnas =['Alumno','Edad']
df = pd.DataFrame(datos,columns=columnas,)
porprom = df.sort_values('Edad',ascending=False)                                                                       
porprom.head()
arx = porprom.iloc[0,:]
print ("La lista ingresada es la siguiente:")
print (df)
print()
print("El alumno con mayor edad es:")
print(arx)