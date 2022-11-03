from .models import Category


def catedropdown(request):
    categories = Category.objects.all()

    context ={
        'category':categories
    }

    return context