import request_api.api as api

data = api.get_data('https://openapi.xpi.com.br/openbanking/users/?limit=1')
print(data.json())
