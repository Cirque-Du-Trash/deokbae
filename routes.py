from flask import Blueprint, jsonify, request
from models import db, MMR

routes = Blueprint('routes', __name__)

@routes.route('/v1/mmr/update', methods=['POST'])
def update_mmr():
    data = request.json
    user_id = data.get('id')
    mmr_change = data.get('mmr_change')
    
    if not isinstance(user_id, int) or not isinstance(mmr_change, int):
        return jsonify({'error': 'Invalid input: id and mmr_change must be integers.'}), 400
    try:  
        user = MMR.query.get(user_id)
        if not user:
            user = MMR(id=user_id)
            db.session.add(user)

        user.mmr = max(0, user.mmr + mmr_change)
        db.session.commit()

        return jsonify(user.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@routes.route('/v1/rank/<int:user_id>', methods=['GET'])
def get_user_rank(user_id):
    user = MMR.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user.to_dict()), 200

@routes.route('/v1/leaderboard', methods=['GET'])
def get_leaderboard():
    all_users =  MMR.query.order_by(MMR.mmr.desc()).limit(10).all()
    
    leaderboard = []
    for rank, user in enumerate(all_users, start=1):
        leaderboard.append({
            'id': user.id,
            'mmr': user.mmr,
            'rank': rank
        })
        
    return jsonify(leaderboard), 200