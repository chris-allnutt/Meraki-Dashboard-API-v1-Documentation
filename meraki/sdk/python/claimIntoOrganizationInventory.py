import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'

response = dashboard.organizations.claimIntoOrganizationInventory(
    organization_id, 
    orders=['4CXXXXXXX'], 
    serials=['Q234-ABCD-5678'], 
    licenses=[{'key': 'Z2XXXXXXXXXX', 'mode': 'addDevices'}]
)

print(response)