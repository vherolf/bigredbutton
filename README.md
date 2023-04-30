# bigredbutton

"Remote" Big Red Button with ssh and textual

Executes a script on a remote ssh server at login.  
The idea is to have a TUI app automatically pop up at the login.


# Installation on remote ssh server

You can use any textual app.  
I put this here up for testing only.  

```
git clone <this repo>
cd bigredbutton
python3 -m venv venv
source venv/bin/activate
pip install textual
```

# ssh user config on remote ssh server

In your home directory put this in your .zshrc or .bashrc

```
if [[ -n $SSH_CONNECTION ]] ; then
    echo "I am logged in remotely"
    
    # EDIT THIS PATH TO WHERE THE REPO IS
    export BIGREDBUTTON="$HOME/projects/bigredbutton"
    source $BIGREDBUTTON/venv/bin/activate
    
    python $BIGREDBUTTON/bigredbutton.py
    # for testing comment the above and use one of these
    #python $BIGREDBUTTON/key3.py
    #python $BIGREDBUTTON/custom01.py
fi
```

# Testing from Linux

With linux to linux I hab no problems and everything worked fine.

# Testing from Android

**DISCALIMER - Android Terminals are made for easy to use on touchscreens and are not real terminals and not all events are given through properly.**

**These ARE NOT python/textual issues**

## Termius

With the **Termius** App
- [x] Button click works
- [x] Tab works
- [x] Arrow keys work
- [x] TextLog works
- [ ] Input not tested
- [ ] Mouse events are sent as arrow keys. ( test with key3.py )

## JuicySSH

With **JuicySSH** App I had some troubles and quited testing, but simple button clicks seems to work.
