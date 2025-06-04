from matplotlib.pyplot import (
    scatter,
    title,
    xlabel,
    ylabel,
    show,
    gca,
    xscale,
    tight_layout)
from matplotlib.ticker import FuncFormatter
from load_csv import load


def plot_life_expectancy_vs_gdp(date="1800"):
    """
    Function to display life expectancy vs GDP per capita for the given year
    """
    life_df = load("life_expectancy_years.csv")
    income_df = load("income_per_person_gdppercapita_"
                     "ppp_inflation_adjusted.csv")

    if life_df is None:
        raise ValueError("Failed to load life expectancy dataset")

    if income_df is None:
        raise ValueError("Failed to load income dataset")

    if date not in life_df.columns:
        raise ValueError(f"Year {date} not found in life expectancy dataset")

    if date not in income_df.columns:
        raise ValueError(f"Year {date} not found in income dataset")

    life = life_df[["country", date]].copy()
    income = income_df[["country", date]].copy()

    life.columns = ["country", "life_expectancy"]
    income.columns = ["country", "gdp_per_capita"]

    merged_data = life.merge(income, on="country", how="inner")

    merged_data = merged_data.dropna()

    merged_data["life_expectancy"] = \
        convert_to_numeric(merged_data["life_expectancy"])
    merged_data["gdp_per_capita"] = \
        convert_to_numeric(merged_data["gdp_per_capita"])

    merged_data = merged_data.dropna()

    if merged_data.empty:
        raise ValueError(f"No valid data found for year {date}")

    scatter(merged_data["gdp_per_capita"], merged_data["life_expectancy"])

    title(date)
    xlabel("Gross domestic product")
    ylabel("Life Expectancy")
    xscale("log")

    gca().xaxis.set_major_formatter(FuncFormatter(
        lambda x, pos: f"{x / 1000000000:.1f}B" if x >= 1000000000
        else f"{x / 1000000:.1f}M" if x >= 1000000
        else f"{x / 1000:.0f}k" if x >= 1000
        else f"{x:.0f}"
    ))

    tight_layout()
    show()


def convert_to_numeric(series):
    """
    Convert a pandas series to numeric values, handling string formats

    Args:
        series: Pandas series with potential string values

    Returns:
        Pandas series with numeric values
    """
    result = []
    for value in series:
        if isinstance(value, str):
            try:
                if value.endswith("k"):
                    result.append(float(value[:-1]) * 1000)
                elif value.endswith("M"):
                    result.append(float(value[:-1]) * 1000000)
                elif value.endswith("B"):
                    result.append(float(value[:-1]) * 1000000000)
                else:
                    result.append(float(value))
            except ValueError:
                result.append(None)
        else:
            try:
                result.append(float(value))
            except (ValueError, TypeError):
                result.append(None)
    return result


def main():
    """
    Main function with error handling
    """
    try:
        plot_life_expectancy_vs_gdp()
    except ValueError as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
