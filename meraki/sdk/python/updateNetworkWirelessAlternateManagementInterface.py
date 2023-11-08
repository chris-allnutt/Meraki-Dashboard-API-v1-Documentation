import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.wireless.updateNetworkWirelessAlternateManagementInterface(
    network_id, 
    enabled=True, 
    vlanId=100, 
    protocols=['radius', 'snmp', 'syslog', 'ldap'], 
    accessPoints=[{'serial': 'Q234-ABCD-5678', 'alternateManagementIp': '1.2.3.4', 'subnetMask': '255.255.255.0', 'gateway': '1.2.3.5', 'dns1': '8.8.8.8', 'dns2': '8.8.4.4'}]
)

print(response)