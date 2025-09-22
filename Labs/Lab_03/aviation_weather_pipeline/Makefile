.PHONY: all fetch analyze clean

all: analyze

fetch:
	@echo "Starting data fetch..."
	./fetch_metars.sh
	@echo "Data fetch complete. Files saved in raw_metars/"

analyze: fetch
	@echo "Starting data analysis..."
	./analyze_data.sh
	@echo "Analysis complete. CSV file created: weather_report.csv"
	@echo "Pipeline completed successfully!"

clean:
	@echo "Cleaning up generated files..."
	rm -rf weather_report.csv raw_metars/
	@echo "Cleanup complete."
