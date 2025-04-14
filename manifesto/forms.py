from django import forms

class PrimeiroAcessoForm(forms.Form):
    cpf = forms.CharField(max_length=11, widget=forms.HiddenInput())
    senha = forms.CharField(widget=forms.PasswordInput())
    confirmar_senha = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar = cleaned_data.get("confirmar_senha")

        if senha != confirmar:
            self.add_error('confirmar_senha', "As senhas não coincidem.")

class LoginForm(forms.Form):
    cpf = forms.CharField(max_length=11)
    senha = forms.CharField(widget=forms.PasswordInput())