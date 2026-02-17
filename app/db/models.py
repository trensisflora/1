from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    apartments = relationship('Apartment', back_populates='owner')
    events = relationship('Event', back_populates='host')
    referrals = relationship('Referral', back_populates='referrer')

class Apartment(Base):
    __tablename__ = 'apartments'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='apartments')

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    host_id = Column(Integer, ForeignKey('users.id'))
    apartment = relationship('Apartment')
    host = relationship('User', back_populates='events')

class ClickEvent(Base):
    __tablename__ = 'click_events'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    timestamp = Column(DateTime, nullable=False)
    event = relationship('Event')

class PromoCode(Base):
    __tablename__ = 'promo_codes'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    discount = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

class Referral(Base):
    __tablename__ = 'referrals'

    id = Column(Integer, primary_key=True)
    referrer_id = Column(Integer, ForeignKey('users.id'))
    code = Column(String, unique=True, nullable=False)
    referrer = relationship('User', back_populates='referrals')

class DateRequest(Base):
    __tablename__ = 'date_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    requested_date = Column(DateTime, nullable=False)

class GiveawayEntry(Base):
    __tablename__ = 'giveaway_entries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))
    entered_at = Column(DateTime, nullable=False)