from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 导入 Customer 对象定义
from common.models import Customer


# 订单列表
def list_orders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")


# 客户列表
def list_customers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    # 定义返回字符串
    ret_str = ''
    for customer in qs:
        for name, value in customer.items():
            ret_str += f'{name} : {value} | '

        # <br> 表示换行
        ret_str += '<br>'

    return HttpResponse(ret_str)
