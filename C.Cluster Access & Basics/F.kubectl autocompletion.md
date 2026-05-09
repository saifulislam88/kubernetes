
```sh
sudo apt update
sudo apt install -y bash-completion
source <(kubectl completion bash)
source /usr/share/bash-completion/bash_completion
alias k=kubectl
complete -o default -F __start_kubectl k
source ~/.bashrc
```
