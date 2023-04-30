# bigredbutton
"Remote" Big Red Button with ssh and textual

Executes a scrip on a remote ssh server on login.
The idea is to have a TUI app automatically pop up upon login.


# installation on remote ssh server

```
git clone this <repo>
cd <repo>
python3 -m venv venv
source venv/bin/activate
pip install textual
```

# ssh (client) config on remote ssh server

Put this in your .zshrc or .bashrc
```
if [[ -n $SSH_CONNECTION ]] ; then
    echo "I am logged in remotely"
    
    # EDIT THIS PATH TO WHERE THE REPO IS
    export BRB="$HOME/projects/bigredbutton"
    source $BRB/venv/bin/activate
    #python $BRB/brb.py
    #python $BRB/mouse.py
    #python $BRB/key3.py
    python $BRB/custom01.py

fi
```

# Linux

With linux to linux I hab no problems and it worked fine.

# Android

Under Android use "Termius" App. 
With "JuicySSH" App I had some troubles

In Termius I played a bit but it seems.
* Boutton click works
* Tab works
* Arrow keys work
* Drawback is that mouse events are sent as keys. ( test with key3.py )
