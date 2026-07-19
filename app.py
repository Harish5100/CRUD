from flask import Flask, render_template, request, redirect
app = Flask(__name__)
students = []
@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name'].strip()
    dept = request.form['dept'].strip()
    year = request.form['year'].strip()
    if name and dept and year:
        students.append({
            'name': name,
            'dept': dept,
            'year': year
        })
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if 0 <= id < len(students):
        students.pop(id)
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if id < 0 or id >= len(students):
        return redirect('/')
    if request.method == 'POST':
        name = request.form['name'].strip()
        dept = request.form['dept'].strip()
        year = request.form['year'].strip()
        if name and dept and year:
            students[id] = {
                'name': name,
                'dept': dept,
                'year': year
            }
        return redirect('/')
    return render_template('edit.html', student=students[id], student_id=id)

if __name__ == '__main__':
    app.run(debug=True)
