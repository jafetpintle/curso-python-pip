import matplotlib.pyplot as plt 

def generate_pie_charts():
    labels = ['A','B','C']
    values = [200,100,500]

    fig, axes = plt.subplots()
    axes.pie(values, labels=labels)
    fig.savefig('pie.png')
    plt.close()