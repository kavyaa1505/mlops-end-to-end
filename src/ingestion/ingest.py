from pathlib import Path
import pandas as pd

def run_ingestion():
    df = pd.DataFrame({
        "Amount": [100.5, 250.0, 75.25],
        "Class": [0, 1, 0]
    })

    BASE_DIR = Path(__file__).resolve().parents[2]
    output_path = BASE_DIR / "data" / "processed" / "data.csv"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    run_ingestion()
