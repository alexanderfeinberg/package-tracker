from flask import Flask, render_template, redirect
from .config import Config
from .shipping_form import ShippingForm
from flask_migrate import Migrate
from .models import db, Package

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

def handle_db_add(data, redirect_path=None):
    db.session.add(data)
    db.session.commit()
    return redirect(redirect_path) if redirect_path else None


@app.route('/', methods=["GET", "POST"])
def index():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)


@app.route('/new_package', methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        new_package_data = form.data
        del new_package_data['csrf_token']
        del new_package_data['submit']
        new_package = Package(**new_package_data, location=new_package_data['origin'])
        Package.advance_all_locations()
        return handle_db_add(new_package, '/')
    return render_template('shipping_request.html', form=form)
