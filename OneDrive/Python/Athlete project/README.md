# Shot Put Analytics - Streamlit Application

A comprehensive analytics dashboard for shot put performance tracking, statistics, and predictions.

## Features

- **Overview**: View and edit athlete performance data
- **Statistics**: Analyze key metrics (best throw, improvement, consistency, etc.)
- **Visualizations**: Interactive charts and graphs for performance tracking
- **Predictions**: ML-based predictions for future performance

## Local Setup

### Prerequisites
- Python 3.9 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Athlete project"
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app locally**
   ```bash
   streamlit run app.py
   ```
   
   The app will open at `http://localhost:8501`

## CI/CD Pipeline

This project uses GitHub Actions for automated testing and deployment.

### Workflows

#### 1. **CI - Code Quality & Testing** (`ci.yml`)
- **Trigger**: Push to `main`/`develop` or Pull Requests
- **Actions**:
  - Tests on Python 3.9, 3.10, and 3.11
  - Code formatting check (Black)
  - Linting (Flake8, Pylint)
  - Import validation

#### 2. **Streamlit App Validation** (`streamlit-validation.yml`)
- **Trigger**: Push to `main`/`develop` or Pull Requests
- **Actions**:
  - Validates Streamlit app syntax
  - Python syntax compilation check

#### 3. **Deploy to Streamlit Cloud** (`deploy.yml`)
- **Trigger**: Push to `main` branch only
- **Actions**:
  - Runs on successful CI checks
  - Deploys to Streamlit Cloud (if configured)

### Setting Up Automated Deployment

#### Option 1: Streamlit Cloud (Recommended for simplicity)

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Connect your GitHub repository
4. Select:
   - Repository: Your repo
   - Branch: `main`
   - Main file path: `app.py`
5. Click "Deploy"

Streamlit Cloud will automatically redeploy whenever you push to the `main` branch.

#### Option 2: GitHub Pages or Custom Server

For more advanced deployment options, modify `.github/workflows/deploy.yml` to deploy to:
- GitHub Pages
- AWS Lambda
- Heroku
- DigitalOcean
- Custom VPS

## Project Structure

```
Athlete project/
├── app.py                      # Main Streamlit application
├── shotput_Statistics.py       # Statistics and prediction functions
├── shotput_data.xlsx          # Excel data file
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore patterns
└── .github/
    └── workflows/
        ├── ci.yml                        # CI pipeline
        ├── streamlit-validation.yml      # Streamlit validation
        └── deploy.yml                    # Deployment pipeline
```

## Data Format

The `shotput_data.xlsx` file should contain the following columns:
- `best throw`
- `2nd best throw`
- `3rd best throw`
- `4th best throw`
- `5th best throw`
- `squat` (for strength index)
- `deadlift` (for strength index)
- `bench` (for strength index)
- `bodyweight`
- `technique` (numeric score)
- `style` (spin/glide/standing)
- `number of throws in past 3 days`
- `number of gym sessions in past 3 days`
- `number of rest days since`

## Development

### Making Changes

1. Create a feature branch
   ```bash
   git checkout -b feature/my-feature
   ```

2. Make your changes and test locally
   ```bash
   streamlit run app.py
   ```

3. Commit and push
   ```bash
   git add .
   git commit -m "Add my feature"
   git push origin feature/my-feature
   ```

4. Open a Pull Request on GitHub
   - CI checks will run automatically
   - Review and merge once checks pass

5. After merging to `main`
   - CI/Streamlit validation runs
   - App automatically deploys to Streamlit Cloud (if configured)

### Code Quality

Before committing, you can run local checks:

```bash
# Format code with Black
black app.py shotput_Statistics.py

# Lint with Flake8
flake8 app.py shotput_Statistics.py

# Lint with Pylint
pylint app.py shotput_Statistics.py
```

## Troubleshooting

### Import errors when running app
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Excel file not found
Make sure `shotput_data.xlsx` is in the same directory as `app.py`

### Streamlit port already in use
```bash
streamlit run app.py --server.port 8502
```

## Dependencies

- **pandas** - Data manipulation and analysis
- **streamlit** - Web application framework
- **matplotlib** - Plotting and visualization
- **openpyxl** - Excel file handling

