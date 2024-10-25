
# def save_operation(operation, result):
#     conn = get_connection()
#     with conn.cursor() as cursor:
#         cursor.execute("""
#             INSERT INTO operations (operation, result)
#             VALUES (%s, %s)
#         """, (operation, result))
#         conn.commit()
#     conn.close()
