from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()  # 实例化数据库对象，它提供访问Flask-SQLAlchemy的所有功能


class Delivery(db.Model):  # 所有模型的基类叫 db.Model，它存储在创建的SQLAlchemy实例上。
    # 定义表名
    __tablename__ = 'delivery'

    # 定义对象
    ID = db.Column(db.String(64), primary_key=True, unique=True, nullable=False)
    NAME = db.Column(db.Text, nullable=False)
    TEL = db.Column(db.String(64), nullable=False)
    Time = db.Column(db.DATETIME, nullable=False)
    Status = db.Column(db.Text, nullable=False)

    # __repr__()方法显示一个可读字符串，虽然不是完全必要，不过用于调试、测试是很不错的。
    def __repr__(self):
        return '<Role {}>'.format(self.name)
