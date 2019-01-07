import ply.lex as lex
import ply.yacc as yacc
import sys
import os
import psutil
import subprocess


def kill(name):
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == name:
            p.kill()


tokens = [
    'RUN',
    'CLOSE',
    'CHROME',
    'NOTEPAD',
    'STEAM',
    'DISCORD',
    'WEBSITE',
    'SITE',
    'DOCUMENT',
    'PLIK'
]

def t_PLIK(t):
    r'\w+\.(txt|doc|pdf)'
    return t

def t_DOCUMENT(t):
    r'do[kc]ument|plik|pdf'
    return t

def t_WEBSITE(t):
    r'(www\.)?\w+\.[a-z]{2,3}'
    return t

def t_SAVE(t):
    r'zapinsz|napisz'
    return t


def t_RUN(t):
    r'otw[oó]rz|uruchom|w[lł][aą]cz'
    return t


def t_CLOSE(t):
    r'zamknij|wy[lł][aą]cz'
    return t


def t_CHROME(t):
    r'go+gle|chrome'
    return t

def t_STEAM(t):
    r'steam'
    return t

def t_DISCORD(t):
    r'discord'
    return t


def t_NOTEPAD(t):
    r'notatnik|notepad'
    return t

def t_SITE(t):
    r'\w+'
    return t


t_ignore = r' '


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()


def p_start(p):
    '''
    start : run program
        | close program
        | search WEBSITE
        | open doc
    '''
    p[0] = (p[1], p[2])
    run(p[0])

def p_open(p):
    """
    open : run DOCUMENT
    """
    p[0] = ('doc')

def p_doc(p):
    '''
    doc : PLIK
    '''
    p[0] = p[1]

def p_program(p):
    '''
    program : chrome
        | notepad
        | steam
        | discord
    '''
    p[0] = (p[1])

def p_discord(p):
    '''
    discord : DISCORD
    '''
    p[0] = ('discord')

def p_steam(p):
    '''
    steam : STEAM
    '''
    p[0] = ('steam')

def p_chrome(p):
    '''
    chrome : CHROME
    '''
    p[0] = ('chrome')

def p_notepad(p):
    '''
    notepad : NOTEPAD
    '''
    p[0] = ('notepad')

def p_run(p):
    '''
    run : RUN
    '''
    p[0] = ('run')

def p_close(p):
    '''
    close : CLOSE
    '''
    p[0] = ('close')




def p_serch(p):
    '''
    search : run
    '''
    p[0] = ('web')


def p_error(p):
    print("Syntax error found!")


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


parser = yacc.yacc()


def run(p):
    print(p)
    if p[0] == 'run':
        if p[1] == 'chrome':
            os.system("start chrome")
        if p[1] == 'notepad':
            os.system("start notepad")
        if p[1] == 'steam':
            os.system("start steam:\\\\")
        if p[1] == 'discord':
            os.system("start discord:\\\\")

    if p[0] == 'close':
        if p[1] == 'chrome':
            kill("chrome.exe")
        if p[1] == 'notepad':
            kill("notepad.exe")
        if p[1] == 'steam':
            kill("steam.exe")
        if p[1] == 'discord':
            kill("Discord.exe")

    if p[0] == 'web':
        os.system("start chrome " + str(p[1]))

    if p[0] == 'doc':
        os.startfile(p[1])


while True:
    try:
        s = input('>> ')

    except EOFError:
        break
    parser.parse(s)
