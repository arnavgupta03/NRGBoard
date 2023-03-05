from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    city = request.args.get('city')
    if city:
        bills = []
        with open(city + '.csv', 'r') as f:
            reader = csv.DictReader(f)
            bills = list(reader)
        return render_template('index.html', bills=bills, city = " ".join(city.split("-")).title())
    else:
        return render_template('index.html', bills=[])
    
@app.route('/addBill', methods=['POST'])
def addBill():
    print(request.form)
    city = request.form['city']
    city = "-".join(city.split(" ")).lower()
    name = request.form['nickname']
    amount = request.form['amount']
    point1 = request.form['point1']
    point2 = request.form['point2']
    point3 = request.form['point3']
    with open(city + '.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, amount, point1, point2, point3])
    return redirect(url_for('index', city=city))
    
if __name__ == '__main__':
    app.run(debug=True)