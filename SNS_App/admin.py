from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

class ReserveRegistrationInlineAdmin(admin.TabularInline):
    model = CustomUser.reserved_books.through

class FinishRegistrationInlineAdmin(admin.TabularInline):
    model = CustomUser.finished_books.through

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    list_display = ['email','username','ProfileImage']

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('ProfileImage',)}),
    )

    add_fieldsets = (
        (None,{
            'fields':('email','username','password1','password2')
        }),
    )
    inlines = (ReserveRegistrationInlineAdmin, FinishRegistrationInlineAdmin)


class MemberInlineAdmin(admin.TabularInline):
    model = Room.room_member.through

class RoomAdmin(admin.ModelAdmin):
    inlines = (MemberInlineAdmin,)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TweetModel)
admin.site.register(Like)
admin.site.register(Connection)
admin.site.register(Comment)
admin.site.register(Room,RoomAdmin)
admin.site.register(Message)
admin.site.register(Entries)
admin.site.register(BookData)
admin.site.register(ReserveRegistration)
admin.site.register(FinishRegistration)