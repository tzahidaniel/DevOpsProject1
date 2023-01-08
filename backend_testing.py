import requests
from flask import Flask
import pymysql


app = Flask(__name__)


schema_name = "freedb_devops"
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_lalala', passwd='P!?k!gbS*5QXnU8', db=schema_name)
conn.autocommit(True)
cursor = conn.cursor()


def test_add_user():
    try:
       response = requests.post('http://127.0.0.1:5000/users/99ed1db2-4abc-42a9-8074-60a9584de1f1' , json={'user_name': "asdf"})
       print("post", response.status_code)
       get_req_test = requests.get('http://localhost:5000/users/99ed1db2-4abc-42a9-8074-60a9584de1f1')
       print("get", get_req_test.status_code)
       print(response.json()) #Expected output: {'status': 'ok', 'user_name': 'john'}
       if not get_req_test.ok:
            raise Exception("error...")
        # cursor.execute("SELECT * FROM freedb_devops.project WHERE name = 'asdf'")
        # user = cursor.fetchone()
        # if not user:
        #     raise Exception("test failed 2")
        # print('here')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_add_user()

