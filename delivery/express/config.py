class Config:
    SECRET_KEY = 'asndkanskdnkajsndknasdnk'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bupt:654321@116.63.34.228:3306/delivery'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/dat'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
