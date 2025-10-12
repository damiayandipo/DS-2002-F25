import sys
from update_portfolio import main as update_main
from generate_summary import main as summary_main

def run_production_pipeline():
    print("Starting production pipeline...", file=sys.stderr)
    print("Updating portfolio...", file=sys.stderr)
    update_main()
    print("Generating summary...", file=sys.stderr)
    summary_main()
    print("Pipeline complete!", file=sys.stderr)

if __name__ == "__main__":
    run_production_pipeline()