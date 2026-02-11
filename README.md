# gitwho

Analyze git repos for code ownership, bus factor, and knowledge silos.

## Install from source

```bash
git clone https://github.com/openkickstartai/gitwho.git
cd gitwho
pip install -e .
```

## Usage

```bash
gitwho analyze .          # ownership report
gitwho report --bus-factor # bus factor analysis
gitwho heatmap --output ownership.html
```

## Testing

```bash
pytest -v
```
