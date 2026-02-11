"""CLI entry point."""
import click
from gitwho.analyzer import analyze_repo
from gitwho.report import print_report, print_bus_factor

@click.group()
def main():
    """Analyze git code ownership."""
    pass

@main.command()
@click.argument("path", default=".")
@click.option("--depth", default=None, type=int)
def analyze(path, depth):
    """Analyze a git repository."""
    data = analyze_repo(path, max_depth=depth)
    print_report(data)

@main.command()
@click.argument("path", default=".")
def report(path):
    """Show bus factor report."""
    data = analyze_repo(path)
    print_bus_factor(data)
