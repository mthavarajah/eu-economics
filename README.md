# EU-Economics

EU-Economics is a web application that visualizes European economic indicators over time. The project leverages interactive graphs and a user-friendly interface to present both financial and macroeconomic data. The application is built using Python for data processing and Plotly for interactive visualizations. It is hosted on Render, providing a seamless experience for users to explore various economic indicators.

## Features

- **Financial Economics Data**: Interactive visualizations of financial indicators including reserve assets, direct investments, portfolio investment balance, real exchange rate, nominal exchange rate, and current account.
- **Macroeconomics Data**: Interactive visualizations for macroeconomic indicators such as inflation, government debt, unemployment, and real GDP.
- **Interactive Graphs**: Graphs are generated using Plotly, offering dynamic interaction with the data.
- **Data Download**: Users can download CSV files of the displayed data for offline analysis.
- **Information Links**: External links are provided for more information on each economic indicator.

## Technology Stack

- **Backend**: Python (Pandas for data manipulation, Plotly for graph generation)
- **Frontend**: HTML, CSS, JavaScript
- **Web Hosting**: Render

## Installation

To set up the EU-Economics project locally, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/mthavarajah/eu-economics.git
    cd eu-economics
    ```

2. **Install Dependencies**

    Ensure Python is installed, then create a virtual environment and install the required packages:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install pandas plotly
    ```

3. **Prepare Data**

    Place your data files (e.g., `current_account.csv`) in the `datafiles/external/` directory. Adjust file paths in Python scripts as needed.

4. **Generate Graphs**

    Run the Python scripts to generate HTML files for each graph. For example:

    ```bash
    python current_account.py
    ```

    This will generate an HTML file (`current_account.html`) which is inline framed into `financial-economics.html` for display.

6. **View Graphs**

    Open the generated HTML files in your web browser to view the interactive graphs.

7. **Open a Pull Request**

## Contact

For any inquiries or issues, please reach out to [Mathu Thavarajah](mthavarajah10@gmail.com).

---

**Ethernance** | Explore transactions and balances for Ethereum and Binance wallet addresses.
