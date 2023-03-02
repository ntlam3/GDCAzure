from distutils.log import debug
from flask import Flask, render_template
from requests import session
import main
my_se=main.login()
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eupromo')
def eupromo():
    eu_folder=main.eupromo(my_se)
    return render_template('eupromo.html',eu_folder=eu_folder)
@app.route('/kcdm')
def kcdm():
    kcdm_folder=main.KCDM(my_se)
    return render_template('kcdm.html',kcdm_folder=kcdm_folder)
@app.route('/crm')
def crm():
    crm_folder=main.crm(my_se)
    return render_template('crm.html',crm_folder=crm_folder)

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__=='__main__':
    app.run(debug=True)