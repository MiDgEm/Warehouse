from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Product
from .forms import FormAdd
from docx import Document
from datetime import datetime


# Получение данных из бд
def index(request):
    products = Product.objects.all()
    return TemplateResponse(request, "firstapp/main.html", {"products": products})


# Сохранение данных в бд
def add(request):
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.article = request.POST.get("article")
        product.state = request.POST.get("state")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.save()
        return HttpResponseRedirect("/")
    else:
        form = FormAdd()
        return render(request, "firstapp/addPage.html", {"form": form})


# Редактирование данных в бд
def edit(request, id):
    try:
        product_in_form = Product.objects.get(id=id)

        if request.method == "POST":
            product_in_form.name = request.POST.get("name")
            product_in_form.article = request.POST.get("article")
            product_in_form.state = request.POST.get("state")
            product_in_form.price = request.POST.get("price")
            product_in_form.description = request.POST.get("description")
            product_in_form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "firstapp/editPage.html", {"products": product_in_form})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found<h2>")


# Удаление данных из бд
def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found<h2>")


def find(request):
    name = request.GET.get("name")

    if name == "":
        return HttpResponseRedirect("/")

    product = Product.objects.filter(name=name)
    return TemplateResponse(request, 'firstapp/main.html', {"products": product})


def createDocumentDOCX(request):
    arr_id = request.GET.getlist('checkbox-id')

    document = Document()
    arr = list()

    for id in arr_id:
        arr.append(Product.objects.get(id=id))

    if len(arr) == 0:
        return HttpResponse("<h1>Не были выбраны данные<h1>")

    arr_new = tuple(arr)

    table = document.add_table(rows=1, cols=4)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Наименование'
    hdr_cells[1].text = 'Артикл'
    hdr_cells[2].text = 'Состояние'
    hdr_cells[3].text = 'Цена'

    for name in arr_new:
        row_cells = table.add_row().cells
        row_cells[0].text = name.name
        row_cells[1].text = name.article
        row_cells[2].text = name.state
        row_cells[3].text = str(name.price)

    now = datetime.now()
    document.save(f'document-{str(now.day)}-{str(now.month)}-{str(now.year)}-{str(now.hour)}-{str(now.minute)}-{str(now.second)}.docx')

    arr_id.clear()
    return HttpResponseRedirect('/')
