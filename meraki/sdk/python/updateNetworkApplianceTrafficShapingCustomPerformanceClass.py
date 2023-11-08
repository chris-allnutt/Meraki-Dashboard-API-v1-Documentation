import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
custom_performance_class_id = ''

response = dashboard.appliance.updateNetworkApplianceTrafficShapingCustomPerformanceClass(
    network_id, custom_performance_class_id, 
    name='myCustomPerformanceClass', 
    maxLatency=100, 
    maxJitter=100, 
    maxLossPercentage=5
)

print(response)