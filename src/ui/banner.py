from rich.console import Console
console = Console()

def get_banner() -> None:
    """ Return aGLPI's banner """

    ascii_art = """
       _______   ___  ____
 ___ _/ ___/ /  / _ \/  _/
/ _ `/ (_ / /__/ ___// /   - against GLPI, by opps3c
\_,_/\___/____/_/  /___/     v1.0.0        
"""

    console.print(f"[light_green]{ascii_art}[/]")