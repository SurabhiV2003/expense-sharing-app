from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Expense, Participant
from app.utils import calculate_split
from flask import render_template

api = Blueprint('api', __name__)

@api.route('/users', methods=['POST'])
def create_user():
    from app import db  # Import db here
    from app.models import User
    data = request.get_json()
    user = User(email=data['email'], name=data['name'], mobile=data['mobile'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@api.route('/expenses', methods=['POST'])
def add_expense():
    from app import db  # Import db here
    from app.models import Expense, Participant  # Import models here

    data = request.get_json()
    expense = Expense(description=data['description'], total_amount=data['total_amount'],
                      split_type=data['split_type'], created_by=data['created_by'])
    db.session.add(expense)
    participants = calculate_split(data['split_type'], data['participants'], data['total_amount'])
    for participant in participants:
        db.session.add(Participant(**participant))
    db.session.commit()
    return jsonify({"message": "Expense added successfully"}), 201

@api.route('/users/<int:user_id>/expenses', methods=['GET'])
def get_user_expenses(user_id):
    expenses = Expense.query.filter_by(created_by=user_id).all()
    return jsonify([expense.to_dict() for expense in expenses])

@api.route('/expenses/download', methods=['GET'])
def download_balance_sheet():
    # Generate a downloadable balance sheet (CSV or PDF)
    pass



@api.route('/')
def index():
    return render_template('index.html')
