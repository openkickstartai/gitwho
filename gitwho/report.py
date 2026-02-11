"""Report formatting."""
from rich.console import Console
from rich.table import Table
console = Console()

def print_report(data):
    t = Table(title="Code Ownership")
    t.add_column("Author", style="cyan")
    t.add_column("Files", justify="right")
    t.add_column("Lines", justify="right")
    t.add_column("Sole Owner", justify="right", style="red")
    for a, s in sorted(data["authors"].items(), key=lambda x: -x[1]["lines"]):
        t.add_row(a, str(s["files"]), str(s["lines"]), str(s["sole_owner"]))
    console.print(t)

def print_bus_factor(data):
    sole = sum(1 for c in data["files"].values() if len(c)==1)
    total = data["total_files"]
    console.print(f"Bus Factor: {len(data['authors'])}")
    console.print(f"Sole-owned: {sole}/{total} ({sole*100//max(total,1)}%)")
    if sole > total*0.5: console.print("[red]Warning: >50% sole-owned[/red]")
