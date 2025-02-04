from matplotlib import pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib import font_manager as fm
import os

FONT_PROPS = fm.FontProperties(fname='./assets/fonts/Anton-Regular.ttf')
ROWS       = 5
COLS       = 7

RED1       = '#9d0000'
RED2       = '#b5374e'
RED3       = '#c86b7c'

def make_table(data, start_from=1):
    fig, ax = plt.subplots(figsize=(8,4))

    ax.set_ylim(1, ROWS + 2)
    ax.set_xlim(1, COLS + 1)

    ax.text(3.5, 6.5, 'Time', va='center', ha='center', fontproperties=FONT_PROPS, color=RED1)
    ax.text(4.5, 6.5, 'Doadores', va='center', ha='center', fontproperties=FONT_PROPS, color=RED1)
    ax.text(5.5, 6.5, 'Apoiadores', va='center', ha='center', fontproperties=FONT_PROPS, color=RED1)
    ax.text(6.5, 6.5, 'Total\nPresente', va='center', ha='center', fontproperties=FONT_PROPS, color=RED1)
    ax.text(7.5, 6.5, 'Total\nPontos', va='center', ha='center', fontproperties=FONT_PROPS, color=RED1)

    rect = patches.Rectangle(
            (1, 6.1),  # bottom left starting position (x,y)
            8,  # width
            0.8,  # height
            ec='none',
            fc='white',
            zorder=-1
        )
    ax.add_patch(rect)

    for i, row in enumerate(data):
        y = 5.5 - i
        time = '\n'.join(row['time'].rsplit(' ', 1)).capitalize()
        ax.text(1.1, y, f'{start_from + i}º lugar', va='center', ha='left', fontproperties=FONT_PROPS, color='white')
        ax.text(3, y, time, va='center', ha='left', fontproperties=FONT_PROPS, color='white')
        ax.text(4.5, y, str(row['doadores']), va='center', ha='center', fontproperties=FONT_PROPS, color='white')
        ax.text(5.5, y, str(row['apoiadores']), va='center', ha='center', fontproperties=FONT_PROPS, color='white')
        ax.text(6.5, y, str(row['total presente']), va='center', ha='center', fontproperties=FONT_PROPS, color='white')
        ax.text(7.5, y, str(row['total pontos']), va='center', ha='center', fontproperties=FONT_PROPS, color='white')

        escudo = row['time'].replace(' ', '_')
        image = mpimg.imread(f"./assets/escudos/{escudo}.png")
        im = OffsetImage(image, zoom=0.35)
        ab = AnnotationBbox(im, (2.3, y), frameon=False, xycoords="data")
        ax.add_artist(ab)
        
        if start_from + i != 1:
            rect = patches.Rectangle(
                (1, 5.1 - i),  # bottom left starting position (x,y)
                7,  # width
                0.8,  # height
                ec='none',
                fc=RED3,
                zorder=-1
            )
            ax.add_patch(rect)
        else:
            rect = patches.Rectangle(
                (1, 5.1 - i),  # bottom left starting position (x,y)
                7,  # width
                0.8,  # height
                ec='none',
                fc='#ffffff',
                zorder=-2
            )
            ax.add_patch(rect)
            rect2 = patches.Rectangle(
                (1.05, 5.15 - i),  # bottom left starting position (x,y)
                6.9,  # width
                0.7,  # height
                ec='none',
                fc=RED2,
                zorder=-1
            )
            ax.add_patch(rect2)

    ax.axis('off')

    if not os.path.exists('./resultados'):
        os.makedirs('./resultados')

    plt.savefig(f'./resultados/tabela{start_from // 5 + 1}', dpi=300, bbox_inches='tight', transparent=True)

if __name__ == '__main__':
    data = [
        {'time': 'vasco', 'doadores': 8, 'apoiadores': 2, 'total presente': 10, 'total pontos': 10},
        {'time': 'real madrid', 'doadores': 7, 'apoiadores': 3, 'total presente': 10, 'total pontos': 10},
        {'time': 'flamengo', 'doadores': 5, 'apoiadores': 3, 'total presente': 8, 'total pontos': 8},
        {'time': 'botafogo', 'doadores': 3, 'apoiadores': 2, 'total presente': 5, 'total pontos': 5},
        {'time': 'fluminense', 'doadores': 2, 'apoiadores': 1, 'total presente': 3, 'total pontos': 3},
        {'time': 'palmeiras', 'doadores': 1, 'apoiadores': 1, 'total presente': 2, 'total pontos': 2},
        {'time': 'potiguar de mossoró', 'doadores': 1, 'apoiadores': 0, 'total presente': 1, 'total pontos': 1},
    ]

    for i in range(0, len(data), 5):
        make_table(data[i:i+5], start_from=i+1)