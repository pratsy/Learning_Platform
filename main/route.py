from flask import request, jsonify
from main import app
from main.model import (
    User,
    user_schema,
    users_schema,
    UserSchema,

    Course,
    CourseSchema,
    course_schema,
    courses_schema,

    Subject,
    SubjectSchema,
    subject_schema,
    subjects_schema,

    Tag,
    TagSchema,
    tag_schema,
    tags_schema,

    Content,
    ContentSchema,
    content_schema,
    contents_schema,
    
)
from flask_marshmallow import Marshmallow
from main import db
from sqlalchemy import and_

import time
from datetime import date, datetime, timedelta


@app.route("/")
def func():
    return "working"

#-----<Validation of User APIs>--------

@app.route("/isRegisteredUserEmail/<email>", methods=["GET"])
def isRegisteredUserEmail(email):
    data = User.query.filter_by(email=email).first()
    if (data.email != email) :
        return "False"
    else :
        return "True"


#-----<User APIs>--------

@app.route("/doRegistration", methods=["POST"])
def doRegistration():

    user_id = request.json['user_id']
    user_name = request.json['user_name'].encode('ascii','ignore')
    email = request.json['email'].encode('ascii','ignore')
    user_type = request.json['user_type'].encode('ascii','ignore')

    new_user = User(user_id, user_name, email, user_type)

    db.session.add(new_user)
    db.session.commit()
    return "True"

@app.route("/getRegistration/<email>", methods=["GET"])
def reg_detail(email):
    user = User.query.get(email)
    return user_schema.jsonify(user)

@app.route("/updateRegistration/<email>", methods=["PUT"])
def reg_update(email):
    user = User.query.get(email)

    user_id = request.json['user_id']
    user_name = request.json['user_name'].encode('ascii','ignore')
    email = request.json['email'].encode('ascii','ignore')
    user_type = request.json['user_type'].encode('ascii','ignore')



    user.user_id = user_id
    user.user_name = user_name
    user.email = email
    user.user_type = user_type
 
    db.session.commit()
    return user_schema.jsonify(user)

@app.route("/deleteRegistrationEmail/<email>", methods=["DELETE"])
def user_deleteemail(email):
    user = User.query.get(email)
    db.session.delete(user)
    db.session.commit()
    return "True"


@app.route("/searchUser/<user_name>", methods=["GET"])
def searchUser(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    return user_schema.jsonify(user)


@app.route("/isUserNameAvail/<user_name>", methods=["GET"])
def isUserNameAvail(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    if (user==None):
        return "True"
    else:
        return "False"


@app.route("/getAllUsers", methods=["GET"])
def getAllUsers():
    data = User.query.all()
    result = users_schema.dump(data)
    return jsonify(a=result)


#-----<Course APIs>--------

@app.route("/doCourse", methods=["POST"])
def doCourse():

    course_name = request.json['course_name'].encode('ascii','ignore')
    course_view_count = request.json['course_view_count'].encode('ascii','ignore')

    new_course = Course(course_name, course_view_count)

    db.session.add(new_course)
    db.session.commit()
    return "True"

@app.route("/updateCourse/<course_id>", methods=["PUT"])
def updateCourse(course_id):
    course = Course.query.get(course_id)

    course_name = request.json['course_name'].encode('ascii','ignore')
    course_view_count = request.json['course_view_count'].encode('ascii','ignore')
    
    course.course_name = course_name
    course.course_view_count = course_view_count

    db.session.add(course)
    db.session.commit()
    return course_schema.jsonify(course)

@app.route("/getCourse/<course_id>", methods=["GET"])
def getCourse(course_id):
    data = Course.query.get(course_id)
    return course_schema.jsonify(data)


@app.route("/getAllCourse", methods=["GET"])
def getAllCourse():
    data = Course.query.all()
    result = courses_schema.dump(data)
    return jsonify(a=result)

@app.route("/deleteCourse/<course_id>", methods=["DELETE"])
def course_delete(course_id):
    course = Course.query.get(course_id)
    db.session.delete(course)
    db.session.commit()
    return "True"

#-----<Subject APIs>--------

@app.route("/doSubject", methods=["POST"])
def doSubject():

    subject_name = request.json['subject_name'].encode('ascii','ignore')

    new_subject = Course(subject_name)

    db.session.add(new_subject)
    db.session.commit()
    return "True"

@app.route("/updateSubject/<subject_id>", methods=["PUT"])
def updateSubject(subject_id):
    subject = Subject.query.get(subject_id)

    subject_name = request.json['subjet_name'].encode('ascii','ignore')
    
    subject.subject_name = subject_name

    db.session.add(subject)
    db.session.commit()
    return subject_schema.jsonify(subject)

@app.route("/getSubject/<subject_id>", methods=["GET"])
def getSubject(subject_id):
    data = Subject.query.get(subject_id)
    return subject_schema.jsonify(data)


@app.route("/getAllSubject", methods=["GET"])
def getAllSubject():
    data = Subject.query.all()
    result = subject_schema.dump(data)
    return jsonify(a=result)


@app.route("/deleteSubject/<subject_id>", methods=["DELETE"])
def subject_delete(subject_id):
    subject = Subject.query.get(subject_id)
    db.session.delete(subject)
    db.session.commit()
    return "True"

#-----<Tag APIs>--------

@app.route("/doTag", methods=["POST"])
def doTag():

    tag_name = request.json['tag_name'].encode('ascii','ignore')

    new_tag = Tag(tag_name)

    db.session.add(new_tag)
    db.session.commit()
    return "True"

@app.route("/updateTag/<tag_id>", methods=["PUT"])
def updateTag(tag_id):
    tag = Tag.query.get(tag_id)

    tag_name = request.json['subjet_name'].encode('ascii','ignore')
    
    tag.tag_name = tag_name

    db.session.add(tag)
    db.session.commit()
    return tag_schema.jsonify(tag)

@app.route("/getTag/<tag_id>", methods=["GET"])
def getTag(tag_id):
    data = Subject.query.get(tag_id)
    return tag_schema.jsonify(data)


@app.route("/getAllTag", methods=["GET"])
def getAllTagt():
    data = Tag.query.all()
    result = tag_schema.dump(data)
    return jsonify(a=result)


@app.route("/deleteTag/<tag_id>", methods=["DELETE"])
def tag_delete(tag_id):
    tag = Tag.query.get(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return "True"

#-----<Content - Webinar / Video APIs>--------

@app.route("/postContent", methods=["POST"])
def postContent():

    content_id = request.json['content_id']
    content_title = request.json['content_title'].encode('ascii','ignore')
    content_type = request.json['content_type'].encode('ascii','ignore')
    instructor_id = request.json['instructor_id']
    subject_id = request.json['subject_id']
    course_id = request.json['course_id']
    tag_id = request.json['tag_id']
    content_view_count = request.json['content_view_count']
    
    new_content = Content(content_id, content_title, content_type, instructor_id, subject_id, course_id, tag_id, content_view_count)

    db.session.add(new_content)
    db.session.commit()
    return "True"

@app.route("/getContentById/<content_id>", methods=["GET"])
def getContentById(content_id):
    content = Content.query.get(content_id)
    return content_schema.jsonify(content)

@app.route("/updateContent/<content_id>", methods=["PUT"])
def updateContent(content_id):
    content = Content.query.get(content_id)

    content_title = request.json['content_title'].encode('ascii','ignore')
    content_type = request.json['content_type'].encode('ascii','ignore')
    instructor_id = request.json['instructor_id']
    subject_id = request.json['subject_id']
    course_id = request.json['course_id']
    tag_id = request.json['tag_id']
    content_view_count = request.json['content_view_count']


    content.content_title = content_title
    content.content_type = content_type
    content.instructor_id = instructor_id
    content.subject_id = subject_id
    content.course_id = course_id
    content.tag_id = tag_id
    content.content_view_count = content_view_count

    db.session.commit()
    return user_schema.jsonify(content)

#-----<filter webinars & videos by course, subjects, tags>--------

@app.route("/filterContentByCourse/<course_id>/<content_type>", methods=["GET"])
def filterContentByCourse(course_id=None, content_type=None):
    data = Content.query.filter_by(course_id=course_id,content_type=content_type).first()
    return content_schema.jsonify(data)

@app.route("/filterContentBySubject/<subject_id>/<content_type>", methods=["GET"])
def filterContentBySubject(subjet_id=None, content_type=None):
    data = Content.query.filter_by(subjet_id=subject_id,content_type=content_type).first()
    return content_schema.jsonify(data)

@app.route("/filterContentByTag/<tag_id>/<content_type>", methods=["GET"])
def filterContentByTag(tag_id=None, content_type=None):
    data = Content.query.filter_by(tag_id=tag_id,content_type=content_type).first()
    return content_schema.jsonify(data)

#-----<can search webinars & videos by title>--------

# @app.route("/filterContentByTitle/<content_title>/<content_type>", methods=["GET"])
# def filterContentByTitle(content_title=None, content_type=None):
#     data = Content.query.filter(Content.content_title.ilike('%' + < content_title > + '%'),content_type=content_type).all()
#     return content_schema.jsonify(data)


