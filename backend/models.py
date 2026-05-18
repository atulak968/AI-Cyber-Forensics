from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from database import Base

# -------------------------
# ANALYSIS TABLE
# -------------------------

class Analysis(Base):

    __tablename__ = "analyses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    input_text = Column(String)

    prediction = Column(String)

    confidence = Column(Float)

    analysis_type = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )