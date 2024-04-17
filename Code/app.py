from flask import Flask, render_template, request
from final_result import ProvideResult
import matplotlib.pyplot as plt
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def final_result():
    input_dict = request.form.to_dict()
    print(input_dict)
    provide_result = ProvideResult()
    output = provide_result.get_final_result(input_dict=input_dict)
    print(output)
    # # Define disease categories (modify based on your system)
    # disease_categories = ["Healthy", "Sick1", "Sick2", "Sick3", "Sick4"]
    #
    # # Create a bar chart
    # plt.bar(disease_categories, [0, 0, 0, 0, 0])  # Initialize empty bar values
    # plt.bar_label(plt.gca().containers[0], [output])  # Update specific bar with crisp output value
    #
    # plt.xlabel("Disease Category")
    # plt.ylabel("Likelihood")
    # plt.title("Heart Disease Diagnosis")
    #
    #
    # # Saving the plot to a file
    # plt.savefig('static/result_plot.png')  # Save the plot as a PNG file
    # input_string = output
    #
    # # Split the string based on the colon
    # split_string = input_string.split(":")
    #
    # # Extract the second part (after the colon)
    # numeric_part = split_string[1]
    #
    # # Strip leading and trailing spaces and convert to float
    # numeric_value = float(numeric_part.strip())
    #
    # print(numeric_value)
    # # Convert output to float
    # output = float(numeric_value)
    #
    # # Define disease categories and their ranges
    # disease_categories = ["Healthy", "Sick1", "Sick2", "Sick3", "Sick4"]
    # lower_bounds = [0, 1, 1.78, 1.5, 3.25]
    # upper_bounds = [1.78, 2.51, 3.25, 4.5, float('inf')]  # Use float('inf') for upper bound of last category
    #
    # # Find the appropriate category for the output
    # category = split_string[0]
    #
    # # Create a bar chart
    # plt.bar(disease_categories, [0, 0, 0, 0, 0])  # Initialize empty bar values
    # plt.bar_label(plt.gca().containers[0], [output])  # Update specific bar with crisp output value
    #
    # plt.xlabel("Disease Category")
    # plt.ylabel("Likelihood")
    # plt.title("Heart Disease Diagnosis")
    #
    # # Saving the plot to a file
    # plt.savefig('static/image/result_plot.png')  # Save the plot as a PNG file

    return render_template('result.html', output=output)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8448, debug=True)
