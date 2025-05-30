# -*- coding: utf-8 -*-

from __future__ import absolute_import
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.static import serve
from django.contrib.auth import views as django_auth_views
from common.forms import ChangePasswordForm, RecoverUserForm, CustomPasswordResetForm
from candidates import views as candidates_views
from common import views as common_views
from common import ajax as common_ajax_views
from companies import views as companies_views
from activities import views as activities_views
from TRM import views as TRM_views
from example import views as example_views
from payments import views as payments_views
from vacancies import views as vacancy_views
# from socialmultishare import views as socialmultishare_views
from TRM import settings
# from django.views.generic.simple import direct_to_template
from companies.views import upload_vacancy_file, delete_vacancy_file

admin.autodiscover()
handler500 = 'TRM.views.handler500'

urlpatterns = [

    # Index
    # url(r'^$', vacancy_views.search_vacancies, {'template_name': 'index.html'}, name='TRM-index'),
    path('', companies_views.VacanciesSummaryView.as_view(), name='TRM-Subindex'),
    path('activities/', activities_views.ActivitiesView.as_view(), name="activity_view"),
    path('activities/<int:activity_id>/', activities_views.ActivitiesView.as_view(), name="activity_view"),

    # Static files
    path('robots.txt', TRM_views.RobotsTxtView.as_view()),
    path('sitemap.xml', TRM_views.SitemapXmlView.as_view()),
    path('google7467b69f25fa8f1e.html', TRM_views.GoogleVerificationView.as_view()),
    path('aboutus/',  TRM_views.about_us, name="about_us"),
    path('product/',  TRM_views.product, name="product"),
    path('pricing/',  TRM_views.pricing, name="pricing"),
    path('contact/',  TRM_views.contact, name="contact"),
    path('comingsoon/',  TRM_views.comingsoon, name="comingsoon"),
    path('jobs/',  TRM_views.job_board, name="job_board"),
    path('resources/comments/', include('django_comments.urls')),
    path('modal/', TRM_views.ModalView.as_view()),

    # Candidates - candidates.views.py
    path('signup/talent/', candidates_views.record_candidate, name='candidates_register_candidate'),
    path('profile/', candidates_views.edit_curriculum, name='candidates_edit_curriculum'),
    path('profile/pdf/<int:candidate_id>/', candidates_views.curriculum_to_pdf, name='vacancies_curriculum_to_pdf'),
    path('appliedjobs/', candidates_views.vacancies_postulated, name='candidates_vacancies_postuladed'),
    path('applylater/', candidates_views.vacancies_favorites, name='candidates_vacancies_favourites'),
    
    # Common - Django Contrib Auth
    # url(r'^', include('common.common_auth_urls')),
    path('login/', django_auth_views.LoginView.as_view(), name='auth_login'),
    path('logout/', django_auth_views.LogoutView.as_view(), name='auth_logout'),
    path('password/change/', django_auth_views.PasswordChangeView.as_view(), name='auth_password_change'),
    path('password/reset/', django_auth_views.PasswordResetView.as_view(), name='auth_password_reset'),
    path('password/reset/<uidb64>[0-9A-Za-z]+>-<token>.+/',
        django_auth_views.PasswordResetConfirmView.as_view(),
        name='auth_password_reset_confirm'),
    path('password/reset/done/', django_auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('username/recover/', django_auth_views.PasswordResetView.as_view(), name='recover_user'),

    # Common - common.views.py
    path('login/social/<str:social_code>/', common_views.social_login, name="social_login"),
    path('login/social/<str:social_code>/<int:vacancy_id>/', common_views.social_login, name="social_login"),
    path('login/social/<str:social_code>/<int:vacancy_id>/<int:recruiter_id>/', common_views.social_login, name="social_login"),
    path('redirect/', common_views.redirect_after_login, name='common_redirect_after_login'),
    path('signup/completed/', common_views.registration_complete, name='common_registration_complete'),
    path('email/change/', common_views.email_change, name='common_email_change'),
    path('email/changerequested/', common_views.email_change_requested, name='common_email_change_requested'),
    path('email/verify/<str:token>/<str:code>/', common_views.email_change_approve,
        name='common_email_change_approve'),
    path('activate/<str:activation_key>/', common_views.registration_activate, name='common_registration_activate'),
    path('password/changed/', common_views.password_change_done, name='common_password_change_done'),
    path('password/reset/completed/', common_views.custom_password_reset_complete, name='custom_password_reset_complete'),
    path('username/recover/requested/', common_views.recover_user_requested, name='common_recover_user_requested'),
    # url(r'^contactus/$', common_views.ContactFormView.as_view(), name='common_contact_form'),
    # url(r'^sent/$', TemplateView.as_view(template_name='contact_form_sent.html'), name='common_contact_form_sent'),
    # url(r'^register_email/$', common_views.register_blank_email, name='common_register_blank_email'),

    # Common Ajax - common.ajax.py
    path('ajax/login/', common_ajax_views.ajax_login, name='ajax_login'),
    path('ajax/companies-change-academic-area/', common_ajax_views.companies_change_academic_area),
    path('ajax/companies-allow-career/', common_ajax_views.companies_allow_career),
    # url(r'^ajax/companies-change-state/$', common_ajax_views.companies_change_state),
    path('ajax/candidates-change-degree/', common_ajax_views.candidates_change_degree),
    # url(r'^ajax/candidates-change-career/$', common_ajax_views.candidates_change_career),
    path('ajax/candidates-change-academic-status/', common_ajax_views.candidates_change_academic_status),
    # url(r'^ajax/get-company-areas/$', common_ajax_views.get_company_areas),
    path('ajax/vacancies-postulate/', common_ajax_views.vacancies_postulate),
    # url(r'^ajax/get-municipals/$', common_ajax_views.get_municipals),
    # url(r'^ajax/get-common-areas/$', common_ajax_views.get_common_areas),
    path('ajax/get-salarytype-codename/', common_ajax_views.get_salarytype_codename),
    path('ajax/vacancies-answer-question/', common_ajax_views.vacancies_answer_question),
    path('ajax/mark-vacancy-asfavorite/', common_ajax_views.mark_unmark_vacancy_as_favorite),
    path('ajax/addstage/', common_ajax_views.add_stage),
    path('ajax/validate_personal_form/',common_ajax_views.validate_personal_form),
    path('ajax/validate_contact_form/',common_ajax_views.validate_contact_form),
    path('ajax/validate_academic_form/',common_ajax_views.validate_academic_form),
    path('ajax/validate_experience_form/',common_ajax_views.validate_experience_form),
    path('ajax/validate_training_form/',common_ajax_views.validate_training_form),
    path('ajax/validate_project_form/',common_ajax_views.validate_project_form),
    path('ajax/validate_certificate_form/',common_ajax_views.validate_certificate_form),
    path('ajax/validate_objective_form/',common_ajax_views.validate_objective_form),
    path('ajax/validate_interests_form/',common_ajax_views.validate_interests_form),
    path('ajax/validate_hobbies_form/',common_ajax_views.validate_hobbies_form),
    path('ajax/validate_extra_curriculars_form/',common_ajax_views.validate_extra_curriculars_form),
    path('ajax/validate_others_form/',common_ajax_views.validate_others_form),
    path('ajax/validate_language_form/',common_ajax_views.validate_language_form),
    path('ajax/updatevacancystage/', common_ajax_views.update_vacancy_stage),
    path('ajax/upgradepostulate/', common_ajax_views.upgrade_postulate),
    path('ajax/downgradepostulate/', common_ajax_views.downgrade_postulate),
    path('ajax/archivepostulate/', common_ajax_views.archive_postulate),
    path('ajax/delete_section/',common_ajax_views.delete_section),
    path('ajax/publicapplication/', common_ajax_views.public_application),
    path('ajax/updatepermissions/', common_ajax_views.update_permissions),
    path('ajax/removemember/', common_ajax_views.remove_member),
    path('ajax/changeownership/', common_ajax_views.change_ownership),
    path('ajax/addmembertojob/', common_ajax_views.add_member_to_job),
    path('ajax/removememberfromjob/', common_ajax_views.remove_member_from_job),
    path('ajax/addmembertojobprocess/', common_ajax_views.add_member_to_job_process),
    path('ajax/removememberfromjobprocess/', common_ajax_views.remove_member_from_job_process),
    path('ajax/updatecriteria/', common_ajax_views.update_criteria),
    path('ajax/comment/', common_ajax_views.comment),
    path('ajax/comment/retrieveall/', common_ajax_views.retreive_comments),
    path('ajax/rate/', common_ajax_views.rate),
    path('ajax/spot/', common_ajax_views.spot),
    path('ajax/rate/retrieveall/', common_ajax_views.retreive_ratings),
    path('ajax/tag/', common_ajax_views.tag),
    path('ajax/get-schedule/', common_ajax_views.get_upcoming_schedule),
    path('ajax/schedule/', common_ajax_views.schedule),
    path('ajax/remove-schedule/', common_ajax_views.remove_schedule),
    path('ajax/withdraw/', common_ajax_views.withdraw),
    path('ajax/filter-candidates/', common_ajax_views.filter_candidates),
    path('ajax/post/', common_ajax_views.post_message_to_stream),
    path('ajax/mark_as_read/', common_ajax_views.mark_as_read),
    path('ajax/set_plan/', common_ajax_views.set_plan),
    path('ajax/verify_code/', common_ajax_views.verify_code),
    path('ajax/update_recurring/', common_ajax_views.update_recurring),
    path('ajax/renew_now/', common_ajax_views.renew_now),
    path('ajax/smart-share/<int:id>/', common_ajax_views.smart_share),
    path('ajax/socialshare/', common_ajax_views.socialshare),
    path('ajax/revokesocial/<str:social_code>/', common_ajax_views.revoke_social_auth),
    path('ajax/template/', common_ajax_views.custom_template),
    path('ajax/template-form/', common_ajax_views.template_form),
    path('ajax/get-candidate-form-data/', common_ajax_views.template_form_data),
    path('ajax/updatesitetemplate/', common_ajax_views.update_site_template),
    path('ajax/save_template/', common_ajax_views.save_template),
    path('ajax/get_evaluators/', common_ajax_views.get_evaluators),
    path('ajax/get_process_criterias/', common_ajax_views.get_process_criterias),
    path('ajax/resolve_conflicts_delete/', common_ajax_views.resolve_conflicts_delete),
    path('ajax/resolve_conflicts_unconflict/', common_ajax_views.resolve_conflicts_unconflict),
    path('ajax/resolve_conflicts_merge/', common_ajax_views.resolve_conflicts_merge),
    path('ajax/add_external_referal/', common_ajax_views.add_external_referal),
    path('ajax/remove_external_referal/', common_ajax_views.remove_external_referal),

    # Companies - companies.views.py
    path('signup/employer/', companies_views.record_recruiter, name='companies_record_recruiter'),
    path('signup/employer/<str:token>/', companies_views.record_recruiter, name='companies_recruiter_invitation'),
    path('profile/company/create/', companies_views.record_company, name='companies_record_company'),
    path('profile/employer/', companies_views.recruiter_profile, name='companies_recruiter_profile'),
    path('profile/company/', companies_views.company_profile, name='companies_company_profile'),
    path('careerssite/editor/', companies_views.template_editor, name="companies_edit_template"),
    path('careerssite/get_site_template/', companies_views.get_site_template, name="companies_get_site_template"),
    path('careerssite/preview/<int:template_id>/', companies_views.site_template_preview, name="companies_site_template_preview"),
    path('careerssite/<str:setting>/', companies_views.site_management, name='companies_site_management'),
    path('team/', companies_views.team_space, name = 'companies_company_team_space'),
    path('billing/', companies_views.billing, name = 'companies_billing'),
    path('payment/', payments_views.payment, name = 'companies_payment'),
    path('checkout/', payments_views.checkout, name = 'payments_checkout'),
    path('job/edit/', companies_views.add_update_vacancy, name='companies_add_update_vacancy'),
    path('job/edit/<int:vacancy_id>/', companies_views.add_update_vacancy, name='companies_add_update_vacancy'),
    path('job/edit_hiring_process/<int:vacancy_id>/', companies_views.add_update_vacancy_hiring_process, name='companies_add_update_vacancy_hiring_process'),
    path('job/edit_talent_sourcing/<int:vacancy_id>/', companies_views.add_update_vacancy_talent_sourcing, name='companies_add_update_vacancy_talent_sourcing'),
    path('Finalizevacancy/<int:vacancy_id>/<str:message>/', companies_views.finalize_vacancy, name='companies_finalize_vacancy'),
    path('Publishvacancy/<int:vacancy_id>/', companies_views.publish_vacancy, name='companies_publish_vacancy'),
    path('UnPublishvacancy/<int:vacancy_id>/', companies_views.unpublish_vacancy, name='companies_unpublish_vacancy'),
    path('profile/candidate/<int:candidate_id>/', companies_views.curriculum_detail, name='companies_curriculum_detail'),
    path('profile/candidate/<int:candidate_id>/<int:vacancy_id>/', companies_views.curriculum_detail,
        name='companies_curriculum_detail'),
    path('jobs/pdf/<int:vacancy_id>/', vacancy_views.vacancy_to_pdf, name='vacancies_vacancy_to_pdf'),

    # TRM - TRM.views.py
    path('privacypolicy/', TRM_views.privacy_policy, name='TRM_privacy_policy'),
    path('termsandconditions/', TRM_views.terms_and_conditions, name='TRM_terms_and_conditions'),

    # Example - example.views.py

    # Vacancies - vacancies.views.py
    path('jobs/<int:vacancy_id>/', vacancy_views.vacancy_details, name='vacancies_get_vacancy_details'),
    path('jobs/<int:vacancy_id>/ref-<str:referer>/', vacancy_views.vacancy_details, name='vacancies_get_vacancy_details_with_referal'),
    path('jobs/<int:vacancy_id>/eref-<str:external_referer>/', vacancy_views.vacancy_details, name='vacancies_get_vacancy_details_with_external_referal'),
    path('jobs/<int:vacancy_id>/apply/', vacancy_views.public_apply, name='vacancies_public_apply'),
    path('jobs/<int:vacancy_id>/apply/ref-<str:referer>/', vacancy_views.public_apply, name='vacancies_public_apply_with_referal'),
    path('jobs/<int:vacancy_id>/apply/eref-<str:external_referer>/', vacancy_views.public_apply, name='vacancies_public_apply_with_external_referal'),
    path('jobs/<int:vacancy_id>/new_application/', vacancy_views.new_application, name='vacancies_new_application'),
    path('jobs/<int:vacancy_id>/new_application/resolve/<str:card_type>/', vacancy_views.new_application_resolve_conflicts, name='vacancies_new_application_resolve_conflicts'),
    path('jobs/<int:vacancy_id>/complete_application/', vacancy_views.complete_application, name='vacancies_complete_application'),
    path('jobs/<int:vacancy_id>/talent_sourcing/', vacancy_views.vacancy_talent_sourcing, name="vacancies_talent_sourcing"),
    path('jobs/<int:vacancy_id>/process/<int:vacancy_stage>/', vacancy_views.vacancy_stage_details, name='vacancies_get_vacancy_stage_details'),
    path('jobs/<int:vacancy_id>/process/<int:vacancy_stage>/<int:stage_section>/', vacancy_views.vacancy_stage_details, name='vacancies_get_vacancy_stage_details'),
    path('jobs/<int:vacancy_id>/social/<str:social_code>/', vacancy_views.vacancy_details, name='vacancies_apply_via_social'),
    path('jobs/<int:vacancy_id>/<str:social_code>/', vacancy_views.vacancy_details, name='social_verification'),
    path('jobs/pdf/<int:vacancy_id>/', vacancy_views.vacancy_to_pdf, name='vacancies_vacancy_to_pdf'),

    #Social Multi Share views

    # Google Verification

    # Includes
    path('i18n/', include('django.conf.urls.i18n')),
    path('ajax-uploads/', include('upload_logos.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('ckeditor/', include('ckeditor.urls')),
    path('upload/file/', upload_vacancy_file, name='upload-file'),
    path('delete/file/', delete_vacancy_file, name='delete-file'),
    path('pricing-request/', common_ajax_views.pricing_request, name="pricing_request"),
    path('compare-candidates/', common_ajax_views.compare_candidates, name="compare_candidates"),
    path('notifications/', common_ajax_views.notifications, name="notifications"),
    re_path(r'^(?P<vacancy_status_name>\w+)/$', companies_views.vacancies_summary, name="companies_vacancies_by_status"),

    #Widget Urls
    path('widget/jobs/', companies_views.widget_jobs, name="companies_job_widget"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# if settings.DEBUG:
urlpatterns += [
    path('media/<path:path>', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]