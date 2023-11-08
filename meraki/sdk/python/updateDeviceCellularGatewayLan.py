import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.cellularGateway.updateDeviceCellularGatewayLan(
    serial, 
    reservedIpRanges=[{'start': '192.168.1.0', 'end': '192.168.1.1', 'comment': 'A reserved IP range'}], 
    fixedIpAssignments=[{'mac': '0b:00:00:00:00:ac', 'name': 'server 1', 'ip': '192.168.0.10'}, {'mac': '0b:00:00:00:00:ab', 'name': 'server 2', 'ip': '192.168.0.20'}]
)

print(response)