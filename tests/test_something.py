import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User

# resp = requests.get(SERVICE_URL)
#
# print(resp.__getstate__())
# print(resp.url)





def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(300).validate(User)

#
# z = {
#   "meta": {
#     "pagination": {
#       "total": 1725,
#       "pages": 87,
#       "page": 1,
#       "limit": 20,
#       "links": {
#         "previous": null,
#         "current": "https://gorest.co.in/public/v1/users?page=1",
#         "next": "https://gorest.co.in/public/v1/users?page=2"
#       }
#     }
#   },
#   "data": [
#     {
#       "id": 1753,
#       "name": "API Monitoring:5y3",
#       "email": "apimonitoring5y3at@synthetic.com",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 31,
#       "name": "Mandaakin Putta",
#       "email": "mandaakin_dutta@gusikowski.org",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 13,
#       "name": "Sucheta Jain",
#       "email": "jain_sucheta@stanton.info",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 14,
#       "name": "Gopee Asan",
#       "email": "asan_gopee@schulist-von.com",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 16,
#       "name": "Shashi Prajapat",
#       "email": "prajapat_shashi@rosenbaum.io",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 17,
#       "name": "Diptendu Pandey",
#       "email": "pandey_diptendu@ankunding.info",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 18,
#       "name": "Devdan Iyer",
#       "email": "devdan_iyer@gorczany.io",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 19,
#       "name": "Gouranga Iyengar CPA",
#       "email": "cpa_iyengar_gouranga@hills.org",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 20,
#       "name": "Adhiraj Malik II",
#       "email": "adhiraj_ii_malik@wiegand.co",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 21,
#       "name": "Uttam Varrier",
#       "email": "uttam_varrier@sanford.name",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 22,
#       "name": "Mandaakin Embranthiri",
#       "email": "embranthiri_mandaakin@muller.net",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 23,
#       "name": "Dhananjay Nayar",
#       "email": "dhananjay_nayar@conn.org",
#       "gender": "male",
#       "status": "inactive"
#     },
#     {
#       "id": 24,
#       "name": "Devadatt Tagore",
#       "email": "devadatt_tagore@keeling.io",
#       "gender": "male",
#       "status": "active"
#     },
#     {
#       "id": 25,
#       "name": "Ganapati Pandey V",
#       "email": "ganapati_pandey_v@parker-crooks.org",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 26,
#       "name": "Prof. Brijesh Embranthiri",
#       "email": "embranthiri_brijesh_prof@grant.org",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 27,
#       "name": "Opalina Butt",
#       "email": "opalina_butt@grimes.info",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 28,
#       "name": "Bandhul Gandhi",
#       "email": "bandhul_gandhi@maggio.net",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 29,
#       "name": "Tej Sethi Ret.",
#       "email": "sethi_tej_ret@hickle-rodriguez.biz",
#       "gender": "female",
#       "status": "inactive"
#     },
#     {
#       "id": 30,
#       "name": "Dinakar Banerjee",
#       "email": "banerjee_dinakar@windler.com",
#       "gender": "female",
#       "status": "active"
#     },
#     {
#       "id": 32,
#       "name": "Jitendra Pothuvaal",
#       "email": "jitendra_pothuvaal@conroy.org",
#       "gender": "female",
#       "status": "active"
#     }
#   ]
# }