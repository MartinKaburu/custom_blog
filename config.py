import os
from app import app

#db path
#path = os.path.join(os.getenv('HOME'),'blog/instance/blog.db')
#path = r'sqlite://C:/Users/kaburu/Desktop/Muguna/Flask/blog/instance/blog.db'
#database_path = os.path.abspath('blog.db')
#database_path = r'sqlite://{}'.format(database_path)
app.config['SQLALCHEMY_DATABASE_URI'] = str(r'sqlite:///C://Users//kaburu//Desktop//Muguna//Flask//blog//instance//blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

