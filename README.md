# End-to-End MLOps Platform

A production-grade MLOps platform demonstrating the full machine learning lifecycle:
data ingestion, validation, training, deployment, monitoring, and automated retraining.

## Features
- Data ingestion with raw/processed separation
- Automated data validation using Great Expectations
- Pytest-based data quality tests
- Modular, scalable project structure

## Project Structure
## 📊 Data Handling & Storage Strategy

This repository intentionally does **not** include the raw or processed dataset.

### Why the data is not in GitHub
- The original dataset exceeds GitHub’s recommended file size limits.
- In real-world MLOps systems, raw datasets are **not stored in Git repositories**.
- Storing large or sensitive datasets in Git can cause versioning, security, and compliance issues.

### How data is handled instead
- GitHub is used only for:
  - source code
  - configuration files
  - tests
  - pipeline logic
- Datasets are expected to be stored externally (e.g., cloud storage, databases, or DVC-managed remotes).
- Small sample data may be added later **only for demonstration and testing purposes**.

> This approach aligns with industry best practices for production-grade MLOps pipelines.
