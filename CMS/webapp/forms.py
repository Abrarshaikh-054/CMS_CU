from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

from .models import (
    StudentBasicInfo,
    GenderOption,
    CasteCategory,
    SpecialCategory,
    Nationality,
    BloodGroup,
    Religion,
    State,
    PreviousAcademicInfo,
)


NAME_REGEX = r"^[A-Za-z][A-Za-z\s]{1,}$"


class StudentBasicInfoForm(forms.ModelForm):
    aadhar_number = forms.CharField(
        label=_('Aadhar Number'),
        max_length=12,
        min_length=12,
        required=True,
        widget=forms.TextInput(attrs={'inputmode': 'numeric', 'pattern': '\\d{12}'}),
    )

    class Meta:
        model = StudentBasicInfo
        fields = [
            'gender', 'dob', 'caste_category', 'caste_name', 'special_category',
            'place_of_residence', 'nationality', 'blood_group', 'religion',
            'marital_status', 'physically_challenged', 'father_name', 'mother_name',
            'ews', 'state_of_domicile',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamic querysets for dropdowns
        self.fields['gender'].queryset = GenderOption.objects.filter(is_active=True).order_by('name')
        self.fields['caste_category'].queryset = CasteCategory.objects.filter(is_active=True).order_by('name')
        self.fields['special_category'].queryset = SpecialCategory.objects.filter(is_active=True).order_by('name')
        self.fields['nationality'].queryset = Nationality.objects.filter(is_active=True).order_by('name')
        self.fields['blood_group'].queryset = BloodGroup.objects.filter(is_active=True).order_by('name')
        self.fields['religion'].queryset = Religion.objects.filter(is_active=True).order_by('name')
        # state_of_domicile now a CharField text input

        required_fields = [
            'gender', 'dob', 'caste_category', 'caste_name', 'place_of_residence',
            'nationality', 'religion', 'marital_status', 'physically_challenged',
            'father_name', 'mother_name', 'ews', 'state_of_domicile',
        ]
        for field_name in required_fields:
            self.fields[field_name].required = True

        # Add Bootstrap classes
        for name, field in self.fields.items():
            widget = field.widget
            classes = widget.attrs.get('class', '')
            if isinstance(field, (forms.ModelChoiceField, forms.ChoiceField)) and name != 'aadhar_number':
                widget.attrs['class'] = f"{classes} form-select".strip()
            else:
                widget.attrs['class'] = f"{classes} form-control".strip()

    def clean_aadhar_number(self):
        value = (self.cleaned_data.get('aadhar_number') or '').strip()
        if not value.isdigit() or len(value) != 12:
            raise ValidationError(_('Aadhar must be exactly 12 digits.'))
        return value

    def _validate_name(self, field_name: str):
        value = (self.cleaned_data.get(field_name) or '').strip()
        if value and not re.compile(NAME_REGEX).match(value):
            raise ValidationError(_('Only alphabets, spaces, hyphens and apostrophes are allowed.'))
        return value

    def clean_father_name(self):
        return self._validate_name('father_name')

    def clean_mother_name(self):
        return self._validate_name('mother_name')

    def clean_caste_name(self):
        return self._validate_name('caste_name')

    def save(self, student, commit=True):
        instance = super().save(commit=False)
        instance.student = student
        aadhar_plain = self.cleaned_data.get('aadhar_number')
        instance.set_aadhar(aadhar_plain)
        if commit:
            instance.save()
        return instance

class PreviousAcademicInfoForm(forms.ModelForm):
    class Meta:
        model = PreviousAcademicInfo
        exclude = ['student', 'tenth_percentage', 'twelfth_percentage', 'created_at', 'updated_at']
        widgets = {
            'tenth_year': forms.NumberInput(attrs={'min': '1900', 'max': '2099'}),
            'twelfth_year': forms.NumberInput(attrs={'min': '1900', 'max': '2099'}),
            'tenth_marks_obtained': forms.NumberInput(attrs={'min': '0'}),
            'tenth_max_marks': forms.NumberInput(attrs={'min': '0'}),
            'twelfth_marks_obtained': forms.NumberInput(attrs={'min': '0'}),
            'twelfth_max_marks': forms.NumberInput(attrs={'min': '0'}),
            'gap_year_reason': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes
        for name, field in self.fields.items():
            widget = field.widget
            classes = widget.attrs.get('class', '')
            if isinstance(widget, forms.Select):
                widget.attrs['class'] = f"{classes} form-select".strip()
            else:
                widget.attrs['class'] = f"{classes} form-control".strip()
                
        # Set required fields
        required_fields = [
            'tenth_board', 'tenth_school', 'tenth_year', 'tenth_roll',
            'tenth_marks_obtained', 'tenth_max_marks', 'twelfth_board',
            'twelfth_school', 'twelfth_year', 'twelfth_roll', 'twelfth_stream',
            'twelfth_marks_obtained', 'twelfth_max_marks', 'gap_year'
        ]
        for field_name in required_fields:
            self.fields[field_name].required = True

    def clean(self):
        cleaned_data = super().clean()
        
        # Validate gap year reason if gap year is "Yes"
        gap_year = cleaned_data.get('gap_year')
        gap_year_reason = cleaned_data.get('gap_year_reason')
        
        if gap_year == 'Yes' and not gap_year_reason:
            self.add_error('gap_year_reason', 'Reason is required if gap year is "Yes"')
            
        return cleaned_data

    def save(self, student, commit=True):
        instance = super().save(commit=False)
        instance.student = student
        
        # Calculate percentages
        tenth_marks = self.cleaned_data.get('tenth_marks_obtained')
        tenth_max = self.cleaned_data.get('tenth_max_marks')
        if tenth_marks and tenth_max:
            instance.tenth_percentage = (tenth_marks / tenth_max) * 100
            
        twelfth_marks = self.cleaned_data.get('twelfth_marks_obtained')
        twelfth_max = self.cleaned_data.get('twelfth_max_marks')
        if twelfth_marks and twelfth_max:
            instance.twelfth_percentage = (twelfth_marks / twelfth_max) * 100
        
        if commit:
            instance.save()
        return instance
