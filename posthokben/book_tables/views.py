from unittest import result
from colorama import Cursor
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from menu.models import ms_menu, ms_harga, ms_item, ms_komposisi, ms_komposisi_detail, ms_layanan, transaksi, transaksi_detail

curs = connection.cursor()
time_f = ' 00:00:00'
time_t = ' 23:59:00'
def index(request):
    layanan = ms_layanan.objects.all()
    # try:
    curs.execute('CALL GetAllData_1')
    result = curs.fetchall()
    context = {
        'judul' : 'Dashboard',
        'listdata_1' : result,
        'list_layanan' : layanan
    }
    return render(request, 'book/index.html' , context)
    # finally:
    #     curs.close()

def search(request):
    layanan = ms_layanan.objects.all()
    f_date = request.GET["transaksi_date_from"]
    t_date = request.GET["transaksi_date_to"]
    
    lay_id = request.GET["layanan_id"]
    curs.execute('CALL GetAllDataFilter_1 (%s, %s, %s)', (f_date+time_f, t_date+time_t, lay_id ))
    result_filter = curs.fetchall()
    context = {
        'judul' : 'Dashboard',
        'listdata_1' : result_filter,
        'list_layanan' : layanan
    }
    return render(request, 'book/index.html' , context)

def use_raw(request):
    curs.execute('CALL GetAllData_2')
    result = curs.fetchall()
    context = {
        'judul' : 'Dashboard',
        'listdata_2' : result,
    }
    return render(request, 'book/book_use_raw.html' , context)

def search_use_raw(request):
    f_date = request.GET["transaksi_date_from"]
    t_date = request.GET["transaksi_date_to"]
    curs.execute('CALL GetAllDataFilter_2 (%s, %s)', (f_date+time_f, t_date+time_t))
    result_filter = curs.fetchall()
    context = {
        'judul' : 'Dashboard',
        'listdata_2' : result_filter,
    }
    return render(request, 'book/book_use_raw.html' , context)

def pay_type(request):
    curs.execute('CALL GetAllData_3')
    result = curs.fetchall()
    context = {
        'judul' : 'Dashboard',
        'listdata_3' : result,
    }
    return render(request, 'book/book_pay.html' , context)

def search_pay(request):
    f_date = request.GET["transaksi_date_from"]
    t_date = request.GET["transaksi_date_to"]
    curs.execute('CALL GetAllDataFilter_3 (%s, %s)', (f_date+time_f, t_date+time_t))
    result_filter = curs.fetchall()
    context = {
        'judul' : 'Dashboard',
        'listdata_3' : result_filter,
    }
    return render(request, 'book/book_pay.html' , context)