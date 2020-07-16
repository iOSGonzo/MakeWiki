from models import User

class SignupView(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
