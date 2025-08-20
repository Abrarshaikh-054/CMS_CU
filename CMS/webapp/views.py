from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
import re

from .models import StudentAccount, StudentBasicInfo
from .forms import StudentBasicInfoForm,PreviousAcademicInfoForm


def home(request):
    return render(request, 'webapp/index.html')


def student_login(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier', '').strip()
        password = request.POST.get('password', '')

        if identifier == '' or password == '':
            messages.error(request, 'Please enter your email/mobile and password.')
            return render(request, 'webapp/student-login.html', {"identifier": identifier})

        try:
            student = StudentAccount.objects.filter(
                Q(email__iexact=identifier) | Q(mobile=identifier)
            ).first()
        except Exception:
            student = None

        if student and check_password(password, student.password):
            request.session['student_id'] = student.id
            request.session['student_name'] = f"{student.first_name} {student.last_name}"
            messages.success(request, 'Logged in successfully.')
            return redirect('admission_basic_info')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'webapp/student-login.html', {"identifier": identifier})

    return render(request, 'webapp/student-login.html')


def student_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'mobile': mobile,
        }

        # Basic required validation
        if not all([first_name, last_name, email, mobile, password, confirm_password]):
            messages.error(request, 'All fields are required.')
            return render(request, 'webapp/student-registration.html', context)

        # Email validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Please enter a valid email address.')
            return render(request, 'webapp/student-registration.html', context)

        # Mobile validation: digits only, length 10-15
        if not re.fullmatch(r"\d{10,15}", mobile):
            messages.error(request, 'Please enter a valid mobile number (10-15 digits).')
            return render(request, 'webapp/student-registration.html', context)

        # Password validation
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'webapp/student-registration.html', context)

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'webapp/student-registration.html', context)

        # Uniqueness check
        if StudentAccount.objects.filter(Q(email__iexact=email) | Q(mobile=mobile)).exists():
            messages.error(request, 'An account with this email or mobile already exists.')
            return render(request, 'webapp/student-registration.html', context)

        # Create account with hashed password
        student = StudentAccount(
            first_name=first_name,
            last_name=last_name,
            email=email.lower(),
            mobile=mobile,
            password=make_password(password),
        )
        student.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('student_login')

    return render(request, 'webapp/student-registration.html')


def student_logout(request):
    request.session.pop('student_id', None)
    request.session.pop('student_name', None)
    messages.success(request, 'You have been logged out.')
    return redirect('student_login')


def _require_student_login(request: HttpRequest):
    student_id = request.session.get('student_id')
    if not student_id:
        return False, redirect('student_login')
    try:
        student = StudentAccount.objects.get(id=student_id)
    except StudentAccount.DoesNotExist:
        return False, redirect('student_login')
    return True, student


def admission_basic_info(request: HttpRequest):
    ok, result = _require_student_login(request)
    if not ok:
        return result
    student: StudentAccount = result

    instance = getattr(student, 'basic_info', None)
    initial = {}
    if instance:
        initial['aadhar_number'] = instance.get_aadhar()
    form = StudentBasicInfoForm(instance=instance, initial=initial)
    context = {
        'form': form,
        'student_name': request.session.get('student_name', ''),
        'page_title': 'Student Admission – Basic Information',
    }
    return render(request, 'webapp/admission_basic_info.html', context)


@require_POST
def admission_basic_info_save(request: HttpRequest) -> HttpResponse:
    ok, result = _require_student_login(request)
    if not ok:
        return JsonResponse({'ok': False, 'message': 'Unauthorized'}, status=401)
    student: StudentAccount = result

    instance = getattr(student, 'basic_info', None)
    form = StudentBasicInfoForm(request.POST, instance=instance)
    if form.is_valid():
        try:
            form.save(student=student)
            return JsonResponse({'ok': True, 'message': 'Basic Information Saved Successfully'})
        except Exception as exc:
            return JsonResponse({'ok': False, 'message': 'Failed to save data.'}, status=500)
    else:
        return JsonResponse({'ok': False, 'errors': form.errors}, status=400)

def admission_previous_academic(request: HttpRequest):
    ok, result = _require_student_login(request)
    if not ok:
        return result
    student: StudentAccount = result
    return render(request, 'webapp/admission_previous_academic.html')

def admission_previous_academic(request: HttpRequest):
    ok, result = _require_student_login(request)
    if not ok:
        return result
    student: StudentAccount = result

    instance = getattr(student, 'previous_academic', None)
    form = PreviousAcademicInfoForm(instance=instance)
    
    context = {
        'form': form,
        'student_name': request.session.get('student_name', ''),
        'page_title': 'Student Admission – Previous Academic Information',
    }
    return render(request, 'webapp/admission_previous_academic.html', context)


@require_POST
def admission_previous_academic_save(request: HttpRequest) -> HttpResponse:
    ok, result = _require_student_login(request)
    if not ok:
        return JsonResponse({'ok': False, 'message': 'Unauthorized'}, status=401)
    student: StudentAccount = result

    # Always create a new entry instead of updating existing one
    # Delete existing entry if it exists
    existing = getattr(student, 'previous_academic', None)
    if existing:
        existing.delete()
    
    # Create new form without instance
    form = PreviousAcademicInfoForm(request.POST)
    
    if form.is_valid():
        try:
            form.save(student=student)
            # Reload the form with the new instance for the next page load
            updated_instance = getattr(student, 'previous_academic', None)
            request.session['academic_info_saved'] = True
            return JsonResponse({'ok': True, 'message': 'Previous Academic Information Saved Successfully'})
        except Exception as exc:
            return JsonResponse({'ok': False, 'message': 'Failed to save data.'}, status=500)
    else:
        return JsonResponse({'ok': False, 'errors': form.errors}, status=400)