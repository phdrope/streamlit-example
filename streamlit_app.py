import streamlit as st


tipoSolicitacao = st.selectbox(
    'Tipo de Solicição:',
    (
    '...',
    'Integração de Pedidos',
    'Integração Vários Pedidos',
    'Pré-pagamento',
    'Alterações via Update - Permitir faturar s/ conciliar',
    'Alterações via Update - Taxa Adm, Markup, FEE, Comissão, Outras Taxas',
    'Alterações via Update - Agente, Cliente, Consolidador, Fornecedor',
    'Alterar Origem do Pedido',
    'Cancelar / Emitir Notas Fiscais - NF',
    'Cancelar, Excluir Pedidos ou Duplicidade',
    'Erro Faturas / Lotes',
    'Erro/Problema Portal de Faturas',
    'VM WEB fora / WEBTES fora (Sem Conexão)',
    'Instalação do Sistema Benner',
    'Outras Solicitações' ))


if tipoSolicitacao == 'Integração de Pedidos':
    st.write(' ')
    st.write('Para integração de dois ou mais pedidos, utilize a opção "Integração Vários Pedido"')
    st.number_input('Número do Pedido, OS ou SV: *')
    st.selectbox('Sistema de Reserva: *', ('...','ARGO','RESERVE', 'LEMONTECH','PAYTRACK','WOOBA'))
    st.selectbox('Cliente: *', ('Exemplos','Vale','BRF', 'Minerva', 'Kroton - Cogna'))
    st.text_area("Descrição:")

if tipoSolicitacao == 'Integração Vários Pedidos':
    st.write(f'''Para a integração de vários pedidos, por gentileza, anexar uma planilha contendo as informações:

1) Número do Pedido, OS ou SV
2) Nome do Cliente
3) Sistema de Reserva - OBT
''')

    st.text_input('Assunto:')
    st.text_area('Descrição:')
    st.file_uploader('Anexar a planilha com os pedidos: *')
    st.checkbox('Está anexada a planilha com as informações solicitadas? *')

if ((tipoSolicitacao == 'Pré-pagamento')
    or (tipoSolicitacao == 'Outras Solicitações') 
    or (tipoSolicitacao == 'VM WEB fora / WEBTES fora (Sem Conexão)') 
    or (tipoSolicitacao == 'Erro/Problema Portal de Faturas')
    or (tipoSolicitacao == 'Cancelar, Excluir Pedidos ou Duplicidade')
    or (tipoSolicitacao == 'Erro Faturas / Lotes')
    ):
    st.write('Ao fazer a solicitação, detalhe o máximo que conseguir, com: prints, arquivos ou qualquer tipo de evidência')
    st.text_input('Assunto: *')
    st.text_area('Descrição: *')
    st.file_uploader('Anexar um arquivo:')


if ((tipoSolicitacao == 'Alterar Origem do Pedido')    
    or (tipoSolicitacao == 'Alterações via Update - Permitir faturar s/ conciliar') ):

    st.write('Ao fazer a solicitação, anexar um arquivo de planilha contendo pelo menos o RLOC de localização no Benner')

    st.text_input('Assunto:')
    st.text_area('Descrição:')
    st.file_uploader('Anexar um arquivo: *')
    st.checkbox('Está anexada a planilha com as informações solicitadas? *')

if tipoSolicitacao == 'Alterações via Update - Taxa Adm, Markup, FEE, Comissão, Outras Taxas':
    
    st.write('Informar exatamente o novo valor do campo. O chamado retornará em caso de solicitação de ajustes por percentuais')
    st.selectbox('Selecionar o campo a ser alterado:',('Taxa Adm','Markup', 'FEE', 'Comissão', 'Outras Taxas'))
    st.text_input('Assunto:')
    st.text_area('Descrição:')
    st.file_uploader('Anexar um arquivo: *')
    st.checkbox('Está anexada a planilha com as informações solicitadas? *')

if tipoSolicitacao == 'Alterações via Update - Agente, Cliente, Consolidador, Fornecedor':

    st.write('Informar o RLOC e para qual BKO alterar.')

    st.selectbox('Selecionar o campo a ser alterado:',('Agente','Cliente', 'Consolidador', 'Fornecedor'))
    st.text_input('Assunto:')
    st.text_area('Descrição:')
    st.file_uploader('Anexar um arquivo:')

if tipoSolicitacao == 'Cancelar / Emitir Notas Fiscais - NF':

    st.selectbox('Solicitação:',('Cancelar', 'Emitir'))

    st.text_input('Ordem de Venda: *',placeholder='Preencha com o número da Ordem de Venda da NF')
    st.text_input('Nota Fiscal: *', placeholder='Preencha o número da Nota Fiscal')
    st.text_input('Data de Emissão: *')
    st.text_input('Valor da NF: *')


    st.text_input('Assunto:')
    st.text_area('Descrição:')
    st.file_uploader('Anexar um arquivo:')

if tipoSolicitacao == 'Instalação do Sistema Benner':

    st.write(f'''Para instalação do Sistema Benner, encaminhar um chamado para equipe de Infraestrutura, através link: 
https://chamados.copastur.com.br/support/catalog/items/86''')
