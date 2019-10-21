# from django.contrib import admin
# from django.conf import settings
from django.conf.urls import url

urlpatterns = []

from .views.corporate import CorporateCreateList, CorporateRetriveUpdateDelete

urlpatterns.append(url(r'^corporates$', CorporateCreateList.as_view()))
urlpatterns.append(url(r'^corporates/(?P<corporate>\d)$', CorporateRetriveUpdateDelete.as_view()))

from .views.corporate_main_branch import CorporateMainBranchCreateList, CorporateMainBranchRetriveUpdateDelete

urlpatterns.append(url(r'^corporates/(?P<corporate>\d)/main-branches$', CorporateMainBranchCreateList.as_view()))
urlpatterns.append(url(r'^corporates/(?P<corporate>\d)/main-branches/(?P<main_branch>\d)$', CorporateMainBranchRetriveUpdateDelete.as_view()))

from .views.company import CompanyCreateList, CompanyRetriveUpdateDelete

urlpatterns.append(url(r'^companies$', CompanyCreateList.as_view()))
urlpatterns.append(url(r'^companies/(?P<company>\d)$', CompanyRetriveUpdateDelete.as_view()))

from .views.company_user import CompanyUserCreateList, CompanyUserRetriveUpdateDelete

urlpatterns.append(url(r'^companies/(?P<company>\d)/users$', CompanyUserCreateList.as_view()))
urlpatterns.append(url(r'^companies/(?P<company>\d)/users/(?P<user>\d)$', CompanyUserRetriveUpdateDelete.as_view()))

from .views.notification import NotificationCreateList, NotificationRetriveUpdateDelete

urlpatterns.append(url(r'^notifications$', NotificationCreateList.as_view()))
urlpatterns.append(url(r'^notifications/(?P<notification>\d)$', NotificationRetriveUpdateDelete.as_view()))


from .views.company_user_user_notification import CompanyUserUserNotificationCreateList, CompanyUserUserNotificationRetriveUpdateDelete

urlpatterns.append(url(r'^companies/(?P<company>\d)/users/(?P<user>\d)/user-notifications$', CompanyUserUserNotificationCreateList.as_view()))
urlpatterns.append(url(r'^companies/(?P<company>\d)/users/(?P<user>\d)/user-notifications/(?P<user_notification>\d)$', CompanyUserUserNotificationRetriveUpdateDelete.as_view()))