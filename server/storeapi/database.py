import databases
from sqlalchemy import (
    REAL,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

from storeapi.config import config

metadata = MetaData()

# Tabla Ports (Puertos)
ports_table = Table(
    "Ports",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("country", String(100), nullable=False),
    Column("code", String(10), unique=True, nullable=False),
    Column("latitude", REAL),
    Column("longitude", REAL),
    Column("timezone", String(50)),
    sqlite_autoincrement=True,
)

# Tabla Vessels (Barcos)
vessels_table = Table(
    "Vessels",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("imo_number", String, unique=True),
    Column("mmsi_number", String, unique=True),
    Column("call_sign", String),
    Column("flag", String),
    Column("capacity", Integer),
    Column("built_year", Integer),
    Column("vessel_type", String),
    sqlite_autoincrement=True,
)

# Tabla Routes (Rutas)
routes_table = Table(
    "Routes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("origin_port_id", Integer, ForeignKey("Ports.id"), nullable=False),
    Column("destination_port_id", Integer, ForeignKey("Ports.id"), nullable=False),
    Column("distance", REAL),
    sqlite_autoincrement=True,
)

# Tabla Voyages (Viajes)
voyages_table = Table(
    "Voyages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("vessel_id", Integer, ForeignKey("Vessels.id"), nullable=False),
    Column("route_id", Integer, ForeignKey("Routes.id"), nullable=False),
    Column("departure_date", String),
    Column("arrival_date", String),
    Column("status", String),
    sqlite_autoincrement=True,
)

# Tabla Customers (Clientes)
customers_table = Table(
    "Customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("address", String),
    Column("phone", String),
    Column("email", String),
    Column("contact_person", String),
    sqlite_autoincrement=True,
)

# Tabla Shipments (Envíos)
shipments_table = Table(
    "Shipments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("Customers.id"), nullable=False),
    Column("booking_number", String, unique=True),
    Column("origin_port_id", Integer, ForeignKey("Ports.id"), nullable=False),
    Column("destination_port_id", Integer, ForeignKey("Ports.id"), nullable=False),
    Column("cargo_description", String),
    Column("weight", REAL),
    Column("volume", REAL),
    Column("number_of_containers", Integer),
    Column("status", String),
    sqlite_autoincrement=True,
)

# Tabla Containers (Contenedores)
containers_table = Table(
    "Containers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("container_number", String, unique=True, nullable=False),
    Column("container_type", String),
    Column("status", String),
    Column("current_location_port_id", Integer, ForeignKey("Ports.id")),
    Column("shipment_id", Integer, ForeignKey("Shipments.id")),
    Column("vessel_id", Integer, ForeignKey("Vessels.id")),
    sqlite_autoincrement=True,
)

# Tabla Employees (Empleados)
employees_table = Table(
    "Employees",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("position", String),
    Column("vessel_id", Integer, ForeignKey("Vessels.id")),
    Column("date_joined", String),
    Column("date_left", String),
    sqlite_autoincrement=True,
)

# Tabla Bookings (Reservas)
bookings_table = Table(
    "Bookings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("Customers.id"), nullable=False),
    Column("voyage_id", Integer, ForeignKey("Voyages.id"), nullable=False),
    Column("booking_number", String, unique=True),
    Column("status", String),
    Column("total_weight", REAL),
    Column("total_volume", REAL),
    Column("number_of_containers", Integer),
    sqlite_autoincrement=True,
)

# Tabla Cargo (Carga)
cargo_table = Table(
    "Cargo",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("shipment_id", Integer, ForeignKey("Shipments.id"), nullable=False),
    Column("description", String),
    Column("weight", REAL),
    Column("volume", REAL),
    Column("quantity", Integer),
    sqlite_autoincrement=True,
)

# Tabla Tracking (Seguimiento)
tracking_table = Table(
    "Tracking",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("container_id", Integer, ForeignKey("Containers.id"), nullable=False),
    Column("location", String),
    Column("timestamp", String),
    Column("status", String),
    sqlite_autoincrement=True,
)

# Tabla Invoices (Facturas)
invoices_table = Table(
    "Invoices",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("Customers.id"), nullable=False),
    Column("shipment_id", Integer, ForeignKey("Shipments.id"), nullable=False),
    Column("amount", REAL),
    Column("due_date", String),
    Column("status", String),
    sqlite_autoincrement=True,
)

# Tabla Payments (Pagos)
payments_table = Table(
    "Payments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("invoice_id", Integer, ForeignKey("Invoices.id"), nullable=False),
    Column("payment_date", String),
    Column("amount", REAL),
    Column("method", String),
    Column("reference", String),
    sqlite_autoincrement=True,
)

# Tabla Maintenance (Mantenimiento)
maintenance_table = Table(
    "Maintenance",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("vessel_id", Integer, ForeignKey("Vessels.id"), nullable=False),
    Column("description", String),
    Column("maintenance_date", String),
    Column("cost", REAL),
    sqlite_autoincrement=True,
)

# Tabla Schedules (Horarios)
schedules_table = Table(
    "Schedules",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("voyage_id", Integer, ForeignKey("Voyages.id"), nullable=False),
    Column("port_id", Integer, ForeignKey("Ports.id"), nullable=False),
    Column("arrival_date", String),
    Column("departure_date", String),
    sqlite_autoincrement=True,
)

# Tabla Users (Usuarios)
users_table = Table(
    "Users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True, nullable=False),
    Column("password", String, nullable=False),
    Column("role", String),
    Column("employee_id", Integer, ForeignKey("Employees.id")),
    sqlite_autoincrement=True,
)

# Tabla Roles (Roles)
roles_table = Table(
    "Roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True, nullable=False),
    Column("description", String),
    sqlite_autoincrement=True,
)

# Tabla RoleAssignments (Asignaciones de Roles)
role_assignments_table = Table(
    "RoleAssignments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("Users.id"), nullable=False),
    Column("role_id", Integer, ForeignKey("Roles.id"), nullable=False),
    sqlite_autoincrement=True,
)

# Tabla Notifications (Notificaciones)
notifications_table = Table(
    "Notifications",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("Users.id"), nullable=False),
    Column("message", String),
    Column("is_read", Integer, default=0),
    Column("timestamp", String),
    sqlite_autoincrement=True,
)

# Tabla Documents (Documentos)
documents_table = Table(
    "Documents",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("shipment_id", Integer, ForeignKey("Shipments.id"), nullable=False),
    Column("document_type", String),
    Column("file_path", String),
    Column("uploaded_at", String),
    sqlite_autoincrement=True,
)

# Tabla Insurance (Seguros)
insurance_table = Table(
    "Insurance",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("shipment_id", Integer, ForeignKey("Shipments.id"), nullable=False),
    Column("provider", String),
    Column("policy_number", String),
    Column("coverage_amount", REAL),
    Column("expiration_date", String),
    sqlite_autoincrement=True,
)

engine = create_engine(config.DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)

database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)
