from flask import Blueprint, jsonify, request
from models import db, MMR

routes = Blueprint('routes', __name__)

@routes.route('/v1/mmr/update', methods=['POST'])
def update_mmr():
    data = request.json
    user_id = data.get('id')
    mmr_change = data.get('mmr_change')

    user = MMR.query.get(user_id)
    if not user:
        user = MMR(id=user_id)
        db.session.add(user)

    user.mmr = max(0, mmr_change)
    db.session.commit()

    return jsonify(user.to_dict()), 200

@routes.route('/v1/rank/<int:user_id>', methods=['GET'])
def get_user_rank(user_id):
    user = MMR.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user.to_dict()), 200

@routes.route('/v1/leaderboard', methods=['GET'])
def get_leaderboard():
    top_users = MMR.query.order_by(MMR.mmr.desc()).limit(10).all()
    return jsonify([user.to_dict() for user in top_users]), 200