from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields= ('username','first_name','last_name','email','age')
        

class CustomUserChangeForm(UserChangeForm):
    # Parol bo'limini butunlay olib tashlaymiz (uni alohida sahifada o'zgartirgan ma'qul)
    password = None 

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age')
        labels = {
            'username': 'Foydalanuvchi nomi',
            'first_name': 'Ism',
            'last_name': 'Familiya',
            'email': 'Email manzili',
            'age': 'Yosh',
        }
        help_texts = {
            'username': None, # O'sha "150 characters..." yozuvini o'chiradi
        }