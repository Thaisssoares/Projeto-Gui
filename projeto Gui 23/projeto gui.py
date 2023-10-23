#Introdução à GUI

import PySimpleGUI as psg

#Desenho da interface grafica
layout = [
    [psg.Text('***'),psg.Text('-------'),psg.Text('*****')],
    [psg.Button('---Clique Aqui---')]],
#Definir o frame
window= psg.Window('Minha primeira tela em Python', layout)

#Imprimir a janela na tela
while True:
    evento,valor= window.read()
    if evento == psg.WIN_CLOSED:
        break
        psg.popoup('Progremação Python \n botão clicado!', title=Senai)

window.close()
