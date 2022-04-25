from app.models import cadastro, movimento
from django.forms import ModelForm

# Formularios


TIPO_CHOISE = {('40', '40'), ('20', '20')}

CATEGORIA_CHOISE = {('Exportação', 'Exportação'), ('Importação', 'Importação')}

STATUS_CHOISE = {('Vazio', 'Vazio'), ('Cheio', 'Cheio')}

MOVIMENTOS_CHOISE = {('Gate Entrada', 'Gate Entrada'), ('Pesagem', 'Pesagem'), ('Posicionamento', 'Posicionamento'),
                     ('Scanner', 'Scanner'), ('Reposicionamento', 'Reposicionamento'), ('Embarque', 'Embarque'),
                     ('Descarga', 'Descarga'), ('Gate Saida', 'Gate Saida')}


class cadastroForm(ModelForm):
    class Meta:
        model = cadastro
        fields = ['cliente', 'idContainer', 'tipo', 'categoria', 'status']


class movimentoForm(ModelForm):
    class Meta:
        model = movimento
        fields = ['idcontainer', 'movimentos', 'datacomeco', 'datafim']
