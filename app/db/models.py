from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Apartment(Base):
    __tablename__ = 'apartments'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='apartments')

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date = Column(DateTime)
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    apartment = relationship('Apartment', back_populates='events')

class ClickEvent(Base):
    __tablename__ = 'click_events'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    clicked_at = Column(DateTime, default=datetime.utcnow)
    event = relationship('Event', back_populates='click_events')

class PromoCode(Base):
    __tablename__ = 'promo_codes'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    discount = Column(Integer)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Referral(Base):
    __tablename__ = 'referrals'

    id = Column(Integer, primary_key=True)
    referrer_id = Column(Integer, ForeignKey('users.id'))
    referred_email = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    referrer = relationship('User', back_populates='referrals')

class DateRequest(Base):
    __tablename__ = 'date_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    requested_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='date_requests')

class GiveawayEntry(Base):
    __tablename__ = 'giveaway_entries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='giveaway_entries')

User.apartments = relationship('Apartment', order_by=Apartment.id, back_populates='user')
User.referrals = relationship('Referral', order_by=Referral.id, back_populates='referrer')
User.date_requests = relationship('DateRequest', order_by=DateRequest.id, back_populates='user')
User.giveaway_entries = relationship('GiveawayEntry', order_by=GiveawayEntry.id, back_populates='user')
Apartment.events = relationship('Event', order_by=Event.id, back_populates='apartment')
Event.click_events = relationship('ClickEvent', order_by=ClickEvent.id, back_populates='event')