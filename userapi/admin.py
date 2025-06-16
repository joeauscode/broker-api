from django.contrib import admin
from .models import Account, DepositHistory, WithdrawalHistory, Investment, InvestmentHistory
from django.utils.html import format_html



@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'balance', 'avatar_preview', 'steel', 'iron_ore', 'lithium', 
        'gold', 'kaolin', 'date_created', 'last_updated'        
    )
    search_fields = ('user__username',)
    list_filter = ('date_created',)
    ordering = ('-date_created',)

    # ✅ Only editable fields here
    fields = (
        'user', 'balance', 'avatar', 'steel', 'iron_ore', 'lithium', 
        'gold', 'kaolin'
    )

    # ✅ Non-editable fields go here
    readonly_fields = ('date_created', 'last_updated')

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', 
                obj.avatar.url
            )
        return "-"
    avatar_preview.short_description = 'Avatar Preview'


# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = (
#         'user', 'balance', 'avatar_preview', 'steel', 'iron_ore', 'lithium', 
#         'gold', 'kaolin', 'date_created', 'last_updated'        
#     )
#     search_fields = ('user__username',)
#     list_filter = ('date_created',)
#     ordering = ('-date_created',)
#     fields = (
#         'user', 'balance', 'avatar', 'steel', 'iron_ore', 'lithium', 
#         'gold', 'kaolin', 'date_created', 'last_updated'
#     )

#     def avatar_preview(self, obj):
#         if obj.avatar:
#             return format_html(
#                 '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', 
#                 obj.avatar.url
#             )
#         return "-"
#     avatar_preview.short_description = 'Avatar Preview'


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'earnings', 'total_profit', 'activation_date', 'end_date', 'status')
    list_filter = ('status', 'payment_method')
    search_fields = ('user__username', 'payment_method')
    readonly_fields = ()  # Optional


@admin.register(DepositHistory)
class DepositHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'crypto', 'amount', 'timestamp', 'description')
    list_filter = ('crypto', 'timestamp')
    search_fields = ('account__fullname', 'crypto', 'description')
    readonly_fields = ('timestamp',)
    fieldsets = (
        (None, {
            'fields': ('account', 'crypto', 'amount', 'description', 'timestamp'),
        }),
    )


@admin.register(WithdrawalHistory)
class WithdrawalHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'crypto', 'amount', 'timestamp', 'description')
    list_filter = ('crypto', 'timestamp')
    search_fields = ('account__fullname', 'crypto', 'description')
    readonly_fields = ('timestamp',)
    fieldsets = (
        (None, {
            'fields': ('account', 'crypto', 'amount', 'description', 'timestamp'),
        }),
    )


@admin.register(InvestmentHistory)
class InvestmentHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'amount', 'status', 'date')
    list_filter = ('status', 'payment_method', 'date')
    search_fields = ('user__username', 'payment_method')
    readonly_fields = ('date',)
