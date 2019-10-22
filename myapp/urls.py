# from django.contrib import admin
# from django.conf import settings
from django.conf.urls import url

from .views.corporate import CorporateCreateList, CorporateRetriveUpdateDelete
from .views.corporate_main_branch import CorporateMainBranchCreateList, CorporateMainBranchRetriveUpdateDelete # NOQA
from .views.company import CompanyCreateList, CompanyRetriveUpdateDelete
from .views.company_user import CompanyUserCreateList, CompanyUserRetriveUpdateDelete  # NOQA
from .views.notification import NotificationCreateList, NotificationRetriveUpdateDelete  # NOQA
from .views.company_user_user_notification import CompanyUserUserNotificationCreateList, CompanyUserUserNotificationRetriveUpdateDelete  # NOQA

urlpatterns = []

urlpatterns.append(url(r'^corporates$', CorporateCreateList.as_view()))
urlpatterns.append(url(r'^corporates/(?P<corporate>\d)$', CorporateRetriveUpdateDelete.as_view()))  # NOQA

urlpatterns.append(url(r'^corporates/(?P<corporate>\d)/main-branches$', CorporateMainBranchCreateList.as_view()))  # NOQA
urlpatterns.append(url(r'^corporates/(?P<corporate>\d)/main-branches/(?P<main_branch>\d)$', CorporateMainBranchRetriveUpdateDelete.as_view()))  # NOQA

urlpatterns.append(url(r'^companies$', CompanyCreateList.as_view()))
urlpatterns.append(url(r'^companies/(?P<company>\d)$', CompanyRetriveUpdateDelete.as_view()))  # NOQA

urlpatterns.append(url(r'^companies/(?P<company>\d)/users$', CompanyUserCreateList.as_view()))  # NOQA
urlpatterns.append(url(r'^companies/(?P<company>\d)/users/(?P<user>\d)$', CompanyUserRetriveUpdateDelete.as_view()))  # NOQA

urlpatterns.append(url(r'^notifications$', NotificationCreateList.as_view()))
urlpatterns.append(url(r'^notifications/(?P<notification>\d)$', NotificationRetriveUpdateDelete.as_view()))  # NOQA

urlpatterns.append(url(r'^companies/(?P<company>\d)/users/(?P<user>\d)/user-notifications$', CompanyUserUserNotificationCreateList.as_view()))  # NOQA
urlpatterns.append(url(r'^companies/(?P<company>\d)/users/(?P<user>\d)/user-notifications/(?P<user_notification>\d)$', CompanyUserUserNotificationRetriveUpdateDelete.as_view()))  # NOQA