from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", help_text="Краткая запись: Фамилия И.О.")
    age = forms.IntegerField(label="Возраст клиента")
    basket = forms.BooleanField(label="Согласие с условиями")
    vyb = forms.NullBooleanField(label="Доволен сервисом?")
    email = forms.EmailField(label="Адрес электронной почты:")
    about = forms.RegexField(regex="G. *s", label="О клиенте:")
    url_text = forms.URLField(label="Ссылка на профиль:")
    file_path = forms.FilePathField(label="Выберите файл", path="D:\Downloads")
    file = forms.FileField(label="Файл")
