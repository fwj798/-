from flask import request
from flask import Blueprint, render_template, redirect, url_for, flash
from python.model.user import User
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from python.extensions import db, login_manager
import pymysql
from flask import jsonify

manger_bp = Blueprint('manger', __name__, url_prefix='/manger')

def get_conn():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="123456",
                           database="stat", charset='utf8',)
    return conn

@manger_bp.route('/user_manager')
def user_manager():
    return render_template('manger/user_manager.html')

@manger_bp.route('/selectallUserInfo', methods=['POST','GET'])
def selectallUserInfo():
    page = request.form.get("page")
    limit = request.form.get("limit")
    conn = get_conn()
    cursor = conn.cursor()
    sql1 = "select * from user"
    cursor.execute(sql1)
    results1 = cursor.fetchall()
    print(len(results1))

    sql2 = "select * from user limit %s,%s "
    limit = int(limit)
    page = int(page)
    start = (page-1)*limit
    print(type(start))
    print(type(limit))

    cursor.execute(sql2, (start, limit))
    results2 = cursor.fetchall()
    print(len((results2)))
    res = {}
    print(results2)
    # 转换数据格式：元组 → 字典列表
    formatted_data = [
        {
            "id": item[0],
            "username": item[1],  # 注意：此处字段名需与前端定义一致
            "email": item[2],
            "password_hash": item[3]
        }
        for item in results2
    ]
    res['data'] = formatted_data
    res['code'] = 0
    res['msg'] = ''
    res['count'] = len(results1)
    print(res)
    print(len(results2))
    return res
@manger_bp.route('/deleteUser', methods=['POST','GET'])
def deleteUser():
    try:
        user_id = request.form.get('id')
        if not user_id:
            return jsonify(success=False, message="缺少用户ID"), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify(success=False, message="用户不存在"), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify(success=True, message="删除成功") # ✅ 必须返回 success 字段

    except Exception as e:
        db.session.rollback()
        return jsonify(success=False, message="服务器错误: {str(e)}"), 500




