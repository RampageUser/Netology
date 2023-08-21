import pytest
from rest_framework.test import APIClient
from model_bakery import baker
import random

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)
    request = client.get(f'/api/v1/courses/1/')
    assert request.status_code == 200
    assert course[0].name == request.data['name']


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    request = client.get('/api/v1/courses/')
    assert request.status_code == 200
    assert len(request.data) == len(courses)


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    id = 19
    courses = course_factory(_quantity=10)
    for course in courses:
        if course.id == id:
            correct_course = course
            break
    request = client.get(f'/api/v1/courses/?id={id}')
    data = request.json()
    assert request.status_code == 200
    assert data[0]['name'] == correct_course.name


@pytest.mark.django_db
def test_filter_name(client, course_factory):
    course = course_factory(_quantity=1)
    course_name = course[0].name
    print(course_name)
    request = client.get(f'/api/v1/courses/?name={course_name}')
    data = request.json()
    assert request.status_code == 200
    assert data[0]['name'] == course_name


@pytest.mark.django_db
def test_create_course(client):
    data = {'name': 'simple course'}
    count = Course.objects.count()
    request = client.post('/api/v1/courses/', data=data)
    assert request.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    count = Course.objects.count()
    some_course = course_factory(_quantity=1)
    course = {
        'id': some_course[0].id,
        'name': some_course[0].name
    }
    data = {'name': 'new name'}
    request = client.patch(f'/api/v1/courses/{course["id"]}/', data=data)
    changed_course = Course.objects.filter(id=course["id"])
    assert request.status_code == 200
    assert Course.objects.count() == count + 1
    assert changed_course[0].name != course['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    count = Course.objects.count()
    course = course_factory(_quantity=1)
    request = client.delete(f'/api/v1/courses/{course[0].id}/')
    assert request.status_code == 204
    assert Course.objects.count() == count
