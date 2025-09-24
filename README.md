This Streamlit app predicts **drinking water quality compliance** from lab parameters (pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, turbidity).
## Machine Learning
- **Algorithm:** Random Forest Classifier
- **Explainability:** SHAP feature importance plots
- **Outputs:** Accuracy, Precision, Recall, F1, ROC AUC
- **Reports:** Auto-generated PDF and PPTX summaries

## Features
- Upload lab CSVs or use the demo dataset
- Train/retrain model interactively
- Batch score new water quality samples
- Ops agent log for flagging risks
- Multi-tenant (workspaces), role-based login

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py# phila-water-quality-streamlit-app
This Streamlit app predicts drinking water quality compliance from lab parameters
