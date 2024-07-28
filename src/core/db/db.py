from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.db.schemas import Base, Cliente, Proyecto, Usuario, Herramienta
from datetime import date
import random

# Configuración de la base de datos
engine = create_engine('sqlite:///info.db')
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Getters y setters de la base de datos

def get_user(username: str, password: str) -> Usuario:
  return session.query(Usuario).filter(Usuario.nombre == username, Usuario.contrasena == password).first()

def add_user(username: str, password: str, rol: str):
  user = Usuario(nombre=username, contrasena=password, rol=rol)
  session.add(user)
  session.commit()


def get_cliente(name: str) -> Cliente:
  return session.query(Cliente).filter(Cliente.nombre == name).first()

def add_cliente(name: str, email: str, phone: str, address: str, dedication: str):
  client = session.query(Cliente).filter(Cliente.nombre == name).first()
  if not client:
    cliente = Cliente(nombre=name, correo=email, telefono=phone, direccion=address, dedicacion=dedication)
  session.add(cliente)
  session.commit()


def get_project(name: str) -> Proyecto:
  return session.query(Proyecto).filter(Proyecto.nombre == name).first()

def add_project(name: str, description: str, state: str, user_id: int, client_id: int, feha_entrega: date):
  project = session.query(Proyecto).filter(Proyecto.nombre == name).first()
  if not project:
    project = Proyecto(nombre=name, descripcion=description, estado=state, usuario_id=user_id, cliente_id=client_id, fecha_entrega=feha_entrega)
  session.add(project)
  session.commit()


def get_tool(name: str) -> Herramienta:
  return session.query(Herramienta).filter(Herramienta.nombre == name).first()

def add_tool(name: str, type: str):
  tool = session.query(Herramienta).filter(Herramienta.nombre == name).first()
  if not tool:
    tool = Herramienta(nombre=name, tipo=type)
  session.add(tool)
  session.commit()


def get_all_users() -> list[Usuario]:
  return session.query(Usuario).all()

def get_all_clients() -> list[Cliente]:
  return session.query(Cliente).all()

def get_all_projects() -> list[str]:
  return [project.get_all_info() for project in session.query(Proyecto).all()]

def get_all_tools() -> list[Herramienta]:
  return session.query(Herramienta).all()


# Asignaciones de la base de datos

def add_user_project(user_id: int, project_id: int):
  user = session.query(Usuario).filter(Usuario.id == user_id).first()
  project = session.query(Proyecto).filter(Proyecto.id == project_id).first()
  user.proyectos.append(project)
  session.commit()

def assign_tools_to_project(project_name: str, tool_names: list):
  project = session.query(Proyecto).filter(Proyecto.nombre == project_name).first()
  tools = session.query(Herramienta).filter(Herramienta.nombre.in_(tool_names)).all()
  project.herramientas.extend(tools)
  session.commit()

def assign_time_to_project(project_name: str, time: date):
  project = session.query(Proyecto).filter(Proyecto.nombre == project_name).first()
  project.fecha_entrega = time
  session.commit()

session.close()