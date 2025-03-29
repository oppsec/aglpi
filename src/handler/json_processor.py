from rich.console import Console
console = Console()

def format_value(value):
    """ Pretty print the keys and their values to better reading """

    if isinstance(value, list):
        return '\n'.join([f"- {plugin}" if isinstance(plugin, str) else f"- {plugin['key']}: {plugin['version']}" for plugin in value])
    elif isinstance(value, dict):
        return '\n' + '\n'.join([f"  {k}: {v}" for k, v in value.items()])
    else:
        return f"\n  {value}"

def format_keys(content) -> None:
    """ Get the keys from parsed JSON and call format_value function to pretty print """

    for key, value in content.items():
        formatted_value = format_value(value)
        console.print(f"[green]{key}[/]:{formatted_value}", highlight=False)