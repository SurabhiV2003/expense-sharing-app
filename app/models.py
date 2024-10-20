from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    total_amount = db.Column(db.Float, nullable=False)
    split_type = db.Column(db.String(50), nullable=False)  # equal, exact, percentage
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    participants = db.relationship('Participant', backref='expense', lazy=True)

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expense_id = db.Column(db.Integer, db.ForeignKey('expense.id'), nullable=False)
    amount_owed = db.Column(db.Float, nullable=False)
