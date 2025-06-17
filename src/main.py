from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator

def main():

    file_path = r"C:\Users\FIEK X\Documents\GitHub\water_quality_monitoring\data\sensor_data.csv"

    # 1. Loading CSV
    df = load_csv(file_path)
    print("Data loaded successfully.")

    # 2. Clean the data
    cleaned_df = clean_sensor_data(df)
    print("Data cleaned.")

    # 3. Evaluate water quality
    evaluator = WaterQualityEvaluator(cleaned_df)
    evaluated_df = evaluator.is_safe()
    print("Evaluation complete.")

    # 4. Display results
    print(evaluated_df)

if __name__ == "__main__":
    main()
