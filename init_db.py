from app import app, db, Usuario, Sucursal, Empleado

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
    print("✅ BD inicializada con datos de prueba")