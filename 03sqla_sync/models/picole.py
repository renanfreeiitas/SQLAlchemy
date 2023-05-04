import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime
from typing import List, Optional

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

# Um picole, pode ter varios ingredientes
ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey('ingredientes.id'))
)

# Um picole pode ter muitos conservantes
conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_conservantes', sa.Integer, sa.ForeignKey('conservantes.id'))
)

# Um picole poder ter muitos aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_aditivos_nutritivos', sa.Integer,
              sa.ForeignKey('aditivos_nutritivos.id'))
)


class Picole(ModelBase):
    __tablename__: str = 'picoles'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(
        sa.DateTime, default=datetime.now, index=True)

    preco: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)

    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey('sabores.id'))
    # configuracao interna do SQL Alchemy
    sabor: Sabor = orm.relationship('Sabor', lazy='joined')

    id_tipo_embalagem: int = sa.Column(
        sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = orm.relationship(
        'TipoEmbalagem', lazy='joined')  # configuracao interna do SQL Alchemy

    id_tipo_picole: int = sa.Column(
        sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: TipoPicole = orm.relationship(
        'TipoPicole', lazy='joined')  # configuracao interna do SQL Alchemy

    # Um picole pode ter varios ingredientes
    ingredientes: List[Ingrediente] = orm.relationship(
        'Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='joined')

    # Um picole pode ter varios conservantes ou nenhum
    conservantes: Optional[List[Conservante]] = orm.relationship(
        'Conservante', secondary=conservantes_picole, backref='conservante', lazy='joined')

    # Um picole pode ter varios aditivos nutritivos ou nenhum
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = orm.relationship(
        'AditivoNutritivo', secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo', lazy='joined')

    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preco {self.preco}>'
