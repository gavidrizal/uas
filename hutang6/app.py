from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import Config
from models import db, Hutang
from forms import HutangForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'rizal' and password == '1234':
        return redirect(url_for('list_hutang'))
    else:
        flash('Username atau password salah. Silahkan coba lagi.')
        return redirect(url_for('index'))

@app.route('/list_hutang', methods=['GET', 'POST'])
def list_hutang():
    search_term = request.args.get('search', '')
    hutang2 = Hutang.query.filter(Hutang.kode.contains(search_term)).all()
    return render_template('list_hutang.html', hutang2=hutang2)

@app.route('/add', methods=['GET', 'POST'])
def add_hutang():
    form = HutangForm()
    if form.validate_on_submit():
        if Hutang.query.filter_by(kode=form.kode.data).first():
            flash('Kode sudah ada. Silahkan gunakan kode lain.')
            return render_template('add_hutang.html', form=form)
        
        new_hutang = Hutang(
            id=form.id.data,
            kode=form.kode.data,
            nama=form.nama.data,
            harga=form.harga.data,
            barang=form.barang.data,
            tanggal=form.tanggal.data
        )
        db.session.add(new_hutang)
        db.session.commit()
        flash('Hutang berhasil ditambahkan!')
        return redirect(url_for('list_hutang'))
    return render_template('add_hutang.html', form=form)


@app.route('/edit/<kode>', methods=['GET', 'POST'])
def edit_hutang(kode):
    hutang = Hutang.query.filter_by(kode=kode).first_or_404()
    form = HutangForm(obj=hutang)
    if form.validate_on_submit():
        form.populate_obj(hutang)
        db.session.commit()
        flash('Hutang berhasil diperbarui!')
        return redirect(url_for('list_hutang'))
    return render_template('edit_hutang.html', form=form, kode=kode)

@app.route('/delete/<kode>', methods=['POST'])
def delete_hutang(kode):
    try:
        app.logger.info(f"Attempting to delete hutang with kode {kode}")
        hutang = Hutang.query.filter_by(kode=kode).first_or_404()
        db.session.delete(hutang)
        db.session.commit()
        app.logger.info(f"Successfully deleted hutang with kode {kode}")
        return jsonify(message='Hutang berhasil dihapus!')
    except Exception as e:
        app.logger.error(f"Error deleting hutang with kode {kode}: {e}")
        return jsonify(message='Terjadi kesalahan saat menghapus hutang'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
