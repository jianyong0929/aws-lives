from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    # Create a connection to the database
    connection = pymysql.connect(host='internship.cxtk9ixv8wey.us-east-1.rds.amazonaws.com',
                                 user='awsuser',
                                 password='Bait3273',
                                 db='internship')

    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute("SELECT com_id, com_name, com_hp, com_email  FROM company WHERE status = 0")

            # Fetch all the rows
            result = cursor.fetchall()
    finally:
        # Close the connection to the database
        connection.close()

    # Render the HTML template with the data
    return render_template('admin.html', registrations=result)

if __name__ == '__main__':
    app.run(debug=True)
