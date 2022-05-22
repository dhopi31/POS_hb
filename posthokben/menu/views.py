from django.http import HttpResponse
from django.shortcuts import render
from .models import ms_menu,ms_komposisi,transaksi, transaksi_detail
from django.db.models import Max
from datetime import datetime 

def index(request):
    menu = ms_menu.objects.all()
    context = {
        'judul' : 'Menu',
        'list_menu' : menu,
    }
    if request.method=="POST":
        max_code_trx = transaksi.objects.aggregate(Max('transaksi_code'))
        # print(max_code_trx['transaksi_code__max'])
        date_str = datetime.now().strftime("%d%m%Y") 
        
        if max_code_trx['transaksi_code__max'] == None:
            code_trx = date_str+".00001"
        else:
            max_code =max_code_trx['transaksi_code__max'][9:15] 
            max_code_int = int(max_code)
            next_code = max_code_int+1
            code_trx = date_str+"."+"{:05d}".format(next_code)
            
        T_header = transaksi(
                transaksi_code = code_trx,
                customer_name = request.POST['customer_name'],
                sub_value   = request.POST['sub_value'],
                ppn_value   = request.POST['ppn_value'],
                pay_type      = request.POST['pay_type'],
                transaksi_date= datetime.now(),
                created_by   = 1,
                updated_date  = datetime.now(),
                updated_by    = 1,
                )
        T_header.save()
       
        komposisi_code_arr = request.POST.getlist('komposisi_code[]')
        qty_porsi_arr = request.POST.getlist('qty_porsi[]')
        c = min([len(komposisi_code_arr), len(qty_porsi_arr)])

        for i in range(c):
            print(type(qty_porsi_arr[i]))
            if qty_porsi_arr[i]=='0' or qty_porsi_arr[i]=='' :
                qty_fix = 0
            else:
                qty_fix = qty_porsi_arr[i]
                T_detail = transaksi_detail(
                    transaksi_code = transaksi.objects.get(transaksi_code=code_trx),
                    komposisi_code = ms_komposisi.objects.get(komposisi_code=komposisi_code_arr[i]),
                    qty_porsi = int(qty_fix)
                    )
                 
                T_detail.save()

    return render(request, 'menu/index.html' , context)
