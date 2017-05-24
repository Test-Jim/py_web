#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import need,user

def search_form(request):
    return render_to_response('search_form.html')
'''
def search(request):
    error=False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 10:
            error = True
        else:
            items = Item.objects.filter(ItemName__icontains=q)
            return render_to_response('search_results.html',{'items': items, 'query': q})
    return render_to_response('search_form.html',{'error':error})

def AddInStockBill(request):
    if request.method == 'POST':
        form = InStockBillForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            inStockBill = InStockBill()
            inStockBill.InStockBillCode = cd['InStockBillCode']
            inStockBill.InStockDate = cd['InStockDate']
            inStockBill.Amount = cd['Amount']
            inStockBill.Operator = cd['Operator']
            inStockBill.Item = cd['Item']
            inventorys = inStockBill.Item.inventory_set.all()
            currentInventory = Inventory()
            if (inventorys.count()==0):
                currentInventory.Item = inStockBill.Item
                currentInventory.Amount = inStockBill.Amount
            else:
                #这里假定只有一个物料，后面我们会根据进程重构代码
                currentInventory = inventorys[0]
                currentInventory.Amount = currentInventory.Amount + inStockBill.Amount
            currentInventory.save() #更新库存
            inStockBill.save()      #保存入库单数据
            return HttpResponseRedirect('/success/')
    else:
        form = InStockBillForm()
    return render_to_response('InStockAdd.html',{'form': form}
                              ,context_instance = RequestContext(request))
def AddItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            item = Item()
            item.ItemCode = cd['ItemCode']
            item.ItemName = cd['ItemName']
            item.save()
            return HttpResponseRedirect('/success/')
        else:
            # print '111',form.errors
            return render_to_response('ItemAdd.html', {'form': form},context_instance = RequestContext(request))
    else:
        form = ItemForm()
        return render_to_response('ItemAdd.html', {'form': form},context_instance = RequestContext(request))
'''
def index(request):
    # needs=need.objects.all().values_list('need_id','need_name','need_status','finish_test','need_day','need_url')
    userPhone=request.POST.get('userPhone')
    userPwd=request.POST.get('userPwd')
    info=user.objects.filter(mobile=userPhone,password=userPwd)
    if list(info) !=[]:

        need_tester=user.objects.values('name').get(mobile=userPhone)['name']
        needs=need.objects.filter(need_tester=need_tester).order_by('-need_id')
        return render_to_response('compact-table.html',{'needs':needs,'need_tester':need_tester},context_instance = RequestContext(request))
    else:
        return render_to_response('login.html',{'messages':'error'},context_instance = RequestContext(request))

def login(request):

    return render_to_response('login.html',context_instance = RequestContext(request))



def update(request):
    finish_test=request.POST.get('status')
    need_id=request.POST.get('needid')
    beizhu=request.POST.get('beizhu')
    need.objects.filter(need_id=need_id).update(finish_test=finish_test,beizhu=beizhu)
    need_tester=need.objects.filter(need_id=need_id).values('need_tester')
    needs=need.objects.filter(need_tester=need_tester[0]['need_tester']).order_by('-need_id')
    return render_to_response('compact-table.html',{'needs':needs,'need_tester':need_tester[0]['need_tester']},context_instance = RequestContext(request))


def success(request):
    return HttpResponse('success')