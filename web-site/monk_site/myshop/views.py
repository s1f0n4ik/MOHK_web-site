from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Gender
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    cart_product_form = CartAddProductForm()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                      'cart_product_form': cart_product_form
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form })


def main(request, category_slug=None):
    cart_product_form = CartAddProductForm()
    category = None
    categories = Gender.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Gender, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/main.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                      'cart_product_form': cart_product_form
                  })


def politika(request):
    return render(request, 'shop/politika.html')


def sogl(request):
    return render(request, 'shop/sogl.html')

# def br(request):
#     return render(request, 'shop/base_br.html')
