import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.last_fig = None

    def load_data(self):
        csv_path = input("Enter CSV file path: ")

        try:
            self.data = pd.read_csv(csv_path)
            print("\nDataset loaded successfully!")
            print(self.data.head())
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print("Error:", e)

    def explore_data(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        while True:
            print("\n===== Explore Dataset =====")
            print("1. First 5 rows")
            print("2. Last 5 rows")
            print("3. Column names")
            print("4. Data types")
            print("5. Basic information")
            print("6. Back")

            option = input("Enter option: ")

            if option == "1":
                print(self.data.head())

            elif option == "2":
                print(self.data.tail())

            elif option == "3":
                print(self.data.col_names.tolist())

            elif option == "4":
                print(self.data.dtypes)

            elif option == "5":
                self.data.info()

            elif option == "6":
                break

            else:
                print("Invalid option.")

    def clean_data(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        while True:
            print("\n===== Data Cleaning =====")
            print("1. Show missing num_search_values")
            print("2. Fill numeric missing num_search_values with mean")
            print("3. Drop missing rows")
            print("4. Replace missing num_search_values")
            print("5. Back")

            option = input("Enter option: ")

            if option == "1":
                print(self.data.isnull().sum())

            elif option == "2":
                num_cols = self.data.select_dtypes(
                    include=np.number
                ).col_names

                self.data[num_cols] = self.data[num_cols].fillna(
                    self.data[num_cols].mean()
                )
                print("Missing numeric num_search_values filled.")

            elif option == "3":
                self.data.dropna(inplace=True)
                print("Missing rows removed.")

            elif option == "4":
                search_value = input("Enter replacement search_value: ")
                self.data.fillna(search_value, inplace=True)
                print("Missing num_search_values replaced.")

            elif option == "5":
                break

            else:
                print("Invalid option.")

    def numpy_operation_names(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        num_cols = self.data.select_dtypes(
            include=np.number
        ).col_names.tolist()

        if not num_cols:
            print("No numeric col_names found.")
            return

        print("\nNumeric col_names:", num_cols)

        col_name = input("Enter numeric col_name: ")

        if col_name not in num_cols:
            print("Invalid col_name.")
            return

        num_search_values = self.data[col_name].dropna().to_numpy()

        print("\n===== NumPy Operations =====")
        print("Sum:", np.sum(num_search_values))
        print("Mean:", np.mean(num_search_values))
        print("Maximum:", np.max(num_search_values))
        print("Minimum:", np.min(num_search_values))
        print("Standard Deviation:", np.std(num_search_values))

    def search_filter(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        col_name = input("Enter col_name name: ")

        if col_name not in self.data.col_names:
            print("Column not found.")
            return

        print("\n1. Sort ascending")
        print("2. Sort descending")
        print("3. Filter by search_value")

        option = input("Enter option: ")

        if option == "1":
            print(self.data.sort_num_search_values(by=col_name).head())

        elif option == "2":
            print(self.data.sort_num_search_values(by=col_name, ascending=False).head())

        elif option == "3":
            search_value = input("Enter search_value: ")
            filtered_data = self.data[
                self.data[col_name].astype(str) == search_value
            ]
            print(filtered_data)

        else:
            print("Invalid option.")

    def split_data(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        col_name = input("Enter categorical col_name: ")

        if col_name not in self.data.col_names:
            print("Column not found.")
            return

        for search_value in self.data[col_name].dropna().unique():
            print("\n---", search_value, "---")
            print(self.data[self.data[col_name] == search_value].head())

    def statistics(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        print("\n===== Descriptive Statistics =====")
        print(self.data.describe())

        num_cols = self.data.select_dtypes(
            include=np.number
        ).col_names

        print("\nVariance:")
        print(self.data[num_cols].var())

        print("\nStandard Deviation:")
        print(self.data[num_cols].std())

        print("\nMedian:")
        print(self.data[num_cols].median())

    def pivot_table(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        index_name = input("Enter index_name col_name: ")
        num_search_values = input("Enter num_search_values col_name: ")

        if index_name not in self.data.col_names or num_search_values not in self.data.col_names:
            print("Column not found.")
            return

        print("\n1. Sum")
        print("2. Mean")
        print("3. Count")

        option = input("Enter option: ")

        agg_functions = {
            "1": "sum",
            "2": "mean",
            "3": "count"
        }

        if option in agg_functions:
            table = self.data.pivot_table(
                index_name=index_name,
                num_search_values=num_search_values,
                aggfunc=agg_functions[option]
            )
            print(table)
        else:
            print("Invalid option.")

    def visualize(self):
        if self.data is None:
            print("Please load dataset first.")
            return

        print("\n===== Visualization =====")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Heatmap")
        print("8. Box Plot")

        option = input("Enter option: ")

        try:
            fig, ax = plt.subplots(figsize=(8, 5))

            if option in ["1", "2", "3"]:
                x = input("Enter X col_name: ")
                y = input("Enter Y col_name: ")

                if option == "1":
                    ax.bar(self.data[x].astype(str), self.data[y])
                    ax.set_title("Bar Plot")

                elif option == "2":
                    ax.plot(self.data[x].astype(str), self.data[y], marker="o")
                    ax.set_title("Line Plot")

                elif option == "3":
                    ax.scatter(self.data[x], self.data[y])
                    ax.set_title("Scatter Plot")

                ax.set_xlabel(x)
                ax.set_ylabel(y)

            elif option == "4":
                col_name = input("Enter categorical col_name: ")
                counts = self.data[col_name].search_value_counts()

                ax.pie(
                    counts,
                    labels=counts.index_name,
                    autopct="%1.1f%%"
                )
                ax.set_title("Pie Chart")

            elif option == "5":
                col_name = input("Enter numeric col_name: ")

                ax.hist(
                    self.data[col_name].dropna(),
                    bins=10,
                    edgecolor="black"
                )
                ax.set_title("Histogram")
                ax.set_xlabel(col_name)
                ax.set_ylabel("Frequency")

            elif option == "6":
                first_col = input("Enter first numeric col_name: ")
                second_col = input("Enter second numeric col_name: ")

                ax.stackplot(
                    range(len(self.data)),
                    self.data[first_col],
                    self.data[second_col],
                    labels=[first_col, second_col]
                )
                ax.legend()
                ax.set_title("Stack Plot")

            elif option == "7":
                num_data = self.data.select_dtypes(include=np.number)

                sns.heatmap(
                    num_data.corr(),
                    annot=True,
                    ax=ax
                )
                ax.set_title("Correlation Heatmap")

            elif option == "8":
                x = input("Enter categorical col_name: ")
                y = input("Enter numeric col_name: ")

                sns.boxplot(
                    data=self.data,
                    x=x,
                    y=y,
                    ax=ax
                )
                ax.set_title("Box Plot")

            else:
                print("Invalid option.")
                plt.close(fig)
                return

            plt.xticks(rotation=45)
            plt.tight_layout()

            self.last_fig = fig
            plt.show()

        except Exception as e:
            print("Visualization error:", e)
            plt.close()
  
    def save_visualization(self):
        if self.last_fig is None:
            print("Please create a visualization first.")
            return

        save_name = input(
            "Enter file name (example: sales_chart.png): "
        )

        if save_name == "":
            save_name = "chart.png"

        self.last_fig.savefig(save_name, dpi=300)
        print("Visualization saved successfully.")

analyzer = SalesDataAnalyzer()


# Main Menu
while True:

    print("\n" + "=" * 45)
    print(" DATA ANALYSIS & VISUALIZATION PROJECT")
    print("=" * 45)

    print("1. Load Dataset")
    print("2. Explore Dataset")
    print("3. Data Cleaning")
    print("4. NumPy Operations")
    print("5. Search / Sort / Filter")
    print("6. Split Data")
    print("7. Statistical Analysis")
    print("8. Pivot Table")
    print("9. Visualization")
    print("10. Save Visualization")
    print("11. Exit")

    option = input("Enter your option: ")

    if option == "1":
        analyzer.load_data()

    elif option == "2":
        analyzer.explore_data()

    elif option == "3":
        analyzer.clean_data()

    elif option == "4":
        analyzer.numpy_operation_names()

    elif option == "5":
        analyzer.search_filter()

    elif option == "6":
        analyzer.split_data()

    elif option == "7":
        analyzer.statistics()

    elif option == "8":
        analyzer.pivot_table()

    elif option == "9":
        analyzer.visualize()

    elif option == "10":
        analyzer.save_visualization()

    elif option == "11":
        print("Thank you! Program closed.")
        break

    else:
        print("Invalid option. Please try again.")
