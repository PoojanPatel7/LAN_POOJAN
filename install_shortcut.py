"""
Creates a Windows Start Menu shortcut for LAN File Sharer.
Run this once: python install_shortcut.py
After this, search "LAN File Sharer" in Windows Start Menu.
"""
import os
import sys

def create_shortcut():
    try:
        import winshell
        from win32com.client import Dispatch
    except ImportError:
        # Fallback: use PowerShell to create the shortcut
        create_shortcut_powershell()
        return

    start_menu = winshell.start_menu()
    shortcut_path = os.path.join(start_menu, "Programs", "LAN File Sharer.lnk")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target = sys.executable
    arguments = f'"{os.path.join(script_dir, "local_lan.py")}"'
    icon = os.path.join(script_dir, "lan.ico")
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.Arguments = arguments
    shortcut.WorkingDirectory = script_dir
    shortcut.IconLocation = icon
    shortcut.Description = "LAN File Sharer - Premium Edition"
    shortcut.save()
    print(f"[OK] Shortcut created: {shortcut_path}")
    print("   You can now search 'LAN File Sharer' in Windows Start Menu!")


def create_shortcut_powershell():
    """Fallback method using PowerShell — no extra dependencies needed."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    python_exe = sys.executable
    script_path = os.path.join(script_dir, "local_lan.py")
    icon_path = os.path.join(script_dir, "lan.ico")
    
    # Start Menu Programs folder
    start_menu = os.path.join(os.environ.get("APPDATA", ""), "Microsoft", "Windows", "Start Menu", "Programs")
    shortcut_path = os.path.join(start_menu, "LAN File Sharer.lnk")
    
    # Also create a Desktop shortcut
    desktop = os.path.join(os.environ.get("USERPROFILE", ""), "Desktop")
    desktop_shortcut = os.path.join(desktop, "LAN File Sharer.lnk")
    
    ps_script = f'''
$WshShell = New-Object -ComObject WScript.Shell

# Start Menu shortcut
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "{python_exe}"
$Shortcut.Arguments = '"{script_path}"'
$Shortcut.WorkingDirectory = "{script_dir}"
$Shortcut.IconLocation = "{icon_path}"
$Shortcut.Description = "LAN File Sharer - Premium Edition"
$Shortcut.Save()

# Desktop shortcut
$Shortcut2 = $WshShell.CreateShortcut("{desktop_shortcut}")
$Shortcut2.TargetPath = "{python_exe}"
$Shortcut2.Arguments = '"{script_path}"'
$Shortcut2.WorkingDirectory = "{script_dir}"
$Shortcut2.IconLocation = "{icon_path}"
$Shortcut2.Description = "LAN File Sharer - Premium Edition"
$Shortcut2.Save()
'''
    
    # Write temp PS1 script and execute
    temp_ps = os.path.join(script_dir, "_create_shortcut.ps1")
    with open(temp_ps, 'w') as f:
        f.write(ps_script)
    
    import subprocess
    result = subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "-File", temp_ps],
        capture_output=True, text=True
    )
    
    # Cleanup
    if os.path.exists(temp_ps):
        os.remove(temp_ps)
    
    if result.returncode == 0:
        print(f"[OK] Start Menu shortcut created: {shortcut_path}")
        print(f"[OK] Desktop shortcut created: {desktop_shortcut}")
        print("\n   You can now search 'LAN File Sharer' in Windows Start Menu!")
    else:
        print(f"[ERROR] {result.stderr}")


if __name__ == "__main__":
    create_shortcut()
