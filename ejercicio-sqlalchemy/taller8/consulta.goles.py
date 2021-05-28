from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

# Se importan las clases tanto de la base de datos como la tabla creada
from configuracion import cadena_base_datos
from genera_tablas import Mundial


engine = create_engine(cadena_base_datos)
 
Session = sessionmaker(bind=engine)
session = Session()

# Sacar todos los jugadores y ordenar por los goles
goles = session.query(Mundial).order_by(Mundial.goals).all() 

print("Presentar todos los jugadores, ordenados por el número de goles")

for i in goles:
    print("%s" % (i))
