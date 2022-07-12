#!/usr/bin/env python3


# GUI
# A GUI (graphical user interface) is a system of interactive visual components for computer software.
# https://www.computerhope.com/jargon/g/gui.htm


# IMPORT PYTHON MODULE
# IMPORT SEMUA MODUL PYTHON3 YANG KITA PERLUKAN, UNTUK MEMBUAT ALAT ATAU PROGRAM GUI ChatBot INI.
import os
from os import system
import sys
from sys import *
from sys import platform
if platform=="win32":
	system("cls")
	system("pip install tk")
	system("pip install pyfiglet")
	system("cls")
elif platform=="linux" or platform=="linux2" or platform=="linux3":
	system("clear")
	# system("sudo apt-get update")
	# system("sudo apt-get upgrade")
	# system("sudo apt-get install python")
	# system("sudo apt-get install python3")
	# system("sudo apt-get install pip")
	# system("pip install tk")
	# system("pip install pyfiglet")
	# system("pip install pywhatkit")
	system("clear")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mYou Are Using The Operating System: \033[3m\033[92m\033[5m{sys.platform}")
	print("\033[0m")
elif platform=="darwin":
	system("clear")
	os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
	os.system("python3 get-pip.py")
	os.system("pip3 --version")
	os.system("pip --version")
	os.system("python3 -m pip install –upgrade pip")
	system("pip install pyfiglet")
	system("pip install tk")
	system("clear")
import time
from time import sleep,time
import datetime
from datetime import *
import re
from re import *
import tkinter
from tkinter import *
import random
from random import *
import pyfiglet
from pyfiglet import Figlet
import pywhatkit
from pywhatkit import playonyt
Tulisan_Seorang_Remaja_Kesepian=Figlet(font="speed")
print("\033[92m")
print(Tulisan_Seorang_Remaja_Kesepian.renderText("Bot"))
print("\033[91m[\033[94m!\033[91m] \033[94mCreated By: \033[92mRuben Leonardo Sigalingging")
print("\033[91m[\033[94m!\033[91m] \033[94mCreated On: \033[92mSunday, July 10, 2022, 7:42 PM.")
print("\033[91m[\033[94m!\033[91m] \033[94mUsing: \033[92mPython Version 3.8.10")
print("\033[91m[\033[94m!\033[91m] \033[94mMessage: \033[92mKeep Spirit. You Can Do It.\n")


Tkinter_Cursors=[
"arrow","circle","clock","cross","dotbox",
"exchange","fleur","heart","heart","man",
"mouse","pirate","plus","shuttle","sizing",
"spider","spraycan","star","target","tcross",
"trek","watch"
]


# BUAT TAMPILAN PROGRAM GUI NYA. DI DALAM SEBUAH FUNGSI.
def GUI_Chat_Bot(Created_By="Ruben Leonardo Sigalingging"):
	# LANGKAH PERTAMA: KITA BUAT SEBUAH FUNGSI ATAU METODE TKINTER.
	Fungsi_Utama_GUI_ChatBot=Tk()


	# expand Jika disetel ke true, 
	# widget akan diperluas untuk mengisi ruang apa pun yang tidak digunakan di induk widget.
	# fill Menentukan apakah widget mengisi ruang ekstra yang dialokasikan oleh packer, atau mempertahankan dimensi minimalnya sendiri: 
	# NONE (default), X (hanya mengisi secara horizontal), Y (mengisi hanya secara vertikal),
	# atau BOTH (mengisi keduanya secara horizontal dan vertikal ).
	# side Menentukan sisi mana dari paket induk widget terhadap:
	# TOP (default), BOTTOM, LEFT, atau RIGHT.
	Bingkai_Utama_Program_GUI_ChatBot=Frame(Fungsi_Utama_GUI_ChatBot,bg="#2D3033",cursor="fleur",highlightbackground="#808080",bd=2)
	Bingkai_Utama_Program_GUI_ChatBot.pack(expand=False,fill=BOTH,side=TOP)
	# LANGKAH KEDUA: KITA UBAH JUDUL ATAU TITLE PROGRAM GUI NYA.
	# MENGGUNAKAN METODE .TITLE
	Fungsi_Utama_GUI_ChatBot.title("ChatBot GUI By Ruben Leonardo Sigalingging")
	# LANGKAH KETIGA: KITA UBAH UKURAN ATAU SIZE.
	Fungsi_Utama_GUI_ChatBot.geometry("500x500")
	# LANGKAH KEEMPAT: KITA UBAH WARNA LATAR BELAKANG ATAU BACKGROUND PROGRAM.
	Fungsi_Utama_GUI_ChatBot.configure(background="#000000",cursor="crosshair")


	# LANGKAH KELIMA: KITA UBAH LABEL GUI NYA.
	Label_Program_ChatBot_GUI_Ke_1=Label(Bingkai_Utama_Program_GUI_ChatBot,text="Program ChatBot GUI",font=("Ubuntu",25),cursor="pirate",bd=3,width=25,height=1,background="#008b8b",foreground="#ffffff",justify="center")
	Label_Program_ChatBot_GUI_Ke_1.pack(padx=12,pady=12)


	# AKU AKAN MEMBUAT PROGRAM GUI INI MEMPUNYAI NAVBAR, SEPERTI SEBUAH WEBSITE.
	# DAN AKU AKAN MEMBUAT BEBERAPA MENU YANG DAPAT USER PILIH.
	# SEPERTI: Home, GitHub dan ChatBot
	Responsive_Navbar=["Home","GitHub","ChatBot"]


	Python_Tkinter_Pack_Method={"expand ~> ": "True atau False",
	"fill ~> ": "NONE (default), X (Horizontal), Y (Vertikal), BOTH (Horizontal dan Vertikal)",
	"side ~> ": "TOP (default), BOTTOM, LEFT, or RIGHT."}


	Navigation_Bar_Home=Frame(Fungsi_Utama_GUI_ChatBot,cursor="fleur",bg="#4D5157",width=12,height=1)
	Navigation_Bar_Home.pack(expand=False,fill=BOTH,side="left")


	Frame_Ruben_Leonardo_Sigalingging=Frame(Fungsi_Utama_GUI_ChatBot,bg="#a9a9a9",bd=3,cursor="pirate",height=2)
	Frame_Ruben_Leonardo_Sigalingging.pack(expand=False,fill=X,side=TOP)
	Ruben_Leonardo_Sigalingging=Label(Frame_Ruben_Leonardo_Sigalingging,text="Ruben Leonardo Sigalingging",bg="#008b8b",fg="#f5f5f5",activebackground="#f5f5f5",activeforeground="#008b8b",font=("Ubuntu",15,"roman"))
	Ruben_Leonardo_Sigalingging.pack(expand=False,fill=X,side=TOP)


	# Hash & Cryptography Related Tools
	Hash_And_Cryptography_Related_Tools=Frame(Fungsi_Utama_GUI_ChatBot,bg="#49b675",bd=3,cursor="fleur",height=1)
	Hash_And_Cryptography_Related_Tools.pack(expand=False,fill=X,side=TOP)
	Hash_And_Cryptography_Tools=Label(Hash_And_Cryptography_Related_Tools,text="Hash & Cryptography Related Tools",font=("Ubuntu",15),bd=3,bg="#92763a",fg="#ffffff",justify="center",cursor="pirate")
	Hash_And_Cryptography_Tools.pack(expand=False,fill=X,side=TOP,padx=12,pady=12)


	# MD5 Hash Generator
	def MD5_Message_Digest_Algorithm(Created_By="Ruben Leonardo Sigalingging"):
		print("[!] MD5 Hash Tools")
	MD5_Hash_Generator=Frame(Fungsi_Utama_GUI_ChatBot,bg="#4D5157",bd=3,cursor="fleur",height=1)
	MD5_Hash_Generator.pack(expand=False,fill=X,side=TOP)
	MD5_Hash=Button(MD5_Hash_Generator,text="MD5 Hash Generator Tool",bg="#008b8b",fg="#ffffff",activebackground="#ffffff",activeforeground="#008b8b",bd=2,font=("Ubuntu",15),height=1,justify="center",width=20,command=MD5_Message_Digest_Algorithm)
	MD5_Hash.pack(expand=False,fill=X,side=LEFT)


	# FUNGSI ATAU TOMBOL HOME
	def Home(Created_By="Ruben Leonardo Sigalingging"):
		if platform=="linux" or platform=="linux2" or platform=="linux3":
			Home_Function=system("clear")
			Tulisan_Seorang_Remaja_Kesepian=Tk()
			Tulisan_Seorang_Remaja_Kesepian.title("Welcome To Home My Friend")
			Tulisan_Seorang_Remaja_Kesepian.geometry("500x250")
			Tulisan_Seorang_Remaja_Kesepian.configure(bg="black")
			Label_Tulisan_Seorang_Remaja_Kesepian=Label(Tulisan_Seorang_Remaja_Kesepian,text="Welcome To Home My Friend :)",font=("Ubuntu",15),width=25,bg="#008b8b",fg="#ffffff",justify="center")
			Label_Tulisan_Seorang_Remaja_Kesepian.pack()
			Tulisan_Seorang_Remaja_Kesepian.mainloop()
			# Home_NavBar.config(text=Tulisan_Seorang_Remaja_Kesepian)
			Home_NavBar.after(125,Home)

	Home_NavBar=Button(Navigation_Bar_Home,text="Home",cursor="pirate",activebackground="#ffffff",activeforeground="#008b8b",bg="#008b8b",fg="#ffffff",font=("Ubuntu",12),height=1,justify=CENTER,padx=12,pady=12,width=12,command=Home)
	Home_NavBar.pack(padx=33,pady=33)


	def GitHub(Created_By="Ruben Leonardo Sigalingging"):
		import webbrowser
		Buka_WebBrowser=webbrowser.open("https://github.com/RubenLeonardoSigalingging")
		# Buka_WebBrowser.after(125,GitHub)


	def Exit_Program(Created_By="Ruben Leonardo Sigalingging"):
		quit()

	GitHub_NavBar=Button(Navigation_Bar_Home,text="GitHub",bg="#008b8b",fg="#ffffff",activebackground="#ffffff",activeforeground="#008b8b",bd=2,font=("Ubuntu",12),height=1,justify="center",padx=12,pady=12,width=12,cursor="pirate",command=GitHub)
	GitHub_NavBar.pack(padx=33,pady=33)


	ChatBot_NavBar=Button(Navigation_Bar_Home,text="ChatBot",bg="#008b8b",fg="#ffffff",activebackground="#ffffff",activeforeground="#008b8b",bd=2,font=("Ubuntu",12),height=1,justify="center",padx=12,pady=12,width=12,cursor="pirate")
	ChatBot_NavBar.pack(padx=33,pady=33)


	Exit_NavBar=Button(Navigation_Bar_Home,text="Exit",bg="#008b8b",fg="#ffffff",activebackground="#ffffff",activeforeground="#008b8b",bd=2,font=("Ubuntu",12),height=1,justify="center",padx=12,pady=12,width=12,cursor="pirate",command=Exit_Program)
	Exit_NavBar.pack(padx=33,pady=33)
	# BUAT PROGRAM ATAU ALAT INI, SELALU AKTIF.
	Fungsi_Utama_GUI_ChatBot.mainloop()


if __name__ == '__main__':
	GUI_Chat_Bot()