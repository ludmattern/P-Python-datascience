from matplotlib.pyplot import (
    plot,
    title,
    xlabel,
    ylabel,
    show,
    tight_layout)
from load_csv import load


def plot_france_life_expectancy():
    """
    Function to load life expectancy data and display France's data
    """
    df = load("life_expectancy_years.csv")

    if df is None:
        raise ValueError("Failed to load the dataset")

    france_data = df[df["country"] == "France"]

    if france_data.empty:
        raise ValueError("France not found in the dataset")

    years = df.columns[1:]
    life_expectancy = france_data.iloc[0, 1:].values

    years_int = [int(year) for year in years]

    plot(years_int, life_expectancy)
    title("France Life expectancy Projections")
    xlabel("Year")
    ylabel("Life expectancy")
    tight_layout()
    show()


def main():
    """
    Main function with error handling
    """
    try:
        plot_france_life_expectancy()
    except ValueError as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
