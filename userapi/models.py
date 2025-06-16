from django.db import models
from django.contrib.auth.models import User

CRYPTO_CHOICES = [
    ('FORGEX', 'Steel'),
    ('FEVAULT', 'Iron Ore'),
    ('CHARGECOIN', 'Lithium'),
    ('AUXCOIN', 'Gold'),
    ('WHITEEARTH', 'Kaolin'),
]

GENDER_CHOICE = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

COUNTRY_CHOICES = [
    ('Afghanistan', 'Afghanistan'),
    ('Albania', 'Albania'),
    ('Algeria', 'Algeria'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahamas', 'Bahamas'),
    ('Bahrain', 'Bahrain'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bhutan', 'Bhutan'),
    ('Bolivia', 'Bolivia'),
    ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Brazil', 'Brazil'),
    ('Brunei', 'Brunei'),
    ('Bulgaria', 'Bulgaria'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Cambodia', 'Cambodia'),
    ('Cameroon', 'Cameroon'),
    ('Canada', 'Canada'),
    ('Cape Verde', 'Cape Verde'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Colombia', 'Colombia'),
    ('Comoros', 'Comoros'),
    ('Congo (Brazzaville)', 'Congo (Brazzaville)'),
    ('Congo (Kinshasa)', 'Congo (Kinshasa)'),
    ('Costa Rica', 'Costa Rica'),
    ('Croatia', 'Croatia'),
    ('Cuba', 'Cuba'),
    ('Cyprus', 'Cyprus'),
    ('Czech Republic', 'Czech Republic'),
    ('Denmark', 'Denmark'),
    ('Djibouti', 'Djibouti'),
    ('Dominica', 'Dominica'),
    ('Dominican Republic', 'Dominican Republic'),
    ('Ecuador', 'Ecuador'),
    ('Egypt', 'Egypt'),
    ('El Salvador', 'El Salvador'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),
    ('Eswatini', 'Eswatini'),
    ('Ethiopia', 'Ethiopia'),
    ('Fiji', 'Fiji'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('Gabon', 'Gabon'),
    ('Gambia', 'Gambia'),
    ('Georgia', 'Georgia'),
    ('Germany', 'Germany'),
    ('Ghana', 'Ghana'),
    ('Greece', 'Greece'),
    ('Grenada', 'Grenada'),
    ('Guatemala', 'Guatemala'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Guyana', 'Guyana'),
    ('Haiti', 'Haiti'),
    ('Honduras', 'Honduras'),
    ('Hungary', 'Hungary'),
    ('Iceland', 'Iceland'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Iraq', 'Iraq'),
    ('Ireland', 'Ireland'),
    ('Israel', 'Israel'),
    ('Italy', 'Italy'),
    ('Jamaica', 'Jamaica'),
    ('Japan', 'Japan'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya', 'Kenya'),
    ('Kiribati', 'Kiribati'),
    ('Kuwait', 'Kuwait'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ('Laos', 'Laos'),
    ('Latvia', 'Latvia'),
    ('Lebanon', 'Lebanon'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Libya', 'Libya'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg', 'Luxembourg'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Malaysia', 'Malaysia'),
    ('Maldives', 'Maldives'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marshall Islands', 'Marshall Islands'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Mexico', 'Mexico'),
    ('Micronesia', 'Micronesia'),
    ('Moldova', 'Moldova'),
    ('Monaco', 'Monaco'),
    ('Mongolia', 'Mongolia'),
    ('Montenegro', 'Montenegro'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Myanmar', 'Myanmar'),
    ('Namibia', 'Namibia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('New Zealand', 'New Zealand'),
    ('Nicaragua', 'Nicaragua'),
    ('Niger', 'Niger'),
    ('Nigeria', 'Nigeria'),
    ('North Korea', 'North Korea'),
    ('North Macedonia', 'North Macedonia'),
    ('Norway', 'Norway'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Palau', 'Palau'),
    ('Palestine', 'Palestine'),
    ('Panama', 'Panama'),
    ('Papua New Guinea', 'Papua New Guinea'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Philippines', 'Philippines'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Qatar', 'Qatar'),
    ('Romania', 'Romania'),
    ('Russia', 'Russia'),
    ('Rwanda', 'Rwanda'),
    ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
    ('Saint Lucia', 'Saint Lucia'),
    ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
    ('Samoa', 'Samoa'),
    ('San Marino', 'San Marino'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Senegal', 'Senegal'),
    ('Serbia', 'Serbia'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Singapore', 'Singapore'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Solomon Islands', 'Solomon Islands'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('South Korea', 'South Korea'),
    ('South Sudan', 'South Sudan'),
    ('Spain', 'Spain'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudan', 'Sudan'),
    ('Suriname', 'Suriname'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Syria', 'Syria'),
    ('Taiwan', 'Taiwan'),
    ('Tajikistan', 'Tajikistan'),
    ('Tanzania', 'Tanzania'),
    ('Thailand', 'Thailand'),
    ('Timor-Leste', 'Timor-Leste'),
    ('Togo', 'Togo'),
    ('Tonga', 'Tonga'),
    ('Trinidad and Tobago', 'Trinidad and Tobago'),
    ('Tunisia', 'Tunisia'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ukraine', 'Ukraine'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('United Kingdom', 'United Kingdom'),
    ('United States', 'United States'),
    ('Uruguay', 'Uruguay'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Vanuatu', 'Vanuatu'),
    ('Vatican City', 'Vatican City'),
    ('Venezuela', 'Venezuela'),
    ('Vietnam', 'Vietnam'),
    ('Yemen', 'Yemen'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
]

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(unique=True)
    nationality = models.CharField(max_length=100, choices=COUNTRY_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Investment balances
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    steel = models.DecimalField(max_digits=20, decimal_places=10, default=0.00)
    iron_ore = models.DecimalField(max_digits=20, decimal_places=10, default=0.00)
    lithium = models.DecimalField(max_digits=20, decimal_places=10, default=0.00)
    gold = models.DecimalField(max_digits=20, decimal_places=10, default=0.00)
    kaolin = models.DecimalField(max_digits=20, decimal_places=10, default=0.00)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def deposit(self, crypto: str, amount, description=""):
        field_map = {
            'FORGEX': 'steel',
            'FEVAULT': 'iron_ore',
            'CHARGECOIN': 'lithium',
            'AUXCOIN': 'gold',
            'WHITEEARTH': 'kaolin',
        }
        field = field_map.get(crypto)
        if not field:
            raise ValueError("Invalid cryptocurrency type")

        current_balance = getattr(self, field)
        setattr(self, field, current_balance + amount)
        self.save()

        DepositHistory.objects.create(
            account=self,
            crypto=crypto,
            amount=amount,
            description=description,
        )

    def withdraw(self, crypto: str, amount, description=""):
        field_map = {
            'FORGEX': 'steel',
            'FEVAULT': 'iron_ore',
            'CHARGECOIN': 'lithium',
            'AUXCOIN': 'gold',
            'WHITEEARTH': 'kaolin',
        }

        field = field_map.get(crypto)
        if not field:
            raise ValueError("Invalid cryptocurrency type")

        current_balance = getattr(self, field)
        if current_balance >= amount:
            setattr(self, field, current_balance - amount)
            self.save()

            WithdrawalHistory.objects.create(
                account=self,
                crypto=crypto,
                amount=amount,
                description=description,
            )
        else:
            raise ValueError("Insufficient balance")

class DepositHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='deposits')
    crypto = models.CharField(max_length=20, choices=CRYPTO_CHOICES)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.fullname} - {self.crypto} Deposit: {self.amount}"

    @property
    def crypto_symbol(self):
        return {
            'FORGEX': '🔩',     
            'FEVAULT': '⛓️',    
            'CHARGECOIN': '⚡',  
            'AUXCOIN': '🪙',     
            'WHITEEARTH': '🏺',  
        }.get(self.crypto, '')

class WithdrawalHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='withdrawals')
    crypto = models.CharField(max_length=20, choices=CRYPTO_CHOICES)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.fullname} - {self.crypto} Withdrawal: {self.amount}"

    @property
    def crypto_symbol(self):
        return {
            'FORGEX': '🔩', 
            'FEVAULT': '⛓️',   
            'CHARGECOIN': '⚡',  
            'AUXCOIN': '🪙',     
            'WHITEEARTH': '🏺',  
        }.get(self.crypto, '')

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investments')
    payment_method = models.CharField(max_length=100)
    earnings = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    activation_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)  # e.g., "active", "completed", "pending"

    def __str__(self):
        return f"{self.user.username} - {self.payment_method}"

class InvestmentHistory(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investment_histories')
    payment_method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(auto_now_add=True)

