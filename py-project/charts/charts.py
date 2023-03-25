import matplotlib.pyplot as plt
import io

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('img.jpg'.format('svg'))
    plt.close()