from mysql.connector import connect

hostname = "localhost"
user_name = "root"
pwd = "Ghaney17!!"


def add_job(job_class: str, charge_hour: float):
    # step1: create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # step2: create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # step3: write the statement
            add_record_to_job = f"""INSERT INTO sampleproject.job (job_class, chg_hour) 
                                    values ("{job_class}", {charge_hour});"""
            # step4: execute the statement
            mysql_cursor.execute(add_record_to_job)
            # step5: commit the changes
            mysql_connection_object.commit()


def add_employee():
    pass


def add_project():
    pass


def assign_employee_to_project():
    pass


def testing():
    add_job(job_class="J1005", charge_hour=42.99)


if __name__ == '__main__':
    testing()

