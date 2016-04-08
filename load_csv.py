__author__ = 'riccardo'

import psycopg2

try:
    conn = psycopg2.connect("dbname='BIopen' user='riccardo' password='postgres'")
except:
    print "can't connect"

cur = conn.cursor()

# cur.execute("""CREATE TABLE medie_strutt_vendita
#             (id integer NOT NULL,
#              istat integer,
#              comune character varying(50),
#              provincia character varying(3),
#              indirizzo text,
#              titolare text,
#              settore_merc_non_alim character varying(3),
#              sup_alim integer,
#              sup_non_alim integer,
#              sup_totale integer,
#              lat double precision,
#              lng double precision);""")
#
# cur.execute("""ALTER TABLE medie_strutt_vendita
#             ADD CONSTRAINT medie_strutt_vendita_pkey PRIMARY KEY(id);""")
#
# cur.execute("""copy medie_strutt_vendita
#             FROM '/Users/riccardo/Documents/progetti/BIopen/Medie_Strutture_di_Vendita.csv'
#             DELIMITER ',' CSV HEADER;""")
#
# cur.execute("""ALTER TABLE medie_strutt_vendita ADD COLUMN the_geom geometry(POINT,4326);""")
#
# cur.execute("""CREATE INDEX medie_strutt_vendita_the_geom_gist
#             ON medie_strutt_vendita
#             USING gist
#             (the_geom);""")

cur.execute("""UPDATE grandi_strutt_vendita
            SET the_geom = ST_SetSRID(ST_MakePoint(longitude,latitude),4326);""")



conn.commit()

