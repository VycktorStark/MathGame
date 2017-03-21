#!/usr/bin/env bash
xtitle PROJECTS STARK
clear
sessoes(){
  clear
  printf "\n\033[01;36m"
  figlet Robo DB
	echo -e "\033[01;37m############# \033[01;32mSessões\033[01;37m #############"
	echo -e "#  \033[01;31m1\033[01;37m - Criar sessão.              #"
	echo -e "#  \033[01;31m2\033[01;37m - Conectar sessão.           #"
	echo -e "#  \033[01;31m3\033[01;37m - Ver sessões ativas.        #"
	echo -e "#  \033[01;31m4\033[01;37m - Encerrar sessões ativas.   #"
	echo -e "#  \033[01;31m5\033[01;37m - Manual TMUX.               #"
	echo -e "#  \033[01;31m0\033[01;37m - Voltar.                    #"
	echo -e "###################################"
	echo -n "Digite o número da opção > "
	read VAR

	if [ "$VAR" = 1 ]; then
		clear;tmux new -s Workspace -n DbRobot;read -n1 -r -p 'Pressione uma tecla para voltar.';sessoes
	elif [ "$VAR" = 2 ]; then
		clear;tmux attach-session -t Workspace;sessoes
	elif [ "$VAR" = 3 ]; then
		clear;tmux ls;read -n1 -r -p 'Pressione uma tecla para voltar.';sessoes
	elif [ "$VAR" = 4 ]; then
    clear;killall tmux;read -n1 -r -p 'Pressione uma tecla para voltar.';sessoes
  elif [ "$VAR" = 5 ]; then
		clear;echo -e '\033[01;05m\033[01;36m';figlet Manual TMUX
		echo -e '
\033[01;31mPrefix = ctrl + b\033[01;37m\n\n
\033[01;31mtmux new-session -d -s \033[01;34m$NAME\033[01;37m - Criar uma session.
\033[01;31mtmux attach-session -t \033[01;34m$NAME\033[01;37m - Entre em uma session.
\033[01;31mPrefix + \033[01;34m(\033[01;37m or \033[01;34m)\033[01;37m - Troca de janela.
\033[01;31mPrefix + numero\033[01;37m - Abre janela com o numero número.
\033[01;31mPrefix + c\033[01;34m - Criar uma janela.
\033[01;31mPrefix + %\033[01;37m - Criar um painel vertial.
\033[01;31mPrefix + \033[01;34m{\033[01;37m or \033[01;34m}\033[01;37m - Troca de painel.
\033[01;31mPrefix + !\033[01;37m - Criar janela do painel e fecha o painel.
\033[01;31mPrefix + x\033[01;37m - Fecha painel.
\033[01;31mPrefix + :\033[01;37m - Command Mode.
\033[01;31mPrefix + d\033[01;37m - Sair.
		';read -n1 -r -p 'Pressione uma tecla para voltar.';sessoes
	elif [ "$VAR" = 0 ]; then
		OPC
	else
		sessoes
		sleep 2
	fi
}

OPC=0
while [ $OPC -ne 5 ];do
	clear
	printf "\033[01;36m\n"
	figlet Robo DB
        printf "\n\033[01;37m############ \033[01;32mMENU\033[01;37m ############"
	printf "\n# \033[01;31m1\033[01;37m - Iniciar.               #"
	printf "\n# \033[01;31m2\033[01;37m - Sessões.               #"
	printf "\n# \033[01;31m3\033[01;37m - Sincronizar.           #"
	printf "\n# \033[01;31m4\033[01;37m - Instalar libs.         #"
	printf "\n# \033[01;31m0\033[01;37m - Sair.                  #"
	printf "\n##############################\n"
	echo -n "Digite o número da opção > "
	read OPC
	case $OPC in
		1) clear;python3 main.py "${@}";;
    2) sessoes;;
    3) clear;git pull;read -n1 -r -p 'Pressione uma tecla para voltar.';;
		4) clear;sudo pip3 install -r requirements.txt;read -n1 -r -p 'Pressione uma tecla para voltar.';;
		0) break;;
		*) printf "\n\033[01;31mOpção Inválida\033[0m";;
	esac
done
