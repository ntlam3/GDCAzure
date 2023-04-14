#!/usr/bin/env python3
from distutils.log import debug
from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.azure import make_azure_blueprint, azure
#import sys
#sys.path.insert(0,'/var/www/webapp/webapp')
#from requests import session
import URL
import sys
import MainProcessor
from MainProcessor import login
import my_superman
import subprocess
#import az_stats
POWERSHELL_PATH="powershell.exe"
ps_script_path=".//KCDM.ps1"
commandline_options = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', ps_script_path]
#import test
my_se=MainProcessor.login()
app=Flask(__name__)
eu_folder=MainProcessor.eupromo(my_se)
kcdm_folder=MainProcessor.KCDM(my_se)
kcdm_dynamic_folder=MainProcessor.kcdm_dynamic(my_se)
length=len(URL.get_cm_db_cpu())
crm_folder=MainProcessor.crm(my_se)

app.secret_key = "supersekrit"
blueprint = make_azure_blueprint(
    client_id="468b52ff-4da0-4bda-b933-728b6d8b07b8",
    client_secret="9db8Q~uMDPBPGCcHVqRKjzhyrgAsrXe5OqwnWa9_",
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route('/')
def index():
	#test.hello()
    if not azure.authorized:
        return redirect(url_for("azure.login"))
    resp = azure.get("/v1.0/me")
    assert resp.ok
    return render_template('home.html')
    #return "You are {mail} on Azure AD".format(mail=resp.json()["mail"])

@app.route('/eupromo')
def eupromo():
    #eu_folder=main.eupromo(my_se)
    return render_template('eupromo.html',eu_folder=eu_folder)

@app.route('/kcdm')
def kcdm():
    #kcdm_folder=main.KCDM(my_se)
    return render_template('kcdm.html',kcdm_folder=kcdm_folder,kcdm_dynamic_folder=kcdm_dynamic_folder,length=length)

@app.route('/crm')
def crm():
	#crm_folder=main.crm(my_se)
	return render_template('crm.html',crm_folder=crm_folder)
@app.route('/superman')
def superman():
    myfile=my_superman.login()
    file_path=myfile['file_path']
    file_name=myfile['file_name']
    mydict=my_superman.display_info(file_path)
    print(file_name)
    return render_template('superman.html',mydict=mydict,file_path=file_path,file_name=file_name)
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)

@app.route('/loading')
def loading():
    return render_template('loading.html')

"""
@app.route('/kcdm/statistics')

def mena_statsistics():
    az_stats.set_env_mena()
    dataenrich=az_stats.SUB_ME_DATAENRICH_PRD()
    dwf_dev=az_stats.SUB_ME_DWF_DEV()
    dwf_prd=az_stats.SUB_ME_DWF_PRD()
    return render_template('mena_stats.html',dataenrich=dataenrich,dwf_dev=dwf_dev, dwf_prd=dwf_prd)
"""
"""
@app.route('/azurestats/crm')
def crm_statistics():
    az_stats.set_env_crmeu()
    az_stats.set_env_crmcis()
    az_stats.set_env_crmlatam()
    crmeu=az_stats.CRM_EU()
    crmcisdev=az_stats.CRM_CIS_DEV()
    crmcisprd=az_stats.CRM_CIS_PRD()
    crmlatam=az_stats.CRM_LATAM()
    return render_template('crm_stats.html',crmeu=crmeu,crmcisdev=crmcisdev,crmcisprd=crmcisprd,crmlatam=crmlatam)

def kcdmstatistics():
    #render_template('loading.html')
    subprocess.run(commandline_options, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)

    f= open(".//templates//Next-CDM.txt","r")
    #f =open("C:\\Log.txt","r")
    contents=f.readlines()
    f.close()
    #print('Next-CDM details:')
    print(contents)
    return render_template('Next-CDM.html',contents=contents)
"""
#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404
if __name__=='__main__':
    app.run(debug=True)
