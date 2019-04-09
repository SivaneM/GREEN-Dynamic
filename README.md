
<img src = "https://mgv.coop/wp-content/uploads/2016/02/ecologique-MGV.png" alt = "Eco" title = "Ecologie" width = "400" height = "400" >


## Pourquoi l'écologie ? 

>Vous vous demandez sûrement : Pourquoi l'écologie ? A quoi ça sert ? Et surtout comment ?
>Alors, on vous rassure directement , pas besoin de planter des arbres chaque dimanche pour adhérer à ce mouvement qui encourage la protection de nos écosystèmes, ou plus généralement de notre environnement.

>Nous, on vous propose quelque chose de beaucoup plus simple et qui changera vraiment la donne : bien choisir vos poubelles ! 
En effet, notre projet se concentre sur l'importance du tri sélectif dans 



## Modèle simple

>Pour évaluer la pertinence de notre sujet, nous avons décidé d'établir dans un premier temps un modèle simple qui utiliserait une loi de répartition telle que 90% des déchets vont dans la poubelle qui leur sont destinés et 10% dans la mauvaise.
>Ainsi, ce modèle consiste à utiliser uniquement deux sortes de poubelles : une bonne poubelle et une mauvaise, pour seulement deux types de déchets : A et B. 

<p> Premièrement, l’algorithme utilise un dictionnaire de probabilités de la présence des déchets dans la poubelle, probabilités que l'on a distribué équitablement entre les deux déchets A et B : </p>
  <pre><code>p = {"A" : 0.5,
       "B" : 0.5}
</code></pre>



Nous tirons aléatoirement un déchet et nous observons si le déchet ira dans la bonne ou dans la mauvaise poubelle. 
On remarque ainsi que le facteur dépend de celui qui a jeter précédemment un déchet.
Une fois la bonne poubelle remplie, celle-ci est vidée et le mécanisme continue. 

<p>

<p> Ceci est un paragraphe normal : </p>
  <pre><code>Ceci est un bloc de code.
c'est la fin 
</code></pre>

def nb_dans_poubelle(p,q):
    p1 = 0
    p2 = 0
    n = 100
    for d in range(n+1):
        if poubelle_choisie(p,q)== "BonnePoubelle" :
            p1 = p1 + 1
        else :
            p2 = p2 + 1
    return (p1, p2)

  




## Modèle complexe 

On utilise un dictionnaire pour chaque type de déchets on associe sa poubelle correspondante.


## Interprétation et optimisation

L’étude que nous avons cherchée à modéliser montre que pour un traitement typique des déchets seulement un peu plus de la moitié sont  triés correctement. Cette modélisation s’est montrée pertinente par rapport aux enquêtes sur le tri sélectif en France.

Le tri sélectif est un geste anodin du quotidien qui peut apporter une grande différence à l’échelle du réchauffement climatique. Fabriquer consomme plus d’énergie que recycler, mais émet aussi plus de gaz à effet de serre. Ainsi, trier permet non seulement de réduire les émissions de gaz à effets de serres, mais permet aussi d’économiser les ressources naturelles.

Bien que des efforts et des progrès soient apparues en ce qui concerne le recyclage et le tri sélectif depuis quelques années, ils sont encore insuffisant comparés aux enjeux et risques encourus par notre planète.
Pour permettre aux futures générations de vivre dans un environnement propice, il est nécessaire pour chacun de commencer par faire les bons gestes au quotidien, trier.
