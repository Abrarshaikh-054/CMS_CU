// JS for Admission Previous Academic Information page
(function(){
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const form = document.getElementById('previousAcademicForm');
  const btnSave = document.getElementById('btnSaveAcademic');
  const alertContainer = document.getElementById('alertContainer');

  if (!form || !btnSave) return;

  const showAlert = (message, level='danger') => {
    alertContainer.innerHTML = `<div class="alert alert-${level} alert-dismissible fade show" role="alert">${message}<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`;
  };

  const showToast = () => {
    const toastEl = document.getElementById('saveToast');
    if (!toastEl) return;
    const toast = new bootstrap.Toast(toastEl);
    toast.show();
  };

  function validateForm() {
    // Required fields for 10th education
    const tenthRequiredFields = ['tenth_board', 'tenth_school', 'tenth_year', 'tenth_roll', 'tenth_marks_obtained', 'tenth_max_marks'];
    
    // Required fields for 12th education
    const twelfthRequiredFields = ['twelfth_board', 'twelfth_school', 'twelfth_year', 'twelfth_roll', 'twelfth_stream', 'twelfth_marks_obtained', 'twelfth_max_marks'];
    
    // Additional required fields
    const additionalRequiredFields = ['gap_year'];
    
    // Combine all required fields
    const requiredFields = [...tenthRequiredFields, ...twelfthRequiredFields, ...additionalRequiredFields];
    
    // Check all required fields
    for (const fieldName of requiredFields) {
      const el = document.querySelector(`[name="${fieldName}"]`);
      if (!el || !String(el.value).trim()) {
        el && el.classList.add('is-invalid');
        return false;
      } else {
        el.classList.remove('is-invalid');
      }
    }
    
    // Check if gap year is "Yes" and reason is provided
    const gapYear = document.querySelector('[name="gap_year"]');
    if (gapYear && gapYear.value === 'Yes') {
      const gapYearReason = document.querySelector('[name="gap_year_reason"]');
      if (!gapYearReason || !String(gapYearReason.value).trim()) {
        gapYearReason && gapYearReason.classList.add('is-invalid');
        return false;
      } else {
        gapYearReason.classList.remove('is-invalid');
      }
    }
    
    return true;
  }

  // Real-time field validation
  function setupRealTimeValidation() {
    // Add event listeners to all required fields
    const tenthRequiredFields = ['tenth_board', 'tenth_school', 'tenth_year', 'tenth_roll', 'tenth_marks_obtained', 'tenth_max_marks'];
    const twelfthRequiredFields = ['twelfth_board', 'twelfth_school', 'twelfth_year', 'twelfth_roll', 'twelfth_stream', 'twelfth_marks_obtained', 'twelfth_max_marks'];
    const additionalRequiredFields = ['gap_year'];
    
    const allFields = [...tenthRequiredFields, ...twelfthRequiredFields, ...additionalRequiredFields, 'gap_year_reason'];
    
    // Function to validate a field
    function validateField(field) {
      // Remove existing validation classes
      field.classList.remove('is-invalid');
      
      // Check if field is empty
      if (!field.value.trim()) {
        field.classList.add('is-invalid');
        return false;
      }
      
      // Special validation for number fields
      if (field.type === 'number' && field.value) {
        const min = parseFloat(field.getAttribute('min'));
        const max = parseFloat(field.getAttribute('max'));
        const value = parseFloat(field.value);
        
        if ((min !== null && !isNaN(min) && value < min) || 
            (max !== null && !isNaN(max) && value > max)) {
          field.classList.add('is-invalid');
          return false;
        }
      }
      
      return true;
    }
    
    // Special validation for gap year reason
    function validateGapYearReason() {
      const gapYearSelect = document.querySelector('[name="gap_year"]');
      const gapYearReason = document.querySelector('[name="gap_year_reason"]');
      
      if (gapYearSelect && gapYearSelect.value === 'Yes' && gapYearReason) {
        if (!gapYearReason.value.trim()) {
          gapYearReason.classList.add('is-invalid');
          return false;
        } else {
          gapYearReason.classList.remove('is-invalid');
        }
      }
      return true;
    }
    
    // Add event listeners for real-time validation
    allFields.forEach(fieldName => {
      const field = document.querySelector(`[name="${fieldName}"]`);
      if (field) {
        // Validate on blur
        field.addEventListener('blur', function() {
          validateField(this);
          
          // Special handling for gap year
          if (fieldName === 'gap_year') {
            validateGapYearReason();
          }
        });
        
        // Validate on input with debounce for real-time feedback
        const debounce = (fn, wait=150) => { let t; return () => { clearTimeout(t); t=setTimeout(fn, wait); }; };
        const debouncedValidate = debounce(() => {
          validateField(field);
          if (fieldName === 'gap_year') {
            validateGapYearReason();
          }
        }, 300);
        
        field.addEventListener('input', debouncedValidate);
      }
    });
  }

  // Real-time percentage calculation
  function calcPercentage(marks, max) {
    if (!marks || !max || isNaN(marks) || isNaN(max) || max == 0) return '';
    return ((parseFloat(marks) / parseFloat(max)) * 100).toFixed(2);
  }

  function setupPercentageCalculation() {
    const tenthMarksField = document.querySelector('[name="tenth_marks_obtained"]');
    const tenthMaxField = document.querySelector('[name="tenth_max_marks"]');
    const tenthPercentageField = document.querySelector('[name="tenth_percentage"]');
    
    const twelfthMarksField = document.querySelector('[name="twelfth_marks_obtained"]');
    const twelfthMaxField = document.querySelector('[name="twelfth_max_marks"]');
    const twelfthPercentageField = document.querySelector('[name="twelfth_percentage"]');

    function updateTenthPercentage() {
      if (tenthMarksField && tenthMaxField && tenthPercentageField) {
        tenthPercentageField.value = calcPercentage(tenthMarksField.value, tenthMaxField.value);
      }
    }

    function updateTwelfthPercentage() {
      if (twelfthMarksField && twelfthMaxField && twelfthPercentageField) {
        twelfthPercentageField.value = calcPercentage(twelfthMarksField.value, twelfthMaxField.value);
      }
    }

    // Add event listeners for real-time calculation
    if (tenthMarksField) tenthMarksField.addEventListener('input', updateTenthPercentage);
    if (tenthMaxField) tenthMaxField.addEventListener('input', updateTenthPercentage);
    if (twelfthMarksField) twelfthMarksField.addEventListener('input', updateTwelfthPercentage);
    if (twelfthMaxField) twelfthMaxField.addEventListener('input', updateTwelfthPercentage);

    // Initial calculation
    updateTenthPercentage();
    updateTwelfthPercentage();
  }

  // Set gapYearSelect event handler
  const gapYearSelect = document.querySelector('[name="gap_year"]');
  if (gapYearSelect) {
    gapYearSelect.id = 'gapYearSelect';
    gapYearSelect.addEventListener('change', function() {
      const reasonDiv = document.getElementById('gapYearReasonDiv');
      if (this.value === 'Yes') {
        reasonDiv.classList.remove('d-none');
      } else {
        reasonDiv.classList.add('d-none');
      }
    });
  }

  // Initialize validation and calculations
  setupRealTimeValidation();
  setupPercentageCalculation();

  btnSave.addEventListener('click', function(){
    alertContainer.innerHTML = '';
    if (!validateForm()) { showAlert('Please correct the highlighted fields.'); return; }

    const formData = new FormData(form);
    fetch(window.CMS.urls.savePreviousAcademic, {
      method: 'POST',
      headers: { 'X-CSRFToken': getCookie('csrftoken') },
      body: formData,
      credentials: 'same-origin'
    }).then(async (res) => {
      const data = await res.json().catch(()=>({ ok:false, message:'Unexpected response'}));
      if (res.ok && data.ok) {
        showToast();
        // Reload the page to show the newly saved data
        setTimeout(() => {
          window.location.reload();
        }, 1500); // Wait for toast to be visible before reload
      } else if (data.errors) {
        const firstErrField = Object.keys(data.errors)[0];
        showAlert(data.errors[firstErrField].join('<br/>'), 'danger');
      } else {
        showAlert(data.message || 'Failed to save data.', 'danger');
      }
    }).catch(() => {
      showAlert('Network error. Please try again.', 'danger');
    });
  });
})();