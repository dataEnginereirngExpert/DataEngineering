import psycopg2

def update_student_course():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="studentdb_uk",       # change to your database name
            user="postgres",
            password="postgres"
        )

        cursor = conn.cursor()

        # Update course for student ID = 1
        update_query = """
            UPDATE courses
            SET course_name = %s
            WHERE student_id = %s;
        """

        new_course = "life Science"
        student_id = 2

        cursor.execute(update_query, (new_course, student_id))
        conn.commit()

        print("Course updated successfully for student ID = 2.")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()


# Run the function
update_student_course()
