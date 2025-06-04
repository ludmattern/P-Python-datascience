from matplotlib.pyplot import (
    plot,
    title,
    xlabel,
    ylabel,
    legend,
    show,
    gca,
    tight_layout)
from matplotlib.ticker import FuncFormatter
from load_csv import load


def plot_population_comparison():
    """
    Function to load population data and display comparison between countries
    """
    df = load("population_total.csv")

    if df is None:
        raise ValueError("Failed to load the dataset")

    country1 = "France"
    country2 = "Germany"

    france_data = df[df["country"] == country1]
    other_data = df[df["country"] == country2]

    if france_data.empty:
        raise ValueError(f"{country1} not found in the dataset")

    if other_data.empty:
        raise ValueError(f"{country2} not found in the dataset")

    years = df.columns[1:]
    years_filtered = [year for year in years if 1800 <= int(year) <= 2050]

    france_population = france_data[years_filtered].iloc[0].values
    other_population = other_data[years_filtered].iloc[0].values

    years_int = [int(year) for year in years_filtered]

    france_pop_float = convert_population_to_float(france_population)
    other_pop_float = convert_population_to_float(other_population)

    plot(years_int, france_pop_float, color="green", label=country1)
    plot(years_int, other_pop_float, label=country2)

    title("Population Projections")
    xlabel("Year")
    ylabel("Population")
    legend(loc="lower right")

    gca().yaxis.set_major_formatter(FuncFormatter(
        lambda x, pos: f"{x / 1000000000:.1f}B" if x >= 1000000000
        else f"{x / 1000000:.1f}M" if x >= 1000000
        else f"{x / 1000:.1f}k" if x >= 1000
        else f"{x:.0f}"
    ))

    tight_layout()
    show()


def convert_population_to_float(population_data):
    """
    Convert population data with suffixes (B, M, k) to float values

    Args:
        population_data: Array of population strings with suffixes

    Returns:
        list: Population values as floats
    """
    result = []
    for pop_str in population_data:
        if isinstance(pop_str, str):
            if pop_str.endswith("B"):
                result.append(float(pop_str[:-1]) * 1000000000)
            elif pop_str.endswith("M"):
                result.append(float(pop_str[:-1]) * 1000000)
            elif pop_str.endswith("k"):
                result.append(float(pop_str[:-1]) * 1000)
            else:
                result.append(float(pop_str))
        else:
            result.append(float(pop_str))
    return result


def main():
    """
    Main function with error handling
    """
    try:
        plot_population_comparison()
    except ValueError as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
