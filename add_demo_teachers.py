from teachers.models import Teacher

Teacher.objects.bulk_create([
    Teacher(first_name='John', last_name='Doe', subject='Mathematics'),
    Teacher(first_name='Jane', last_name='Smith', subject='Science'),
    Teacher(first_name='Emily', last_name='Johnson', subject='English'),
])

print("Demo teacher data added successfully!") 