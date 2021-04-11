from main import db
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.sqlite import BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, INTEGER, NUMERIC, SMALLINT, TEXT, TIME, TIMESTAMP, VARCHAR
from datetime import datetime
from main import ma

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.String(255), unique=True)
    user_name = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), primary_key=True)
    user_type = db.Column(db.String(255))

    def __init__(self, user_id, user_name, email, user_type):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.user_type = user_type


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('user_id', 'user_name', 'email', 'user_type')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Course(db.Model):
    __tablename__ = 'course'
    course_name = db.Column(db.String(255))
    course_id = db.Column(db.Integer, primary_key=True)
    course_view_count = db.Column(db.Integer)

    def __init__(self, course_name, course_id, course_view_count):
        self.course_name = course_name
        self.course_id = course_id
        self.course_view_count = course_view_count


class CourseSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('course_name', 'course_id', 'course_view_count')

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)


class Subject(db.Model):
    __tablename__ = 'subject'
    subject_name = db.Column(db.String(255))
    subject_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, subject_name, subject_id):
        self.subject_name = subject_name
        self.subject_id = subject_id

class SubjectSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('subject_name', 'subject_id')

subject_schema = SubjectSchema()
subjects_schema = SubjectSchema(many=True)

class Tag(db.Model):
    __tablename__ = 'tag'
    tag_name = db.Column(db.String(255))
    tag_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, tag_name, tag_id):
        self.tag_name = tag_name
        self.tag_id = tag_id

class TagSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('tag_name', 'tag_id')

tag_schema = TagSchema()
tags_schema = TagSchema(many=True)



class Content(db.Model):
    __tablename__ = 'content'
    content_id = db.Column(db.Integer, primary_key=True)
    content_type = db.Column(db.String(255))
    content_title = db.Column(db.String(255))
    instructor_id = db.Column(db.Integer)
    subject_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)
    tag_id = db.Column(db.Integer)
    content_view_count = db.Column(db.Integer)

    def __init__(self, content_id, content_type, content_title, instructor_id, subject_id, course_id, tag_id,content_view_count):
        self.content_id = content_id
        self.content_type = content_type
        self.content_title = content_title
        self.instructor_id = instructor_id
        self.subject_id = subject_id
        self.course_id = course_id
        self.tag_id = tag_id
        self.content_view_count = content_view_count

class ContentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('course_id', 'content_type', 'content_title', 'instructor_id', 'subject_id', 'course_id', 'tag_id','content_view_count')

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)

