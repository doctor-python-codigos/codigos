# Autor : Doctor Python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

datos_cuidades = pd.read_csv('city_populations.csv', usecols=['name','group','year','value'])
colores = dict(zip(
            ['India','Europe','Asia','Latin America','Middle East','North America','Africa'],
            ['#adb0ff','#ffb3ff','#90d595','#e48381','#aafbff','#f7bb5f','#eafb50']))

grupo_lk = datos_cuidades.set_index('name')['group'].to_dict()

def draw_barchart(current_year):
    dff = datos_cuidades[datos_cuidades['year'].eq(current_year)].sort_values(by='value', ascending=True)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colores[grupo_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value-dx, i,     name,            size=12, weight='bold',   horizontalalignment='right', verticalalignment='bottom')
        ax.text(value-dx, i-.25, grupo_lk[name],  size=10, color='#444444', horizontalalignment='right', verticalalignment='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}', size=12,                  horizontalalignment='left' , verticalalignment='center')
   
    ax.text(1, 0.4, current_year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=900)
    
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.15, 'Las ciudades más pobladas del mundo desde 1500 hasta 2019',
                      transform=ax.transAxes, size=24, weight=600, ha='left', va='top')
    ax.text(0, 1.06, 'Poblacion (miles)', transform = ax.transAxes, size=12, color='#777777')

    ax.text(1, -0.09, '@doctor_python', transform=ax.transAxes, color='#000000', ha='right',
                       bbox=dict(facecolor='red', alpha=0.8, edgecolor='black'))
    plt.box(True)

fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart,interval=10, frames=range(1500, 2019))
plt.show()