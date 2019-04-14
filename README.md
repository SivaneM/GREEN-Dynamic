<p align ="center">
  <img width = "400" height = "400" src = "https://hijab-in.com/wp-content/uploads/2013/09/ecologie.jpg">
</p>
  
# **SOMMAIRE**

* [Membre du groupe](#ariel)
* [Pourquoi l'écologie ?](#siv)
* [Modèle simple](#avi)
* [Modèle complexe](#lilo)

<a name="ariel"></a>
## _**Membre du groupe**_

>Marciano Sivane 

>Baichère Mathéo

>Torjmane Ariel

>Tabbakh Amine


<a name="siv"></a>
## _**Pourquoi l'écologie ?**_


Vous vous demandez sûrement : Pourquoi l'écologie ? A quoi ça sert ? Et surtout comment ?
Alors, on vous rassure directement , pas besoin de planter des arbres chaque dimanche pour adhérer à ce mouvement qui encourage la protection de nos écosystèmes, ou plus généralement de notre environnement.

Nous, on vous propose quelque chose de beaucoup plus simple et qui changera vraiment la donne:
**bien choisir vos poubelles** ! 
En effet, notre projet se concentre sur l'importance du tri sélectif dans la défense de notre planète face à la menace grandissante du réchauffement climatique. Et on peut y gagner beaucoup ! Grâce au tri quotidien des déchets , non seulement on favorise leur recyclage mais en plus, on préserve les ressources naturelles (qui sont de plus en plus *faibles*) et on évite le gaspillage. 

Alors, toujours pas convaincu ?

Ce n'est pas un problème, là est tout l'enjeu de notre projet. Ainsi, nous allons vous présenter deux différents programmes qui modélisent de manière simple et plus complexe, l'intêret du tri sélectif.

Mais alors, quel lien avec la dynamique ?  En nous basant ainsi sur le modèle du tri séléctif et sur l'idée de l'écologie en général, nos deux programmes sont élaborés de sorte à ce qu'ils correspondent à des **sytèmes dynamiques**. En effet, dans ces systèmes, le temps est défini par le nombre de fois où l'on envoie de noveaux déchets dans les différentes poubelles et au niveau microscopique,  on observe la destination de chaque déchet. De cette façon, on évalue de manière macroscopique, le nombre de déchets qui sont bien placés ou pas dans chaque poubelle pour mettre en avant que l'action de chacun influence *fortement* l'avenir de tous.


<a name="avi"></a>
## _**Modèle simple**_

Pour évaluer la pertinence de notre sujet, nous avons décidé d'établir dans un premier temps un modèle simple qui utilise une loi de répartition telle que 90% des déchets vont dans la poubelle qui leur sont destinés et 10% dans la mauvaise.
Ainsi, ce modèle consiste à utiliser uniquement deux sortes de poubelles : une bonne poubelle et une mauvaise, pour seulement deux types de déchets : A et B. 

<p> Premièrement, l’algorithme utilise un dictionnaire de probabilités de la présence des déchets dans la poubelle, probabilités que l'on a distribué équitablement entre les deux déchets A et B : </p>
  <pre><code>p = {"A" : 0.5,
     "B" : 0.5}
</code></pre>


<p> Nous tirons aléatoirement un déchet par la fonction <code>flux(p)</code> et nous observons si le déchet ira dans la bonne ou dans la mauvaise poubelle grâce à la fonction <code>poubelle-choisie(p,q)</code> suivante, avec q, le dictionnaire de probabilités de répartition des déchets: </p>
  <pre><code> q = {"BonnePoubelle" : 0.9,
    "MauvaisePoubelle" : 0.1,
    ""}
  
  def poubelle_choisie(p,q):
    f = flux(p)
    n = (randrange(0,100)x1.0)/100
    if f == "A":
        if n >= q["MauvaisePoubelle"]:
            return "BonnePoubelle"
        else: 
            return "MauvaisePoubelle"
    else:
        if n >= q["MauvaisePoubelle"]:
            return "BonnePoubelle"
        else: 
            return "MauvaisePoubelle"
      
</code></pre>

Ainsi, en utilisant le résultat de cette dernière fonction qui à chaque déchet, attribue une destination, nous avons pu coder une autre fonction, <code>nb_dans_poubelle(p,q)</code>, qui présente le nombre de déchet dans chaque poubelle pour 100 déchets. C'est ce qui nous a permis d'écricre la fonction <code>nfoispoubelle(p,q,n)</code> qui, selon un nombre n de tours choisi par l'utilisateur, permet de visualiser le nombre de déchet par tour obtenu grâce à la fonction précédente. Enfin, nous avons programmé un graphique, par la fonction <code>plot_poubelle(M,n)</code> qui, en somme de cette suite de fonctions, permet de se rendre compte de la constance du nombre de déchets par poubelle, bonne et mauvaise, et ce, dû au dictionnaire de probabilités de répartition q, initialisé plus tôt. 

<p align ="center">
  <img width = "800" height = "300" src = "https://image.noelshack.com/fichiers/2019/15/4/1555009279-lilo.png">
</p>

On peut effectivement observer dans le graphique ci dessus, que le nombre de déchets dans la bonne poubelle se situe toujours aux environ de 90 et cela s'exlique du fait que pour chaque tour, 100 déchets sont traités et leur probabilité d'être bien placés est de 0,9. On suit le même raisonnement avec les déchets des mauvaises poubelles avec une probabilités de 0,1.
De ce

Ainsi, après avoir établi notre premier modèle, nous avons décidé d'établir la suite de notre projet en partant du même principe mais ce de manière plus complexifiée et travaillée, qui constitua notre **Modèle complexe**.

 
<a name="lilo"></a>
## _**Modèle complexe**_

Pour affiner notre projet, nous avons décidé d'établir un modèle complexe qui veut que, non pas deux types de déchéts ne soient traités mais sept. Ainsi, nous nous sommes référencés aux sortes de déchéts les plus rencontrées quotidiennement dans le but de préserver un lien de cohérence entre les résultats de notre projet et les conditions de la réalité. En effet, l'écologie étant placée au centre de notre sujet, nous nous devions de respecter au maximum les critères déja existants pour pouvoir possiblement faire avancer cet enjeu environnemental et politique.

De cette manière, en nous basant sur des chiffres de statistiques réelles, nous avons tout d'abord initialisé un dictionnaire rapportant les répartitions des déchets dans les poubelles. Ceci nous a premis par la suite d'établir une base de données quant aux probabilités d'envoi d'un type de déchet ou d'un autre pour chaque flux utilisé par notre programme. Ainsi, nous avons obtenu ce dictionnaire initial : 


<p align ="center">
  <img width = "500" height = "200" src = "https://image.noelshack.com/fichiers/2019/15/7/1555238545-capture-d-ecran-2019-04-14-a-12-42-07.png">
</p>





<a name="lol"></a>
## _**Interprétation et optimisation**_

L’étude que nous avons cherchée à modéliser montre que pour un traitement typique des déchets seulement un peu plus de la moitié sont  triés correctement. Cette modélisation s’est montrée pertinente par rapport aux enquêtes sur le tri sélectif en France.

Le tri sélectif est un geste anodin du quotidien qui peut apporter une grande différence à l’échelle du réchauffement climatique. Fabriquer consomme plus d’énergie que recycler, mais émet aussi plus de gaz à effet de serre. Ainsi, trier permet non seulement de réduire les émissions de gaz à effets de serres, mais permet aussi d’économiser les ressources naturelles.

Bien que des efforts et des progrès soient apparues en ce qui concerne le recyclage et le tri sélectif depuis quelques années, ils sont encore insuffisant comparés aux enjeux et risques encourus par notre planète.
Pour permettre aux futures générations de vivre dans un environnement propice, il est nécessaire pour chacun de commencer par faire les bons gestes au quotidien, trier.
