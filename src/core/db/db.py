from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.db.schemas import Base, Cliente, Proyecto, Usuario

# Configuración de la base de datos
engine = create_engine('sqlite:///info.db')
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

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

def get_all_users() -> list[Usuario]:
  return session.query(Usuario).all()

def get_all_clients() -> list[Cliente]:
  return session.query(Cliente).all()

def get_all_projects() -> list[Proyecto]:
  return session.query(Proyecto).all()

def get_project(name: str) -> Proyecto:
  return session.query(Proyecto).filter(Proyecto.nombre == name).first()

def add_project(name: str, description: str, state: str, user_id: int, client_id: int):
  project = session.query(Proyecto).filter(Proyecto.nombre == name).first()
  if not project:
    project = Proyecto(nombre=name, descripcion=description, estado=state, usuario_id=user_id, cliente_id=client_id)
  session.add(project)
  session.commit()

def add_user_project(user_id: int, project_id: int):
  user = session.query(Usuario).filter(Usuario.id == user_id).first()
  project = session.query(Proyecto).filter(Proyecto.id == project_id).first()
  user.proyectos.append(project)
  session.commit()



session.close()