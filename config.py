import os
from app import app

#--windows config--
#app.config['SQLALCHEMY_DATABASE_URI'] = str(r'sqlite:///C://Users//kaburu//Desktop//Muguna//Flask//blog//instance//blog.db')

#--Linux config--
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(os.path.join(os.getenv('HOME'), 'Desktop/blog/instance/blog.db'))
print('sqlite:////{}'.format(os.path.join(os.getenv('HOME'), 'Desktop/blog/instance/blog.db')))

#--common--
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

