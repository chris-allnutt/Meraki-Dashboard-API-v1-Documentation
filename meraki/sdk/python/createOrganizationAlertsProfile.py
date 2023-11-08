import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
type = 'wanUtilization'
alert_condition = {'duration': 60, 'window': 600, 'bit_rate_bps': 10000, 'interface': 'wan1'}
recipients = {'emails': ['admin@example.org'], 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vcGF0aA==']}
network_tags = ['tag1', 'tag2']

response = dashboard.organizations.createOrganizationAlertsProfile(
    organization_id, type, alert_condition, recipients, network_tags, 
    description='WAN 1 high utilization'
)

print(response)