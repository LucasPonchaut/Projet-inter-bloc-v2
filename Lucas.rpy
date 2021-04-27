label invertebre_marin_carnivore:
    play music "audio/P1mc.mp3" noloop
    n "Tu as donc décidé de continuer ton aventure avec les potentiels futurs super prédateurs des eaux troubles de l’archipel."
    play music "audio/P2mc.mp3" noloop
    n "Pour en arriver là il a fallu du temps, de plus ce résultat est le fruit d’une sélection sexuelle parfaitement effectuée."
    play music "audio/P3mc.mp3" noloop
    n "Dans la nature il existe plusieurs critères de sélection, dans ce mécanisme les individus répondant le plus aux critères exigés auront tendance à plus transmettre leurs gènes aux générations suivantes." 
    play music "audio/P4mc.mp3" noloop
    n "Et ainsi de suite jusqu’à ce que le critère sélectionné soit si amplifié qu’on ne retrouvera plus que lui (ou du moins il sera très dominant) parmi notre population jusqu’à ce que les critères changent à nouveaux."
 #(Image de la planète avec un représentant de chacun des 2 milieux aquatiques)

#MISTER ADN QUEL BG  
    
    m "Cette population d'iliaqus asichinus devenue carnivore après quelques millions d’années d’adaptation/d’évolution, a développé une structure spécifique selon sa faune locale."
    
    m "C’est-à-dire que la bestiole s'est adaptée à son environnement, lui permettant ainsi d’être mieux accommodé aux conditions de son habitat."
    
    m "Tu sais donc maintenant que ces carnivores selon qu’ils se retrouvent vers l’océan Iliaque ou bien vers l’océan Agressif, ont une adaptation morphologique différente. La bestiole se retrouve donc à 2 endroits différents de HERMITEON-1."

#(iliaqus asichinus dans océan Indien)(+ possible zoom sur coupe de l’animal pour voir la couche entre l’exosquelette et les organes de l’animal)
    play music "audio/P5mc.mp3" noloop
    n "Mais, à l’origine la bestiole se trouvait dans l’océan Iliaque et avait développé dans ce dernier un exosquelette lui permettant de protéger ses organes des potentiels ultra-prédateurs. Ce n’est qu’il y a une centaine de millions d’années qu’une nouvelle structure s'est créée."

#(animal 1 un peu dodus + animal 1 qui mangent l’ensemble des proies)
    play music "audio/P6mc.mp3" noloop
    n "Et pourquoi me diras-tu ? la raison est simple."
    play music "audio/P7mc.mp3" noloop
    n "En fait, ces carnivores étaient des super prédateurs très gourmands, ce qui leur a causé du tort car ces derniers avaient mangé l’entièreté de leurs captures en un temps-record." 
    play music "audio/P8mc.mp3" noloop
    n "Cela n'a pas permis à leurs proies les Protodarius de se reproduire afin d’engendrer une descendance qui aurait pu servir de nourriture à ces iliaqus asichinus."

#(zoom sur estomac d’iliaqus asichinus avant et après avoir tous mangé)(Quelque iliaqus asichinus mort)
    play music "audio/P9mc.mp3" noloop
    n "En manque de nourriture, une partie de la population se déplaçait et migrait petit à petit vers l’océan Agressif, là où leurs nourritures y étaient abondantes."
    play music "audio/P10mc.mp3" noloop
    n "Tandis que l’autre partie de la population restait dans l’océan Iliaque, ce qui a permis à cette population de réduire considérablement la taille de leur estomac dû au manque de nourriture et ainsi d’avoir la capacité de jeûner pendant plusieurs jours." 
    play music "audio/P11mc.mp3" noloop
    n "Mais uniquement pour les bestioles qui ont survécu grâce à cette nouvelle adaptation."

#(trombe marine dans l’océan Iliaque + proie à l’intérieur de celle-ci)
    play music "audio/P12mc.mp3" noloop
    n "De plus, un événement est venu perturber leur environnement. Il s’agissait d’une trombe marine. Mais en quoi la trombe marine est-elle un perturbateur environnemental pour ces iliaqus asichinus vivant dans l’océan Iliaque ?"
    play music "audio/P12.5mc.mp3" noloop
    n "En fait, la trombe marine a aspiré les Protodarius de ces iliaqus asichinus hors de l’eau jusque dans les nuages, mais malheureusement selon le temps passé dans l’atmosphère certaines de ces proies sont mortes."
    play music "audio/P13mc.mp3" noloop
    n "Cette trombe marine s’est déplacée jusque dans l’océan Agressif, ce qui a permis un enrichissement en Protodarius pour cet océan et par effet inverse, à appauvri l’océan Iliaque."

#(perte de l’exosquelette + mise en place d’un nouvel) si pas trop compliqué à dessiner
    play music "audio/P14mc.mp3" noloop
    n "La migration de la population en quête de nourriture se fit sur plusieurs centaines de milliers d’années, ce qui a causé la perte de l’exosquelette de la bestiole comme celle-ci grandissait (la taille de l’exosquelette n’était plus adaptée à la bestiole)."
    play music "audio/P15mc.mp3" noloop
    n "Du coup, forcément lorsque la bestiole est « nue » elle est vulnérable à toute attaque."
    play music "audio/P17mc.mp3" noloop
    n "Mais ne vous inquiétez, lors de leur quête elle retrouvera une coquille dans laquelle elle se glissera et sera de nouveau protégée, mais uniquement pour les bestioles ayant été les plus vives, car bien que vivant en groupe ces bestioles n’ont pas de craintes concernant leurs propres protections."
    play music "audio/P18mc.mp3" noloop
    n "Plusieurs centaines d’années passèrent..." #horloge qui tourne
    play music "audio/P19mc.mp3" noloop
    n "Une partie de la population vivant dans l'océan Agressif développèrent une structure différente à celle de l’océan Iliaque dû au fait que dans l’océan Agressif, les conditions météorologiques sont telles que le déplacement de la bestiole est freiné par la force qu’exerce le vent dans l’océan."

#(agressivus asichinus qui lutte contre les courants marins)
    play music "audio/P20mc.mp3" noloop
    n "Ces bestioles développeront donc au fil des générations une coquille interne lui permettant de contrer cette force due au vent et ainsi se déplacer plutôt librement dans l’eau."
    play music "audio/P21mc.mp3" noloop
    menu:
        n "Qui voulez-vous suivre ? les individus possédants un exosquelette leur permettant de protéger leurs organes et ayant la capacité de jeûne ou les individus possédants une coquille interne permettant de contrer la force due aux courants marins mais pouvant manger quand ils le souhaitent."

        "Avec exosquelette":
            jump marin_carnivore_exosquelette
        "Sans exosquelette":
            
            n "Woww très bon choix, je ressens en toi une âme de petit scientifique !"

    n "La population ayant ces adaptations a un avantage sélectif sur la population vivant dans l’océan Iliaque, car celle-ci se nourrit suivant son besoin et permet de se développer."

    n "Donc celle ayant les meilleures intégrations à son environnement aura d’autant plus tendance à se reproduire et à engendrer une descendance."

#DIRIGER VERS TEXTE FINAL

    #jump TF
    return

label marin_carnivore_exosquelette:

#(Extinction de l’espèce) (océan Indien sans vie)

    n "Malheureusement pour toi, cette population n’a pas pu survivre à toutes ces adaptations. La raison en est, que la population a été soumise à la sélection naturelle." 
    
    n "Tiens, sais-tu ce qu’est la sélection naturelle ?" 
    
    n "En fait, il s'agit l'un des mécanismes principal de l'évolution expliquant le succès reproductif des individus d'une espèce ainsi que le succès des gènes au sein d'une population." 

    n "Alors, la population vivant dans l’océan Agressif a un avantage sélectif, c’est-à-dire qu’ au fur et à mesure du temps, elle a développé une partie de sa capacitée cérébrale lui permettant de se déplacer vers d' autre étendue d’eau afin de se nourrir."

    n "Tandis que la population se trouvant dans l’océan Iliaque, a un désavantage, c’est-à-dire qu'en manque de nourriture, ces derniers n’ont pas pu se développer suffisamment pour engendrer une descendance."

#DIRIGER VERS TEXTE FINAL

    #jump TF
    #return

label invertebre_terrestre:

#(Vidéo d’une plage avec sable vert si possible) 
    
    n "Depuis plus d’un million d’années notre nouvelle espèce, les Strongis-rius et leurs descendants vivent paisiblement sur une plage de sable vert où ils ont un régime alimentaire varié."

    n "Ils n’ont pas vraiment de mode de chasse, ce sont des poubelles de plage, ils mangent aussi bien de petits mollusques terrestres immobiles que des algues ou d’autres petits animaux marins échouées."

    n "Au cours des générations on observe une distinction physique dans l’espèce."

#Image de notre bestiole ronde et allongé avec la bouche ouverte où on voit bien ses dents comme les sangsues sur la plage

    n "Notre population ne se caractérise pas spécialement par sa forme, certains individus sont plus allongés alors que d’autres sont un peu plus arrondis tout en restant « difforme »."

    n "Cela est permis par une absence de structure rigides dans leur corps mise à part dans leur bouche où on peut retrouver plusieurs rangées de dents en cercle concentrique."

#« Image de l’arrivée d’une troupe de crabes araignées avec des pinces de mante religieuse (mantis-crabus) sur la plage avec une tornade en fond »

    n "Des giga-tempêtes entrainent régulièrement le naufrage de plusieurs baleines volcaniques sur les plages de l’île. Des tornades de mauvais présage vont aussi laisser derrière elles des mantis-crabus sur la plage."

    n "Cette arrivée va troubler et mettre en danger la vie de nos petits strongis-rius car malheureusement ces crabes sont très voraces et nouvellement friand de leur viande moelleuse."

    n "Dans notre population de strongis-rius les plus allongés sont avantagés sur les arrondis car leur forme leur permet de s’ensevelir d’une certaine couche de sable pour se cacher de leur nouveau prédateur."

    n "Les arrondis  quant à eux sont très mauvais à cache-cache et ne parviennent pas à se cacher ou à s’enfuir dans le sable et donc ils arrivent rarement à échapper à ces mantis."

    n "Au cours des générations la population des strongis-rius arrondis va grandement diminuer sauf en périphérie de la forêt car les mantis ne s’aventurent pas aussi loin sinon ils meurent déshydratés, en effet ils doivent retourner dans l’eau pour survivre ce qui donne un avantage aux strongis."

    n "Pour les allongés la vie suit son cours ils restent sur la plage en sécurité dans le sable même si parfois les crabes arrivent à creuser et trouver les individus qui ne sont pas enfui assez profondément."

    menu:
        n "Qui voulez-vous suivre ?"

        "La population de strongis-rius allongé sur la plage":
            jump allongé
        "La population arrondie en périphérie de la forêt":

#MISTER ADN LE SEUL ET UNIQUE
            m "Vous avez décidé de poursuivre votre aventure avec la population d’arrondis en périphérie de la forêt."

    m "Au cours des générations la population d’arrondis sur la plage s’est faite complétement décimée alors que près de la forêt ils prospèrent."

    m "Ayant une alimentation variée (5 fruits et légumes par jours, mangez ni trop gras ni trop sucré ni trop salé) ils n’ont pas eu de mal à s’adapter et à se nourrir près et dans la forêt, grâce à ça ils n’ont pas de difficulté pour vivre et se reproduire dans ce nouvel environnement."

#SCENARIO STRONGIS ARRONDI
#(Image d’Assimilus Strongis, une boulette de viande visqueuse dans la forêt)

    n "Vous continuez votre découverte de l’évolution en suivant les descendants strongis-rius arrondis à la fin de leur adaptation dans la forêt plusieurs millions d’années après leur extinction sur la plage."

    n "Ce sont des créatures uniques qui subviennent à leur besoin nutritif en assimilant d’autres animaux. À chaque assimilation la taille de la boulette va augmenter jusqu’à atteindre une taille critique dans le but d’imploser et de se diviser en plein de boulettes."

    n "Ce mode de reproduction asexuée va leur permettre de s’étendre à grande vitesse sur l’archipel."

#MISTER ADN DANS SA GRANDE SPLENDEUR

    m "La reproduction asexuée est un mode de reproduction qui ne nécessite pas de partenaire pour avoir une descendance que l’ont peu assimiler à des clones en tout point."

    m "D’une certaine manière c’est avantageux car si notre individu est bien portant et dans des conditions idéales, il n’aura pas de mal à se reproduire mais faut savoir qu’ils seront vulanirables aux maladies à cause de leur similarité génétique."

    m "Ayant un mode de vie très solitaire les individus capables de se reproduire seules sont plus avantagés que les autres et aux cours des générations nous allons retrouver que des modes de reproduction asexuée car les autres sont morts sans trouver de partenaire."

#(image d’un paysage avec des grottes dans la forêt)

    n "Après plusieurs milliers d’années notre nouvelle population d’assimilus-strongis s’est dispersée à travers toutes la zone boisée de l’archipel."

    n "Toujours en quête de proies à assimiler, au fil du temps, de plus en plus de ces créatures se retrouvent dans des réseaux de grottes et tunnels souterrains où un tout nouvel écosystème s’étaient développer au cours des millions d’années à l’insu de tous."

    menu:
        n "Qui voulez-vous suivre ?"

        "La population souterraine":
            jump souterrain
        "La population des forêts":
        
            n "Vous avez décidé de suivre la population des forêts malheureusement les explosions de “baleine de lave” ont détruit toute vie et la lave ce qui va provoquer l’extinction de l’espèce dans les forêts ils n’ont pas survécu aux coulées de lave, aux chaleurs extrêmes et aux incendies."

    n "Un destin tragique mais inévitable."

    n "Toutefois ceux qui se sont dirigés vers les souterrains, eux, s’en sont sortis et continuent à se développer."

    #jump TF
    return

label souterrain:

    n "Vous avez décidé de suivre la population souterraine, les explosions de “baleine de lave” ont détruit toute vie à la surface avec leurs souffles et la lave."

    n "Cela ne laissant d’autre choix que de rester dans les souterrains de l’archipel où ils ont assez de victimes à assimiler pour se reproduire."

    n "Cet écosystème est un refuge où les assimilus-strongis ont pu prospérer à l’abri des coulées de lave."

    #jump TF
    return