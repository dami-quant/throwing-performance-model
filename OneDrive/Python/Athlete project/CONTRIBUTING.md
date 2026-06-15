# Contributing Guide

Thank you for contributing to the Shot Put Analytics project!

## Workflow

### 1. Before You Start
- Ensure you have the latest changes from main
- Create a new branch for your feature/fix

```bash
git fetch origin
git checkout -b feature/your-feature-name
```

### 2. Development
- Install dependencies: `pip install -r requirements.txt`
- Test your changes locally: `streamlit run app.py`
- Follow Python best practices

### 3. Pre-Commit Checks
Run these before committing:

```bash
# Format your code
pip install black flake8 pylint
black app.py shotput_Statistics.py

# Lint
flake8 app.py shotput_Statistics.py
pylint app.py shotput_Statistics.py
```

### 4. Commit & Push
```bash
git add .
git commit -m "Clear description of changes"
git push origin feature/your-feature-name
```

### 5. Create a Pull Request
- Go to GitHub and create a PR against `main`
- Describe your changes
- Wait for CI checks to pass
- Request a review if needed

### 6. CI/CD Checks
GitHub Actions will automatically:
- ✓ Run linting (Flake8, Pylint, Black)
- ✓ Validate Streamlit app syntax
- ✓ Test on Python 3.9, 3.10, 3.11
- ✓ Check imports

All checks must pass before merging.

## Code Style

- Follow PEP 8 standards
- Use descriptive variable and function names
- Add docstrings to functions
- Keep lines under 120 characters

Example:
```python
def calculate_average_throw(df):
    """
    Calculate the average of best throws.
    
    Args:
        df (pd.DataFrame): DataFrame with throw columns
        
    Returns:
        float: Average throw distance
    """
    throw_cols = ["best throw", "2nd best throw", "3rd best throw"]
    return df[throw_cols].mean().mean()
```

## Testing

If you add new functionality, please add validation:

```python
# Test your function locally before committing
import pandas as pd
from shotput_Statistics import your_new_function

df = pd.read_excel("shotput_data.xlsx")
result = your_new_function(df)
print(f"Result: {result}")
```

## Reporting Issues

Found a bug? Create a GitHub Issue with:
- Clear description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python version and OS

## Questions?

- Check the README.md
- Look at existing issues/PRs
- Comment on the related issue/PR

Happy coding! 🚀
