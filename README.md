# Task_07_Decision_Making
This project is a continuation of my earlier WNBA data analysis work. I turned the LLM-produced narrative into a stakeholder-facing decision report, focusing on ethics, uncertainty, fairness, and robustness checks.  

## Overview
The goal is to take sports data insights and show how they can be used in real decisions (like coaching or management), while also pointing out the risks, bias, and limits of relying on AI outputs.  

## Files in this repo
- `stakeholder_report.md` → the main report written for stakeholders (coach/AD)  
- `analyse_data.py` → script to recreate basic stats and correlation plots  
- `correlation_plot.png` → correlation chart for win% and other stats  
- `bias_analysis.txt` → notes on fairness, bias, and ethics  
- `prompts.txt` → all prompts I used with the LLM  
- `llm_raw_outputs.txt` → raw model outputs before edits  
- `process_notes.md` → record of my workflow, attempts, and decisions  


## How to run
1. Make sure to update the CSV path in `analyse_data.py`.  
2. Install needed packages:
   ```bash
   pip install pandas numpy matplotlib
3. Run the analysis script: python analyse_data.py
