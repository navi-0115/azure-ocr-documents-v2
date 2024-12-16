from sqlalchemy import Column, Integer, String, Text, Float, Date, TIMESTAMP, JSON
from sqlalchemy.sql import func
from models.database_config import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(50), nullable=False, unique=True)
    buyer_name = Column(String(255), nullable=False)
    buyer_address = Column(Text, nullable=True)
    issue_date = Column(Date, nullable=False)
    order_id = Column(String(50), nullable=True)
    items = Column(Text, nullable=True)
    quantity = Column(Integer, nullable=True)
    unit_price = Column(Float, nullable=True)
    amount = Column(Float, nullable=True)
    subtotal = Column(Float, nullable=True)
    discount = Column(Float, nullable=True)
    shipping_cost = Column(Float, nullable=True)
    outstanding_balance = Column(Float, nullable=True)
    total_amount = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.now(), onupdate=func.now())
    # id = Column(Integer, primary_key=True, index=True)
    # buyer_name = Column(String(255), nullable=False)
    # buyer_address = Column(Text, nullable=True)
    # buyer_phone = Column(String(50), nullable=True)
    # buyer_tax_id = Column(String(50), nullable=True)
    # seller_name = Column(String(255), nullable=False)
    # seller_address = Column(Text, nullable=True)
    # seller_phone = Column(String(50), nullable=True)
    # seller_tax_id = Column(String(50), nullable=True)
    # invoice_number = Column(String(50), nullable=False, unique=True)
    # issue_date = Column(Date, nullable=False)
    # payment_method = Column(String(50), nullable=True)
    # subtotal = Column(Float, nullable=False)
    # tax_rate = Column(Float, nullable=False)
    # tax_amount = Column(Float, nullable=False)
    # total_amount = Column(Float, nullable=False)
    # total_amount_in_words = Column(Text, nullable=True)
    # remarks = Column(Text, nullable=True)
    # payee = Column(String(255), nullable=True)
    # bank_name = Column(String(255), nullable=True)
    # bank_account = Column(String(255), nullable=True)
    # items = Column(JSON, nullable=True)
    # created_at = Column(TIMESTAMP, server_default=func.now())
