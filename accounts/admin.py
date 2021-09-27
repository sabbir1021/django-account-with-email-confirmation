from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
User = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','password1', 'password2',)
        }),
    )
    model = User
    list_display = ['email', 'username', 'first_name',
                    'last_name', 'is_staff','active','email_confirmed']
    list_filter = ['is_staff']
    list_editable = ['active','is_staff','email_confirmed']
    list_perpage = 20


admin.site.register(User, CustomUserAdmin)

