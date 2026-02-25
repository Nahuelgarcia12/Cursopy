import  mysql.connector

personas_db=mysql.connector.connect(host="localhost",user="root",password="Juanfiestas2",database="personas_db")
cursor = personas_db.cursor()
sentencia_sql = ('INSERT INTO personas(nombre, apellido, edad) '
                 'VALUES(%s, %s, %s)')
valores = ('Victor', 'Ramos', 46),('Nahuel','Garcia',23)
cursor.executemany(sentencia_sql, valores) #multiples ingresos
#cursor.execute(sentencia_sql, valores) un registro solo
personas_db.commit()  # guardar los cambios en la bd
personas_db.close()