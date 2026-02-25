import  mysql.connector

personas_db=mysql.connector.connect(host="localhost",user="root",password="Juanfiestas2",database="personas_db")

cursor = personas_db.cursor()
cursor.execute("select * from personas")
# cursor.execute ("select id edad apellido nombre from personas")
# otra forma seleccionando columnas y cambiando orden
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)