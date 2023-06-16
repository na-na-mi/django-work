from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def rfm(request):
    return render(request, "RFM.html")


def four(request):
    return render(request, "年销售统计.html")


def one(request):
    return render(request, "销售地区数据.html")


def third(request):
    return render(request, "销售额.html")


def five(request):
    return render(request, "价格分析.html")


def two(request):
    return render(request, "热销top5.html")


def second(request):
    return render(request, "客户占比.html")


def three(request):
    return render(request, "发货时效.html")


def ra(request):
    return render(request, "relative.html")
