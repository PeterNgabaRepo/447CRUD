from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('grades', __name__)

@bp.route('/')
def index():
	db = get_db()
	grades = db.execute(
		'SELECT id, name, points'
		' FROM grades g'
		' ORDER BY id DESC'
		).fetchall()
	return render_template('grades/index.html', grades = grades)


@bp.route('/create', methods=('GET', 'POST'))
def create():
	id = None
	error = None

	if request.method == 'POST':
		id = request.form['id']
		name = request.form['name']
		points = request.form['points']
		error = None

	if not id:
		error = 'Id is required.'

	if error is not None:
		flash(error)
	else:
		db = get_db()
		db.execute(
		'INSERT INTO grades (name, id, points)'
		' VALUES (?, ?, ?)',
		(name, id, points)
		)
		db.commit()
		return redirect(url_for('grades.index'))

	return render_template('grades/create.html')

def get_grades(id):
	grades = get_db().execute(
		'SELECT id, name, points'
		' FROM grades g'
		' WHERE id = ?',
		(id,)
		).fetchone()

	if grades is None:
		abort(404, f"Grades id {id} doesn't exist.")
	
	return grades


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
	grades = get_grades(id)
	error = None

	if request.method == 'POST':
		name = request.form['name']
		points = request.form['points']
		error = None

		if not name:
            		error = 'Name is required.'

		if error is not None:
			flash(error)
		else:
            		db = get_db()
            		db.execute(
                	'UPDATE grades SET name  = ?, points = ?'
                	' WHERE id = ?',
                	(name, points, id)
            	)
		db.commit()
		return redirect(url_for('grades.index'))

	return render_template('grades/update.html', grades=grades)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
	get_grades(id)
	db = get_db()
	db.execute('DELETE FROM grades WHERE id = ?', (id,))
	db.commit()
	return redirect(url_for('grades.index'))
