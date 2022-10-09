import datetime
import pymysql

db_config = {
    "host": "INSERT_HERE_HOST",
    "user": "INSERT_HERE_USER",
    "password": INSERT_HERE_PASSWORD",
    "db": "INSERT_HERE_DATABASE_NAME",
    "port": INSERT_HERE_PORT
}
table = "INSERT_HERE_TABLE_NAME"

try:
    mysql = pymysql.connect(host=db_config['host'],port=db_config['port'],user=db_config['user'],password=db_config['password'],database=db_config['db'],cursorclass=pymysql.cursors.DictCursor)
    print(f"[{datetime.datetime.today()}] [DATABASE] Connected")
except Exception as e:
    print(f"[{datetime.datetime.today()}] [DATABASE] Disconnected:\n -> {e}")

class MYSQL_TOOLZ():
    def get_all():
        try:
            with mysql.cursor() as cursor:
                query = f"SELECT * FROM `{table}`"
                cursor.execute(query)
                ret = cursor.fetchall();
                print(f"[{datetime.datetime.today()}] [DATABASE -> TOOL: GET_ALL] Information parsed!")
                return ret;
        except Exception as e:
            print(f"[{datetime.datetime.today()}] [DATABASE -> TOOL: GET_ALL] ERROR:\n -> {e}")
    def update(base, where, what, where_what, to, operation):
        # base: get_all()
        # where: item (id, discord_id, .....)
        # what: search (item == 1234567890)
        # where_what: editable (xp, max_xp, level......)
        # to: update to ??
        # operation: + =
        try:
            with mysql.cursor() as cursor:
                for i in base:
                    if str(i[f'{where}']) == str(what):
                        if operation == '=':
                            query = f"UPDATE `{table}` SET `{where_what}`={to} WHERE `{table}`.`id` = {i['id']}"
                            cursor.execute(query)
                            mysql.commit()
                            print(f"[{datetime.datetime.today()}] [DATABASE -> TOOL: UPDATE] Information updated!\n -> {where}={what} {where_what} = {to}")
                            break;
                        elif operation == '+':
                            query = f"UPDATE `{table}` SET `{where_what}`={to+int(i[f'{where_what}'])} WHERE `{table}`.`id` = {i['id']}"
                            cursor.execute(query)
                            mysql.commit()
                            print(f"[{datetime.datetime.today()}] [DATABASE -> TOOL: UPDATE] Information updated!\n -> {where}={what} {where_what} += {to}")
                        elif operation == '-':
                            query = f"UPDATE `{table}` SET `{where_what}`={int(i[f'{where_what}'])-{to}} WHERE `{table}`.`id` = {i['id']}"
                            cursor.execute(query)
                            mysql.commit()
                            print(f"[{datetime.datetime.today()}] [DATABASE -> TOOL: UPDATE] Information updated!\n -> {where}={what} {where_what} -= {to}")
                        else:
                            print(f"[{datetime.datetime.today()}] [DATABASE -> TOOL: UPDATE] Invalid operation")
        except Exception as e:
            print(f"[{datetime.datetime.today()}] [DATABASE -> TOOL: UPDATE] ERROR:\n -> {e}")
