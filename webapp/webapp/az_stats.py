

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
#import azure.storage.blob
#from azure.storage.blob import BlobClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
import os
# Acquire a credential object

#print(token_credential.credentials)
#tenant_id=os.environ["AZURE_CLIENT_ID"]
#print(tenant_id)
def set_env_mena():
    os.environ["AZURE_TENANT_ID"]="6ffaf6ac-0c82-4a59-bd70-32921ddcb4af"
    os.environ["AZURE_CLIENT_ID"]="dec9d583-91f6-4eea-8565-8b7c00b088d7"
    os.environ["AZURE_CLIENT_SECRET"]="V7_8Q~NUDIhrItEPhHBxDeA8gC0mpdzU5j9uOdcp"
def set_env_crmeu():
    os.environ["AZURE_TENANT_ID"]="768fd379-2f7a-43a2-b9d3-fd0641e19ac4"
    os.environ["AZURE_CLIENT_ID"]="b7528b48-76c0-4097-9ff6-ff83215ebfed"
    os.environ["AZURE_CLIENT_SECRET"]="Hwf8Q~csSoKsf5selvDEVXWVoW68uxVeCzI~5aq-"

def set_env_crmcis():
    os.environ["AZURE_TENANT_ID"]="0d8cd626-0b9d-4a1c-a99a-d18b9f80ccb3"
    os.environ["AZURE_CLIENT_ID"]="44256882-8ef0-4ad8-8d76-bcdb001d9fef"
    os.environ["AZURE_CLIENT_SECRET"]="5P.8Q~q6OaIyEMGWmiyOTyxOJ-ZOPSESc8zv6bMT"
def set_env_crmlatam():
    os.environ["AZURE_TENANT_ID"]="c67d82c3-bec8-45bd-bb6e-da0a8d56e7b5"
    os.environ["AZURE_CLIENT_ID"]="42e1f033-5188-422d-a4d0-a2f8af3477d0"
    os.environ["AZURE_CLIENT_SECRET"]="tTi8Q~eL1S.eyYMUfY0dFovOT96jRY.Hd8SItbAG"    

def CRM_EU():
    set_env_crmeu()
    os.environ["AZURE_SUBSCRIPTION_ID"]="eb5d9a4a-3a05-4b4f-9efc-b2685d6318f1"
    subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"]
    print(os.environ["AZURE_SUBSCRIPTION_ID"])
    crmeu_dict=process(subscription_id) # Assign the dictionary object to the result of the process function
    return crmeu_dict
def CRM_CIS_DEV():
    set_env_crmcis()
    os.environ["AZURE_SUBSCRIPTION_ID"]="5101949e-0630-4274-b425-4f5628fcc14a"
    subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"]
    print(os.environ["AZURE_SUBSCRIPTION_ID"])
    crmcisdev_dict=process(subscription_id) # Assign the dictionary object to the result of the process function
    return crmcisdev_dict

def CRM_CIS_PRD():
    set_env_crmcis()
    os.environ["AZURE_SUBSCRIPTION_ID"]="be4ff6f2-e060-46d5-84a0-d62af62cbe51"
    subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"]
    print(os.environ["AZURE_SUBSCRIPTION_ID"])
    crmcisprd_dict=process(subscription_id) # Assign the dictionary object to the result of the process function
    return crmcisprd_dict
    
def CRM_LATAM():
    set_env_crmlatam()
    os.environ["AZURE_SUBSCRIPTION_ID"]="ca665f3d-6578-4f7d-9f5b-cf602413a0db"
    subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"]
    print(os.environ["AZURE_SUBSCRIPTION_ID"])
    crmlatam_dict=process(subscription_id) # Assign the dictionary object to the result of the process function
    return crmlatam_dict
def SUB_ME_DATAENRICH_PRD():
    set_env_mena()
    os.environ["AZURE_SUBSCRIPTION_ID"]="2e86746b-d0ed-4151-ab93-aae3f943bff4"
    subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"]
    print(os.environ["AZURE_SUBSCRIPTION_ID"])
    dataenrich_dict=process(subscription_id) # Assign the dictionary object to the result of the process function
    return dataenrich_dict

def SUB_ME_DWF_DEV():
    set_env_mena()
    os.environ["AZURE_SUBSCRIPTION_ID"]="53103845-dce5-4046-b931-ef1bc0ea4540"
    subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"]
    print(os.environ["AZURE_SUBSCRIPTION_ID"])
    dwf_dev_dict=process(subscription_id) # Assign the dictionary object to the result of the process function
    return dwf_dev_dict

def SUB_ME_DWF_PRD():
    set_env_mena()
    os.environ["AZURE_SUBSCRIPTION_ID"]="358d9e7d-3c6c-4f7e-b0cb-8f4d5aef09f3"
    subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"]
    print(os.environ["AZURE_SUBSCRIPTION_ID"])
    dwf_prd_dict=process(subscription_id) # Assign the dictionary object to the result of the process function
    return dwf_prd_dict

def process(subscription_id):
    token_credential = DefaultAzureCredential()
    #resource_client=ResourceManagementClient(token_credential,subscription_id)
    
    #for resource in list(resource_list):
    #    print(resource.name)

    storage_client= StorageManagementClient(token_credential,subscription_id)
    storage_list=storage_client.storage_accounts.list()
    count_strg=0
    for storage_acc in storage_list:
        print(storage_acc.name)
        count_strg+=1
    print('Total number of storage account: {}'.format(count_strg))

    compute_client=ComputeManagementClient(token_credential,subscription_id)
    compute_list=compute_client.virtual_machines.list_all()
    disk_list=compute_client.disks.list()

    count_vm=0
    count_disk=0
    unused_disk=0
    for compute_vm in compute_list:
        print(compute_vm.name)
        count_vm+=1
    print('Total number of VM: {}'.format(count_vm))
    for disk in disk_list:
        print(disk.managed_by)
        if (disk.managed_by == None):
            unused_disk+=1
        count_disk+=1
    print('Total number of disks: {}'.format(count_disk))
    print('Total number of unused disks: {}'.format(unused_disk))

    network_client=NetworkManagementClient(token_credential,subscription_id)
    nw_list=network_client.network_interfaces.list_all()
    unused_nw=0 #Unused network interfaces
    lb_list=network_client.load_balancers.list_all()
    unused_lb=0 #Unused load balancers
    unused_ip=0 # Unused Public IP addresses
    publicip_list=network_client.public_ip_addresses.list_all()
    for nw_interface in nw_list:
        if (nw_interface.virtual_machine==None):
            unused_nw+=1
    print('Total number of unused network interfaces: {}'.format(unused_nw))
    for lb in lb_list:
        if(lb.backend_address_pools==None):
            unused_lb+=1
    print('Total number of unused load balancers: {}'.format(unused_lb))
    for public_ip in publicip_list:
        if (public_ip.ip_configuration==None):
            unused_ip+=1
    print('Total number of unused public ip addresses: {}'.format(unused_ip))
    return {'count_strg':count_strg,'count_vm':count_vm,'count_disk':count_disk,'unused_disk':unused_disk,'unused_nw':unused_nw,'unused_lb':unused_lb,'unused_ip':unused_ip}

set_env_mena()
set_env_crmeu()
SUB_ME_DATAENRICH_PRD()
SUB_ME_DWF_DEV()
SUB_ME_DWF_PRD()
CRM_EU()
