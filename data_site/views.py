from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.translation import gettext as _
# from .models import *
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render

# def get_menu_and_services(current_menu):
#     return {
#         "current_menu": current_menu,
#         "services": Service.objects.all().order_by('position'),
#         "contacts": DataContact.objects.all()
#     }


# def about(request):
#     return render(
#         request,
#         'about.html',
#         {**{
#             "breadcrumbs": [
#                 {
#                     "name": _("Головна"),
#                     "link": "/"
#                 },
#                 {
#                     "name": _("Про нас"),
#                     "link": None}
#             ]
#         }, **get_menu_and_services(_('Про нас'))})




# def main(request):
#     articles = Article.objects.all().order_by('-date')
#     return render(request, 'index.html', {
#         "articles": articles,
#         **get_menu_and_services(_('Головна'))
#     })



# def blog(request):
#     category = request.GET.get("category")
#     tag = request.GET.get("tag")
#     search_text = request.GET.get("text")
#     page_count = 1
#     page = request.GET.get("page")

#     if page:
#         page_count = int(page)
#     article = None
#     if category:
#         article = Article.objects.filter(categories=category)
#     if tag:
#         article = Article.objects.filter(teg=tag)
#     if search_text:
#         article = Article.objects.filter(Q(title__contains=search_text) | Q(description__contains=search_text))
#     if article is None:
#         article = Article.objects.all()
#     category = CategoryArticle.objects.all()
#     list_category = []
#     for i in category:
#         list_category.append({"obj": i, "count": len(Article.objects.filter(categories=i))})
#     list_article = Paginator(article.order_by('date'), 3)
#     return render(request, 'blog.html', {**{
#         "is_submit": consultation_form(request),
#         "article": list_article.page(page_count),
#         "cur_page": page_count,
#         "pages": list_article.page_range,
#         "category": list_category,
#         "tags": ArticleTeg.objects.all(),
#         "last_articles": Article.objects.all()[:5],
#         "breadcrumbs": [
#             {
#                 "name": _("Головна"),
#                 "link": "/"
#             },
#             {
#                 "name": _("Блог"),
#                 "link": None
#             }]}, **get_menu_and_services(_('Блог'))})


# def single_blog(request, name):
#     category = CategoryArticle.objects.all()
#     list_category = []
#     for i in category:
#         list_category.append({"obj": i, "count": len(Article.objects.filter(categories=i))})
#     article = Article.objects.get(id=name)
#     return render(request, 'blog-single.html', {**{
#         "is_submit": consultation_form(request),
#         "article": article,
#         "category": list_category,
#         "tags": ArticleTeg.objects.all(),
#         "last_articles": Article.objects.all()[:5],
#         "breadcrumbs": [
#             {
#                 "name": _("Головна"),
#                 "link": "/"
#             },
#             {
#                 "name": _("Блог"),
#                 "link": "/blog"
#             },
#             {
#                 "name": article.title,
#                 "link": None
#             }]}, **get_menu_and_services(_('Блог'))})


# def contact_us_view(request):
#     services = Service.objects.all()

#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone', '')
#         message = request.POST.get('message')
#         file = request.FILES.get('file_upload')

#         email_subject = 'New Contact Form Submission'
#         email_body = render_to_string('email_template_contact.html', {
#             'first_name': first_name,
#             'last_name': last_name,
#             'email': email,
#             'phone': phone,
#             'message': message,
#         })


#         email_message = EmailMessage(
#             email_subject,
#             email_body,
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.CONTACT_EMAIL],
#         )

#         if file:
#             email_message.attach(file.name, file.read(), file.content_type)

#         email_message.content_subtype = 'html'
#         email_message.send(fail_silently=False)

#         return render(request, 'contactus.html', {'is_submit': True, 'services': services, **get_menu_and_services(_('Про нас'))})
#     return render(request, 'contactus.html', {'services': services, **get_menu_and_services(_('Про нас'))})

# def employ_view(request):
#     services = Service.objects.all()

#     if request.method == 'POST':
#         first_name = request.POST.get('firstname')
#         last_name = request.POST.get('lastname')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone', '')
#         position = request.POST.get('position')
#         start_date = request.POST.get('start_date')
#         address = request.POST.get('address')
#         message = request.POST.get('message')
#         file = request.FILES.get('upload')


#         email_subject = 'New Employment Application Submission'
#         email_body = render_to_string('email_template_employment.html', {
#             'first_name': first_name,
#             'last_name': last_name,
#             'email': email,
#             'phone': phone,
#             'position': position,
#             'start_date': start_date,
#             'address': address,
#             'message': message,
#         })

#         email_message = EmailMessage(
#             email_subject,
#             email_body,
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.CONTACT_EMAIL],
#         )

#         if file:
#             email_message.attach(file.name, file.read(), file.content_type)

#         email_message.content_subtype = 'html'
#         email_message.send(fail_silently=False)

#         return render(request, 'employment.html', {'services': services, **get_menu_and_services(_('Робота')), 'is_submit': True})

#     return render(request, 'employment.html', {'services': services, **get_menu_and_services(_('Робота'))})

# def support_us_view(request):
#     services = Service.objects.all()
#     return render(request, 'supportus.html', {'services': services, **get_menu_and_services(_('Підтримка'))})



# def services_details(request, name):
#     services = Service.objects.get(id=name)
#     return render(request, 'services-details.html', {**{
#         "content": services,
#         "is_submit": consultation_form(request),
#         "breadcrumbs": [
#             {
#                 "name": _("Головна"),
#                 "link": "/"
#             },
#             {
#                 "name": _("Послуги"),
#                 "link": "/#services"
#             },
#             {
#                 "name": services.name,
#                 "link": None
#             }]}, **{
#                   }, **get_menu_and_services(_('Послуги'))})

# def training_view(request):
#     is_submit = False  # Початкове значення для перевірки відправки форми

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone', '')
#         desired_program = request.POST.get('desired_program')
#         message = request.POST.get('message')
#         file = request.FILES.get('file_upload')

#         email_subject = 'Нова заявка на навчання'
#         email_body = render_to_string('training.html', {
#             'name': name,
#             'email': email,
#             'phone': phone,
#             'desired_program': desired_program,
#             'message': message,
#         })

#         email_message = EmailMessage(
#             email_subject,
#             email_body,
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.CONTACT_EMAIL],  # Email адміністратора
#         )

#         # Прикріплюємо файл, якщо він є
#         if file:
#             email_message.attach(file.name, file.read(), file.content_type)

#         email_message.content_subtype = 'html'
#         email_message.send(fail_silently=False)

#         is_submit = True  # Встановлюємо, що форма була відправлена

#     return render(request, "training.html", {"is_submit": is_submit})

# def error_404_view(request, exception):
#     return render(request, 'blocks/404.html')


# def consultation_form(request):
#     try:
#         if request.method == 'POST':
#             name = request.POST.get('name')
#             email = request.POST.get('email')

#             # Формуємо текст для email
#             email_subject = 'New Consultation Request'
#             email_body = render_to_string('consultation_email_template.html', {
#                 'name': name,
#                 'email': email,
#             })

#             email_message = EmailMessage(
#                 email_subject,
#                 email_body,
#                 settings.DEFAULT_FROM_EMAIL,
#                 [settings.CONTACT_EMAIL],
#             )

#             email_message.content_subtype = 'html'
#             email_message.send(fail_silently=False)

#             return True
#     except Exception as e:
#         print("Error in send to email consultation form:  " + str(e))
#         pass
#     return False
def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about-us.html')

def services(request):
    return render(request, 'services.html')

def service_single(request):
    return render(request, 'service-single.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def blog_1_col(request):
    return render(request, 'blog-home-1-col.html')

def blog_2_col(request):
    return render(request, 'blog-home-2-col.html')

def blog_3_col(request):
    return render(request, 'blog-home-3-col.html')

def post_single(request):
    return render(request, 'post-single.html')

def pricing(request):
    return render(request, 'pricing.html')

def our_team(request):
    return render(request, 'our-team.html')

def team_member(request):
    return render(request, 'team-member.html')

def faq(request):
    return render(request, 'faq.html')

def portfolio_grid(request):
    return render(request, 'portfolio-grid.html')

def portfolio_slider(request):
    return render(request, 'portfolio-slider.html')

def portfolio_single(request):
    return render(request, 'portfolio-single.html')

def page_404(request, exception):
    return render(request, '404.html', status=404)