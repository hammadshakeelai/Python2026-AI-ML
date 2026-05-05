"""
Script to download Student Performance dataset from Kaggle
Ensure you have kaggle API credentials configured at ~/.kaggle/kaggle.json
"""

import os
import zipfile
import sys
from pathlib import Path

def setup_kaggle_api():
    """Check if Kaggle API is configured"""
    kaggle_dir = Path.home() / '.kaggle'
    kaggle_json = kaggle_dir / 'kaggle.json'

    if not kaggle_json.exists():
        print("❌ Kaggle API credentials not found!")
        print(f"Please create {kaggle_json} with your Kaggle API credentials")
        print("\nSteps:")
        print("1. Go to https://www.kaggle.com/account")
        print("2. Scroll to 'API' section and click 'Create New API Token'")
        print("3. This will download kaggle.json")
        print(f"4. Move it to {kaggle_dir}")
        print("5. Run: chmod 600 ~/.kaggle/kaggle.json")
        return False
    return True

def download_dataset():
    """Download Student Performance dataset from Kaggle"""
    dataset_name = "nikhil7280/student-performance-multiple-linear-regression"
    output_file = "Student_Performance.csv"

    # Check if already downloaded
    if os.path.exists(output_file):
        print(f"✓ Dataset already exists: {output_file}")
        return True

    try:
        print(f"Downloading dataset: {dataset_name}")
        print("This may take a moment...")

        # Download using kaggle CLI
        exit_code = os.system(f'kaggle datasets download -d {dataset_name}')

        if exit_code != 0:
            print(f"❌ Error downloading dataset (exit code: {exit_code})")
            return False

        # Find and extract zip file
        zip_files = [f for f in os.listdir('.') if f.endswith('.zip') and 'student' in f.lower()]

        if not zip_files:
            print("❌ Downloaded zip file not found")
            return False

        zip_file = zip_files[0]
        print(f"Extracting {zip_file}...")

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall('.')

        # Clean up zip file
        os.remove(zip_file)

        # Verify CSV exists
        if os.path.exists(output_file):
            print(f"✓ Successfully downloaded: {output_file}")

            # Show dataset info
            import pandas as pd
            df = pd.read_csv(output_file)
            print(f"\nDataset Info:")
            print(f"  Shape: {df.shape}")
            print(f"  Features: {list(df.columns)}")
            return True
        else:
            print(f"❌ CSV file not found after extraction")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main function"""
    print("Student Performance Dataset Downloader")
    print("=" * 50)

    # Check Kaggle API setup
    if not setup_kaggle_api():
        sys.exit(1)

    # Download dataset
    if download_dataset():
        print("\n✓ Ready to use in test.ipynb!")
    else:
        print("\n❌ Download failed")
        print("\nAlternative: Manual Download")
        print("-" * 50)
        print("1. Visit: https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression")
        print("2. Download the CSV file")
        print("3. Place it in the current directory as 'Student_Performance.csv'")
        sys.exit(1)

if __name__ == "__main__":
    main()
