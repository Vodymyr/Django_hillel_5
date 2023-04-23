# generate_teachers.py

from random import choice

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import Teacher


class Command(BaseCommand):
    help = 'Generates random teachers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            dest='count',
            default=100,
            type=int,
            help='Number of teachers to generate'
        )

    def handle(self, *args, **options):
        teacher_names = ['Jane', 'John', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
        subjects = ['Math', 'Science', 'History', 'English', 'Art', 'Music']

        # Generate teachers
        for i in range(options['count']):
            # Create a user for each teacher
            user = User.objects.create_user(
                username=f'teacher{i}',
                email=f'teacher{i}@example.com',
                password='password'
            )

            # Create the teacher
            teacher = Teacher.objects.create(
                name=choice(teacher_names),
                subject=choice(subjects),
                user=user
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created teacher {teacher.name}'))
