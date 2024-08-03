import streamlit as st
import time

def main():
    st.title("Estudos Streamlit")
    st.header("Input de texto")
    input_text = st.text_input(label="digite um texto")
    if input_text:
        st.write(f'você digitou: {input_text}')

    st.header("Seleção")
    selected_option = st.selectbox(f"Selecione uma opção: ",['Opção 1','Opção 2','Opção 3','Opção 4'])
    if selected_option:
        st.write(f"Você selecionou: {selected_option}")
    

    st.header("Slider")
    slider_value = st.slider("Escolha um valor")
    st.write(f"Você selecionou o valor {slider_value}")

    st.header("Checkbox")
    checkbox_state = st.checkbox("Marque para ativar")
    if checkbox_state:
        st.write(f"Checkbox ativado")

    st.header("Botão")
    botao= st.button("Clique aqui")
    if botao:
        clicado = st.write("Você clicou no botão")



    st.header("Upload de arquivo")
    uploaded_file = st.file_uploader("Escolha um arquivo", accept_multiple_files=True)
    if uploaded_file:
        with st.spinner("Aguarde"):
            time.sleep(3)
            st.success("Carregado com sucesso!")        
    

    st.header("Gráfico")
    data = {'x': [0,10,30,10,50], 'y':[0,20,30,40,50]}
    st.line_chart(data)
    


main()