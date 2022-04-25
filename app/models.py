from django.db import models

# Create your models here.


TIPO_CHOISE = {
    ('40', '40'),
    ('20', '20'),
}


CATEGORIA_CHOISE = {
    ('Exportação', 'Exportação'),
    ('Importação', 'Importação'),
}


STATUS_CHOISE = {
    ('Vazio', 'Vazio'),
    ('Cheio', 'Cheio'),
}


MOVIMENTOS_CHOISE = {
    ('Gate Entrada', 'Gate Entrada'),
    ('Pesagem', 'Pesagem'),
    ('Posicionamento', 'Posicionamento'),
    ('Scanner', 'Scanner'),
    ('Reposicionamento', 'Reposicionamento'),
    ('Embarque', 'Embarque'),
    ('Descarga', 'Descarga'),
    ('Gate Saida', 'Gate Saida')
}


class cadastro(models.Model):
    cliente = models.CharField(max_length=100)
    idContainer = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOISE)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOISE)
    status = models.CharField(max_length=10, choices=STATUS_CHOISE)


class movimento(models.Model):
    idcontainer = models.ForeignKey(cadastro, on_delete=models.CASCADE)
    movimentos = models.CharField(max_length=20, choices=MOVIMENTOS_CHOISE)
    datacomeco = models.DateTimeField('Data/Hora', null=True, blank=True)
    datafim = models.DateTimeField('Data/Hora', null=True, blank=True)
