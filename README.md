<p align ="center">
  <img width = "400" height = "400" src = "https://hijab-in.com/wp-content/uploads/2013/09/ecologie.jpg">
</p>
   
 # **SOMMAIRE**

* [Membre du groupe](#ariel)<br/>
* [Pourquoi l'écologie ?](#siv)<br/>
* [Modèle simple](#avi)<br/>
* [Modèle complexe](#lilo)<br/>

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

Ce n'est pas un problème, là est tout l'enjeu de notre projet. Ainsi, nous allons vous présenter deux différents programmes qui modélisent de manière simple et plus complexe, l'intêret du tri sélectif.

Mais alors, quel lien avec la dynamique ?  En nous basant ainsi sur le modèle du tri séléctif et sur l'idée de l'écologie en général, nos deux programmes sont élaborés de sorte à ce qu'ils correspondent à des **sytèmes dynamiques**. En effet, dans ces systèmes, le temps est défini par le nombre de fois où l'on envoie de noveaux déchets dans les différentes poubelles et au niveau microscopique,  on observe la destination de chaque déchet. De cette façon, on évalue de manière macroscopique, le nombre de déchets qui sont bien placés ou pas dans chaque poubelle pour mettre en avant que l'action de chacun influence _**fortement**_ l'avenir de tous.




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

Ainsi, en utilisant le résultat de cette dernière fonction qui à chaque déchet, attribue une destination, nous avons pu coder une autre fonction, <code>nb_dans_poubelle(p,q)</code>, qui présente le nombre de déchet dans chaque poubelle pour 100 déchets. C'est ce qui nous a permis d'écricre la fonction <code>nfoispoubelle(p,q,n)</code> qui, selon un nombre n de tours choisi par l'utilisateur, permet de visualiser le nombre de déchet par tour obtenu grâce à la fonction précédente. Enfin, nous avons programmé un graphique, par la fonction <code>plot_poubelle(M,n)</code> qui, en somme de cette suite de fonctions, permet de se rendre compte de la constance du nombre de déchets par poubelle, bonne et mauvaise, et ce, dû au dictionnaire de probabilités de répartition q, initialisé plus tôt. 

<p align ="center">
  <img width = "800" height = "300" src = "https://image.noelshack.com/fichiers/2019/15/4/1555009279-lilo.png">
</p>

On peut effectivement observer dans le graphique ci dessus, que le nombre de déchets dans la bonne poubelle se situe toujours aux environ de 90 et cela s'exlique du fait que pour chaque tour, 100 déchets sont traités et leur probabilité d'être bien placés est de 0,9. On suit le même raisonnement avec les déchets des mauvaises poubelles avec une probabilités de 0,1.
De ce

Ainsi, après avoir établi notre premier modèle, nous avons décidé d'établir la suite de notre projet en partant du même principe mais ce de manière plus complexifiée et travaillée, qui constitua notre **modèle complexe**.<br/><br/>

 

 
<a name="lilo"></a>
* ## _**Modèle complexe**_

Pour affiner notre projet, nous avons décidé d'établir un modèle complexe qui veut que, non pas deux types de déchéts ne soient traités mais **sept**. Ainsi, nous nous sommes référencés aux sortes de déchéts les plus rencontrées quotidiennement dans le but de préserver un lien de cohérence entre les résultats de notre projet et les conditions de la réalité. En effet, l'écologie étant placée au centre de notre sujet, nous nous devions de respecter au maximum les critères déja existants pour pouvoir possiblement faire avancer cet enjeu environnemental et politique.

De cette manière, en nous basant sur des chiffres de statistiques réelles, nous avons tout d'abord initialisé un dictionnaire rapportant les répartitions des déchets dans les poubelles. Ceci nous a premis par la suite d'établir une base de données quant aux probabilités d'envoi d'un type de déchet ou d'un autre pour chaque flux utilisé par notre programme. Ainsi, nous avons obtenu ce dictionnaire initial : 


  <img width = "550" height = "200" src = "https://image.noelshack.com/fichiers/2019/15/7/1555238545-capture-d-ecran-2019-04-14-a-12-42-07.png">


Néanmoins, pour ce qui est des autres dictionniaires utlies à notre programmes, nous les avons tous initialisés de manière nulle parce que définis plus tard par différentes fonctions. 
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


On initialise ainsi les tailles des poubelles.

On va par la suite remplir ces mêmes poubelles et ce, principalement par la fonction <code>poubelle_choisie(nom_du_dechet,dict_bd, dict_mv)</code>. Cette fonction va modifier et dépendre des paramètres suivants:

* Le déchet choisi à envoyer dans l'une des poubelles, défini par la fonction <code>dechet_choisi</code>.<br/>


* Un aléatoire de propabilité <span style="color:purple">r</span> donc défini entre 0 et 1, au sein de la fonction, utilisé de la façon suivante :
  - s'il est <span style="color:green"><= 0,7</span>, le déchet est mis dans la bonne poubelle qui correspond simplement aux 70% de chances qu'un déchet a d'être bien placé.
  - s'il est <span style="color:red">>0,7</span>, le déchet est mis dans la mauvaise poubelle.
<br/><br/>
  

* De la taille de la poubelle et plus précisément de la fonction <code>change_si_90_dans_la_poubelle</code> qui renvoie un booléen : True si la poubelle est remplie à plus de 90% et False sinon. En effet, si tel est le cas, le déchet qui est préalablement choisi ne sera pas placé dans la bonne poubelle qui correspond à son type mais de façon sûre dans une des poubelles qui ne lui sont pas destinées.<br/>


* De plus, cette fonction modifie les dictionnaires de bons et mauvais déchets par flux et celui des déchets en total. Nous disposons d'ailleurs d'une fonction appelée <code>testeur_bon_fonctionnement_system()</code> qui vérifie effectivement que la somme des valeurs des clés de chaque type de déchets des dictionnaires <span style="color:black">dic_nb_bonne_poub</span> et  <span style="color:black">dic_nb_mauvaise_poub</span> correspond aux valeurs des clés de chaque type de déchet du dictionnaire  <span style="color:black">dictionaire_nombre_dechet</span>.

<pre><code> <span style="color:green">def</span>  <span style="color:blue">poubelle_choisie(nom_du_dechet,dict_bon_dechet,dict_mauvais_dechet)</span>:
    
  
   var <span style="color:purple">=</span> random.random() <span style="color:blue">#Tire un aléatoirement une proba pour savoir le mettre dans la bonne ou pas</span>
    indicateur <span style="color:purple">=</span> change_si_90_dans_la_poubelle(dictionaire_nombre_dechet,nom_du_dechet,dictionaire_taille)
    <span style="color:blue">#On utilise deux dictionnaire non passés en paramètre !</span>
    
   <span style="color:green">if</span> (indicateur <span style="color:purple">==</span> <span style="color:green">True</span>): <span style="color:blue">#Poubelle pour ce déchet à dépasser 90%
        # On le met directement dans la mauvaise poubelle</span>
        dict_mauvais_dechet[nom_du_dechet]<span style="color:purple">+=</span>1
        dictionaire_nombre_dechet[nom_du_dechet]<span style="color:purple">+=</span>1
        
   <span style="color:green">else</span>:<span style="color:blue"> # Poubelle pour ce déchet pas encore à 90% </span>
        if(var<span style="color:purple"><=</span>0.7): <span style="color:blue"># 70% de le mettre dans la bonne et 30% de la mettre dans la mauvaise</span>
            dict_bon_dechet[nom_du_dechet]<span style="color:purple">+=</span>1
            dictionaire_nombre_dechet[nom_du_dechet]<span style="color:purple">+=</span>1

            
   <span style="color:green">else</span>: <span style="color:blue"># On le met dans la mauvaise poubelle 30% de la mauvaise. </span>
            dict_mauvais_dechet[nom_du_dechet]<span style="color:purple">+=</span>1
            dictionaire_nombre_dechet[nom_du_dechet]<span style="color:purple">+=</span>1

  <span style="color:green">return</span>
    
</code></pre>
<br/>

Par la suite, 



<a name="lol"></a>
* ## _**Interprétation et optimisation**_

L’étude que nous avons cherchée à modéliser montre que pour un traitement typique des déchets seulement un peu plus de la moitié sont  triés correctement. Cette modélisation s’est montrée pertinente par rapport aux enquêtes sur le tri sélectif en France.

Le tri sélectif est un geste anodin du quotidien qui peut apporter une grande différence à l’échelle du réchauffement climatique. Fabriquer consomme plus d’énergie que recycler, mais émet aussi plus de gaz à effet de serre. Ainsi, trier permet non seulement de réduire les émissions de gaz à effets de serres, mais permet aussi d’économiser les ressources naturelles.

Bien que des efforts et des progrès soient apparues en ce qui concerne le recyclage et le tri sélectif depuis quelques années, ils sont encore insuffisant comparés aux enjeux et risques encourus par notre planète.
Pour permettre aux futures générations de vivre dans un environnement propice, il est nécessaire pour chacun de commencer par faire les bons gestes au quotidien, trier.
