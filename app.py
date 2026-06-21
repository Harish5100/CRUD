from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    students.append(name)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    students.pop(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)