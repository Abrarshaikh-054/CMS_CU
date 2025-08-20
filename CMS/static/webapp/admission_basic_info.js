// JS for Admission Basic Information page
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

  const form = document.getElementById('basicInfoForm');
  const btnSave = document.getElementById('btnSaveBasicInfo');
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

  const nameRegex = /^[A-Za-z][A-Za-z\s\-']{1,}$/;
  const aadharRegex = /^\d{12}$/;

  function validateForm() {
    const requiredFields = ['id_gender','id_dob','id_caste_category','id_caste_name','id_place_of_residence','id_nationality','id_religion','id_marital_status','id_physically_challenged','id_father_name','id_mother_name','id_ews','id_state_of_domicile'];
    for (const fid of requiredFields) {
      const el = document.getElementById(fid);
      if (!el || !String(el.value).trim()) {
        el && el.classList.add('is-invalid');
        return false;
      } else {
        el.classList.remove('is-invalid');
      }
    }
    const aadhar = document.getElementById('id_aadhar_number');
    if (!aadharRegex.test(String(aadhar.value).trim())) {
      aadhar.classList.add('is-invalid');
      return false;
    } else { aadhar.classList.remove('is-invalid'); }
    const names = ['id_father_name','id_mother_name','id_caste_name'];
    for (const nid of names) {
      const el = document.getElementById(nid);
      if (el && el.value && !nameRegex.test(String(el.value).trim())) {
        el.classList.add('is-invalid');
        return false;
      } else { el && el.classList.remove('is-invalid'); }
    }
    return true;
  }

  btnSave.addEventListener('click', function(){
    alertContainer.innerHTML = '';
    if (!validateForm()) { showAlert('Please correct the highlighted fields.'); return; }

    const formData = new FormData(form);
    fetch(window.CMS.urls.saveBasicInfo, {
      method: 'POST',
      headers: { 'X-CSRFToken': getCookie('csrftoken') },
      body: formData,
      credentials: 'same-origin'
    }).then(async (res) => {
      const data = await res.json().catch(()=>({ ok:false, message:'Unexpected response'}));
      if (res.ok && data.ok) {
        showToast();
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


