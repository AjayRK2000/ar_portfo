from flask import Flask, render_template, url_for, request, redirect
import csv 

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


def write_to_DB(data):
	name = data['name']
	email = data['email']
	message = data['message']

	with open('pf_Database.txt', mode='a') as db:
		db.write(f'{name} said: \n{message} \nReply to them at {email}\n\n')

def write_to_CSV(data):
	name = data['name']
	email = data['email']
	message = data['message']

	with open('pf_Database.csv', mode='a', newline='') as db2:
		csv_writer = csv.writer(db2, delimiter='|', quotechar='|')

		csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_CSV(data)
		return redirect("/thankyou.html")
	else:
		return "Sorry! Something went wrong! Please try again."

if (__name__ == "__main__"):
	app.run(debug=True)