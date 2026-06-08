from flask import Blueprint, jsonify
from python.extensions import db
from python.model.goods import Goods

anallise_bp = Blueprint('anallise', __name__, url_prefix='/anallise')

@anallise_bp.route('/select_goods')
def select_goods():
    goods_list = db.session.query(Goods).all()
    test_goods_list = []
    for good in goods_list:
        test_goods_list.append(
            {
                'a': good.a,
                'b': good.b,
                'c': good.c
            }
        )
    return jsonify(test_goods_list)

