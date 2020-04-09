from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from .forms import CheckoutForm
from .models import ItemOrder, Items, OrderPlaced


class Index(ListView):
    model = Items
    context_object_name = 'items'


class DetailView(DetailView):
    model = Items
    context_object_name = 'item_detail'


def detailView(request, pk):
    items = Items.objects.all().filter(pk=pk)
    item = items[0]
    return render(request, 'core/items_detail.html', {'item_detail': item})


def cart(request):
    ordered_items = ItemOrder.objects.all().filter(user=request.user)
    return render(request, 'core/cart.html', {'items': ordered_items})


def add_to_cart(request, pk):
    item = Items.objects.all().get(pk=pk)
    print(item)
    if ItemOrder.objects.all().filter(user=request.user, item=item):
        i = ItemOrder.objects.all().get(user=request.user, item=item)
        i.quantity += 1
        i.total_price = i.quantity * i.item.price
        i.save()
        return redirect('core:cart')

    else:
        new_item = ItemOrder(item=item, quantity=1)
        new_item.user = request.user
        new_item.total_price = item.price
        new_item.save()
        print('created')
        return redirect('core:cart')


def remove_from_cart(request, pk):
    item = Items.objects.all().get(pk=pk)
    print(item)
    i = ItemOrder.objects.all().get(item=item, user=request.user)
    i.quantity -= 1
    i.total_price = i.quantity * i.item.price
    if i.quantity == 0:
        i.delete()
    else:
        i.save()
    return redirect('core:cart')


def checkout(request):
    items = ItemOrder.objects.all().filter(user=request.user)
    total_price = 0
    checkoutform = CheckoutForm()
    for item in items:
        total_price += item.total_price
    context = {
        'items': items,
        'total_price': total_price,
        'checkout_form': checkoutform
    }
    return render(request, 'core/checkout.html', context)


class Payment(View):
    def get(self, *args, **kwargs):
        items = ItemOrder.objects.all().filter(user=self.request.user)
        total_price = 0
        checkoutform = CheckoutForm()
        for item in items:
            total_price += item.total_price
        context = {
            'items': items,
            'total_price': total_price,
            'checkout_form': checkoutform
        }
        return render(self.request, 'core/payment.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(data=self.request.POST)
        items = ItemOrder.objects.all().filter(user=self.request.user)
        total_price = 0
        for item in items:
            total_price += item.total_price
        if form.is_valid():
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            country = form.cleaned_data['country']
            country = dict(form.fields['country'].choices)[country]
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            zip = form.cleaned_data['zip']
            context = {
                'address': address,
                'country': country,
                'state': state,
                'city': city,
                'zip': zip,
                'total_price': total_price
            }
            html_content = render_to_string('core/email_content.html', context)
            send_mail('MyShoppingWebsite',
                      strip_tags(html_content),
                      'vnimit1991@gmail.com',
                      [email],
                      fail_silently=False)
            print('sent')
            ordered_items = ItemOrder.objects.all().filter(user=self.request.user)
            for item in ordered_items:
                new_item = OrderPlaced(
                    user=item.user, item=item.item, quantity=item.quantity,
                    total_price=item.total_price)
                new_item.save()
            ordered_items.delete()
            return redirect('core:index')


def profile(request):
    items = OrderPlaced.objects.all().filter(user=request.user).order_by('-time')
    return render(request, 'core/profile.html', {'items': items})
