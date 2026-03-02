#!/usr/bin/env python3
import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

# Import our modules
from brain import get_brain_command
from executor import run_command, is_dangerous

console = Console()

def main():
    console.clear()
    console.print(Panel.fit("[bold cyan]MindShell OS v0.2 (Active Mode)[/bold cyan]", border_style="cyan"))
    
    while True:
        current_dir = os.getcwd()
        
        try:
            user_input = Prompt.ask(f"\n[bold blue]USER ({current_dir})[/]")
        except KeyboardInterrupt:
            break

        if user_input.lower() in ["exit", "quit"]:
            break
        if not user_input.strip():
            continue

        with console.status("[bold magenta]Thinking...[/]", spinner="aesthetic"):
            command = get_brain_command(user_input, current_dir)

        console.print(f"[dim]AI suggests:[/dim] [bold yellow]{command}[/bold yellow]")

        if is_dangerous(command):
            console.print(Panel("[bold red]SAFETY ALERT:[/bold red] This command contains banned keywords.", border_style="red"))
            console.print("[red]Execution Blocked.[/red]")
            continue

        should_run = Confirm.ask("[bold cyan]Execute this command?[/]")

        if should_run:
            # Handle cd separately — subprocess can't change the parent process directory
            if command.strip().startswith("cd "):
                target = command.strip()[3:].strip()
                try:
                    os.chdir(os.path.expanduser(target))
                    console.print(f"[green]Now in:[/green] {os.getcwd()}")
                except FileNotFoundError:
                    console.print(f"[red]Directory not found:[/red] {target}")
                except Exception as e:
                    console.print(f"[red]Error:[/red] {e}")
            else:
                with console.status("[bold green]Running...[/]", spinner="dots"):
                    success, output = run_command(command)

                if success:
                    if output:
                        console.print(Panel(output, title="[green]Success[/]", border_style="green"))
                    else:
                        console.print("[green]Done (No Output).[/green]")
                else:
                    console.print(Panel(output, title="[bold red]Error[/]", border_style="red"))
        else:
            console.print("[dim]Command cancelled.[/dim]")

if __name__ == "__main__":
    main()