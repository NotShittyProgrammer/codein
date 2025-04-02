"""
URL configuration for code_in_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from data_site import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # Pages
    path('about-us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('service-single/', views.service_single, name='service_single'),
    path('contact-us/', views.contact_us, name='contact_us'),

    # Blog
    path('blog-home-1-col/', views.blog_1_col, name='blog_1_col'),
    path('blog-home-2-col/', views.blog_2_col, name='blog_2_col'),
    path('blog-home-3-col/', views.blog_3_col, name='blog_3_col'),
    path('post-single/', views.post_single, name='post_single'),

    # Pricing & Team
    path('pricing/', views.pricing, name='pricing'),
    path('our-team/', views.our_team, name='our_team'),
    path('team-member/', views.team_member, name='team_member'),
    path('faq/', views.faq, name='faq'),

    # Portfolio
    path('portfolio-grid/', views.portfolio_grid, name='portfolio_grid'),
    path('portfolio-slider/', views.portfolio_slider, name='portfolio_slider'),
    path('portfolio-single/', views.portfolio_single, name='portfolio_single'),
]

# Optional for static files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom 404 handler
handler404 = 'data_site.views.page_404'