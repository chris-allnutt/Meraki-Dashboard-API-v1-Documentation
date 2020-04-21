import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
vlan_id = ''

response = dashboard.appliance.updateNetworkApplianceVlan(
    network_id, vlan_id, 
    name='My VLAN', 
    subnet='192.168.1.0/24', 
    applianceIp='192.168.1.1', 
    groupPolicyId='101', 
    dhcpHandling='Run a DHCP server', 
    dhcpLeaseTime='1 day', 
    dhcpBootOptionsEnabled=False, 
    dhcpBootNextServer=None, 
    dhcpBootFilename=None, 
    fixedIpAssignments={'22:33:44:55:66:77': {'ip': '1.2.3.4', 'name': 'Some client name'}}, 
    reservedIpRanges=[{'start': '192.168.1.0', 'end': '192.168.1.1', 'comment': 'A reserved IP range'}], 
    dnsNameservers='google_dns', 
    dhcpOptions=[{'code': 5, 'type': 'text', 'value': 'five'}]
)

print(response)