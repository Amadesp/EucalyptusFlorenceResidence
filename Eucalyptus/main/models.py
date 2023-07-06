from django.db import models

# Create your models here.
class Banner(models.Model):
    imagem = models.ImageField(upload_to='banner_index1')

    class Meta:
        verbose_name_plural = '1. Banner/ pagina inicial'
    
class DemoServicos(models.Model):
    imagem = models.ImageField(upload_to='demo_servicos')
    titulo = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    titulo_link = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = '1.2 Imagens/ portfolio pagina inicial'

class Contactos(models.Model):
    titulo = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icon')
    class Meta:
        verbose_name_plural = '1.3 Contactos/ pagina inicial'

class Siga(models.Model):
    titulo = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icon')
    link = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '1.4 Siga-nos/ pagina inicial'

class Fotos_all(models.Model):
    imagem = models.ImageField(upload_to='all_image')
    titulo = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '1.5 Fotos/ pagina inicial'

class Fotos_exterior_home(models.Model):
    imagem = models.ImageField(upload_to='image_exterior')
    titulo = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '1.6 Fotos exterior/ pagina inicial'

class Fotos_quartos_home(models.Model):
    imagem = models.ImageField(upload_to='image_quartos')
    titulo = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '1.7 Fotos quartos/ pagina inicial'

class Fotos_restaurante_home(models.Model):
    imagem = models.ImageField(upload_to='image_restaurante')
    titulo = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '1.8 Fotos restaurante/ pagina inicial'

# plataforma restaurante
class Banner_restaurante(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='banner_rest')
    class Meta:
        verbose_name_plural = '1.9 Banner/ restaurante'

class Fotos_all_restaurante(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='all_image_rest')

    class Meta:
        verbose_name_plural = '2.0 Fotos/ restaurante'

class Fotos_restaurante(models.Model):
    imagem = models.ImageField(upload_to='image_retaurante')
    titulo = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '2.1 Fotos restaurante/ restaurante'

class Fotos_outras_restaurante(models.Model):
    imagem = models.ImageField(upload_to='image_restaurante')
    titulo = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '2.2 Fotos outras/ restaurante'

# plataforma auditorio
class Banner_auditorio(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='banner_aud')
    class Meta:
        verbose_name_plural = '2.3 Banner/ auditorio'

class Fotos_all_auditorio(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='all_image_aud')

    class Meta:
        verbose_name_plural = '2.4 Fotos/ auditorio'

# plataforma quartos
class Banner_quartos(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='banner_quartos')
    class Meta:
        verbose_name_plural = '2.5 Banner/ quartos'
# quarto images
class Fotos_all_quartos(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='all_image_quartos')

    class Meta:
        verbose_name_plural = '2.6 Todas Fotos/ quartos'

class Fotos_quartos(models.Model):
    imagem = models.ImageField(upload_to='image_quartos')
    titulo = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '2.7 Fotos quartos/ quartos'

class Fotos_outras_quartos(models.Model):
    imagem = models.ImageField(upload_to='image_quartos')
    titulo = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '2.8 Fotos outras/ quartos'

class Quartos_preco(models.Model):
    imagem = models.ImageField(upload_to='imahem_quartos')
    titulo = models.CharField(max_length=200)
    # descricao = models.TextField()
    status = models.CharField(max_length=100)
    preco = models.CharField(max_length=50)
    
# plataforma piscina
class Banner_piscina(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='banner_piscina')
    class Meta:
        verbose_name_plural = '2.9 Banner/ piscina'

class Fotos_all_piscina(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='all_image_piscina')

    class Meta:
        verbose_name_plural = '3.0 Fotos/ piscina'
# plataforma jardim para EVENTOS ao ar livre
class Banner_jardim(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='banner_jardim_')
    class Meta:
        verbose_name_plural = '3.1 Banner/ Jardim eventos'

class Fotos_all_jardim(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='all_image_jardim_')

    class Meta:
        verbose_name_plural = '3.2 Fotos/ Jardim eventos'

# plataforma jardim infantil
class Banner_jardim_infantil(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='banner_jardim_infantil')
    class Meta:
        verbose_name_plural = '3.3 Banner/ Jardim infantil'

class Fotos_all_jardim_infantil(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='all_image_jardim_infantil')

    class Meta:
        verbose_name_plural = '3.4 Fotos/ Jardim infantil'

class Localizacao_mapa(models.Model):
    localizacao = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = '3.5 Localizacao/ mapa'


Emscorpionaiml = {
    'host.king.net': 'smtp.gmail.com',
    '465': '587',
    'cley@gmail.com':'eucalyptusfresidence@gmail.com',
    '0rhjddgsgdgs': 'hewvhwfooyccxfih',
}

