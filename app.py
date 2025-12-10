from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from agent import run_eda_agent, generate_plots

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/plots'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'dataset' not in request.files:
        return redirect(url_for('index'))

    file = request.files['dataset']
    
    if file.filename == '':
        return redirect(url_for('index'))

    # Save uploaded file temporarily
    filepath = os.path.join('sample_data', 'uploaded.csv')
    file.save(filepath)

    # Load dataset
    df = pd.read_csv(filepath)

    # Run agent to produce text-based insights
    insights = run_eda_agent(df)

    # Generate plots (saved to static/plots)
    plot_files = generate_plots(df)

    return render_template('results.html', insights=insights, plots=plot_files)

if __name__ == '__main__':
    app.run(debug=True)
