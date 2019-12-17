# Import all the models, so that Base has them before being
# imported by Alembic
from backend.app.db.base_class import Base
from backend.app.db.models.user import User
from backend.app.db.models.item import Item
