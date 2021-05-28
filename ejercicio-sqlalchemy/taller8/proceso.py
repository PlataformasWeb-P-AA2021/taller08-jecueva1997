from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.base import state_str
from sqlalchemy.orm.session import close_all_sessions

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Mundial

import csv

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Se abre y se lee el archivo csv con los delimitadores
with open('../data/mundial2018.csv', 'r', encoding="utf8") as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    # For para guardar los datos en la posicion que corresponde
    for row in reader:
        # print(row)
        e = Mundial(numero=row[0], fifa_display_name=row[1], countryc=row[2], \
            last_name=row[3], firs_name=row[4], shirt_name=row[5], pos=row[6], \
                height=row[7], caps=row[8], goals=row[9])
        session.add(e)

reader.close()
session.commit()


