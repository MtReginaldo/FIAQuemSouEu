import PySimpleGUI as sg
import sys
import subprocess

sg.theme('DarkBlue13')

personagens = ["Buzz Lightear", "Dexter", 
               "Dick Vigarista", "Doutora Brinquedos", 
               "Edna Moda", "Eustácio", 
               "Fred Flinstone", "Girafales", 
               "Guido", "Johnny Bravo", 
               "Linguini", "Lula Molusco",
               "Mario", "Popeye",
               "Policial", "Prefeito", 
               "Sherlock Holmes", "Vicky",
               "Woody", "Homer Simpson"]

def main():
    layout = [
    [sg.Text("Faça sua pergunta:")],
    [sg.Output(size=(60,2), key='Output'), sg.Button('Próxima'), sg.Button('Perguntar')],
    [sg.Listbox(personagens, size=(20, 10), key="lista_personagens")],
    [sg.Text("Pergunta de seu oponente:")],
    [sg.Output(size=(60,2), key='Output'), sg.Button('Sim'), sg.Button('Não')]
    ]


    janela = sg.Window('Quem eu Sou?', layout, finalize=True)

    while True:          
        event, values = janela.Read()
        if event in (None, 'Exit'):         
            janela.Close()
            break

        if event == 'Perguntar':                 
            runCommand(cmd=values['_IN_'], janela=janela)

def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None       
    retval = p.wait(timeout)
    return (retval, output)

if __name__ == '__main__':
    main()
