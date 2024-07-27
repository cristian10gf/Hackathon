from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Tabla de asociación
usuario_proyecto = Table('usuario_proyecto', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('proyecto_id', Integer, ForeignKey('proyectos.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    nombre = Column(String, nullable=False, unique=True)
    contrasena = Column(String, nullable=False)
    rol = Column(String, nullable=False)

    proyectos = relationship("Proyecto", secondary=usuario_proyecto, back_populates="usuarios")

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, proyectos={self.proyectos}, rol={self.rol})"

class Proyecto(Base):
    __tablename__ = 'proyectos'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

    usuarios = relationship("Usuario", secondary=usuario_proyecto, back_populates="proyectos")
    cliente = relationship("Cliente", back_populates="proyectos")

    def __repr__(self):
        return f"Proyecto(nombre={self.nombre}, estado={self.estado})"
    
    def get_all_info(self):
        return f"Nombre: {self.nombre}\nDescripción: {self.descripcion}\nEstado: {self.estado}\nUsuario: {self.usuario_id}\nCliente: {self.cliente_id}"

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
