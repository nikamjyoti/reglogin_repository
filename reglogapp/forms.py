from django import forms
class registrationform(forms.Form):
    first_name=forms.CharField(label="Enter Your  First Name",
                          widget=forms.TextInput(
                              attrs={
                                  'placeholder':'your first name',
                                  'class':'form-control'
                              }
                          )
                               )
    last_name = forms.CharField(label="Enter Your Last_name",
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'your last name',
                                    'class': 'form-control'
                                }
                            )
                                   )
    Username= forms.CharField(label="Enter Your Username",
                                widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'your user name',
                                        'class': 'form-control'
                                    }
                                )
                                )
    password = forms.CharField(label="Enter Your password",
                                   widget=forms.PasswordInput(
                                       attrs={
                                           'placeholder': 'your password',
                                           'class': 'form-control'
                                       }
                                   )
                                   )
    mobile = forms.CharField(label="Enter Your Mobile Number",
                                widget=forms.NumberInput(
                                    attrs={
                                        'placeholder': 'your number',
                                        'class': 'form-control'
                                    }
                                )
                                )

    email= forms.EmailField(label="Enter your email",
                            widget=forms.EmailInput(
                                attrs={
                                    'placeholder': 'your Email',
                                    'class': 'form-control'
                                }
                            ))
class  loginform(forms.Form):
    Username = forms.CharField(label="Enter Your Username",
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'your user name',
                                       'class': 'form-control'
                                   }
                               )
                               )
    password = forms.CharField(label="Enter Your password",
                                  widget=forms.PasswordInput(
                                      attrs={
                                          'placeholder': 'your password',
                                          'class': 'form-control'
                                      }
                                  )
                                  )




