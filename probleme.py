from random import random
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi
from time import time

# Initialisation des variables
valeurs = []
temps_execution = []  # Liste pour stocker les temps d'exécution
xvals = [10**m for m in range(1, 7)]  # Nombre de points par itération
cercle = np.array([np.array([cos(np.radians(t)), sin(np.radians(t))]) / 2 for t in range(360)])  # Limite du cercle

# Préparation des subplots (figure 2)
fig2, axes = plt.subplots(2, 3, figsize=(15, 8))  # Figure 2 : subplots
axes = axes.ravel()  # Conversion en tableau 1D pour un indexage facile

# Ajustement explicite des espacements
fig2.subplots_adjust(hspace=0.3, wspace=0.3)  # Augmentation verticale, réduction horizontale

# Calcul des points dans le cercle pour chaque itération
for i, n in enumerate(xvals):
    debut = time()
    points = np.array([p for _ in range(n) if np.linalg.norm(p := np.array([random(), random()]) - 0.5) <= 0.5])
    fin = time() - debut
    valeurs.append(len(points) / n)
    temps_execution.append(fin)

    # Tracer les points pour cette itération
    ax = axes[i]
    ax.plot(points[:, 0], points[:, 1], '.')
    ax.plot(cercle[:, 0], cercle[:, 1], 'k--', lw=1)
    
    # Affichage du nombre de points
    n_str = f"{10**(i + 1)}"
    if i + 1 == 1:
        ax.set_title(rf"$n={n_str}$")
    else:
        ax.set_title(rf"$n={10}^{i+1}$")
        
    ax.set_aspect('equal', adjustable='box')

# Estimation finale de π
valeurs = np.array(valeurs) * 4

# Graphique de l'estimation de π et des temps d'exécution (figure 1)
fig1, ax1 = plt.subplots(figsize=(8, 6))

# Axe principal pour l'estimation de π
ax1.semilogx(xvals, valeurs, 'o-', markersize=5)
ax1.set_xlabel(r"Nombre de points")
ax1.set_ylabel(r"Valeur approchée")
ax1.set_title(r"Performances de l'estimation de $\pi$")
ax1.grid()

# Ajouter un tick pour \(\pi\) en plus des ticks par défaut
yticks = list(ax1.get_yticks())
if pi not in yticks:
    yticks.append(pi)
yticks = sorted(yticks)  # Ordonner les ticks

ax1.set_yticks(yticks)
ax1.set_yticklabels([r"$\pi$" if abs(tick - pi) < 1e-5 else f"{tick:.2f}" for tick in yticks])

# Axe secondaire pour les temps d'exécution
ax2 = ax1.twinx()
ax2.semilogx(xvals, temps_execution, 'g--', linewidth=1)
ax2.set_ylabel("Temps d'exécution (s)")
ax2.tick_params(axis='y')

# Titre de la figure
fig2.suptitle("Points dans le cercle pour différents nombres de points", fontsize=16)

# Montrer les graphiques
plt.show()
