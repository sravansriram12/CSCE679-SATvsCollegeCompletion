from flask import Flask, request, render_template
import pandas as pd
from scipy.stats import pearsonr
import math

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
dataset = None
dataset = pd.read_csv('MergedDataset.csv')

@app.route("/")
def hello():
    years = dataset['Year'].unique()
    print('heyaa')
    ls=list()
    print(years)
    for year in years:
        # Filter data for the specific year
        year_data = dataset[dataset['Year'] == year]
        year_data = year_data.dropna(subset=['SAT Mean', 'Total Completion (%)'])
        # Calculate Pearson's correlation coefficient
        year_data['SAT Mean'] = pd.to_numeric(year_data['SAT Mean'], errors='coerce')
        year_data['Total Completion (%)'] = pd.to_numeric(year_data['Total Completion (%)'], errors='coerce')
        #year_data = year_data.dropna(subset=['SAT Mean', 'Total Completion (%)'], axis=1)

        for index, row in year_data.iterrows():
            try:
                sat_mean = float(row['SAT Mean'])
                total_completion = float(row['Total Completion (%)'])
                print(sat_mean, "  ",total_completion)
                if math.isnan(sat_mean) or math.isnan(total_completion) :
                    year_data = year_data.drop(index)
            except ValueError:
                # Drop the row if the value is not a valid number
                year_data = year_data.drop(index)

        correlation_coefficient, p_value = pearsonr(year_data['SAT Mean'], year_data['Total Completion (%)'])
        print(correlation_coefficient)
        ls.append(correlation_coefficient)
        #print(f'Year: {year}, Pearson\'s correlation coefficient: {ls}')

    states = dataset['State'].unique()
    #print('heyaa1')
    lss=list()
    #print(states)
    for state in states:
        # Filter data for the specific year
        state_data = dataset[dataset['State'] == state]
        state_data = state_data.dropna(subset=['SAT Mean', 'Total Completion (%)'])
        # Calculate Pearson's correlation coefficient
        state_data['SAT Mean'] = pd.to_numeric(state_data['SAT Mean'], errors='coerce')
        state_data['Total Completion (%)'] = pd.to_numeric(state_data['Total Completion (%)'], errors='coerce')
        #year_data = year_data.dropna(subset=['SAT Mean', 'Total Completion (%)'], axis=1)

        for index, row in state_data.iterrows():
            try:
                sat_mean = float(row['SAT Mean'])
                total_completion = float(row['Total Completion (%)'])
                print(sat_mean, "  ",total_completion)
                if math.isnan(sat_mean) or math.isnan(total_completion) :
                    state_data = state_data.drop(index)
            except ValueError:
                # Drop the row if the value is not a valid number
                state_data = state_data.drop(index)

        correlation_coefficient, p_value = pearsonr(state_data['SAT Mean'], state_data['Total Completion (%)'])
        print(correlation_coefficient)
        lss.append(correlation_coefficient)
        #print(f'Year: {year}, Pearson\'s correlation coefficient: {ls}')


    return render_template('Overview.html', yearss= years.tolist(), ls1=ls, ls2=lss)


@app.route("/overview")
def overview():

    # Assuming your columns are named 'year', 'x', and 'y'
    years = dataset['Year'].unique()
    #print('heyaa')
    ls=list()
    #print(years)
    for year in years:
        # Filter data for the specific year
        year_data = dataset[dataset['Year'] == year]
        year_data = year_data.dropna(subset=['SAT Mean', 'Total Completion (%)'])
        # Calculate Pearson's correlation coefficient
        year_data['SAT Mean'] = pd.to_numeric(year_data['SAT Mean'], errors='coerce')
        year_data['Total Completion (%)'] = pd.to_numeric(year_data['Total Completion (%)'], errors='coerce')
        #year_data = year_data.dropna(subset=['SAT Mean', 'Total Completion (%)'], axis=1)

        for index, row in year_data.iterrows():
            try:
                sat_mean = float(row['SAT Mean'])
                total_completion = float(row['Total Completion (%)'])
                print(sat_mean, "  ",total_completion)
                if math.isnan(sat_mean) or math.isnan(total_completion) :
                    year_data = year_data.drop(index)
            except ValueError:
                # Drop the row if the value is not a valid number
                year_data = year_data.drop(index)

        correlation_coefficient, p_value = pearsonr(year_data['SAT Mean'], year_data['Total Completion (%)'])
        print(correlation_coefficient)
        ls.append(correlation_coefficient)
        #print(f'Year: {year}, Pearson\'s correlation coefficient: {ls}')

    states = dataset['State'].unique()
    #print('heyaa1')
    lss=list()
    #print(states)
    for state in states:
        # Filter data for the specific year
        state_data = dataset[dataset['State'] == state]
        state_data = state_data.dropna(subset=['SAT Mean', 'Total Completion (%)'])
        # Calculate Pearson's correlation coefficient
        state_data['SAT Mean'] = pd.to_numeric(state_data['SAT Mean'], errors='coerce')
        state_data['Total Completion (%)'] = pd.to_numeric(state_data['Total Completion (%)'], errors='coerce')
        #year_data = year_data.dropna(subset=['SAT Mean', 'Total Completion (%)'], axis=1)

        for index, row in state_data.iterrows():
            try:
                sat_mean = float(row['SAT Mean'])
                total_completion = float(row['Total Completion (%)'])
                print(sat_mean, "  ",total_completion)
                if math.isnan(sat_mean) or math.isnan(total_completion) :
                    state_data = state_data.drop(index)
            except ValueError:
                # Drop the row if the value is not a valid number
                state_data = state_data.drop(index)

        correlation_coefficient, p_value = pearsonr(state_data['SAT Mean'], state_data['Total Completion (%)'])
        print(correlation_coefficient)
        lss.append(correlation_coefficient)
        #print(f'Year: {year}, Pearson\'s correlation coefficient: {ls}')


    return render_template('Overview.html', yearss= years.tolist(), ls1=ls, ls2=lss)

@app.route("/zoom")
def zoom():
    mean_sat_2009 = list()
    mean_sat_2010 = list()
    mean_sat_2011 = list()
    mean_sat_2012 = list()
    mean_sat_2013 = list()
    mean_sat_2014 = list()
    mean_sat_2015 = list()
    mean_sat_2016 = list()
    college_comp_2009 = list()
    college_comp_2010 = list()
    college_comp_2011 = list()
    college_comp_2012 = list()
    college_comp_2013 = list()
    college_comp_2014 = list()
    college_comp_2015 = list()
    college_comp_2016 = list()
    years = dataset['Year'].unique()
    state_data = dataset.dropna(subset=['SAT Mean', 'Total Completion (%)'])
    for index, row in state_data.iterrows():
            try:
                sat_mean = float(row['SAT Mean'])
                total_completion = float(row['Total Completion (%)'])
                print(sat_mean, "  ",total_completion)
                if math.isnan(sat_mean) or math.isnan(total_completion) :
                    state_data = state_data.drop(index)
            except ValueError:
                # Drop the row if the value is not a valid number
                state_data = state_data.drop(index)
    for index, row in state_data.iterrows():
        year = int(row['Year'])
        sat_score = row['SAT Mean']
        comp_rate = row['Total Completion (%)']
        if year == 2009:
            mean_sat_2009.append(sat_score)
            college_comp_2009.append(comp_rate)
        elif year == 2010:
            mean_sat_2010.append(sat_score)
            college_comp_2010.append(comp_rate)
        elif year == 2011:
            mean_sat_2011.append(sat_score)
            college_comp_2011.append(comp_rate)
        elif year == 2012:
            mean_sat_2012.append(sat_score)
            college_comp_2012.append(comp_rate)
        elif year == 2013:
            mean_sat_2013.append(sat_score)
            college_comp_2013.append(comp_rate)
        elif year == 2014:
            mean_sat_2014.append(sat_score)
            college_comp_2014.append(comp_rate)
        elif year == 2015:
            mean_sat_2015.append(sat_score)
            college_comp_2015.append(comp_rate)
        elif year == 2016:
            mean_sat_2016.append(sat_score)
            college_comp_2016.append(comp_rate)
    print(mean_sat_2009)
    return render_template('Zoom.html', mean_sat_2009 = mean_sat_2009, mean_sat_2010= mean_sat_2010, mean_sat_2011=mean_sat_2011, mean_sat_2012=mean_sat_2012, mean_sat_2013=mean_sat_2013, mean_sat_2014=mean_sat_2014, mean_sat_2015=mean_sat_2015, mean_sat_2016=mean_sat_2016,
    college_comp_2009= college_comp_2009, college_comp_2010=college_comp_2010, college_comp_2011=college_comp_2011, college_comp_2012=college_comp_2012, college_comp_2013=college_comp_2013, college_comp_2014=college_comp_2014, college_comp_2015=college_comp_2015, college_comp_2016=college_comp_2016)

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