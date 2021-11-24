#######################
#验证Flask+MySQL的可行性#
#######################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate
pymysql.install_as_MySQLdb()

app = Flask(__name__)

class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = ''
    database = 'sql_test'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user,password,database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# 读取配置
app.config.from_object(Config)

db = SQLAlchemy(app)
Migrate(app, db)

class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    def __init__(self, id, name):
        self.id = id
        self.name = name


if __name__ == '__main__':

    # 删除所有表
    db.drop_all()

    # 创建所有表
    db.create_all()
