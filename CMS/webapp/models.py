# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.conf import settings

try:
    from cryptography.fernet import Fernet
    import base64
    import hashlib
except Exception:  # pragma: no cover
    Fernet = None


class AcademicSession(models.Model):
    session_name = models.CharField(max_length=250)
    course_id = models.IntegerField()
    strtdate = models.DateField()
    enddate = models.DateField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'academic_session'


class AllCourses(models.Model):
    course_name = models.CharField(max_length=250, blank=True, null=True)
    course_type = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    active_status = models.IntegerField()
    exam_active = models.IntegerField()
    reg_active = models.IntegerField()
    pgexam_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'all_courses'


class AlumniPayments(models.Model):
    alumni_id = models.BigIntegerField()
    name = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=250)
    payment_type = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=50, blank=True, null=True)
    paymentid = models.CharField(max_length=250, blank=True, null=True)
    txnid = models.CharField(max_length=250, blank=True, null=True)
    bank_name = models.CharField(max_length=250, blank=True, null=True)
    mmp_txn = models.CharField(max_length=250, blank=True, null=True)
    response = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alumni_payments'


class Alumnis(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=250)
    email = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    whatsapp = models.CharField(max_length=11)
    mob = models.CharField(max_length=250, blank=True, null=True)
    year_passing = models.CharField(max_length=250, blank=True, null=True)
    dob = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    course_tnb = models.CharField(max_length=250, blank=True, null=True)
    marital = models.CharField(max_length=250, blank=True, null=True)
    age_date = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField()
    pres_prof = models.CharField(max_length=250)
    organization = models.CharField(max_length=250)
    present_work = models.CharField(max_length=250)
    nostalgia = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alumnis'


class Application(models.Model):
    college_code = models.IntegerField()
    class_roll = models.CharField(max_length=50, blank=True, null=True)
    coursenameid = models.IntegerField()
    ofss_reference = models.CharField(max_length=250, blank=True, null=True)
    verified_ofss = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    session = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    personal_info = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    proposed_subject = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    previous_academic = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    marksheet = models.CharField(max_length=250, blank=True, null=True)
    tc_clc = models.CharField(max_length=250, blank=True, null=True)
    caste_certificate = models.CharField(max_length=250, blank=True, null=True)
    ppu_offer_letter = models.CharField(max_length=250, blank=True, null=True)
    twelveth_marksheet = models.CharField(max_length=250, blank=True, null=True)
    migration_certificate = models.CharField(max_length=250, blank=True, null=True)
    ph_certificate = models.CharField(max_length=250, blank=True, null=True)
    income_certificate = models.CharField(max_length=250, blank=True, null=True)
    app_status = models.IntegerField()
    flag = models.IntegerField()
    adm_verify = models.IntegerField()
    merit_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'application'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banners(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250, blank=True, null=True)
    alt = models.CharField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    image = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'banners'


class Certificates(models.Model):
    user_id = models.IntegerField()
    previous_record = models.TextField(blank=True, null=True)
    certify = models.CharField(max_length=250, blank=True, null=True)
    serial_number = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    flag = models.IntegerField()
    issue_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificates'


class Cms(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=191)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    meta_title = models.CharField(max_length=191, blank=True, null=True)
    meta_keywords = models.CharField(max_length=191, blank=True, null=True)
    meta_description = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    template = models.CharField(max_length=191)
    image_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms'


class CommanSettings(models.Model):
    name = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comman_settings'


class CouponCode(models.Model):
    couponcode = models.CharField(max_length=250)
    status = models.IntegerField()
    user_id = models.IntegerField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupon_code'


class Coursedetails(models.Model):
    course_id = models.IntegerField()
    paper_code = models.TextField()
    topic = models.CharField(max_length=250)
    format = models.CharField(max_length=250)
    pro_name = models.CharField(max_length=250)
    contact_details = models.TextField()
    uploadfile = models.CharField(max_length=250, blank=True, null=True)
    youtube_link = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coursedetails'


class Courses(models.Model):
    courseid = models.IntegerField()
    title = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    hons_sub = models.CharField(max_length=250, blank=True, null=True)
    class_type = models.CharField(max_length=250, blank=True, null=True)
    tc_flag = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    reg_status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'courses'


class Coursetypes(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coursetypes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ETenders(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    address = models.TextField()
    uploadpdf = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_tenders'


class ExamPayments(models.Model):
    application_id = models.IntegerField()
    user_id = models.IntegerField()
    applicant_id = models.BigIntegerField()
    name = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=250)
    course = models.CharField(max_length=250, blank=True, null=True)
    payment_type = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=50, blank=True, null=True)
    paymentid = models.CharField(max_length=250, blank=True, null=True)
    txnid = models.CharField(max_length=250, blank=True, null=True)
    bank_name = models.CharField(max_length=250, blank=True, null=True)
    mmp_txn = models.CharField(max_length=250, blank=True, null=True)
    coursetype = models.CharField(max_length=50, blank=True, null=True)
    class_type = models.CharField(max_length=50, blank=True, null=True)
    session_year = models.CharField(max_length=50, blank=True, null=True)
    response = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'exam_payments'


class Examination(models.Model):
    regis_number = models.CharField(max_length=100, blank=True, null=True)
    class_roll = models.IntegerField()
    application_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    coursenameid = models.IntegerField()
    course_id = models.IntegerField()
    course_hons = models.CharField(max_length=100, blank=True, null=True)
    college_name = models.CharField(max_length=250, blank=True, null=True)
    student_type = models.CharField(max_length=250, blank=True, null=True)
    session = models.CharField(max_length=250, blank=True, null=True)
    exam_form = models.TextField(blank=True, null=True)
    previous_record = models.TextField(blank=True, null=True)
    exam_subject = models.TextField(blank=True, null=True)
    personal_info = models.TextField(blank=True, null=True)
    previous_academic = models.TextField(blank=True, null=True)
    proposed_subject = models.TextField(blank=True, null=True)
    marksheet = models.CharField(max_length=250, blank=True, null=True)
    tc_clc = models.CharField(max_length=250, blank=True, null=True)
    caste_certificate = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'examination'


class Genralsettings(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genralsettings'


class Helpdesk(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    mobile = models.CharField(max_length=50)
    description = models.TextField()
    replyus = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helpdesk'


class Information(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True, null=True)
    view_details_button = models.CharField(max_length=250, blank=True, null=True)
    view_details_link = models.CharField(max_length=250, blank=True, null=True)
    new_register_button = models.CharField(max_length=250, blank=True, null=True)
    new_register_link = models.CharField(max_length=250, blank=True, null=True)
    undertaking_button = models.CharField(max_length=250, blank=True, null=True)
    undertaking_link = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'information'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class MiscellaneousDetails(models.Model):
    miscellaneous_id = models.IntegerField()
    name = models.CharField(max_length=250)
    amount = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'miscellaneous_details'


class Miscellaneouses(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'miscellaneouses'


class MissPayments(models.Model):
    course = models.IntegerField()
    coursename = models.IntegerField()
    user_id = models.IntegerField()
    applicant_id = models.BigIntegerField()
    name = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=250)
    payment_type = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=50, blank=True, null=True)
    paymentid = models.CharField(max_length=250, blank=True, null=True)
    txnid = models.CharField(max_length=250, blank=True, null=True)
    bank_name = models.CharField(max_length=250, blank=True, null=True)
    mmp_txn = models.CharField(max_length=250, blank=True, null=True)
    response = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'miss_payments'


"""
The following three tables in the source database use composite primary keys
(e.g. from external auth/permission packages). Django does not support composite
primary keys. To avoid invalid import errors, these models are omitted. If you
need to query them, create database views or use raw SQL in a separate module.
Omitted tables:
  - model_has_permissions
  - model_has_roles
  - role_has_permissions
"""


class Notices(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True, null=True)
    alt = models.CharField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    image = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notices'


class OfssAdmissionMeritlist(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    reference_number = models.CharField(max_length=250)
    course_id = models.IntegerField(blank=True, null=True)
    applicant_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250, blank=True, null=True)
    college_code = models.CharField(max_length=250, blank=True, null=True)
    academic_year = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=250)
    honours = models.CharField(max_length=100, blank=True, null=True)
    mic = models.CharField(max_length=250, blank=True, null=True)
    mdc = models.CharField(max_length=250, blank=True, null=True)
    aec = models.CharField(max_length=250, blank=True, null=True)
    vac = models.CharField(max_length=250, blank=True, null=True)
    sec = models.CharField(max_length=250, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    adminssion_date = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    adm_list = models.CharField(max_length=50, blank=True, null=True)
    adm_type = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ofss_admission_meritlist'


class OfssRegistration(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField()
    session_year = models.CharField(max_length=50, blank=True, null=True)
    regis_number = models.CharField(max_length=250)
    applicant_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250, blank=True, null=True)
    mother_name = models.CharField(max_length=250, blank=True, null=True)
    college_name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ofss_registration'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Payment(models.Model):
    application_id = models.IntegerField()
    user_id = models.IntegerField()
    applicant_id = models.BigIntegerField()
    name = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=250)
    course = models.CharField(max_length=250, blank=True, null=True)
    payment_type = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=50, blank=True, null=True)
    paymentid = models.CharField(max_length=250, blank=True, null=True)
    txnid = models.CharField(max_length=250, blank=True, null=True)
    bank_name = models.CharField(max_length=250, blank=True, null=True)
    mmp_txn = models.CharField(max_length=250, blank=True, null=True)
    coursetype = models.CharField(max_length=50, blank=True, null=True)
    class_type = models.CharField(max_length=50, blank=True, null=True)
    session_year = models.CharField(max_length=50, blank=True, null=True)
    admission_type = models.IntegerField(blank=True, null=True)
    college_code = models.IntegerField()
    rollnum = models.IntegerField()
    response = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'


class Permissions(models.Model):
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Registration(models.Model):
    ofss_reference = models.CharField(max_length=250, blank=True, null=True)
    application_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    college_code = models.IntegerField()
    coursenameid = models.IntegerField()
    course_id = models.IntegerField()
    session = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    personal_info = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    proposed_subject = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    previous_academic = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registration'


class RegistrationPayments(models.Model):
    application_id = models.IntegerField()
    user_id = models.IntegerField()
    applicant_id = models.BigIntegerField()
    name = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=250)
    course = models.CharField(max_length=250, blank=True, null=True)
    payment_type = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=50, blank=True, null=True)
    paymentid = models.CharField(max_length=250, blank=True, null=True)
    txnid = models.CharField(max_length=250, blank=True, null=True)
    bank_name = models.CharField(max_length=250, blank=True, null=True)
    mmp_txn = models.CharField(max_length=250, blank=True, null=True)
    coursetype = models.CharField(max_length=50, blank=True, null=True)
    class_type = models.CharField(max_length=50, blank=True, null=True)
    session_year = models.CharField(max_length=50, blank=True, null=True)
    response = models.IntegerField()
    refnum = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registration_payments'


pass


class Roles(models.Model):
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Studentdetails(models.Model):
    user_id = models.IntegerField()
    basic_info = models.TextField(blank=True, null=True)
    photo = models.CharField(max_length=250, blank=True, null=True)
    signature = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentdetails'


class Students(models.Model):
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    dob = models.CharField(max_length=250, blank=True, null=True)
    password = models.CharField(max_length=191)
    phone = models.BigIntegerField()
    applicantid = models.CharField(max_length=12)
    apaar_id = models.BigIntegerField()
    pass_word = models.CharField(max_length=191, blank=True, null=True)
    remember_token = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class SubjectsCombinations(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subjects_combinations'


class TcPayments(models.Model):
    application_id = models.IntegerField()
    user_id = models.IntegerField()
    applicant_id = models.BigIntegerField()
    name = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=250)
    payment_type = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=50, blank=True, null=True)
    paymentid = models.CharField(max_length=250, blank=True, null=True)
    txnid = models.CharField(max_length=250, blank=True, null=True)
    bank_name = models.CharField(max_length=250, blank=True, null=True)
    mmp_txn = models.CharField(max_length=250, blank=True, null=True)
    response = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tc_payments'


class Users(models.Model):
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    phone = models.BigIntegerField(blank=True, null=True)
    applicantid = models.CharField(max_length=12, blank=True, null=True)
    profile_image = models.CharField(max_length=250, blank=True, null=True)
    signature = models.CharField(max_length=250, db_collation='utf8_general_ci', blank=True, null=True)
    signaturehindi = models.CharField(max_length=250, blank=True, null=True)
    pass_word = models.CharField(max_length=191, blank=True, null=True)
    remember_token = models.CharField(max_length=191, blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Webinarfeedbacks(models.Model):
    email = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    candidate = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    webinartopic = models.CharField(max_length=250)
    speakers = models.CharField(max_length=250)
    problemfaced = models.CharField(max_length=250)
    management = models.CharField(max_length=250)
    watchwebinar = models.CharField(max_length=250)
    home_message = models.CharField(max_length=250)
    suggestions = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'webinarfeedbacks'


class Webinars(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    affiliate = models.CharField(max_length=250)
    category = models.IntegerField()
    department = models.IntegerField()
    qualification = models.IntegerField()
    address = models.TextField()
    presentation = models.TextField()
    uploadpdf = models.CharField(max_length=250)
    profileimage = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'webinars'


# Managed model for student authentication within this app
class StudentAccount(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student_accounts'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['mobile']),
        ]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


# ----- Lookup tables for dropdowns (managed) -----
class GenderOption(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'gender_options'

    def __str__(self) -> str:
        return self.name


class CasteCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'caste_categories'

    def __str__(self) -> str:
        return self.name


class SpecialCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'special_categories'

    def __str__(self) -> str:
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'nationalities'

    def __str__(self) -> str:
        return self.name


class BloodGroup(models.Model):
    name = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'blood_groups'

    def __str__(self) -> str:
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'religions'

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'states'

    def __str__(self) -> str:
        return self.name


def _get_fernet():
    if Fernet is None:
        return None
    # Derive a stable 32-byte key from SECRET_KEY using SHA256
    secret = getattr(settings, 'SECRET_KEY', 'cms-default-secret').encode('utf-8')
    digest = hashlib.sha256(secret).digest()
    key = base64.urlsafe_b64encode(digest)
    return Fernet(key)


class StudentBasicInfo(models.Model):
    RESIDENCE_CHOICES = (
        ('Urban', 'Urban'),
        ('Rural', 'Rural'),
        ('Hill', 'Hill'),
    )
    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    MARITAL_CHOICES = (
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
        ('Divorced', 'Divorced'),
    )

    student = models.OneToOneField(StudentAccount, on_delete=models.CASCADE, related_name='basic_info')
    gender = models.ForeignKey(GenderOption, on_delete=models.PROTECT)
    dob = models.DateField()
    caste_category = models.ForeignKey(CasteCategory, on_delete=models.PROTECT)
    caste_name = models.CharField(max_length=100)
    special_category = models.ForeignKey(SpecialCategory, on_delete=models.PROTECT, null=True, blank=True)
    place_of_residence = models.CharField(max_length=10, choices=RESIDENCE_CHOICES)
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.PROTECT, null=True, blank=True)
    religion = models.ForeignKey(Religion, on_delete=models.PROTECT)
    marital_status = models.CharField(max_length=10, choices=MARITAL_CHOICES)
    physically_challenged = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    aadhar_encrypted = models.BinaryField(null=True, blank=True)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    ews = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    state_of_domicile = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student_basic_info'

    def set_aadhar(self, aadhar_plain: str) -> None:
        aadhar_str = (aadhar_plain or '').strip()
        if not aadhar_str:
            self.aadhar_encrypted = None
            return
        f = _get_fernet()
        if f is None:
            # Fallback to storing as bytes of the string reversed (not secure). Strongly recommend installing cryptography.
            self.aadhar_encrypted = aadhar_str[::-1].encode('utf-8')
        else:
            self.aadhar_encrypted = f.encrypt(aadhar_str.encode('utf-8'))

    def get_aadhar(self) -> str:
        if not self.aadhar_encrypted:
            return ''
        f = _get_fernet()
        try:
            if f is None:
                return self.aadhar_encrypted.decode('utf-8')[::-1]
            return f.decrypt(bytes(self.aadhar_encrypted)).decode('utf-8')
        except Exception:
            return ''

class PreviousAcademicInfo(models.Model):
    STREAM_CHOICES = (
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
        ('Other', 'Other'),
    )
    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    student = models.OneToOneField(StudentAccount, on_delete=models.CASCADE, related_name='previous_academic')
    
    # 10th details
    tenth_board = models.CharField(max_length=200)
    tenth_school = models.CharField(max_length=250)
    tenth_year = models.PositiveIntegerField()
    tenth_roll = models.CharField(max_length=50)
    tenth_marks_obtained = models.DecimalField(max_digits=6, decimal_places=2)
    tenth_max_marks = models.DecimalField(max_digits=6, decimal_places=2)
    tenth_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    # 12th details
    twelfth_board = models.CharField(max_length=200)
    twelfth_school = models.CharField(max_length=250)
    twelfth_year = models.PositiveIntegerField()
    twelfth_roll = models.CharField(max_length=50)
    twelfth_stream = models.CharField(max_length=20, choices=STREAM_CHOICES)
    twelfth_marks_obtained = models.DecimalField(max_digits=6, decimal_places=2)
    twelfth_max_marks = models.DecimalField(max_digits=6, decimal_places=2)
    twelfth_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    # Additional information
    entrance_exam_name = models.CharField(max_length=100, blank=True, null=True)
    entrance_exam_roll = models.CharField(max_length=50, blank=True, null=True)
    entrance_exam_score = models.CharField(max_length=50, blank=True, null=True)
    gap_year = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    gap_year_reason = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student_academic_info'

    def save(self, *args, **kwargs):
        # Calculate percentages
        if self.tenth_marks_obtained and self.tenth_max_marks:
            self.tenth_percentage = (self.tenth_marks_obtained / self.tenth_max_marks) * 100
        
        if self.twelfth_marks_obtained and self.twelfth_max_marks:
            self.twelfth_percentage = (self.twelfth_marks_obtained / self.twelfth_max_marks) * 100
        
        super().save(*args, **kwargs)
