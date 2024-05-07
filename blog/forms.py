from django import forms
from django.contrib.auth.models import User
from .models import *

from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField(label="الاسم المستخدم",widget=forms.TextInput(attrs={'class':'form-control form-control-lg input-group-append '}))
    password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))

    class Meta:
        model = User
        fields = ("username", "first_name", 'email')
        widget ={
            'username': forms.TextInput(attrs={'class':'form-control form-control-success '}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-success '}),
            'email': forms.TextInput(attrs={'class':'form-control form-control-success '}),
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("password don\"t match;")
        return cd['password2']

class useredit(forms.ModelForm):
    class Meta:
        model= User
        fields = ('first_name', 'last_name', 'email')
        widget ={
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-success '}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-success '}),
            'email': forms.TextInput(attrs={'class':'form-control form-control-success '}),
        }

class Chat_form(forms.ModelForm):
    class Meta:
        model = chat_model
        fields = ("user", "mas")
        widget ={
            'mas': forms.TextInput(attrs={'class':'form-control form-control-success '}),
           
        }

class Profiledit(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ('__all__')




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'outher',
            'photo_book',
            'photo_outher',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'total_rental',
            'status',
            'Category',
            'open_book',
            'description',
            # 'url_book',
            # 'rating',
            
            
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-success '}),
            'outher': forms.TextInput(attrs={'class':'form-control form-control-success'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control form-control-success'}),
            'photo_outher': forms.FileInput(attrs={'class':'form-control form-control-success'}),
            'pages': forms.NumberInput(attrs={'class':'form-control form-control-success'}),
            'price': forms.NumberInput(attrs={'class':'form-control form-control-success'}),
            'retal_price_day': forms.NumberInput(attrs={'class':'form-control form-control-success', 'id':'rentalprice'}),
            'retal_period': forms.NumberInput(attrs={'class':'form-control form-control-success', 'id':'rentaldays'}),
            'total_rental': forms.NumberInput(attrs={'class':'form-control form-control-success', 'id':'totalrental'}),
            'status': forms.Select(attrs={'class':'form-control form-control-success'}),
            'Category': forms.Select(attrs={'class':'form-control form-control-success'}),
            'open_book': forms.FileInput(attrs={'class':'form-control form-control-success'}),
            'description' :forms.TextInput(attrs={'class':'form-control form-control-success'}),
            # 'rating' :forms.TextInput(attrs={'class':'form-control'}),
            
            
        }
        labels = {
            'title':("العنوان"),
            'outher':('عنوان اخر'),
        }
        help_texts = {
            'title':("ارجاء ادخال عنوان اخر"),
        }
        error_messages ={
            'title':{
                'max_length':('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'),
            },
        }

# class UserRegisterForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100)
#     lest_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ('username', 'first_name','lest_name','email', 'password1', 'password2')
#         widgets = {
#             'user': forms.TextInput(attrs={'class': 'form-control form-control-lg input-group-append'}),
#             'address': forms.TextInput(attrs={'class': 'form-control form-control-lg input-group-append'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg input-group-append'}),
#             'password': forms.EmailInput(attrs={'class': 'form-control form-control-lg input-group-append'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg input-group-append'}),
#         }


# انشاء حساب 
class RegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'username',
            'password1',
            'password2'
        ]
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control form-control-lg input-group-append '}),
            'email':forms.EmailInput(attrs={'class':'form-control form-control-lg input-group-append '}),
            'username':forms.TextInput(attrs={'class':'form-control form-control-lg input-group-append '}),
            'password1':forms.PasswordInput(attrs={'class':'form-control form-control-lg input-group-append'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control form-control-lg input-group-append'}),

        }
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user



class ChangePasswordForm(forms.ModelForm):
	id = forms.CharField(widget=forms.HiddenInput())
	old_password = forms.CharField(widget=forms.PasswordInput(), label="Old password", required=True)
	new_password = forms.CharField(widget=forms.PasswordInput(), label="New password", required=True)
	confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm new password", required=True)

	class Meta:
		model = User
		fields = ('id', 'old_password', 'new_password', 'confirm_password')

	def clean(self):
		super(ChangePasswordForm, self).clean()
		id = self.cleaned_data.get('id')
		old_password = self.cleaned_data.get('old_password')
		new_password = self.cleaned_data.get('new_password')
		confirm_password = self.cleaned_data.get('confirm_password')
		user = User.objects.get(pk=id)

		if not user.check_password(old_password):
			self._errors['old_password'] = self.error_class(['Old password do not match. Try again'])
		if new_password != confirm_password:
			self._errors['new_password'] = self.error_class(['Passwords do not match.'])
		return self.cleaned_data