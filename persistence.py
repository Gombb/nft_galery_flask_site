from psycopg2.extras import RealDictCursor
import database_common


@database_common.connection_handler
def get_product_for_id(cursor, product_id):
    cursor.execute(""" SELECT id, contract_address, token_id, artist_id
                        FROM collectible
                        WHERE id = %(product_id)s;
                        """,
                   {"product_id": product_id})
    return cursor.fetchall()


@database_common.connection_handler
def get_artist_for_artist_id(cursor, artist_id):
    cursor.execute(""" SELECT name, bio, avatar_url
                        FROM artist 
                        WHERE id = %(artist_id)s;""",
                        {"artist_id": artist_id})
    return cursor.fetchall()


@database_common.connection_handler
def get_all_product(cursor):
    cursor.execute(""" SELECT * FROM collectible; """)
    return cursor.fetchall()


@database_common.connection_handler
def get_all_artist(cursor):
    cursor.execute("""
                    SELECT *
                    FROM artist;
                    """)
    return cursor.fetchall()


# lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
