
<img aligne ="right" src = "https://hijab-in.com/wp-content/uploads/2013/09/ecologie.jpg" alt = "Eco" title = "Ecologie" width = "400" height = "400" >


# **SOMMAIRE**

* [Pourquoi l'écologie ?](#siv)
* [Modèle simple](#avi)
* [Modèle complexe](#lilo)

<a name="siv"></a>
## _**Pourquoi l'écologie ?**_


Vous vous demandez sûrement : Pourquoi l'écologie ? A quoi ça sert ? Et surtout comment ?
Alors, on vous rassure directement , pas besoin de planter des arbres chaque dimanche pour adhérer à ce mouvement qui encourage la protection de nos écosystèmes, ou plus généralement de notre environnement.
left
Nous, on vous propose quelque chose de beaucoup plus simple et qui changera vraiment la donne :
**bien choisir vos poubelles** ! 
En effet, notre projet se concentre sur l'importance du tri sélectif dans la défense de notre planète face à la menace grandissante du réchauffement climatique. Et on peut y gagner beaucoup ! Grâce au tri quotidien des déchets , non seulement on favorise leur recyclage mais en plus, on préserve les ressources naturelles (qui sont de plus en plus *faibles*) et on évite le gaspillage. Alors, toujours pas convaincu ?

Ce n'est pas un problème, là est tout l'enjeu de notre projet. Ainsi, nous allons vous présenter deux différents programmes qui modélisent de manière simple et plus complexe, l'intêret du tri sélectif.
Mais alors, quel lien avec la dynamique ?  En nous basant ainsi sur le modèle du tri séléctif et sur l'idée de l'écologie en général, nos deux programmes sont élaborés de sorte à ce qu'ils correspondent à des sytèmes dynamiques. En effet, dans ces systèmes, le temps est défini par le nombre de fois où l'on envoie de noveaux déchets dans les différentes poubelles et au niveau microscopique,  on observe la destination de chaque déchet. De cette façon, on évalue de manière macroscopique, le nombre de déchets qui sont bien placés ou pas dans chaque poubelle pour mettre en avant que l'action de chacun influence fortement l'avenir de tous.


<a name="avi"></a>
## _**Modèle simple**_

Pour évaluer la pertinence de notre sujet, nous avons décidé d'établir dans un premier temps un modèle simple qui utilise une loi de répartition telle que 90% des déchets vont dans la poubelle qui leur sont destinés et 10% dans la mauvaise.
Ainsi, ce modèle consiste à utiliser uniquement deux sortes de poubelles : une bonne poubelle et une mauvaise, pour seulement deux types de déchets : A et B. 

<p> Premièrement, l’algorithme utilise un dictionnaire de probabilités de la présence des déchets dans la poubelle, probabilités que l'on a distribué équitablement entre les deux déchets A et B : </p>
  <pre><code>p = {"A" : 0.5,
     "B" : 0.5}
</code></pre>


<p> Nous tirons aléatoirement un déchet par la fonction <code>flux(p)</code> et nous observons si le déchet ira dans la bonne ou dans la mauvaise poubelle grâce à la fonction <code>poubelle-choisie(p,q)</code> suivante, avec q, le dictionnaire de probabilités de répartition des déchets: </p>
  <pre><code>q = {"BonnePoubelle" : 0.9,
    "MauvaisePoubelle" : 0.1,
    ""}

def poubelle_choisie(p,q):
    f = flux(p)
    n = (randrange(0,100)x1.0)/100
    if f == "A":
        for d in q:
            if n >= q[d]:
                return "BonnePoubelle"
            else: 
                return "MauvaisePoubelle"
    else:
        for d in q:
            if n >= q[d]:
                return "BonnePoubelle"
            else: 
                return "MauvaisePoubelle"
                
</code></pre>

On remarque ainsi que le facteur dépend de celui qui a jeter précédemment un déchet.
Une fois la bonne poubelle remplie, celle-ci est vidée et le mécanisme continue. 

 
<a name="lilo"></a>
## Modèle complexe 

On utilise un dictionnaire pour chaque type de déchets on associe sa poubelle correspondante.



<a name="lol"></a>
## Interprétation et optimisation

L’étude que nous avons cherchée à modéliser montre que pour un traitement typique des déchets seulement un peu plus de la moitié sont  triés correctement. Cette modélisation s’est montrée pertinente par rapport aux enquêtes sur le tri sélectif en France.

Le tri sélectif est un geste anodin du quotidien qui peut apporter une grande différence à l’échelle du réchauffement climatique. Fabriquer consomme plus d’énergie que recycler, mais émet aussi plus de gaz à effet de serre. Ainsi, trier permet non seulement de réduire les émissions de gaz à effets de serres, mais permet aussi d’économiser les ressources naturelles.

Bien que des efforts et des progrès soient apparues en ce qui concerne le recyclage et le tri sélectif depuis quelques années, ils sont encore insuffisant comparés aux enjeux et risques encourus par notre planète.
Pour permettre aux futures générations de vivre dans un environnement propice, il est nécessaire pour chacun de commencer par faire les bons gestes au quotidien, trier.
