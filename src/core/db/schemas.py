from sqlalchemy import Date, DateTime, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Tabla de asociación entre usuarios y proyectos
usuario_proyecto = Table('usuario_proyecto', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('proyecto_id', Integer, ForeignKey('proyectos.id'), primary_key=True)
)

# Tabla de asociación entre proyectos y herramientas
proyecto_herramienta = Table('proyecto_herramienta', Base.metadata,
    Column('proyecto_id', Integer, ForeignKey('proyectos.id'), primary_key=True),
    Column('herramienta_id', Integer, ForeignKey('herramientas.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    nombre = Column(String, nullable=False, unique=True)
    contrasena = Column(String, nullable=False)
    rol = Column(String, nullable=False)

    proyectos = relationship("Proyecto", secondary=usuario_proyecto, back_populates="usuarios")
    mensajes = relationship("Mensaje", back_populates="usuario")

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, proyectos={self.proyectos}, rol={self.rol})"

class Proyecto(Base):
    __tablename__ = 'proyectos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(String, nullable=False, default="En Proceso")
    fecha_entrega = Column(Date, nullable=False, default="2022-12-31")
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=True)

    usuarios = relationship("Usuario", secondary=usuario_proyecto, back_populates="proyectos")
    cliente = relationship("Cliente", back_populates="proyectos")
    herramientas = relationship("Herramienta", secondary=proyecto_herramienta, back_populates="proyectos")

    def __repr__(self):
        return f"Proyecto(nombre={self.nombre}, estado={self.estado}, fecha_entrega={self.fecha_entrega})"
    
    def get_all_info(self):
        return f"Nombre: {self.nombre}\nDescripción: {self.descripcion}\nEstado: {self.estado}\nFecha de Entrega: {self.fecha_entrega}\nUsuario: {self.usuario_id}\nCliente: {self.cliente}\nHerramientas: {self.herramientas}"

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    dedicacion = Column(String, nullable=False)

    proyectos = relationship("Proyecto", back_populates="cliente")

    def __repr__(self):
        return f"Cliente(nombre={self.nombre}, correo={self.correo}, telefono={self.telefono}, direccion={self.direccion}, dedicacion={self.dedicacion})"
    
    def get_all_info(self):
        return f"Nombre: {self.nombre}\nCorreo: {self.correo}\nTeléfono: {self.telefono}\nDirección: {self.direccion}\nDedicación: {self.dedicacion}"

class Herramienta(Base):
    __tablename__ = 'herramientas'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # Ejemplo: Lenguaje de Programación, Framework, Librería

    proyectos = relationship("Proyecto", secondary=proyecto_herramienta, back_populates="herramientas")

    def __repr__(self):
        return f"Herramienta(nombre={self.nombre}, tipo={self.tipo})"
    
class Mensaje(Base):
    __tablename__ = 'mensajes'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    name = Column(String, nullable=False)
    texto = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
    response = Column(String, nullable=True)

    usuario = relationship("Usuario", back_populates="mensajes")

    def __repr__(self):
        return f"Mensaje(usuario={self.usuario}, texto={self.texto}, fecha={self.fecha})"