##################################################
## XAliases for using terminal more effectively ## 
##################################################

# System Aliases
# Aliases primarily used for system related operations.
# These operations range from basic apt update to
# default yes installation and clean up.
alias update='sudo apt-get update && sudo apt-get upgrade -y'
alias install='sudo apt-get install -y'
alias uninstall='sudo apt remove --purge -y'
alias clean='sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y'

# Python Aliases
# Aliases used when working with python and installing
# dependencies via pip.
alias py='python3'
alias pip='pip3'

# Git Aliases
# Aliases used when working with git
alias gs="git status"
alias ga="git add"
alias gA="git add -A"
alias gc="git commit -m"
alias gm="git checkout main"
alias gpull="git pull origin"
alias gpush="git push origin"
