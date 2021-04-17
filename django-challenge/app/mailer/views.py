# -*- coding: utf-8 -*-
from django.db.models.aggregates import Count, Sum
from django.db.models.query import Prefetch
from .models import Contact
from .models import Order
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Company


class IndexView(ListView):
    template_name = "mailer/index.html"
    paginate_by = 100

    def get_queryset(self):
        return Company.objects.prefetch_related(
            Prefetch(
                'contacts', queryset=Contact.objects.prefetch_related(
                    Prefetch(
                        'orders'
                    )
                )),
            Prefetch('orders'),
        )

    # def get(self, request, *args, **kwargs):
    #     orders = Order.objects.select_related('company', 'contact')[:10]
    #     print(orders)
    #     return render(request, 'mailer/index.html', {'orders': orders})

    # def get(self, request, *args, **kwargs):
    #     # company_list = Company.objects.all()[:2]
    #     # object = Order.objects.values('company__name', 'contact__first_name', 'contact__last_name', 'total').annotate(dcount=Count('company__name')).order_by('id')
    #     object = Company.objects.annotate(total = Count('contacts'))
    #     for obj in object:
    #         print(obj.get_order_sum())
    #     return render(request, 'mailer/index.html', {'object': object})
