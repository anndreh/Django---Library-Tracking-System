from django.contrib import admin
from .models import Author, Book, BookCopy, Member, Loan
from django.db.models import Sum

admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Loan)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'genre', 'get_available_copies')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(num_available_copies=Sum('book_copy__available_copies'))
    
    def get_available_copies(self, obj):
        return obj.num_available_copies or 0

    get_available_copies.short_description = 'Available Copies'
    get_available_copies.admin_order_field = 'available_copies'


@admin.register(BookCopy)
class BookCopy(admin.ModelAdmin):
    list_display = ('book', 'printing_date', 'available_copies', 'publisher')