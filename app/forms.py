#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django import  forms
from models import *
# class ItemForm(forms.Form):
#     ItemCode = forms.CharField(max_length=10,label=u'物料编码:',error_messages={'required': u'必填项'})
#     ItemName = forms.CharField(label=u'物料名称:')
#     Remark = forms.CharField(required=False,widget=forms.Textarea,label=u'备注:' )
# class InStockBillForm(forms.Form):
#     InStockBillCode = forms.CharField()
#     Operator = forms.CharField()
#     InStockDate = forms.DateTimeField()
#     Amount = forms.IntegerField()
#     Item = forms.ModelChoiceField(queryset = Item.objects.all(),  required =True)