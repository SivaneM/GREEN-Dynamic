<p align ="center">
  <img width = "400" height = "400" src = "https://hijab-in.com/wp-content/uploads/2013/09/ecologie.jpg">
</p>

# **SOMMAIRE**

* [Membre du groupe](#ariel)
<br/>
* [Pourquoi l'écologie ?](#siv)
<br/>
* [Modèle simple](#avi)
<br/>
* [Modèle complexe](#lilo)
<br/>
* [Optimisation](#tl)
<br/>
* [Interprétation des résultats](#lol)
<br/>

<a name="ariel"></a>
* ## _**Membre du groupe**_

>Marciano Sivane 

>Baichère Mathéo

>Torjmane Ariel

>Tabbakh Amine


<a name="siv"></a>
* ## _**Pourquoi l'écologie ?**_


Vous vous demandez sûrement : Pourquoi l'écologie ? A quoi ça sert ? Et surtout comment ?
Alors, on vous rassure directement , pas besoin de planter des arbres chaque dimanche pour adhérer à ce mouvement qui encourage la protection de nos écosystèmes, ou plus généralement de notre environnement.

Nous, on vous propose quelque chose de beaucoup plus simple et qui changera vraiment la donne:
**bien choisir vos poubelles** ! 
En effet, notre projet se concentre sur l'importance du tri sélectif dans la défense de notre planète face à la menace grandissante du réchauffement climatique. Et on peut y gagner beaucoup ! Grâce au tri quotidien des déchets , non seulement on favorise leur recyclage mais en plus, on préserve les ressources naturelles (qui sont de plus en plus *faibles*) et on évite le gaspillage. 

Alors, toujours pas convaincu ?

Ce n'est pas un problème, là est tout l'enjeu de notre projet. Ainsi, nous allons vous présenter deux différents programmes qui modélisent de manière simple et plus complexe, l'intérêt du tri sélectif.

Mais alors, quel lien avec la dynamique ?  En nous basant ainsi sur le modèle du tri séléctif et sur l'idée de l'écologie en général, nos deux programmes sont élaborés de sorte à ce qu'ils correspondent à des **sytèmes dynamiques**. En effet, dans ces systèmes, le temps est défini par le nombre de fois où l'on envoie de nouveaux déchets dans les différentes poubelles et au niveau microscopique,  on observe la destination de chaque déchet. De cette façon, on évalue de manière macroscopique, le nombre de déchets qui sont bien placés ou pas dans chaque poubelle pour mettre en avant que l'action de chacun influence _**fortement**_ l'avenir de tous.




<a name="avi"></a>
* ## _**Modèle simple**_

Pour évaluer la pertinence de notre sujet, nous avons décidé d'établir dans un premier temps un modèle simple qui utilise une loi de répartition telle que 90% des déchets vont dans la poubelle qui leur sont destinés et 10% dans la mauvaise.
Ainsi, ce modèle consiste à utiliser uniquement deux sortes de poubelles : une bonne poubelle et une mauvaise, pour seulement deux types de déchets : A et B. 

<p> Premièrement, l’algorithme utilise un dictionnaire de probabilités de la présence des déchets dans la poubelle, probabilités que l'on a distribué équitablement entre les deux déchets A et B : </p>
  <pre><code>p = {<span style="color:red">"A"</span> : <span style="color:green">0.5</span>,
     <span style="color:red">"B"</span> : <span style="color:green">0.5</span>}
</code></pre>


<p> Nous tirons aléatoirement un déchet par la fonction <code>flux(p)</code> et nous observons si le déchet ira dans la bonne ou dans la mauvaise poubelle grâce à la fonction <code>poubelle-choisie(p,q)</code> suivante, avec q, le dictionnaire de probabilités de répartition des déchets: </p>
  <pre><code> q = {<span style="color:red">"BonnePoubelle"</span> : <span style="color:green">0.9</span>,
    <span style="color:red">"MauvaisePoubelle"</span> : <span style="color:green">0.1</span>,
    }
  
  <span style="color:black">================================================</span>
  
  <span style="color:green">def</span> <span style="color:blue">poubelle_choisie(p,q)</span>:
    f = flux(p)
    n = (randrange(0,100)x1.0)/100
    <span style="color:green">if</span> f == "A":
        <span style="color:green">if</span> n >= q["MauvaisePoubelle"]:
            return <span style="color:red">"BonnePoubelle"</span>
        <span style="color:green">else</span>: 
            return <span style="color:red">"MauvaisePoubelle"</span>
    <span style="color:green">else</span>:
        <span style="color:green">if</span> n >= q["MauvaisePoubelle"]:
            return <span style="color:red">"BonnePoubelle"</span>
        <span style="color:green">else</span>: 
            return <span style="color:red">"MauvaisePoubelle"</span>      
</code></pre>

Ainsi, en utilisant le résultat de cette dernière fonction qui à chaque déchet, attribue une destination, nous avons pu coder une autre fonction, <code>nb_dans_poubelle(p,q)</code>, qui présente le nombre de déchet dans chaque poubelle pour 100 déchets. C'est ce qui nous a permis d'écrire la fonction <code>nfoispoubelle(p,q,n)</code> qui, selon un nombre n de tours choisi par l'utilisateur, permet de visualiser le nombre de déchet par tour obtenu grâce à la fonction précédente. Enfin, nous avons programmé un graphique, par la fonction <code>plot_poubelle(M,n)</code> qui, en somme de cette suite de fonctions, permet de se rendre compte de la constance du nombre de déchets par poubelle, bonne et mauvaise, et ce, dû au dictionnaire de probabilités de répartition q, initialisé plus tôt. 

<p align ="center">
  <img width = "800" height = "300" src = "https://image.noelshack.com/fichiers/2019/15/4/1555009279-lilo.png">
</p>

On peut effectivement observer dans le graphique ci dessus, que le nombre de déchets dans la bonne poubelle se situe toujours aux environ de 90 et cela s'explique du fait que pour chaque tour, 100 déchets sont traités et leur probabilité d'être bien placés est de 0,9. On suit le même raisonnement avec les déchets des mauvaises poubelles avec une probabilités de 0,1.


Ainsi, après avoir établi notre premier modèle, nous avons décidé d'établir la suite de notre projet en partant du même principe mais ce de manière plus complexifiée et travaillée, qui constitua notre **modèle complexe**.<br/><br/>

 

 
<a name="lilo"></a>
* ## _**Modèle complexe**_

Pour affiner notre projet, nous avons décidé d'établir un modèle complexe qui veut que, non pas deux types de déchets ne soient traités mais **sept**. Ainsi, nous nous sommes référencés aux sortes de déchéts les plus rencontrées quotidiennement dans le but de préserver un lien de cohérence entre les résultats de notre projet et les conditions de la réalité. En effet, l'écologie étant placée au centre de notre sujet, nous nous devions de respecter au maximum les critères déjà existants pour pouvoir possiblement faire avancer cet enjeu environnemental et politique.

De cette manière, en nous basant sur des chiffres de statistiques réelles, nous avons tout d'abord initialisé un dictionnaire rapportant les répartitions des déchets dans les poubelles. Ceci nous a permis par la suite d'établir une base de données quant aux probabilités d'envoi d'un type de déchet ou d'un autre pour chaque flux utilisé par notre programme. Ainsi, nous avons obtenu ce dictionnaire initial : 


  <img width = "550" height = "200" src = "https://image.noelshack.com/fichiers/2019/15/7/1555238545-capture-d-ecran-2019-04-14-a-12-42-07.png">


Néanmoins, pour ce qui est des autres dictionnaires utiles à notre programmes, nous les avons tous initialisés de manière nulle parce que définis plus tard par différentes fonctions. 
Justement, prenons par exemple un des critères de notre système qui correspond à la _**taille des poubelles**_, et qui est décisif pour le reste de notre programme. On peut vous rappeler que dans ce modèle nous  avons décidé de nous pencher sur sept types de déchets. Mais qui dit sept types de déchets dit également **sept types de poubelles** !. En effet on peut pour comprendre se référer à la loi du modèle simple qui veut que :

> **La <span style="color:green">bonne</span> poubelle de l'un correspond à la <span style="color:red">mauvaise</span> des six autres**

De cette façon, la "bonne" poubelle d'un déchet fait de plastique sera _logiquement_ la poubelle de plastique et une "mauvaise" sera par exemple la poubelle de carton ou de métal. On a donc un schéma constitué de sept poubelles différentes, de flux envoyant des n déchets vers ces poubelles et une suite de fonctions perfectionnant ce schéma jusqu'à qu'il devienne un réel modèle complexe.

Ainsi, par exemple, la fonction <code>def_taille_poubelle(df)</code>, instaure une taille aléatoire pour chaque poubelle entre 100 et 400 centimètres pour persévérer sur la voie de la cohérence et, une fois ces tailles atribuées à chaque poubelles, on n'effectue aucun changement par la suite, les tailles restent fixes une fois le programme lancé : 

<pre><code> <span style="color:green">def</span> <span style="color:blue">def_taille_poubelle(df)</span>: #FIXE ! PAS DE CHANGEMENT !
    <span style="color:green">for</span> d <span style="color:green">in</span> df:
        var <span style="color:purple">=</span> random.randint(100,400)
        df[d]<span style="color:purple">=</span>var
    return <span style="color:red">d</span>    
</code></pre>



<br/>

On va par la suite remplir ces mêmes poubelles et ce, principalement par la fonction <code>poubelle_choisie(nom_du_dechet,dict_bd, dict_mv)</code>. Cette fonction va modifier et dépendre des paramètres suivants:

* Le déchet choisi à envoyer dans l'une des poubelles, défini par la fonction <code>dechet_choisi</code>.<br/>


* Un aléatoire de propabilité <span style="color:purple">r</span> donc défini entre 0 et 1, au sein de la fonction, utilisé de la façon suivante :
  - s'il est <span style="color:green"><= 0,7</span>, le déchet est mis dans la bonne poubelle car cela correspond simplement aux 70% de chances qu'un déchet a d'être bien placé.
  - s'il est <span style="color:red">>0,7</span>, le déchet est mis dans la mauvaise poubelle.
<br/><br/>
  

* De la taille de la poubelle et plus précisément de la fonction <code>change_si_90_dans_la_poubelle</code> qui renvoie un booléen : True si la poubelle est remplie à plus de 90% et False sinon. En effet, si tel est le cas, le déchet qui est préalablement choisi ne sera pas placé dans la bonne poubelle qui correspond à son type mais de façon sûre dans une des poubelles qui ne lui sont pas destinées.<br/>


* De plus, cette fonction modifie les dictionnaires de bons et mauvais déchets par flux et celui des déchets en total. Nous disposons d'ailleurs d'une fonction appelée <code>testeur_bon_fonctionnement_system()</code> qui vérifie effectivement que la somme des valeurs des clés de chaque type de déchets des dictionnaires <span style="color:black">dic_nb_bonne_poub</span> et  <span style="color:black">dic_nb_mauvaise_poub</span> correspond aux valeurs des clés de chaque type de déchet du dictionnaire  <span style="color:black">dictionaire_nombre_dechet</span>.


<br/>

Par la suite, la fonction <code>eboueur(diction_nombre_dechet,dict_taille,dict_eboueur)</code> suivante, permet de remettre à vide toutes les poubelles étant remplies à plus de 90% et met à jour le <code>dict_eboueur</code> qui pour chaque type de poubelles, comptabilise le nombre de fois où l'éboueur l'a vidée : 

<pre><code><span style="color:green">def</span> <span style="color:blue">eboueur</span>(diction_nombre_dechet,dict_taille,dict_eboueur):
    <span style="color:blue">#l'eboueur vide toutes les poubelles dépassant >= 90% de leurs taille !</span>
    <span style="color:green">for</span> k <span style="color:green">in</span> diction_nombre_dechet:
        <span style="color:green">if</span> ((change_si_90_dans_la_poubelle(diction_nombre_dechet,k,dict_taille)) <span style="color:purple">==</span> <span style="color:green">True</span>):
            dict_eboueur[k]<span style="color:purple">+=</span> diction_nombre_dechet[k]
            diction_nombre_dechet[k]<span style="color:purple">=</span> 0
             #on rajoute le nombre initational dans le dict ebouer qui nous permettra la vérification finale pour le Plot !
    <span style="color:green">return</span>     
</code></pre>
<br/>

Une fois l'ensemble de ces fonctions établies, on peut enfin coder la fonction <code>flux()</code> qui tire un déchet et lui attribue une poubelle, et celle qui en découle directement, <code>n_flux(n,k)</code> qui fait tourner la fonction <code>flux()</code> n fois pour un n passé en paramètre et qui laisse l'utilisateur décider pour quel k tour, passé en paramètre l'éboueur passera vider les poubelles qui le nécessitent. 


Enfin, on peut visualiser la répartition des déchets au bout d'un flux composé de n tours, dans les bonnes et mauvaises poubelles grâce aux graphiques suivant :

* Le graphique qui présente le nombre total de déchets, et les graphiques correspondants à la répartition de ces mêmes déchets entre les bonnes et les mauvaises poubelles. 
Prenons par exemple, un flux de 140 déchets sans faire passer l'éboueur. On lance donc les fonctions:
  - <code>n_flux(n,k)</code> avec n = 140 et k > 140 pour ne pas faire passer l'éboueur.
  On a donc <code>n_flux(140,144)</code> qui met à jour les différents dictionnaires et on obtient les histogrammes suivant :
 
 <img width = "900" height = "200" src = "https://image.noelshack.com/fichiers/2019/16/1/1555321552-capture-d-ecran-2019-04-15-a-11-45-38.png">
 
 - les fonctions <code>dic_final("plastique")</code>,  <code>dic_final("verre")</code>,  <code>dic_final("papier")</code> qui affichent les taux de déchets bien placés ou non dans les poubelle de plastique,de verre et de papier par exemple et qui donne :

 <img width = "900" height = "300" src = "https://image.noelshack.com/fichiers/2019/16/1/1555323096-capture-d-ecran-2019-04-15-a-12-11-12.png"> 

Ainsi, tels sont les résultats que l'on obtient suite au lancement de notre programme, résultats que nous pouvons encore une fois affiner grâce à une optimisation.

<a name ="tl"></a>
* ## _**Optimisation**_

Le tri sélectif est aujourd’hui un enjeu majeur dans notre société et de plus en plus de pays considèrent primordial la protection de notre environnement. Dans cette optique, nous avons réussi à modéliser ce qui pourrait avoir un impact sur ce phénomène. En effet, nous avons pu constater qu’il est fondamental de trier correctement ses déchets. Lorsque nous jetons nos déchets dans une poubelle, cela influence sur le prochain déchet jeté. D’un autre côté, si chacun triait correctement ses déchets, cela aurait un impact conséquent sur notre environnement. 
Afin de répondre à des problèmes réels sur l’écologie, il est nécessaire de s’améliorer quotidiennement à ce niveau et c’est sur ce principe que nous avons constituer la dernière partie de notre blog. 

Comme vous avez pu constater dans les parties précédentes, il est essentiel de bien trier ses poubelles et de ne pas jeter un déchet dans une mauvaise poubelle, chaque type de déchets a son type de poubelle. 
Ainsi, grâce à une étude approfondie et organisée sur le recyclage, nous avons considérer le fait que l’on pouvait, à partir de probabilités et sur un modèle informatique précis, modéliser le moment le plus opportun au ramassage des poubelles par les éboueurs. 

Nous initialisons à zéro un dictionnaire pour la taille, en centimètre, de chaque de poubelle puis nous tirons aléatoirement une taille de poubelle. On obtient par exemple le dictionnaire suivant :

 <img width = "500" height = "220" src = "https://image.noelshack.com/fichiers/2019/15/7/1555251406-capture-d-ecran-2019-04-14-a-16-15-03.png"> 


Tout au long de notre projet, nous avons suivis le principe suivant : l'éboueur ne ramasse la poubelle que si elle est remplie à plus de 90%. Ceci étant nous pouvons à présent modéliser notre optimisation.

La fonction <code>poubelle_choisie</code> permet de choisir de façon aléatoire un déchet et de le placer dans une des sept poubelles. Si l'on répéte ce phénomène plusieurs fois, on se retrouve avec toutes nos poubelles remplies, certaines plus que d'autres. Ainsi, l'optimisation suivante lance un certain nombre de fois cette fonction même et cela constitue un flux. Grâce à ce flux, on pourra évaluer quel est le moment le plus opportun pour l'éboueur de venir vider les poubelles ou non :

<pre><code>
<span style="color:green">def</span> <span style="color:blue">optimisation_version_final(n)</span>:
   
   <span style="color:blue">#on part du principe que l'eboueur passe chaque entre [100] et [200] par cent.</span>
   epsilon <span style="color:purple">=</span> 100  <span style="color:blue">#on va tester 100 , 200 , 300 ... jusqu'à [5000] cela voudrait dire qu'il passe 2 fois.</span>
   dic_fin <span style="color:purple">=</span> <span style="color:green">dict</span>()
   remet_dico_à_zero() <span style="color:blue">#remet tout à zéro pour pas avoir de problèmes.</span>
   i <span style="color:purple">=</span> <span style="color:green">100</span>
   <span style="color:green">while</span>(epsilon<span style="color:purple"><=</span> n):
  somme_eboueur <span style="color:purple">=</span> <span style="color:green"> 0</span>   <span style="color:blue"># on cherche à évaluer l'efficacité de l'eboueur</span>
     n_flux(10000,epsilon)<span style="color:blue">0#on décide de faire  tourner 10.000 fois pour notre relevé statistique.</span>
  <span style="color:green">for</span> d <span style="color:green">in</span> dict_eboueur:
  somme_eboueur <span style="color:purple">+=</span> dict_eboueur[d]
     dic_fin[i]=somme_eboueur <span style="color:blue"># Nombre de déchet que l'eboueur à jeter.</span>
     i <span style="color:purple">+=</span> 100
     epsilon <span style="color:purple">+=</span> 100
     remet_dico_à_zero()

   <span style="color:green">return</span> dic_fin

</code></pre>



<a name="lol"></a>
* ## _**Interprétation**_

As we explain all along this presentation, ecology is getting more and more important in our lives and its taking a prominent place. 

To help our environment and the futur of our planet, everyone has to take upon themselves and try their best in selective sorting. Indeed, as we saw earlier, there are different types of waste and every waste has its own garbage ; if by mistake you throw out you trash in the wrong garbage you automatically influence the person who will come after to throw his trash. 

Through this idea, the main theme that we wanted to show what can provide a good selective sorting. We show the impact on a larger scale for the garbage men but also the influence when you choose the wrong trash. 

The study we sought to model shows that for a typical waste treatment only slightly more than half are sorted correctly. This modeling proved to be relevant compared to surveys on sorting in France.

Sorting is an insignificant daily gesture that can make a big difference to global warming. Manufacturing consumes more energy than recycling, but also emits more greenhouse gases. Thus, sorting not only reduces greenhouse gas emissions, but also saves natural resources.

Although efforts and progress have been made regarding recycling and sorting in recent years, they are still insufficient compared to the challenges and risks to our planet.

To enable future generations to live in a supportive environment, it is necessary for everyone to start by doing the right things on a daily basis, sorting.
So if everyone would make a small gesture for the environment it would have a big impact on our planet. Just tried not to go wrong. 
