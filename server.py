# from flask import Flask

# app = Flask(__name__)
# print(__name__)
# print(app)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/blog")
# def blog():
#     return "<p>These are my thoughts on blogs</p>"

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "<p>This is my dog blog</p>" 

###############################################################################

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

#@app.route("/index.html")
@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# @app.route("/works.html")
# def works():
#     return render_template("works.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

# @app.route("/work.html")
# def work():
#     return render_template("work.html")

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     # if request.method == 'POST':
#     #     data = request.form.to_dict()
#     #     print(data)
#     #     return 'form submitted'
#     # else:
#     return 'form submitted hooraayyy!'

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        #csv = database2.write(f'\n{email}, {subject}, {message}')
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)     
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # data = request.form.to_dict()
        # #print(data)
        # #write_to_file(data)
        # write_to_csv(data)
        # # return 'form submitted'
        # return redirect('/thankyou.html')
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'
