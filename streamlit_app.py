import streamlit as st
import sql

def cargaErro():


    cursor = sql.conexao_sql()

    cursor.execute('SELECT HANDLE FROM BB_LOGINTEGRACOES WHERE SITUACAO = 2')

    handleCargaErro = cursor.fetchall()

    handles = []
    for i in handleCargaErro:
        i = list(i)
        handles += i

    st.title("CARGA DE ERRO - UPDATE")
    with st.form('cargaErro'):
        
        campoErrado = st.text_input("INSIRA A INFORMAÇÃO ERRADA: ")
        campoCorreto = st.text_input("INSIRA A INFORMAÇÃO CORRETA: ")
        handle = st.text_input("INFORME O HANDLE")
        alterar = st.form_submit_button("ALTERAR")
        if alterar:
            if handle in str(handles):
                query = f"UPDATE BB_LOGINTEGRACOES SET XMLRESERVA = REPLACE(CONVERT(VARCHAR(MAX),XMLRESERVA),'{campoErrado}','{campoCorreto}') WHERE SITUACAO = 2 AND HANDLE IN ({handle})"
                cursor.execute(query)
                cursor.commit()
                st.success("Pedido ajustado | Verifique a correção!")
                st.spinner()
            else:
                st.error("Pedido não localizado | Verifique o HANDLE!")

cargaErro()
