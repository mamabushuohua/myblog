from django.shortcuts import render


def page_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)
