import sys
sys.path.append('../')
from fastly import fastly

if len(sys.argv) < 3:
    print("Usage: ./" + sys.argv[0] + " KEY SERVICE_ID")
    sys.exit(1)

FASTLY_KEY = sys.argv[1]
FASTLY_SERVICE_ID = sys.argv[2]

fastly = fastly.Fastly()
fastly.authenticate_by_key(key=FASTLY_KEY)
#p = fastly.get_service()
#r = fastly.get_service_search(service_name='Lot 1 - lepetitcafedupro.com')
#print(r.text)
#fastly.print_json_pretty(json=r.text)
#z = fastly.get_service_details(service_id = '3wYuSODNFTSh6Hvo7yC8zG')
#fastly.print_json_pretty(json=z.text)
#r = fastly.get_backends(service_id=FASTLY_SERVICE_ID, version=21)
#fastly.print_json_pretty(json=r.text)

status_code, r = fastly.get_backend_name(service_id=FASTLY_SERVICE_ID, version=21, name='leroymerlin fr')
print(status_code)
print(r)

#params = {'ssl_ca_cert': 'test_ca_cert' }
params = {'name': 'leroy_merlin_fr' }
r = fastly.update_backend(service_id=FASTLY_SERVICE_ID, version=21, backend_name='leroymerlin fr', params={'name': 'test_ca_cert' })
print(r.status_code)
print(r.json)

