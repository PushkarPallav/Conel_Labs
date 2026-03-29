from ingest import load_data, preprocess
from detect import detect_anomalies
from utils import save_csv

def main():
    print(" Loading data...")
    df = load_data("../data/clouddocs_logs.jsonl")

    print(" Preprocessing...")
    df = preprocess(df)

    print("Detecting anomalies...")
    anomalies = detect_anomalies(df)

    print("Saving output...")
    save_csv(anomalies, "../output/suspicious_activity.csv")

    print("Done!")

if __name__ == "__main__":
    main()