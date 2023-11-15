from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponse('Страница приложения women.')


def categories(request, cat_id: int):
    return HttpResponse(f'<h1>Статьи по категориям </h1> <p>cat_id: {cat_id} </p>')


def categories_by_slug(request, cat_slug: str):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям </h1> <p>cat_slug: {cat_slug} </p> <p>GET: {request.GET} </p>')


def post_detail(request):
    if not request.GET:
        return HttpResponse('GET is empty')

    ls = []
    for key, value in request.GET.items():
        ls.append(f'{key}={value}')

    return HttpResponse('|'.join(ls))


def about(request):
    return HttpResponse('О сайте')



def archive(request, year: int):
    if year not in range(1990, 2023 + 1):
        uri = reverse('cats', args=['music1',])
        return redirect(uri)
        # return HttpResponseRedirect('home')

    return HttpResponse(f'<h1>Архив по годам </h1> <p>year: {year} </p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def posts_list(request, year: int):
    if year not in range(1990, 2023 + 1):
        raise Http404()

    return HttpResponse(f'posts: {year}')
