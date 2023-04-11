# celery
from celery import shared_task

# standard
import time
import psycopg2
from math import sqrt, log
# The "shared_task" decorator allows creation
# of Celery tasks for reusable apps as it doesn't
# need the instance of the Celery app.
# @celery_app.task()

def sidi_pair(sender_locations, recipient_locations):
    sender_total_lon = 0
    sender_total_lat = 0
    recipient_total_lon = 0
    recipient_total_lat = 0
    for j in sender_locations:
        sender_total_lon += j[0]
        sender_total_lat += j[1]
    for j in recipient_locations:
        recipient_total_lon += j[0]
        recipient_total_lat += j[1]
    if len(sender_locations) != 0:
        centroid_sender_lon = sender_total_lon/len(sender_locations)
        centroid_sender_lat = sender_total_lat/len(sender_locations)
    else:
        centroid_sender_lon = sender_total_lon/1
        centroid_sender_lat = sender_total_lat/1
    if len(recipient_locations) != 0:
        centroid_recipient_lon = recipient_total_lon/len(recipient_locations)
        centroid_recipient_lat = recipient_total_lat/len(recipient_locations)
    else:
        centroid_recipient_lon = recipient_total_lon/1
        centroid_recipient_lat = recipient_total_lat/1
    print(centroid_sender_lon, centroid_recipient_lon, centroid_sender_lat, centroid_recipient_lat)
    print("raiz adentro:")
    if sqrt((centroid_sender_lon - centroid_recipient_lon)**2 + (centroid_sender_lat - centroid_recipient_lat)**2) == 0:
        sidi = 0
        cur.execute("UPDATE pings set sidi_index = %s  where id = %s ", (sidi, i[0],))
        conn.commit()
        cur.close()
        conn.close()
        return None 
    distance = log(sqrt((centroid_sender_lon - centroid_recipient_lon)**2 + (centroid_sender_lat - centroid_recipient_lat)**2))
    sidi = (len(sender_locations) + len(recipient_locations))/distance
    return sidi


@shared_task()
def calc_indices(id_ping):
    """
    Calculates the indices of the ping
    """
    # Connect to the database
    conn = psycopg2.connect(
        database="pingder-db",
        user="postgres",
        password="docker",
        host="db",
        port="5432"
    )
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Query the database
    cur.execute("SELECT * FROM pings WHERE id = %s", (id_ping,))
    # Fetch all the rows in a list of lists.
    ping = cur.fetchone()

    cur.execute("SELECT ST_X(lonlat::geometry), ST_Y(lonlat::geometry) FROM locations WHERE locations.user_id = %s", (ping[3],))
    sender_locations = cur.fetchall()
    cur.execute("SELECT ST_X(lonlat::geometry), ST_Y(lonlat::geometry) FROM locations WHERE locations.user_id = %s", (ping[4],))
    recipient_locations = cur.fetchall()
    
    sidi = sidi_pair(sender_locations, recipient_locations)
    #############
    cur.execute("SELECT * FROM locations WHERE user_id = %s", (ping[0],))
    sender_locations = cur.fetchall()
    dict_sender = {}
    for j in sender_locations:
        cur.execute("SELECT tag_id FROM locations_tags WHERE location_id = %s", (j[0],))
        tags = cur.fetchall()
        for k in tags:
            if k[0] not in dict_sender:
                dict_sender[k[0]] = 1
            else:
                dict_sender[k[0]] += 1 
            
    cur.execute("SELECT * FROM locations WHERE user_id = %s", (i[1],))
    recipient_locations = cur.fetchall()
    dict_recipient = {}
    for j in recipient_locations:
        cur.execute("SELECT tag_id FROM locations_tags WHERE location_id = %s", (j[0],))
        tags = cur.fetchall()
        for k in tags:
            if k[0] not in dict_recipient:
                dict_recipient[k[0]] = 1
            else:
                dict_recipient[k[0]] += 1 
    diff = 0
    suma = len(sender_locations) + len(recipient_locations)
    for i in dict_recipient:
        for j in dict_sender:
            if i == j:
                diff += abs(dict_recipient[i] - dict_sender[j])
    if suma == 0:
        siin = 0
    else: 
        siin = (suma - diff)/suma

    dindin = sidi * siin
    #############
    # Update the database
    cur.execute("UPDATE pings SET sidi_index = %s, siin_index = %s, dindin_index = %s  WHERE id = %s", (sidi, siin, dindin, id_ping))
    # Close communication with the database
    cur.close()
    conn.commit()
    conn.close()
    # Return the result
    return 'Success'

@shared_task()
def sidi_calculator():
    conn = psycopg2.connect("dbname=pingder-db user=postgres password=docker host=db port=5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM pings")
    pings = cur.fetchall()
    print("Pings: ", pings)
    for i in pings:
        cur.execute("SELECT ST_X(lonlat::geometry), ST_Y(lonlat::geometry) FROM locations WHERE locations.user_id = %s", (i[3],))
        sender_locations = cur.fetchall()
        cur.execute("SELECT ST_X(lonlat::geometry), ST_Y(lonlat::geometry) FROM locations WHERE locations.user_id = %s", (i[4],))
        recipient_locations = cur.fetchall()
        sender_total_lon = 0
        sender_total_lat = 0
        recipient_total_lon = 0
        recipient_total_lat = 0
        for j in sender_locations:
            sender_total_lon += j[0]
            sender_total_lat += j[1]
        for j in recipient_locations:
            recipient_total_lon += j[0]
            recipient_total_lat += j[1]
        if len(sender_locations) != 0:
            centroid_sender_lon = sender_total_lon/len(sender_locations)
            centroid_sender_lat = sender_total_lat/len(sender_locations)
        else:
            centroid_sender_lon = sender_total_lon/1
            centroid_sender_lat = sender_total_lat/1
        if len(recipient_locations) != 0:
            centroid_recipient_lon = recipient_total_lon/len(recipient_locations)
            centroid_recipient_lat = recipient_total_lat/len(recipient_locations)
        else:
            centroid_recipient_lon = recipient_total_lon/1
            centroid_recipient_lat = recipient_total_lat/1
        print(centroid_sender_lon, centroid_recipient_lon, centroid_sender_lat, centroid_recipient_lat)
        print("raiz adentro:")
        if sqrt((centroid_sender_lon - centroid_recipient_lon)**2 + (centroid_sender_lat - centroid_recipient_lat)**2) == 0:
            sidi = 0
            cur.execute("UPDATE pings set sidi_index = %s  where id = %s ", (sidi, i[0],))
            conn.commit()
            cur.close()
            conn.close()
            return None 
        distance = log(sqrt((centroid_sender_lon - centroid_recipient_lon)**2 + (centroid_sender_lat - centroid_recipient_lat)**2))
        sidi = (len(sender_locations) + len(recipient_locations))/distance
        cur.execute("UPDATE pings set sidi_index = %s  where id = %s ", (sidi, i[0],))
        cur.execute("SELECT sidi_index FROM pings WHERE id = %s", (i[0],))
    conn.commit()
    cur.close()    
    conn.close()
    return None 

@shared_task
def siin_calculator():
    conn = psycopg2.connect("dbname=pingder-db user=postgres password=docker host=db port=5432")
    cur = conn.cursor()
    cur.execute("SELECT sender_id, recipient_id, id FROM pings")
    pings = cur.fetchall()
    for i in pings:
        cur.execute("SELECT * FROM locations WHERE user_id = %s", (i[0],))
        sender_locations = cur.fetchall()
        dict_sender = {}
        for j in sender_locations:
            cur.execute("SELECT tag_id FROM locations_tags WHERE location_id = %s", (j[0],))
            tags = cur.fetchall()
            for k in tags:
                if k[0] not in dict_sender:
                    dict_sender[k[0]] = 1
                else:
                    dict_sender[k[0]] += 1 
                
        cur.execute("SELECT * FROM locations WHERE user_id = %s", (i[1],))
        recipient_locations = cur.fetchall()
        dict_recipient = {}
        for j in recipient_locations:
            cur.execute("SELECT tag_id FROM locations_tags WHERE location_id = %s", (j[0],))
            tags = cur.fetchall()
            for k in tags:
                if k[0] not in dict_recipient:
                    dict_recipient[k[0]] = 1
                else:
                    dict_recipient[k[0]] += 1 
        dif = 0
        suma = len(sender_locations) + len(recipient_locations)
        for k in dict_recipient:
            for j in dict_sender:
                if k == j:
                    dif += abs(dict_recipient[k] - dict_sender[j])
        print(dif, suma)
        if suma == 0:
            siin = 0
        else: 
            siin = (suma - dif)/suma
        cur.execute("UPDATE pings set siin_index = %s  where id = %s ", (siin, i[2],))
    conn.commit()
    cur.close()    
    conn.close()

@shared_task    
def dindin_calculator():
    conn = psycopg2.connect("dbname=pingder-db user=postgres password=docker host=db port=5432")
    cur = conn.cursor()
    cur.execute("SELECT id FROM pings")
    pings = cur.fetchall()  
    for i in pings:
        cur.execute("SELECT sidi_index FROM pings WHERE id = %s", (i[0],))
        sidi = cur.fetchall()
        cur.execute("SELECT siin_index FROM pings WHERE id = %s", (i[0],))

        siin = cur.fetchall()   
        if sidi[0][0] and siin[0][0]:
            dindin = sidi[0][0] * siin[0][0]
            cur.execute("UPDATE pings set dindin_index = %s  where id = %s ", (dindin, i[0],))
        else:
            cur.execute("UPDATE pings set dindin_index = %s  where id = %s ", (None, i[0],))
    conn.commit()
    cur.close()    
    conn.close()

@shared_task
def grievous():
    print('General Kenobi!')

@shared_task
def wait_and_return():
    time.sleep(5)
    return 'Hello World!'
