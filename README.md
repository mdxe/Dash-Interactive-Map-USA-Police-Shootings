## Dashboard with Dash

Simple Dash/Python Dashboard where you can see the location of deadly shootings by police on a map by race or gender.


## Usage

1. Install requirements (current version of Dash requires Python 3)
```bash
pip install dash
pip install pandas
```

2. Start server

```bash
> python app.py
```

3. Navigate to: http://127.0.0.1:8050/

Screenshot 1: https://i.imgur.com/C4jwNM6.png (by gender)

Screenshot 2: https://i.imgur.com/JGnZK9v.png (by race)

## Todo

- [ ] improve layout
- [ ] death count for current view (when zoomed in)
- [ ] setup live demo
- [ ] add table with shootings/100000 citizens for each state
- [ ] remember chart's current state (for selected race/sex)
- [x] add gender
- [x] add year dropDown
- [x] add total death count for current selection

## Credits

Thanks to:

* https://github.com/washingtonpost/data-police-shootings for the data
* https://dash.plotly.com/ for the Dash framework
