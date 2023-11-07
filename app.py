from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
dataset = None
dataset = pd.read_csv('MergedDataset.csv')

@app.route("/")
def hello():
    return render_template('Overview.html')

@app.route("/overview")
def overview():
    return render_template('Overview.html')

@app.route("/zoom")
def zoom():
    return render_template('Zoom.html')

@app.route("/filter")
def filter():
    states = [
        "Please select a state", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
        "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
        "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
        "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]
    chart_view = [
    "Multi Line graph", "Grouped bar graph"
    ]
    years = [
    "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"
    ]
    return render_template('Filter.html', show_content=False, states=states, chart_view=chart_view, years=years, plot_data={}, view='')

@app.route("/singlestate" , methods=['GET', 'POST'])
def singlestate():
    selected_state = request.args.get('states')
    compare_state = request.args.get('statescompare')
    view = request.args.get('view')
    
    states = [
        "Please select a state", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
        "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
        "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
        "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]
    chart_view = [
    "Multi Line graph", "Grouped bar graph"
    ]
    years = [
    "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"
    ]

    if (selected_state == 'Please select a state'):
        return render_template('Filter.html', show_content=False, states=states, chart_view=chart_view, years=years, current_state=selected_state, current_compare_state=compare_state, plot_data={}, view=view)
    else:
        state_data = dataset[dataset['State'] == selected_state]
        x_values = state_data['Year']
        y_values = state_data['SAT Mean']
        y2_values = state_data['Total Completion (%)']
        plot_data = {
                'x': list(x_values),
                'y1': list(y_values),
                'y2': list(y2_values),
                'state': selected_state
            }
        if (compare_state != 'Please select a state'):
            statec_data = dataset[dataset['State'] == compare_state]
            xc_values = statec_data['Year']
            yc_values = statec_data['SAT Mean']
            yc2_values = statec_data['Total Completion (%)']
            plot_data['yc1'] = list(yc_values)
            plot_data['yc2'] = list(yc2_values)
            plot_data['state2'] = compare_state
        else:
            plot_data['reading'] = list(state_data['Critical reading'])
            plot_data['math'] = list(state_data['Mathematics'])

            
        return render_template('Filter.html', show_content=True, states=states, chart_view=chart_view, years=years, current_state=selected_state, current_compare_state=compare_state, plot_data=plot_data, view=view)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)