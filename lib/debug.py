from __init__ import connection, cursor
from specialty import Specialty

import ipdb

Specialty.drop_table()
Specialty.create_table()

ipdb.set_trace()