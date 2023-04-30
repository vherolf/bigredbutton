# bigredbutton

"Remote" Big Red Button with ssh and textual

Executes a script on a remote ssh server at login.
The idea is to have a TUI app automatically pop up at the login.


# Installation on remote ssh server

You can use any textual app.  
I put this here up for testing only.  

```
git clone this <repo>
cd bigredbutton
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
    
    python $BRB/bigredbutton.py
    # for testing comment the above and use one of these
    #python $BRB/key3.py
    #python $BRB/custom01.py
fi
```

# From Linux

With linux to linux I hab no problems and everything worked fine.

# From Android

With "JuicySSH" App I had some troubles and quited testing.  


With the "Termius" App
* Button click works
* Tab works
* Arrow keys work
* Drawback is that mouse events are sent as arrow keys. ( test with key3.py )
