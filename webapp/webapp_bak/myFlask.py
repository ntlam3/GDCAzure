from distutils.log import debug
from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def index():
    name='Jojo'
    letters=list(name)
    pup_dict={"pup_name":"Lucky"}
    myarray=[1,2,3,5,8,9,10]
    return render_template('basic.html',my_variable=name,letters=letters,pup_dict=pup_dict,myarray=myarray)
@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)
if __name__=='__main__':
    app.run(debug=True)