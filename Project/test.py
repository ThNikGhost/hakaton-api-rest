import os.path
from work_db import *
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
city_id = 15
city_name = 'niko'
cur.execute(f"""INSERT INTO Cities (city_id,city_name)
                   VALUES (
                       '{city_id}',
                       '{city_name}'
                   )
                        """)