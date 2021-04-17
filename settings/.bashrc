# --- Personal preferences ---
# Run password-less sudo:
# sudo bash -c 'echo "$(logname) ALL=(ALL:ALL) NOPASSWD: ALL" | (EDITOR="tee -a" visudo)'

# PS1 command to add line break so that the commands are typed on a new line:
# Custom PS1:
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;92m\]\u@\h\[\033[00m\]:\[\033[01;94m\]\w\[\033[00m\]\n\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\n\$ '
fi
unset color_prompt force_color_prompt

# Setup virtual environments:
# 1. Install virtualenv package: pip3 install virtualenv virtualenvwrapper --no-warn-script-location
# 2. Create a virtualenv: mkvirtualenv <VENV NAME>
# 3. Add the below 4 lines, you might wanna change your virtualenv base directory.
#    If so, then update the first line `export WORKON_HOME=<YOUR DESIRED PATH>`
export WORKON_HOME=$HOME/workspace/environments
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
source $HOME/.local/bin/virtualenvwrapper.sh

# Setup GPG key:
export GPG_TTY=$(tty)

# XAlias definitions:
# Add this at the end of your ~/.bashrc
# APT aliases
alias update='sudo apt-get update && sudo apt-get upgrade -y'
alias install='sudo apt-get install -y'
alias uninstall='sudo apt remove --purge -y'
alias clean='sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y'

# CD navigations aliases
alias ..='cd ..'
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# Common aliases
alias cls='clear'
alias df='df -h'                                # Human readable disk spaces
alias free='free -h'                            # Free RAM in human readable format
alias freem='free -m'                           # Free RAM in MB
alias freeg='free -g'                           # Free RAM in GB
alias ls='ls -lAhSpg --color=auto'              # ls -l -A (skip ./ and ../) -h (human readable sizes) -S (sort by file size) -p (add dir indicator) -g (hide owner)

# Directory navigations aliases - To be updated
alias home='cd $HOME/'
alias repo='cd ~/workshop/repositories/'

# Git aliases
alias add='git add'
alias adda='git add -A'
alias branch='git branch'
alias checkout='git checkout'
alias clone='git clone'
alias commit='git commit -m'
alias fetch='git fetch'
alias pull='git pull origin'
alias push='git push origin'
alias stat='git status'                         # 'status' is a protected name so using 'stat' instead

# Other aliases
alias brc='cat ~/.bashrc'
alias mkdir='mkdir -pv'

# Python aliases
alias py='python3'
alias pip='python3 -m pip'
alias venv='mkvirtualenv'
