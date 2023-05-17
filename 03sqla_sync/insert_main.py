from conf.db_session import create_session

from time import sleep

# insert parte 1
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

# insert parte 2
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole


# 1 Aditivos Nutritivos
def insert_aditivo_nutritivo() -> None:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input('Informe o nome do aditivo nutritivo: ').title()
    formula_quimica: str = input(
        'Informe a formula quimica do aditivo: ').title()

    an: AditivoNutritivo = AditivoNutritivo(
        nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)

        session.commit()

    print('Aditivo cadastrado com sucesso.')
    print(f'ID: {an.id}')
    print(f'Data: {an.data_criacao}')
    print(f'Nome: {an.nome}')
    print(f'Formula quimica: {an.formula_quimica}')

    sleep(2)


# 2 Sabor
def insert_sabor() -> None:
    print('Cadastrando sabor')

    nome: str = input('Informe o sabor a ser cadastrado: ').title()

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)

        session.commit()

    print('Sabor cadastrado com sucesso.')
    print(f'ID: {sabor.id}')
    print(f'Data: {sabor.data_criacao}')
    print(f'Nome: {sabor.nome}')
    sleep(2)


# 3 Tipo de Embalagem
def insert_tipo_embalagem() -> None:
    print('Cadastrando tipo de embalagem')

    nome: str = input('Informe o tipo de embalagem a ser cadastrado: ').title()

    tipo_emb: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_emb)

        session.commit()

    print('Tipo de embalagem cadastrado com sucesso.')
    print(f'ID: {tipo_emb.id}')
    print(f'Data: {tipo_emb.data_criacao}')
    print(f'Nome: {tipo_emb.nome}')
    sleep(2)


# 4 Tipo de Picole
def insert_tipo_picole() -> None:
    print('Cadastrando tipo de picole')

    nome: str = input('Informe o tipo de picole a ser cadastrado: ').title()

    tipo_pic: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_pic)

        session.commit()

    print('Tipo de picole cadastrado com sucesso.')
    print(f'ID: {tipo_pic.id}')
    print(f'Data: {tipo_pic.data_criacao}')
    print(f'Nome: {tipo_pic.nome}')
    sleep(2)


# 5 Ingredientes
def insert_ingrediente() -> None:
    print('Cadastrando ingrediente')

    nome: str = input('Informe o ingrediente a ser cadastrado: ').title()

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)

        session.commit()

    print('Ingrediente cadastrado com sucesso.')
    print(f'ID: {ingrediente.id}')
    print(f'Data: {ingrediente.data_criacao}')
    print(f'Nome: {ingrediente.nome}')
    sleep(2)


# 6 conservantes
def insert_conservante() -> None:
    print('Cadastrando conservante')

    nome: str = input('Informe o conservante a ser cadastrado: ').title()
    descricao: str = input(
        'Insira uma descricao para o conservante: ').capitalize()

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)

        session.commit()

    print('Conservante cadastrado com sucesso.')
    print(f'ID: {conservante.id}')
    print(f'Data: {conservante.data_criacao}')
    print(f'Nome: {conservante.nome}')
    print(f'Descricao: {conservante.descricao}')
    sleep(2)


# 7 Revendedores
def insert_revendedor() -> Revendedor:
    print('Cadastrando revendedor')

    cnpj: str = input('Informe o CNPJ do revendedor a ser cadastrado: ')
    razao_social: str = input(
        'Informe a razao social do revendedor a ser cadastrado: ').title()
    contato: str = input('Informe o contato do revendedor: ').title()

    revendedor: Revendedor = Revendedor(
        cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)

        session.commit()

    return revendedor
    sleep(2)


# 8 Lote
def insert_lote() -> Lote:
    print('Cadastrando lote')

    id_tipo_picole: int = input(
        'Informe o ID do tipo do picole: ')
    quantidade: int = input(
        'Informe a quantidade de picoles a ser cadastrado neste lote: ')

    lote: Lote = Lote(
        id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lote)

        session.commit()

        return lote

    print('Lote cadastrado com sucesso.')
    print(f'ID: {lote.id}')
    print(f'Data: {lote.data_criacao}')
    print(f'Tipo de picole: {lote.id_tipo_picole}')
    print(f'Quantidade: {lote.quantidade}')
    sleep(2)


# 9 Nota fical
def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastrando Nota Fiscal')

    valor: float = input(
        'Informe o valor da nota fiscal: ')
    numero_serie: str = input(
        'Informe o numero de serie: ')
    descricao: str = input(
        'Insira a descricao: ')
    id_revendedor: int = input(
        'Insira o ID do revendedor: ')

    nf: NotaFiscal = NotaFiscal(
        valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)

    lote = insert_lote()
    nf.lotes.append(lote)

    while True:
        opcao: str = input(
            'Cadastrar novo lote a nota fiscal, digite "1" OU digite "0" para continuar: ')
        if opcao == '1':
            lote = insert_lote()
            nf.lotes.append(lote)
        elif opcao == '0':
            print('Finalizando nota fiscal!')
            break
        else:
            print('Opcao invalida!')

        '''lote2 = insert_lote()
        nf.lotes.append(lote2)'''

    with create_session() as session:
        session.add(nf)

        session.commit()

        return nf
    
    
# 10 Picole
def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastrando Nota Fiscal')

    valor: float = input(
        'Informe o valor da nota fiscal: ')
    numero_serie: str = input(
        'Informe o numero de serie: ')
    descricao: str = input(
        'Insira a descricao: ')
    id_revendedor: int = input(
        'Insira o ID do revendedor: ')

    nf: NotaFiscal = NotaFiscal(
        valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)

    lote = insert_lote()
    nf.lotes.append(lote)

    while True:
        opcao: str = input(
            'Cadastrar novo lote a nota fiscal, digite "1" OU digite "0" para continuar: ')
        if opcao == '1':
            lote = insert_lote()
            nf.lotes.append(lote)
        elif opcao == '0':
            print('Finalizando nota fiscal!')
            break
        else:
            print('Opcao invalida!')

    with create_session() as session:
        session.add(nf)

        session.commit()

        return nf



def imprimir_menu():
    print(50*'-')
    print(50*'-')
    print('1 - Aditivo Nutritivo')
    print('2 - Sabor ')
    print('3 - Tipo Embalagem ')
    print('4 - Tipo picole ')
    print('5 - Ingrediente ')
    print('6 - Conservante ')
    print('7 - Revendedor ')
    print('8 - Lote ')
    print('9 - Nota Fiscal ')
    print(50*'-')
    print('0 - Sair ')
    print(50*'-')
    print(50*'-')


if __name__ == '__main__':
    while True:
        imprimir_menu()

        opcao: str = input(
            'Informe o que deseja cadastrar ou  digite "0" para sair: ')
        if opcao == '1':
            insert_aditivo_nutritivo()

        elif opcao == '2':
            insert_sabor()

        elif opcao == '3':
            insert_tipo_embalagem()

        elif opcao == '4':
            insert_tipo_picole()

        elif opcao == '5':
            insert_ingrediente()

        elif opcao == '6':
            insert_conservante()

        elif opcao == '7':
            rev = insert_revendedor()
            print(f'ID: {rev.id}')
            print(f'Data: {rev.data_criacao}')
            print(f'CNPJ: {rev.cnpj}')
            print(f'Razao social: {rev.razao_social}')
            print(f'contato: {rev.contato}')
            sleep(2)

        elif opcao == '8':
            lt = insert_lote()
            print('Lote cadastrado com sucesso.')
            print(f'ID: {lt.id}')
            print(f'Data: {lt.data_criacao}')
            print(f'Tipo de picole: {lt.id_tipo_picole}')
            print(f'Quantidade: {lt.quantidade}')
            sleep(2)

        elif opcao == '9':
            n_fiz = insert_nota_fiscal()
            print('Nota Fiscal cadastrado com sucesso.')
            print(f'ID: {n_fiz.id}')
            print(f'Data: {n_fiz.data_criacao}')
            print(f'Valor: {n_fiz.valor}')
            print(f'Numero de serie: {n_fiz.numero_serie}')
            print(f'Descricao: {n_fiz.descricao}')
            print(f'ID Revendedor: {n_fiz.id_revendedor}')
            sleep(2)

        elif opcao == '0':
            print('Fechando o programa!')
            break
        else:
            print('Opcao invalida!')
