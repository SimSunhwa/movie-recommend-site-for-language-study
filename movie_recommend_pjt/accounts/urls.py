from django.urls import path, include
from . import views

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/user/profile/', views.profile, name='user-profile'),
    path('delete/', views.delete_user, name='delete_user'),
]

# 회원가입
    # accounts/ dj-rest-auth/registration/
# 로그인
    # accounts/ dj-rest-auth/ login/ [name='rest_login']
# 로그아웃
    # accounts/ dj-rest-auth/ logout/ [name='rest_logout']
# 유저 정보 반환
    # accounts/ dj-rest-auth/ user/ [name='rest_user_details']
# 패스워드 초기화(이메일로 전송)
    # accounts/ dj-rest-auth/ password/reset/ [name='rest_password_reset']
# 패스워드 초기화 (이메일 확인 후 초기화 페이지)
    # accounts/ dj-rest-auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
# 패스워드 변경
    # accounts/ dj-rest-auth/ password/change/ [name='rest_password_change']