__author__ = 'riccardo'

import psycopg2

try:
    conn = psycopg2.connect("dbname='BIopen' user='riccardo' password='postgres'")
except:
    print "can't connect"

cur = conn.cursor()

# cur.execute("""CREATE TABLE Pop_sesso_stato_civile_2011
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
cur.execute("""CREATE TABLE Numero_imprese_per_comune_2011
            (anno integer,
             cod_istat_pr integer NOT NULL,
             provincia text,
             cod_istat_com integer NOT NULL,
             comune text,
             A integer,
             B integer,
             C integer,
             D integer,
             E integer,
             F integer,
             G integer,
             H integer,
             I integer,
             J integer,
             K integer,
             L integer,
             M integer,
             N integer,
             O integer,
             P integer,
             Q integer,
             R integer,
             S integer,
             T integer,
             X integer);""")

# cur.execute("""ALTER TABLE Pop_sesso_stato_civile_2011
#             ADD CONSTRAINT Pop_sesso_stato_civile_2011_pkey PRIMARY KEY(cod_istat_com);""")

cur.execute("""copy Numero_imprese_per_comune_2011
            FROM '/Users/riccardo/Documents/progetti/BIopen/Numero_imprese_per_comune.csv'
            DELIMITER ',' CSV HEADER;""")

# cur.execute("""ALTER TABLE Pop_sesso_stato_civile_2011 ADD COLUMN the_geom geometry(POINT,4326);""")
#
# cur.execute("""CREATE INDEX Mappe_Negozi_e_Locali_Storici_the_geom_gist
#             ON Mappe_Negozi_e_Locali_Storici
#             USING gist
#             (the_geom);""")
#
# cur.execute("""UPDATE Mappe_Negozi_e_Locali_Storici
#             SET the_geom = ST_SetSRID(ST_MakePoint(longitude,latitude),4326);""")



conn.commit()

