from flask import Blueprint, render_template, request, redirect, url_for
from .models import create_task, delete_task  # Dodajemy delete_task do importu

views = Blueprint('views', __name__)

# Widok do wyświetlania i dodawania zadań
@views.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        # Pobieranie danych z formularza
        title = request.form['title']
        description = request.form['description']
        task_type = request.form['task_type']
        due_date = request.form['due_date']

        # Dodanie nowego zadania do bazy danych
        create_task(title, description, task_type, due_date)

        # Po dodaniu zadania, przekierowujemy na stronę 'tasks'
        return redirect(url_for('views.tasks'))

    # Jeśli metoda GET, renderujemy formularz
    return render_template("tasks.html")

# Widok do usuwania zadania
@views.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task_view(task_id):
    delete_task(task_id)  # Usuwamy zadanie na podstawie ID
    return redirect(url_for('views.tasks'))
