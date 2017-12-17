import pymysql


host='localhost'
port=3306
user='root'
password='o2tunes123'
db_name='test_ads'

def create_connection():
    conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db_name, autocommit=True,
                       use_unicode=True, charset="utf8")
    return conn

def is_new_member(connection,member_id):
    print("i am checking if you are a new member")
    cursor = connection.cursor()
    cursor.callproc('is_new_member', [member_id])
    result=cursor.fetchone()
    if result is None:
        print('yeah you are new')
        return True
    else:
        print('nope you are not new')
        return False
    print(result)

def add_new_member(connection,member_id):
    print("i want to add your name into my database new commer")
    cursor = connection.cursor()
    cursor.callproc('add_new_member', [member_id])
    print('your info has been recrded successfully')
    return

def update_state(member_id,next_state,connection):
    print("im in db helper,wanna store your desired action")
    cursor = connection.cursor()
    cursor.callproc('update_state', [member_id,next_state])
    print('state is updated successfully')
    return

def fetch_state(chat_id,connection):
    print("im in db helper, wanna know your next state")
    cursor = connection.cursor()
    cursor.callproc('fetch_state', [chat_id])
    last_state = cursor.fetchone()
    print('state retreived successfully')
    print(last_state)
    return last_state[0]

def insert_ad(member_id,ad_title,connection):
    print("im in db helper, create ad title, wanna store it into db")
    try:
        cursor = connection.cursor()
        if 'گزینه' in ad_title:
            pass
        else:
            cursor.callproc('insert_ad', [member_id,ad_title])
            result=cursor.fetchone()
            print('your ad id is as follow:')
            print(result[0])
            return result[0]
    except Exception as e:
        print("Exeception occured:{}".format(e))

def update_state_new_title_added(chat_id,ad_id,connection):
    print('i am in db helper, wanna update your state to your ad id for ease of process')
    cursor = connection.cursor()
    cursor.callproc('update_state_new_title_added', [member_id, ad_id])

def list_null_fields(ad_id,connection):
    null_fields=[]
    print('i am in db helper, fetching your empty fields')
    cursor = connection.cursor()
    cursor.callproc('list_all_fields', [ad_id])
    fields = cursor.fetchone()
    if fields[2] is None:
        null_fields.append('price')
    if fields[3] is None:
        null_fields.append('mileage')
    if fields[4] is None:
        null_fields.append('transmission')
    if fields[5] is None:
        null_fields.append('release_year')
    if fields[6] is None:
        null_fields.append('model')
    if fields[7] is None:
        null_fields.append('brand')
    print(null_fields)
    return null_fields

def update_field(ad_id,field_name,field_value, connection):
    print(' i am updating your')
    print(field_name)
    print(field_value)
    cursor = connection.cursor()
    if type(field_value) is int:
        cursor.callproc('update_int_field',[ad_id,field_name,field_value])
    else:
        cursor.callproc('update_string_field',[ad_id,field_name,field_value])

def get_ad_id(chat_id,connection):
    print('i am in get ad id in dbhelper')
    cursor = connection.cursor()
    cursor.callproc('get_ad_id', [chat_id])
    ad_id = cursor.fetchone()
    print('your ad id in get ad id is')
    print(ad_id[0])
    return ad_id[0]

def search_year(start,end,connection):
    ads=[]
    print('in db helper search year')
    cursor = connection.cursor()
    cursor.callproc('search_year', [start,end])
    years = cursor.fetchall()
    for year in years:
        year=list(year)
        ads.append(year)
    return ads

def insert_ad_transaction(member_id,ad_title,connection):
    print('i am adding yoour ad title and update your status using transactions')
    cursor = connection.cursor()
    cursor.callproc('insert_ad_transaction',[member_id,ad_title])

def search_price(start, end, connection):
    print('in db helper search price')
    cursor = connection.cursor()
    cursor.callproc('search_price', [start, end])
    ads = cursor.fetchall()
    prices=[]
    for ad in ads:
        ad=list(ad)
        prices.append(ad)
    print(prices)
    return prices

def search_mileage(start, end, connection):
    print('in db helper search mileage')
    cursor = connection.cursor()
    cursor.callproc('search_mileage', [start, end])
    ads=[]
    miles=cursor.fetchall()
    for mile in miles:
        mile=list(mile)
        ads.append(mile)
    return ads


