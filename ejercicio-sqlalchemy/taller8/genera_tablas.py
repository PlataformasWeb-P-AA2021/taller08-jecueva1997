from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import CheckConstraint
from sqlalchemy.sql.sqltypes import INTEGER

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Creacion de la tabla con los atributos y el tipo de dato
class Mundial(Base):
    __tablename__ = 'mundial'
    mundial_id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    fifa_display_name = Column(String(50))
    countryc = Column(String(50))
    last_name = Column(String(50))
    firs_name = Column(String(50))
    shirt_name = Column(String(50))
    pos = Column(String(50))
    height = Column(Integer)
    caps = Column(Integer)
    goals = Column(Integer)
    
    def __repr__(self):
        return "Mundial: numero=%s\n fifa_display_name=%s\n countryc=%s\n last_name=%s\n firs_name=%s\n shirt_name=%s\n pos=%s\n height=%s\n caps=%s\n golas=%s"% (
                          self.numero, 
                          self.fifa_display_name,
                          self.countryc,
                          self.last_name,
                          self.firs_name,
                          self.shirt_name,
                          self.pos,
                          self.height,
                          self.caps,
                          self.goals)

Base.metadata.create_all(engine)