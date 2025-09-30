'''from app import app, db, Usuario, Sucursal, Empleado

with app.app_context():
    #db.drop_all()
    db.create_all()

    # Crear sucursal
    sucursal = Sucursal(nombre="Central")
    db.session.add(sucursal)

    # Crear usuario dueño
    dueno = Usuario(nombre="Dueño", email="dueno@empresa.com", rol="dueno", sucursal=sucursal)
    dueno.set_password("1234")
    db.session.add(dueno)

    # Crear empleados
    empleados = [
        ("Juan Pérez", 1),
        ("María López", 2),
        ("Carlos Sánchez", 3)
    ]
    for nombre, huella in empleados:
        db.session.add(Empleado(nombre=nombre, huella_id=huella, sucursal=sucursal))

    db.session.commit()
    print("✅ BD inicializada con datos de prueba")'''

# init_db.py
from werkzeug.security import generate_password_hash
from models import db, Usuario, Sucursal, Empleado

def inicializar_db():
    """
    Crea tablas si no existen y agrega datos de ejemplo solo si la tabla Usuario está vacía.
    Idempotente: si ya hay usuarios, no hace nada.
    """
    # crea tablas (si aún no existen)
    db.create_all()

    # si ya hay usuarios, no hacemos nada (evita borrar datos)
    if Usuario.query.first():
        return

    # crear datos de ejemplo
    sucursal = Sucursal(nombre="Central")
    db.session.add(sucursal)

    dueno = Usuario(nombre="Dueño", email="dueno@empresa.com", rol="dueno", sucursal=sucursal)
    dueno.set_password("1234")
    db.session.add(dueno)

    empleados = [
        ("Juan Pérez", 1),
        ("María López", 2),
        ("Carlos Sánchez", 3)
    ]
    for nombre, huella in empleados:
        db.session.add(Empleado(nombre=nombre, huella_id=huella, sucursal=sucursal))

    db.session.commit()
    print("✅ BD inicializada automáticamente desde init_db.py")
