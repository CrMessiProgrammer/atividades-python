'''-----------------------------------------------------------------------------
   MUNDO 01 - DESAFIO 021
   NOME: Carlos Henrique
   ENUNCIADO: 021 – Faça um programa em Python que abra e reproduza o
   áudio de arquivo MP3.
-----------------------------------------------------------------------------'''
import pygame
pygame.init()
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
