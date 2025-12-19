import subprocess

def run_command(command):
    """
    Executes a shell command and returns the output.
    """
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            text=True, 
            capture_output=True
        )
        
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, result.stderr.strip()
            
    except Exception as e:
        return False, str(e)

def is_dangerous(command):
    """
    Basic safety filter. Returns True if the command looks risky.
    """
    # simple blocklist
    banned_keywords = [
        "rm ",      
        "rm -rf",    
        "sudo",      
        "mv",       
        "mkfs",    
        ":(){ :|:& };:"
    ]
    
    for ban in banned_keywords:
        if ban in command:
            return True
    return False