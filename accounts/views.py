# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from .forms import CustomUserCreationForm

# class SignUpView(CreateView):
#     form_class=CustomUserCreationForm
#     success_url=reverse_lazy('login')
#     template_name='registration/signup.html'


from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import CustomUserChangeForm,CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # 1. Foydalanuvchini bazaga saqlaymiz
        user = form.save()
        
        # 2. Formadan parolni ochiq holda olamiz (Emailga yuborish uchun)
        # Odatda CustomUserCreationForm da parol maydoni 'password1' yoki 'password' bo'ladi
        password = form.cleaned_data.get('password1') or form.cleaned_data.get('password')
        
        # 3. Email xabarini tayyorlaymiz
        subject = "Blog2 - Ro'yxatdan o'tganingiz bilan tabriklaymiz!"
        message = (
            f"Salom {user.username}!\n\n"
            f"Siz muvaffaqiyatli ro'yxatdan o'tdingiz.\n"
            f"Sizning kirish ma'lumotlaringiz:\n"
            f"Login (Email): {user.email}\n"
            f"Parol: {password}\n\n"
            f"Saytga kirish: {self.request.build_absolute_uri('/')}\n\n"
            f"Xush kelibsiz!"
        )
        
        # 4. Emailni yuboramiz
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER, # Yuboruvchi email
                [user.email],             # Qabul qiluvchi email
                fail_silently=False,
            )
        except Exception as e:
            # Xatolik bo'lsa terminalda ko'rinadi (masalan SMTP paroli xato bo'lsa)
            print(f"EMAIL ERROR: {e}")

        return super().form_valid(form)


class UserEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user # Faqat o'zining profilini tahrirlashi uchun
