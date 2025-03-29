import argparse

from ui.banner import get_banner
from core import get_cookie

from rich.console import Console
console = Console()

def menu() -> None:

    get_banner()

    parser = argparse.ArgumentParser(prog='aGLPI', description='against GLPI')
    parser.add_argument('-u', '--url', required=True, help="Specify the URL to be used as target")
    args = parser.parse_args()

    target = args.url
    
    get_cookie(target)