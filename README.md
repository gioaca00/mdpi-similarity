# Setup instructions
## Clone the repository
```bash
git clone https://github.com/gioaca00/mdpi-similarity
cd mdpi-similarity
```

## Create a conda environment
If you don't have conda installed, check how to get started with miniconda [here](https://docs.anaconda.com/miniconda/). You can create your environment also with venv if you prefer.

Create and activate your conda environment like this:
```bash
conda create -n mdpi-similarity python=3.11 -y
conda activate mdpi-similarity
```

## Install the dependencies using poetry
If you aren't familiar with poetry, you can check the documentation [here](https://python-poetry.org/docs/).

Install the dependencies with poetry:
```bash
pip install poetry
poetry install
```

# Running the app
To run the app, you can use the following command in your activated conda environment:
```bash
uvicorn main:app
```

With the app running, on a different terminal, you can test the app with the following command:
### Mac/Linux
```bash
curl -X POST "http://127.0.0.1:8000/similarity" -H "Content-Type: application/json" -d '{
    "reference": "Higgs boson in particle physics",
    "other": ["Best soup recipes", "Basel activities", "Particle physics at CERN"]
}'
```

### Windows
```powershell
$headers = @{
    "Content-Type" = "application/json"
}
$body = @{
    "reference" = "Higgs boson in particle physics"
    "other" = @("Best soup recipes", "Basel activities", "Particle physics at CERN")
} | ConvertTo-Json -Depth 10

Invoke-WebRequest -Uri "http://127.0.0.1:8000/similarity" -Method POST -Headers $headers -Body $body
```

The app should return a JSON response with the most similar title to the reference title.