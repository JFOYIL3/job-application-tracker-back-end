# import os
# import json
# import firebase_admin
# from firebase_admin import credentials, firestore

# if not firebase_admin._apps:
#     service_account_info = json.loads(
#         os.getenv('FIREBASE_CREDENTIALS')
#     )

#     cred = credentials.Certificate(service_account_info)
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
