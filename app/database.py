from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./fitbuddy.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), unique=True, index=True, nullable=False)
    username = Column(String(120), nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(String(30), nullable=False)
    goal = Column(String(100), nullable=False)
    intensity = Column(String(30), nullable=False)
    original_plan = Column(Text, nullable=False)
    updated_plan = Column(Text, nullable=True)
    nutrition_tip = Column(Text, nullable=True)
    feedback = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


def save_user(user_id, username, age, weight, goal, intensity):
    db = SessionLocal()
    try:
        existing = db.query(User).filter(User.user_id == user_id).first()
        if existing:
            existing.username = username
            existing.age = age
            existing.weight = weight
            existing.goal = goal
            existing.intensity = intensity
            db.commit()
            db.refresh(existing)
            return existing
        user = User(
            user_id=user_id,
            username=username,
            age=age,
            weight=weight,
            goal=goal,
            intensity=intensity,
            original_plan="",
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()


def save_plan(user_id, plan, nutrition_tip):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            return None
        user.original_plan = plan
        user.nutrition_tip = nutrition_tip
        user.updated_plan = None
        user.feedback = None
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()


def get_user(user_id):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.user_id == user_id).first()
    finally:
        db.close()


def get_original_plan(user_id):
    user = get_user(user_id)
    return user.original_plan if user else None


def update_plan(user_id, updated_plan, feedback):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            return None
        user.updated_plan = updated_plan
        user.feedback = feedback
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()


def get_all_users():
    db = SessionLocal()
    try:
        return db.query(User).order_by(User.created_at.desc()).all()
    finally:
        db.close()


def delete_user(user_id):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
    finally:
        db.close()
