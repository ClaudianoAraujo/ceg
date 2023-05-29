from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        usuario = self.model(
            email=self.normalize_email(email)
        )
        
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False
        
        if password:
            usuario.set_password()
            
        usuario.save()
        
        return usuario
    
    def create_superuser(self, email, password):
        usuario = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        
        usuario.set_password(password)
        
        usuario.save()
        return usuario
        
        
        
        

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='E-mail do usuario',
        max_length=255,
        unique=True
    )
    
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome:',
        null=False, blank=False,
        default='João',
    )
    
    cel = models.CharField(
        max_length=11,
        null=False, blank=False,
        verbose_name='Cel: 11 93758-8432',
        default=0,
    )
    
    estado = models.CharField(
        max_length=100,
        verbose_name='Estado:',
        null=False, blank=False,
        default='São Paulo',
    )
    
    cidade = models.CharField(
        max_length=100,
        verbose_name='Cidade:',
        null=False, blank=False,
        default='São Paulo',
    )
    
    foto = models.ImageField(
        null=True, blank=True,
        upload_to='fotos'
    )
    
    is_active = models.BooleanField(
        verbose_name='Usuario ativo ?',
        default=True,
    )
    
    is_staff = models.BooleanField(
        default=False,
    )
    
    is_superuser = models.BooleanField(
        verbose_name='Super usuario ?',
        default=False,
    )
    
    USERNAME_FIELD = 'email'
    objects = UsuarioManager()
    
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
    
    def __str__(self):
        return self.email
    
        
        

