from django.urls import path
from . import views

urlpatterns = [
    path('clubs/', views.ClubList.as_view()),
    path('clubs/<int:pk>/', views.ClubDetail.as_view()),

    path('tournaments/', views.TournamentList.as_view()),
    path('tournaments/<int:pk>/', views.TournamentDetail.as_view()),

    path('clubs/', views.ClubList.as_view()),
    path('clubs/<int:pk>/', views.ClubDetail.as_view()),

    path('verificationcodes/', views.VerificationCodeList.as_view()),
    path('verificationcodes/<int:pk>/', views.VerificationCodeDetail.as_view()),

    path('duels/', views.DuelList.as_view()),
    path('duels/<int:pk>/', views.DuelDetail.as_view()),

    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),

    path('trees/', views.TreeList.as_view()),
    path('trees/<int:pk>/', views.TreeDetail.as_view()),

    path('participants/', views.ParticipantList.as_view()),
    path('participants/<int:pk>/', views.ParticipantDetail.as_view()),

    path('me/', views.me),

    path('verifycode/', views.verify_code),
    path('emailtest/', views.emailtest),
    path('sendcode/', views.send_verification_code),

    path('generatetrees/', views.generate_trees),
    path('generatetree/', views.generate_tree),
    path('gettree/<int:category_id>', views.get_tree_by_category),

    path('setduelwinner/<int:participant_id>', views.set_duel_winner),

    path('verificationcodescapacity/', views.get_codes_capacity)
]
