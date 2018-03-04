DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'huajian'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flaskTest'

# 'dialect+driver://username:password@host:port/database?charset=utf8'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

# 这个会产生警告，先忽略掉
SQLALCHEMY_TRACK_MODIFICATIONS = False
