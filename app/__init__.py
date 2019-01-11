import os

from flask import Flask, render_template

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE = os.path.join(app.instance_path, 'app.sqlite')
	)
	
	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)
		
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	@app.route('/')
	def index():
		return render_template('index.html')
		
	from . import db
	db.init_app(app)
	
	from . import blog
	app.register_blueprint(blog.bp)
		
	return app