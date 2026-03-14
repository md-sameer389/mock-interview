import subprocess
import tempfile
import os
import sys

def execute_code(code):
    """
    Executes Python code safely-ish (local environment) and returns output.
    """
    if not code:
        return {"output": "", "error": "No code provided."}

    # Create a temporary file
    fd, temp_path = tempfile.mkstemp(suffix=".py")
    
    try:
        # Write code to temp file
        with os.fdopen(fd, 'w') as temp_file:
            temp_file.write(code)
            
        # Run the code
        # render_output=True capture_output=True (for python < 3.7 use stdout=subprocess.PIPE)
        # timeout=5 seconds to prevent infinite loops
        result = subprocess.run(
            [sys.executable, temp_path], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        
        return {
            "output": result.stdout,
            "error": result.stderr
        }
        
    except subprocess.TimeoutExpired:
        return {
            "output": "",
            "error": "Execution timed out (Limit: 5 seconds)."
        }
    except Exception as e:
        return {
            "output": "",
            "error": f"System Error: {str(e)}"
        }
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)
