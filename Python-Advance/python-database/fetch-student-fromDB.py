import psycopg2

def fetch_students_and_courses():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="studentdb_uk",       # change to your database name
            user="postgres",
            password="postgres"
        )

        cursor = conn.cursor()

        # SQL JOIN query
        query = """
            SELECT s.id, s.name, s.age, c.course_name
            FROM students s
            LEFT JOIN courses c ON s.id = c.student_id
            ORDER BY s.id;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        # Print results
        print("Student List With Courses:\n")
        for row in results:
            student_id, name, age, course = row
            print(f"ID: {student_id} | Name: {name} | Age: {age} | Course: {course}")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()


# Run the function
fetch_students_and_courses()
