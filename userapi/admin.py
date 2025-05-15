from django.contrib import admin
from .models import Account, DepositHistory, WithdrawalHistory

# Customizing the display of the Account model in the admin panel
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'investment', 'bitcoin_balance', 'ethereum_balance', 
        'tron_balance', 'doge_balance', 'bitcoin_cash_balance', 'usdt_trc20_balance',
        'bnb_balance', 'litecoin_balance', 'usdt_erc20_balance', 'binance_usd_balance',
        'date_created', 'last_updated'
    )

    search_fields = ('user__username',)
    list_filter = ('date_created',)
    ordering = ('-date_created',)

    # Add this to control what shows up in the edit form
    fields = (
        'user', 'investment', 'bitcoin_balance', 'ethereum_balance', 
        'tron_balance', 'doge_balance', 'bitcoin_cash_balance', 'usdt_trc20_balance',
        'bnb_balance', 'litecoin_balance', 'usdt_erc20_balance', 'binance_usd_balance'
    )

class DepositHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'crypto', 'timestamp')
    list_filter = ('timestamp',)

class WithdrawalHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'crypto', 'timestamp')
    list_filter = ('timestamp',)


# Register the DepositHistory and WithdrawalHistory models
admin.site.register(DepositHistory, DepositHistoryAdmin)
admin.site.register(WithdrawalHistory, WithdrawalHistoryAdmin)
admin.site.register(Account, AccountAdmin)
