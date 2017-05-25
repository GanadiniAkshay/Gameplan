from flask import Flask
from flask_wizard import Wizard

app = Flask(__name__)
wizard = Wizard(app)

if __name__ == '__main__':
	app.run()