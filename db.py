#Importando las librerías
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Creando el engine
engine = create_engine('sqlite:///database/tareas.db',
                       connect_args={"check_same_thread":False})

#Creando la sesión
Session = sessionmaker(bind=True)
session = Session

#Creando la base
Base = declarative_base()