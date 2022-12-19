from django.http import HttpResponse
from django.shortcuts import render

from firstapp.forms import UserForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        if (request.POST.get("basket") == "on"):
            basket = "Yes"
        else:
            basket = "No"

        # basket = request.POST.get("basket")
        vyb = request.POST.get("vyb")
        email = request.POST.get("email")
        about = request.POST.get("about")
        url_text = request.POST.get("url_text")
        file_path = request.POST.get("file_path")
        file = request.POST.get("file")
        output = "<h2>Пользователь<h2><h3>Имя - {0}, Возраст - {1}</h3>" \
                 "<ul>" \
                 "<li>Согласие с условиями {2}</li>" \
                 "<li>Доволен сервисом? {3}</li>" \
                 "<li>Email для обратной связи: {4}</li>" \
                 "<li>О клиенте: {5}</li>" \
                 "<li>Ссылка на профиль: {6}</li>" \
                 "<li>Путь к файлу: {7}</li>" \
                 "<li>Загруженный файл: {8}</li>" \
                 "</ul>".format(name, age, basket, vyb, email, about, url_text, file_path, file)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


# def about(request):
#   return HttpResponse('<h2>О сайте</h2>')


def contacts(request):
    return HttpResponse('<h2>Контакты</h2>')


def products(request, productid=1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id, name):
    output = "<h2>Пользователь</h2> <h3>id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)
