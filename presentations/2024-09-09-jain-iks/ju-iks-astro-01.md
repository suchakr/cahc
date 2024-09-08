---
marp: true
size: 4:3
footer: "Ancient Indian Astronomy - Jain University IKS - 2024-09-09"

theme: gaia
paginate: true
# backgroundColor: #fff
# backgroundImage: url('https://marp.app/assets/hero-background.jpg')


style : |
    table { margin-left: auto; margin-right: auto; }
    { font-size: 100%} 
    h1:first-of-type { color: blue; font-size: 400%; font-weight: bold; text-align: center; }
    h2:first-of-type { color: purple; font-size: 250%; font-weight: bold; text-align: center; margin-top: -30px; }
    # body { counter-reset: h1; }
    # h1 { counter-reset: h2 }
    # h2 { counter-reset: h3 }
    # h3 { counter-reset: h4 }
    # h1:before, h2:before, h3:before, h4:before { color: purple; font-size: smaller; font-weight: bold}
    # h1:before { counter-increment: h1; /* content: counter(h1) " " */  }
    # h2:before { counter-increment: h2; content: counter(h2) " " ;  }
    # h3:before { counter-increment: h3; content: counter(h2) "." counter(h3) " " ;  }
    # h4:before { counter-increment: h4; content: counter(h2) "." counter(h3) "." counter(h4) " "  }

    h1, h2, h3, h4 { font-weight: bold;  font-size: 225%; }
    footer { position: absolute; bottom: -20px;  }

    h1 em { opacity:60% ; font-size: 80%; } 
    h1 em { display: block; margin-top: -15px; margin-bottom: 20px; font-weight: normal; font-style:normal;  }
    h1 + h1 { font-size: 40px;  text-align: center; margin-top: 250px;  color: blue; border: 10px solid gray; }


---
<style scoped>
    h2  { display: block; margin-top: 20px; margin-bottom: 0px; font-weight: normal; font-style:normal;  font-size: 150%; }
</style>


# Indian Astronomy  *through* Observations *from* Ancient Periods

## Jain University / Sep 2024  <br><br> Sunder Chakravarty , CAHC, Jain University


---
<style scoped>
    table { font-size: 20px;  width: 100%; }  
    td:nth-child(1) { color: blue ; font-weight: bold; text-align: center; }
    th:nth-child(3) { display: none; }
    td:nth-child(3) { display: none; }
    th:nth-child(4) { display: none; }
    td:nth-child(4) { display: none; }
    h2 em { scale: .6; margin-top: 0px; display:block; }
    tr:nth-child(1) { background-color: lightgray;}
    tr:nth-child(6) { background-color: lightgray;}
</style>

## Outline of the talk *(~15 slides in ~60 minutes)*

|Topic|Info|Slides|Minutes|
|--|:--:|--:|--:|
|| **Lecture 1** |---|---|
|Objects | Sun, Moon, Stars, Nakṣatras, Grahas(planets), etc  | 2| 10|
| Sun's Rhythms | Ahorātrā(day), Ayana, Ṛtu(seasons), Samvatsara(year) | 6| 30|
| Rhythms of Nakṣatras and Stars | Ecliptic , Ecliptic Stars, Fixed Dhruva and the Slow Drift of Dhruva | 6| 30|
| Stellarium on Phone and PC | Observing the sky digitally | 2| 10|
|| **Lecture 2** |---|---|
| Moon's Rhythms | Tithi, Pakṣa(fortnight), Māsa(month), Lunar Eclipse | 6| 30|
| Rhythms of Grahas | Visibility, Vakra(Retrograde), Prograde,  | 6| 30|
| Eclipse and their Rhythms | Solar, Lunar | 6 | 30 |
| Calendar Systems | Lunar, Solar, Luni-Solar | 6| 30|

---

## What the Ancients Observed

<style scoped>
    table { font-size: 20px;  width: 100%; }
    td:nth-child(1) { width: 15%; color: blue ; font-weight: bold; text-align: center; }
    td:nth-child(2) { width: 15%; }
    em { color: maroon; font-size: larger; } 
    h3 { font-size: 150%  }
</style> 

||||
|:--|:--|--|
|**पृथिवि** | **Earth**| Where we are firmly grounded
|||Contains rivers, mountains, plants, animals, people etc
|**आकाशः / द्यौः**| **Sky**| the *sun* dominates during daytime, <br> creating *dawn*, *dusk*, *seasons* 
|||the *moon* waxes and wanes in cycles night over night <br> creating *phases*
|||the *stars* emerge in the night <br>forming *recognizable patterns*
|**अन्तरिक्षः** |**Space-in-between**|the *clouds* exists bringing *rains*
|||the *meteors* shower through <br> occasionally bringing *disasters*

### *Astronomy* is a result of these **observations** and ponderings, started by the ancients and continually refined since.

---

## Purpose of these Observations
<style scoped>
    li { font-size: 25px;  margin-left: -25px; }
    li li { font-size: smaller;  margin-left: -25px; }
    em { color: maroon; font-size: larger; } 
    /* li li::before { content: "•"; color: blue; margin-left: -35px; } */

    li li:nth-child(-n+6) { color:green }
    li li:nth-child(n+6) { color:blue }
    p { font-size: 21px; font-family: monospace; }
    p:nth-child(3) { margin-top: 30px; color: green; }
    p:nth-child(4) { margin-top: 0px; color:blue; }


</style>
1. Pursue *curiosity*
2. Answer *questions* like
   1. Where will the sun rise tomorrow
   1. What will be the moon’s phase tomorrow
   1. How many days hence is the next full moon
   1. How many days to the next rainy period
   1. When to sow seeds
   1. What is my birth nakshatra
   1. How does my birth nakshatra affect me
   1. How will the faded sun/moon impact the ruler/people
   1. When, what and whom to offer to adduce desired outcome
   
The greens need observation and calculation - *Astronomy*

The blues need additional interpretation  - *Astrology*


---

#
# Sun's rhythms - ayanas, ṛtus, nakṣatras, drift of ṛtus

---
<style scoped>
    table { align:left; font-size: 23px; }
    /* color cells alternately */
    tr:nth-child(odd) td:nth-child(odd) { background-color: lightyellow; }
    tr:nth-child(odd) td:nth-child(even) { background-color: lightgray; }

    tr:nth-child(even) td:nth-child(odd) { background-color: lightgray; }
    tr:nth-child(even) td:nth-child(even) { background-color: lightyellow; }

    em { color: maroon; font-size: larger ; }
    strong { color: blue; font-size: larger ; font-style: italic; font-weight: normal; }
    h2 strong { color: black; font-size: smaller ; font-style: italic; font-weight: normal; }

</style>

## *Few Sun names - various qualities* <br> **(some qualities observed, others inferred)**

||||||
|:-:|:-:|:-:|:-:|:-:|
सूरः | *सूर्यः* | अर्यमा | *आदित्यः* | द्वादशात्मा |
*दिवाकरः* | भास्करः | अहस्करः | ब्रध्नः |*प्रभाकरः* |
विभाकरः | भास्वान् | विवस्वान् | सप्ताश्वः | **हरिदश्वः** |
**उष्णरश्मि** | विकर्तनः | अर्कः | मार्तण्डः | मिहिरः |
*अरुणः* | पूषः | **द्युमणिः** | तरणिः | मित्रः |
चित्रभानुः | विरोचनः | विभावसुः | **ग्रहपतिः** | त्विषाम्पतिः |
**अहर्पतिः** | भानुः | हंसः | **सहस्रांशुः** | तपनः |
सवितृ | *रविः* | पद्माक्षः | तेजसांराशिः | **छायानाथः** |
तमिस्रहन् | कर्मसाक्षी | **जगच्चक्षुः** | लोकबन्धुः | त्रयीतनुः |
प्रद्योतनः | दिनमणिः | खद्योतः | लोकबान्धवः | ज्योतिष्मान् |


---

<style scoped>
    /* place text at the bottom of the slide */

    table +  p img {
        margin-top: -10px;  margin-left: -10px;
        transform: scaleX(1.025) scaleY(1);
 
    }

    table + p  + p img {
        margin-left:-250px; margin-top: -250px; margin-bottom: -230px; 
        transform: scaleX(.65) scaleY(.35);
        filter: invert(100%);
    }

    table { font-size: 14px;  width: 100%; text-align: center; margin-left:-20px}
    table:nth-child(2) th { display: none; border: 0px }
    table:nth-child(2)  { margin-bottom: -5px; }
    em { color: maroon; text-decoration: line-through; text-decoration-style: double; text-decoration-color: rgb(128,0,0,.6);}

    h2 { margin-top: -70px; margin-bottom: -10px;  }
    /* place text at the bottom of the slide */
</style>


## [Observing the Sun's rhythmns](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/00_sun_rise_swings_with_naks.mp4)


||
|--|
|The **Sun** rises in the _east_  **eastern horizon** and sets in the _west_ **western horizon**|




  
|Season|Sunrise|Sunset|
|-|-|-|
End-Summer| **north**-eastern horizon|  **north**-western horizon|
Mid-Spring/Autumn| **exact** east| **exact** west|
Start-Winter| **south**-eastern horizon|  **south**-western horizon|

![](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/00_sun-rise-swings.jpg)

![](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/00_sun_rise_swings_with_naks.gif)


---

<style scoped>
    {
        /* transform:  scale(1) rotate(0deg) translate(0%, 0%); */
        border: 10px solid gray; border-radius: 10px;
    }
    li { font-size: 18px;  margin-left: -80px; }
    img:nth-child(1) { 
        margin-top:-60px; margin-left:-140px;  margin-bottom: -60px;
        scale: 0.7;
     }
     h2 { margin-top: -50px; margin-left: -50px; }
</style>
![bg fit right:60% ](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/00_sun-path-movie.gif)
## [Annual Sunpath ](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/00_sun-path-movie.mp4)
![img](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/00_sun-path.jpg)

- Video of ~2 minutes shows
- Sun's daily path for few evenly spaced days through the year
- The contrast between the summer and winter paths can be seen
- The contrast between the Bangalore and Kurukshetra paths can be seen

---

<style scoped>
    
    table  { font-size: 17px;  width: 100%; text-align: center; margin-left:-20px}
    td:nth-child(1) { color: navy ; font-weight: bold; text-align: center; }
    td:nth-child(2) { color: blue ; font-weight: xbold; text-align: center; }

    h2 { margin-top: -60px; margin-bottom: 10px;  }
    li { font-size: 20px;  margin-left: -30px; }
    /* place text at the bottom of the slide */
</style>

## A Clock with more features - The Celestial Clock

- The sky is a hemisphere above us
- Stars are painted on the sky
- A band of stars around the east-west arc is the ecliptic
- The ecliptic can be thought of as the dial of a clock
- The stars on the ecliptic are the nakṣatra-s - much like the numbers on a clock
- The sun, moon and gruhas moves along the ecliptic - like hand tips on a clock

|Alarm Clock| Celestial Clock|
|:-:|:-|
|Dial| **Ecliptic**|
|Numbers| **Nakṣatra-s**|
|Hands| Sun, Moon, Gruhas|
|Slow Hour Hand| **Sun** Annual run clockwise|
|Fast Minute Hand| **Moon** Monthly run clockwise <br> Cycling through it phase about every month |
|~ no equivalent ~| **Gruhas** travelling different speeds <br> going anticlockwise sometimes <br> going invisible sometimes|
|~ no equivalent ~| **Precession** <br> The dial itself rotates anticlockwise very very slowly |

---

<style scoped>
{
    transform:  scale(.9) rotate(1deg) translate(0%, 0%) ;
    /* transform:  scale(.9) skew(-10deg, -10deg) translate(0%, 0%) ; */
    opacity: 0.9;
    border: 1px dashed red;
    transition: all 1s;
}
</style>

## Sun and Nakṣatras

We noted that each of the 366 sunrises occurs at different points on the eastern horizon due to the sun's swing. In addition, the stars that are visible just prior to each sunrise at the sunrise point also change. The stars that are visible just prior to sunrise are said to belong to the solar nakṣatra of that day.  

*A nakṣatra is a span of time of about 14 days for the sun*, and contains the stars that are visible at sunrise in its time span. There are 27 such equal nakṣatra spans in a 366 day cycle.

Each of the 27 nakṣtra while of equal time span contains varying counts of stars -  between 1 and 6 - totaling 83 stars. *A nakṣatra is therefore a span of space in the sky as well.*

The *27 nakṣatras* are named in a fixed cyclical order. The current order starting from Aśvinī along with their star count listed below, is an inherited order from around 1500 years ago. The order of the nakṣatra begins with Kṛttikā and ends with Bharanī in more ancient texts.

<style scoped>
    p { font-size: 13.8px; }
    table td {
        border: 1px dotted black;
        text-align: center;
        font-weight: bold;
        color: black;
        width: 14%;
        position: relative;
    }

    #never
    , table tr:nth-child(1) td:nth-child(6)
    , table tr:nth-child(1) td:nth-child(8)
    , table tr:nth-child(2) td:nth-child(5)
    , table tr:nth-child(2) td:nth-child(6)
    , table tr:nth-child(3) td:nth-child(6)
    , table tr:nth-child(3) td:nth-child(9)
    { background-color: rgba(127,127,255,0.1); font-size: 11px; }

    #never
    , table tr:nth-child(1) td:nth-child(7)
    , table tr:nth-child(2) td:nth-child(2)
    , table tr:nth-child(2) td:nth-child(3)
    , table tr:nth-child(2) td:nth-child(7)
    , table tr:nth-child(3) td:nth-child(7)
    , table tr:nth-child(3) td:nth-child(8)
    { background-color: rgba(127,127,255,0.3); font-size: 12px; }

    #never
    , table tr:nth-child(1) td:nth-child(1)
    , table tr:nth-child(1) td:nth-child(2)
    , table tr:nth-child(1) td:nth-child(5)
    , table tr:nth-child(2) td:nth-child(9)
    , table tr:nth-child(3) td:nth-child(4)
    { background-color: rgba(127,127,255,0.5); font-size: 13px; }

    #never
    , table tr:nth-child(2) td:nth-child(8)
    , table tr:nth-child(3) td:nth-child(1)
    , table tr:nth-child(3) td:nth-child(2)
    , table tr:nth-child(3) td:nth-child(3)
    , table tr:nth-child(3) td:nth-child(5)
    { background-color: rgba(127,127,255,0.6); font-size: 14px; }


    #never
    , table tr:nth-child(1) td:nth-child(4)
    , table tr:nth-child(2) td:nth-child(4)
    { background-color: rgba(127,127,255,0.8); font-size: 15px; }
    
    #never
    , table tr:nth-child(1) td:nth-child(3)
    , table tr:nth-child(1) td:nth-child(9)
    , table tr:nth-child(2) td:nth-child(1)
    { background-color: rgba(127,127,255,1); font-size: 16px; }

</style>


||||||||||
|--|--|--|--|--|--|--|--|--|
|Aśvinī<br>3|Bharaṇī<br>3|Kṛttikā<br>6|Rohiṇī<br>5|Mṛgaśiras<br>3|Ārdrā<br>1|Punarvasu<br>2|Puṣya<br>1|Aśleṣā<br>6|
|Maghā<br>6|Pūrva<br>Phalgunī<br>2|Uttara<br>Phalgunī<br>2|Hasta<br>5|Citrā<br>1|Svātī<br>1|Viśākhā<br>2|Anurādhā<br>4|Jyeṣṭhā<br>3|
|Mūla<br>4|Pūrva<br>Aṣāḍhā<br>4|Uttara<br>Aṣāḍhā<br>4|Śravaṇa<br>3|Śraviṣṭhā<br>4|Śatabhiṣā<br>1|Pūrva<br>Bhādrapadā<br>2|Uttara<br>Bhādrapadā<br>2|Revatī<br>1|:


The choice of the first nakṣatra to start the cycle contains information on the epoch and the convention for the year start.

There are texts that associate specific nakṣatras with the ṛtus - seasonal naḳsatras .  Such seasonal naḳsatras also contain vital information on the epoch of the text.

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    li { font-size: 20px;  margin-left: -30px; }
</style>

![bg fit right:60% ](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/01_sun-transit-basics-movie.gif)
## [The Sun, Ṛtus and Nakṣatras](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/01_sun-transit-basics-movie.mp4)
- Video of ~1½ minutes shows
- **Per year sun covers**
  - 2 ayanas 
  - 6 ṛtu-s
  - 27 nakṣatra-s
  - Rtu-s & nakṣatra-s are associated

- **Over millenia**, 
  - the nakṣatra-s drift slowly due to precession  
  - This change is used to date the ancient texts

---
<style scoped>
    
    p { font-size: 17px;  margin-left: 20px; margin-bottom:-20px }
    li { font-size: 17px;  margin-left: 20px; color: blue; margin-top: -4px; }
    h2 { margin-top: -65px; margin-bottom: -10px; }
    h3 { font-size: 150%; margin-top: -15px; margin-bottom: -15px; }
    h3:nth-child(n+9) { color: purple;  font-style: italic;  margin-top: -10px; }
    em { color: maroon; font-size: 110% ; }
    table { font-size: 15px;  margin-top:-10px; margin-left:40px}
</style>

##  Recap - Sun's rhythms

### Every day
- Sunrises in the east *creating day* 
- Sunsets in the west *ushering night*
- Sunrise and sunset *positions change* daily

### Just before every sunrise
- One can observe *eastern horizon star changes* 

### Every ~14 days
- Sun moves through a *nakṣatra*

### Every ~366 days
Sunrise completes one full swing along the eastern hor
izon 
- A northern swing called *uttaryāṇa* for 183 sunrises
- A southern swing called *dakṣiṇāyana* for 183 sunrises
  
|||
|:-:|:-:|
|Start of uttaryāṇa/dakṣiṇāyana | solstice winter/summer
|Mid of *uttaryāṇa*/dakṣiṇāyana | *equinox spring*/autumn
  
Sun cycles through 
- *6 ṛtu-s* of 61 sunrises each vasanta, grīṣma,  varṣā, śarat, hemanta, śiśira
- *27 nakṣatra-s* -  the  *same eastern horizon star* appears just before sunrise

### Occasionally
- Sun goes partially or fully dark before recovering  - *Eclipse*
  
### Every 1000 years
- The *spring equinox nakṣatra moves backward by one naḳsatra* due to precession
- i.e. **seasons move backward by one naḳsatra**



  
---

## Effect of precession over millennia
<style scoped>
    li { font-size: 14px;} 
    table { font-size: 14px;  width: 100%; text-align: center; margin-left:-20px}
</style>

-   About every *1000 years* the start of *seasons move backward by one naḳsatra*. **In addition the precession causes the pole star to change.**

-   The following table/pictures shows the start of the spring equinox seasonal naḳsatra and the pole star for the last 5000 years.


<style scoped>
    th:nth-child(6) { display: none; }
    td:nth-child(6) { display: none; }
    img { filter: invert(100%); height: 240px; }
    table tr:nth-child(1) td:nth-child(1) img { filter: invert(80%); }
</style>

|Epoch|Spring Equinox|Dakṣiṇāyana|Uttaryāṇa | Pole Star|Image|
|---|---|---|---|---|--|
|Present|Uttara Bhādrapadā|Ārdrā|Mūla|Polaris|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-01-2000-ce.jpg)
|1000 years ago|Revatī|Punarvasu|Pūrva Aṣāḍhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-02-1000-ce.jpg)
|2000 years ago|Aṡvinī|Puṣya|Uttara Aṣāḍhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-03-0000-ce.jpg)
|3000 years ago|Bharanī|Aśleṣā|Śravaṇa|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-04-1000-bce.jpg)
|4000 years ago|Kṛttikā|Maghā|Śraviṣṭhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-05-2000-bce.jpg)
|5000 years ago|Rohiṇī|Pūrva Phalgunī |Śatabhiṣā|Thuban|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-06-3000-bce.jpg)

|||
|:---:|:--:|
|Present Day <br> ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-01-2000-ce.jpg) | 5000 years ago <br> ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-06-3000-bce.jpg)|

---
<style scoped>
    table { font-size: 16px;  width: 100%; text-align: center; margin-left:-20px}

    </style>

## Recall questions
|#|Question|
|:---:|:--|
|1|What is an ayanā?|
|2|How many nakṣatra-s and seasons in one ayanā?|
|3|What is the duration of one ṛtu?|
|4|What is the most pleaseant ṛtu? Which among the four solstices/equinox is it associated with?|
|5|Solsitices means still-sun. Using swing in park/tree analogy, explain why it is so.|
|6|How many times does the sun rise in a year? How many are those are closest to true east?|
|7|What is a nakṣatra? Is it a time span or a space span? How many stars are there in a nakṣatra?|
|8|What is the current start  order of the nakṣatra-s? What is the start order in more ancient texts?|
|9|What is the significance of the first nakṣatra in the cycle?|
|10|How is precession of the equinoxes used to date ancient texts?|
|11|List five names of the sun and their qualities.|
|12|What is the difference between astronomy and astrology as we understand it today?|
|13|What is the significance of the pole star in the sky?|
|14|What is your birth nakṣatra? What does it mean to you?|
|15|What is the significance of the ecliptic in the sky?|
|16|Name a few ancient astronomers and their contributions.|

---

<style scoped>
    h3 { text-align: center; margin-top: 20px; margin-bottom: 20px; }
    </style>

### Stellarium on phone and/or PC  <br> Observing the sky digitally

#
# End of Lecture 1 


---

<style scoped>
    /* place text at the bottom of the slide */
    p { position: absolute; bottom: 60px; width: 100%;  font-size:20px; margin-left: -80px; }
    li { list-style-type: none; }
    
    /* place text at the bottom of the slide */
</style>

## Nakṣatra solar zodiac

![bg fit width 100%](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/sun-moon-season-precession-dial.jpg)
![bg fit width 90%](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-nakshatra-table.png)

- The **Sun** completes one circuit in **366 days** in **clockwise** direction<br><br>
- The **ṛtu-s** complete one circuit in ~**25,800 years** in **anticlockwise** direction

-

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    li { font-size: 16px;  margin-left: -30px; }
</style>

![bg right:60% fit ](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/02_precession-movie.gif)
## [The Drift of the Seasonal Nakṣatras](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/02_precession-movie.mp4)

- Video of ~2½ minutes shows,
- **Over millenia**,
  - the nakṣatra-s drift slowly due to precession  
  - This change is used to date the ancient texts

- **Epochs of Ancient passages using Seasonal Nakṣatra-s**
  - Brahmāṇḍa Purāṇa (BP)
  - Vṛddagārgīya Jyotiṣa (VGJ)
  - Parāśaratantra (PT)
  - Maitrāyaṇīya Āraṇyaka Upaniṣat (MAU)
  - Nidānasūtra (NS)
  - Lagadha Jyotiṣa (LJ)
  - Others ...
  
---
#
# The Maghādi/dakṣināyaṇa epoch  - BP, MAU, NS passages

---
<style scoped>
    p, li {font-size: 20px; color:blue;}
    th { display: none; }
    table td:nth-child(2)  { display:none }
    table td { font-size: 19px; }
    table { margin-left: 25px; font-size: 15px;  margin-top: 30px; }
    th { display: none; }
</style>

## The Maghādi/dakṣināyaṇa epoch

### [Brahmāṇḍa Purāṇa *BP 21.143-149*](https://raw.githubusercontent.com/cahcblr/sanchaya/main/Puranani/brahmanda%20purana.txt)

- This BP passage defines visuvat to be of equal day and night duration of 15 muhūrtas each - equinox - in the mid of vasanta and śarat ṛtus.

- The passage further states the nakṣatra location at an aṃsa grain for equinoctal sun and moon at spring and autumn equinoxes.

- It turns out the sun and moon locus at each of the equinox are diametrically opposite - at 1/4 kṛttikā and  3/4 viśākhā,  indicating the description are of the **equinoctial full moon**. 

|||
|--|--|
| **शरद्वसंतयोर्मध्ये मध्यमां गतिमास्थितः । अतस्तुल्यमहोरात्रं करोति तिमिरापहः ॥** | In *mid autumn and spring* having attained moderate pace, *the sun*, remover of darkness, therefore *makes day and night equal*. 
| हरिताश्च हया दिव्यास्तस्य युक्ता महारथे । अनुलिप्ता इवाभान्ति पद्मरक्तैर्गभस्तिभिः ॥ | The divine yellow horses, yoked to his great chariot, shine like covered with the lotus-red rays.
| मेषान्ते च तुलान्ते च भास्करोदयतः स्मृताः । **मुहूर्त्ता दश पञ्चैव अहो रात्रिश्च तावती** ॥ | The hours of the day and night are each reckoned as ten and five muhūrtas from the rising of the sun at the end of meshā and tulā
| **कृत्तिकानां यदा सूर्यः प्रथमांशगतो भवेत् । विशाखानां तदा ज्ञेयश्चतुर्थांश निशाकरः** ॥  | When the *sun is in the first part of kṛttikā*, know the *moon is in the fourth part of viśākhā*
| **विशाखानां यदा सूर्यश्चरतेंशं तृतीयकम् । तदा चन्द्रं विजानीयात्कृत्तिकाशिरसि स्थितम्** ॥ | When the *sun is in the third part of viśākhā*, know the *moon is in the head of kṛttikā*
| विषुवं तं विजानीयादेवमाहुर्महर्षयः । सूर्येण विषुवं विद्यात्कालं सोमेन लक्षयेत् ॥ | It is then understood to be equinox - so say the maharishis. Equinox is known through the sun and time by the moon
| समा रात्रिरहश्चैव यदा तद्विषुवं भवेत् । तदा दानानि देयानि पितृभ्यो विषुवेषु च ॥ | *When equinox occurs, night and day are equal*. Then during equinoxes offerings are made to piṭṛs 

---
<style scoped>
    li, p {font-size:20px;  color: blue}
    th { display: none; }
    table td:nth-child(2) { display:none }
    table { margin-left:15px;  margin-top: 0px; }
    table td { font-size: 16px; }
    h3:nth-child(1) { margin-top: -50px; margin-bottom: -10px; text-align: left; }
</style>


### [Maitrāyaṇīya Āraṇyaka Upaniṣat *MAU 6.14*](https://github.com/cahcblr/sanchaya/blob/647880cd98978d739d122a9a6b7069a4d56c6f3d/Vedic%20texts/YV/MAU-text.txt#L2)

- The year commences in Maghādi (at dakṣiṇāyana).
- A year has 12 parts and each part has 9 amṣa.
- The year's first half , Āgneya,is from **Maghādi** to Śraviṣṭhārdha and 
- The second half , Vāruṇa, is from Sārpādi to Śraviṣṭhārdha in reverse order.

|||
|--|--|
|सूर्यो योनिः कालस्य तस्य एतद्रूपं । | Sun and Time are contemporaries
|यन्निमेषादि कालात्संभृतं द्वादशात्मकं वत्सरम् । | वत्सरः(year) has 12 parts and <br> is filled with time units starting with निमेषा(eye wink)
|एतस्याग्नेयमर्धमर्धं वारुणम् । | Year's first half is आग्नेयः(Āgneya) and <br>the second half is वारुणः(Varuṇa)
| **मघाद्यं** श्रविष्ठार्धमाग्नेयं क्रमेणोत्क्रमेण सार्पाद्यं श्रविष्ठार्धान्तं सौम्यम् ।  | *Āgneya - from मघादि (Maghā start) to श्रविष्ठार्धः(half of Śraviṣṭhā)* <br> Varuṇa - from सार्पादि(Sārpā start) to श्रविष्ठार्धान्तः(end of half of Śraviṣṭhā) in counter order
|तत्र एकमात्मनो *नवांशकं* सचारकविधम् । | In each part, the Sun traverses 9 amṣa( portions) in order <br>**9 amṣa(portion) for each of the 12 year parts implies each nākshatra has 4 amṣa** 


<!-- <style scoped>
    p,  li {font-size: 20px;}
    table td:nth-child(2) , em { display:none }
    table td { font-size: 30px; }
    th { display: none; }
    table { margin-left: 25px;  margin-top: 30px; }

</style> -->

### [Nidānasūtra  *NS 5.12*](https://archive.org/details/in.ernet.dli.2015.408135/page/n173/mode/2up?view=theater)
- Sun traverses 13 and an additional 5/9 ahorāṭras in each nakṣatra. 
- To cover 27 nakṣatras the sun takes 366 ahorāṭras/days. 

|||
|--|--|
स एष नाक्षत्रः आदित्यसंवत्सरो । *सः एषः नाक्षत्रः आदित्यसंवत्सरः ।* | This is the nakṣatra year of the sun
आदित्यः खलु शश्वदेतावद्भिरहोभिर्नक्षत्राणि समवैति । *आदित्यः खलु शश्वत्  एतावत्भिः अहोर्भिः नक्षात्राणि समवैति ।* | The sun, indeed, with these many days, stays with each nakṣatras
त्रयोदशाहं त्रयोदशाहमेकैकं नक्षत्रमुपतिष्ठति। *त्रयोदशाहं त्रयोदशाहम  एकैकं नक्षत्रम् उपतिष्ठति ।* | The sun spends **13 days** with each nakṣatra  
अहस्तृतीयं च नवधा कृतयोरहोरात्रयोर्द्वे द्वे कले चेति संवत्सराः। *अहः तृतीयं च नवधा कृतयोः अहोरात्रयोः  द्वे द्वे कले चेति संवत्सराः ।* | अहोरात्रि/3 + (2* अहः +  2* रात्रि)/9 =  **5 अहोरात्रि/9**  *13 and 5/9 days with each nakṣatra*
ताश्चत्वारिंशच्चतुःपञ्चाशतं कलाः। *ताः चत्वारिंशत् चतुःपञ्चाशतं कलाः ।* | ???? Those are 40 and/times 54 kalās
ते षण्णववर्गाःसषट्षष्टित्रिशतः ॥ *ते षट् नव वर्गाः सः षट्षष्टिः त्रिशतः ॥* | ???? These are 6*9 vargās and 366

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    li { font-size: 20px;  margin-left: -50px; margin-top: 10px; }
    h2 { scale: .6; margin-top: -80px; margin-left: -50px; }
</style>

![bg right:60% fit](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/05_brahmanda-movie.gif)
## [The **Epoch of Brahmāṇḍa Purāṇa** passages 21.143-149](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/05_brahmanda-movie.mp4)
- Video of ~1½ minutes shows,
- **The BP** verses specify the spring and autumnal equinoctial full moons at 1/4 Kṛttikā and 3/4 Viśākhā nakṣatras. 
- This places these observations to ~1800BCE (± 100 years)
    



---

<style scoped>
    li{font-size: 22px; margin-left: -20px;}
    em { background-color: rgba(255,0,0,0.1); }
</style>

## Nakṣatra Chart 1800BCE (± 100) - Maghādi epoch

- The *equinoctial full moons of BP*
  - ¼ kṛttikā sector
  - ¾ viśākhā sector
  - SE-AE axis of the chart
- *aligns with maghādi of MAU*
  - when maghādi (SS 1) is at 
    - start of dakṣiṇāyana
- *around 1800 BCE (± 100)*

<!-- Computatonally, the alignment is found to be
  - when the visible kṛttikā and viśākhā are 
    - *contained in their respective sectors*
  - when the equinoctial full moon at 
    - ¾ viśākhā sector is 
    - nearest to visible viśākhā -->z
  

![bg fit right 100%](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/daynum-dial-season-fm-1700-bce.jpg)

---


#
# The Śraviṣṭhādi/uttarāyaṇa epoch - VGJ/11 and PT passages

---


## Śraviṣṭhādi/ uttarāyaṇa epoch - VGJ/11 Ādityachāra and Parāśharatantra


<style scoped>
    table { margin-left: -25px; font-size: 12px; width: 120%}
    table td:nth-child(2) { width: 10px; }
    table td:nth-child(3) { width: 10px; }
    table th:nth-child(3) { display: none; }
    table td:nth-child(5) { display: none; }
    li { font-size: 13px; margin-left: -50px}
    h2 { scale: .7; margin-bottom: -40px; }
</style>

- Ādityachāra, section 11 of VGJ, describes the transit of Sun through 9 seasonal nakṣatras . 
- Similar information is presented in PT in prose.
- The Ādityachāra passage is shown below.
- Passage maps 6 ṛtus mapped to 9 seasonal nakṣatras  
- Mapping enables passage dating

|Verse|From|To|Ṛtu|Span|
|:---|:---:|:---:|:---:|:--:|
**श्रविष्ठादीनि** चत्वारि **पौष्णार्धञ्च*** दिवाकरः  ।<br>  वर्धयन् सरसस्तिक्तं मासौ तपति **शैशिरे**  ॥ 47 | श्रविष्ठा begin | रेवती mid | शिशिर | 270°-330° |
**रोहिण्यन्तानि** विचरन् **पौष्णार्धाद्याच्च** भानुमान् ।<br> मासौ तपति **वासन्तौ** कषायं वर्धयन् रसम्॥ 48 | रेवती mid | रोहिणी end | वसन्त|330°-30°|
**सार्पार्धान्तानि** विचरन् **सौम्याद्यानि** तु भानुमान् ।<br> **ग्रैष्मिकौ** तपते मासौ कटुकं वर्धयन् रसम्॥ 52 | मृगशिरा begin | आश्लेषा mid | ग्रीष्म| 30°-90°|
**सावित्रान्तानि** विचरन् **सार्पार्धाद्यानि** भास्करः ।<br> **वार्षिकौ** तपते मासौ रसमम्लं विवर्धयन्॥ 53 |आश्लेषा mid | हस्ता end | वर्षा| 90°-150°|
**चित्रादीन्यथ** चत्वारि **ज्येष्ठार्धञ्च** दिवाकरः।<br> **शारदौ** लवणाख्यं च तपत्याप्याययन् रसम्॥ 54 | चित्रा begin | ज्येष्ठा mid | शरद्|150°-210°|
**ज्येष्ठार्धादीनि** चत्वारि **वैष्णवान्तानि** भास्करः ।<br> **हेमन्ते** तपते मासौ मधुरं वर्धयन् रसम् ॥ 55 | ज्येष्ठा mid | श्रवण end | हेमन्त|210°-270°|

  
![bg fit right:50%](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-adityacara-seasons.png)

---

## Dating Ādityachāra - by minimizing error
<style scoped>
    li { font-size: 22px; margin-left: -20px ; width: 300px; margin-top:10px}
    li li { scale : 0.9;  margin-top: 10px; color: navy;}
    h2 { scale: .8; margin-bottom: 20px; }
</style>

![bg fit right:55%](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-adityacara-charts.png)

- The text specifies 9 **seasonal nakṣatra-s** 
- For each epoch from -2500 to 500 in 50 year steps
  - Measures an **error** of the 9 nakṣatra-s from their prescribed season
  - The epoch with **lowest error** is the best epoch **$\mathbb{B}_{epoch}$**

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    li { font-size: 20px;  margin-left: -20px; margin-top: 20px}
    h2 { scale: .8; width: 110%;}
</style>


![bg right:60% fit](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/04_adityacara-movie.gif)
## [The Epoch of Ādityachāra passages in VGJ & PT ](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/04_adityacara-movie.mp4)
- Video of ~1½ minutes shows,
- **The PT and VGJ** verses that specify 9 seasonal nakṣatras
- This information places these observations to ~1300BCE (± 100 years)

---

#
# The Śravaṇādi/uttarāyaṇa epoch - VGJ/59 Ṛtusvabhāva

---

## The Śravaṇādi epoch  - VGJ/59 Ṛtusvabhāva

<style scoped>
    /* table { margin-left: -25px; font-size: 15px; }
    table td:nth-child(2) { width: 10px; }
    table td:nth-child(3) { width: 10px; }
    table th:nth-child(3) { display: none; }
    table td:nth-child(5) { display: none; }
    img { filter: invert(5%); height: 520px;  position: absolute; transform: translate(56%, -5%); z-index: -1;  border: 0px solid black; } */
    li { font-size:15px; margin-left: -30px ; width: 300px}
    h2 { scale: .8; }
    li:nth-child(2) li:nth-child(3) { color: blue; }
    li:nth-child(3) li:nth-child(2) { color: blue; }
</style>

![bg  fit right:55% ](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/sun-transit-rtusvabhava-charts-rni.jpg)

- Ṛtusvabhāva dates to **~500 BCE**
<br>
- This is different from आदित्यचारः
	- Ṛtu sequence begins with वसन्त not शिशिर
	- Ṛtu are related to months, not  *nakṣatra* span & boundaries
	- A 12 month **solar zodiac**, obviating intercalation, emerges
<br>
- It describes Sun's path through
	- 6 seasons and their months
	- 12  **vaidika** and equivalent **laukika** months and  12  *nakṣatra-s* for each of these months - ~30° apart

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    h2 { scale: .8; align: left; margin-left: -50px; }
    li { font-size: 20px;  margin-left: -50px; margin-top: 20px}
</style>


![bg right:60% fit](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/03_rtusvabhava_movie.gif)
## [The Epoch of VGJ Ṛtusvabhāva passages](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/03_rtusvabhava_movie.mp4)
- Video of ~1½ minutes shows,
- **The VGJ** verse information that specify 12 seasonal nakṣatras
- This information places these observations to ~500BCE (± 100 years)

---

## A chronology of Solar transits  

<style scoped>
   table { font-size: 23px; }
   table td:nth-child(4) { width:23% }
   p { font-size: 32px; }
</style>

|Epoch|Scheme|Start|Season|
|--:|:--:|--:|--|
earlier | **2 Ayana/6 Ṛtu** based sun transit   |
~1800 BCE | **MAU/BP**  Equinoctial full moon scheme | Maghādi |dakṣināyaṇa 
~1300 BCE  | **VGJ/ādityacāra** and **PT**  with *4½ nakṣatra-s* per season | Śraviṣṭhādi |uttarāyaṇa
~500 BCE  | **VGJ/ṛtusvabhāva**  with *12 solar months* | Śravaṇādi<br><br>*Revatyādi<Br>Bharaṇyādi*| uttarāyaṇa<br><br>*vasanta<br>spring equinox*

**Solar zodiac** is certainly part of original Indian knowledge - that has been recorded and evolved over time.

---

# Q & A

## References

<style scoped>
    table { font-size: 14px; }
    strong { float : right; }
    th { display: none; }
    h2 { margin-top: 20px; margin-bottom: -20px; }
    h1 { border: 4px solid rgba(0,0,0,0.1); border-radius: 10px; padding: 10px; }

    tr:nth-child(6) a:nth-child(2) { font-weight: bold; color: brown; }
    tr:nth-child(7) a:nth-child(2) { font-weight: bold; color: brown; }

</style>


|  | |
|---:|---|
1|**Abhyankar, K. D. (1991)**[Misidentification of some Indian nakṣatras. Indian Journal of History of Science, 26(1), 1–10.](https://github.com/suchakr/cahc-utils/blob/main/papers/naks/naks-1991-abyn-misidentified-naks.pdf)
2|**Das P. (2018)** [Bhāgavata Cosmology; Vedic Alternative to Modern Cosmology, Tulsi Books, Mumbai.](https://tulsibooks.com/product/bhagavata-cosmology-vedic-alternative-to-modern-cosmology/)
3|**Gondalekhar, P. (2013)** [The time keepers of the Vedas. Manohar. [ISBN 978-81-7304-969- 9].](https://www.amazon.in/Time-Keepers-Vedas-History-Calendar/dp/8173049696)
4|**Iyengar, R. N. (2013)** [Parāśara Tantra (Ed. Trans & Notes). Jain University Press. [ISBN 978-81-9209-924-8].](https://www.amazon.in/Time-Keepers-Vedas-History-Calendar/dp/8173049696)
5|**Iyengar R.N. (2016)** Astronomy in Vedic texts,(Book Chapter pp.107-169).<br>History of Indian Astronomy A Handbook, (Ed. K.Ramsubramanian, A.Sule &M. Vahia)<br> Publn. by IITB and TIFR, Mumbai.
6|**Iyengar R.N. and <br>Chakravarty, S (2023)** [Equinoctial full moon of the Brahmāṇḍa Purāṇa and the nakṣatra](http://cahc.jainuniversity.ac.in/assets/ijhs/rni-maghadi-2023.pdf)
7|**Iyengar R.N. and <br>Chakravarty, S (2021)** [Transit of sun through the seasonal nakṣatra cycle in the Vṛddha‐Gārgīya Jyotiṣa, Indian Journal of History of Science 56:159–170.](https://github.com/suchakr/cahc-utils/blob/main/papers/vgj/vgj-2022-01-rni-sc-sun-transit.pdf)
8|**Koch D. (2014)** [Astronomical dating of the Mahābhārata war. Erlenbach, Switzerland](https://www.gilgamesh.ch/KochMahabharata6x9_V1.00.pdf)
9|**Sastry T. S. K. (1984)** [Vedāṅga Jyotiṣa of Lagadha. Indian Journal of History of Science, 19 (4), l–74.](https://github.com/suchakr/cahc-utils/blob/main/papers/lvj/lvj-1984-kuppanna.pdf)
10|**Sengupta, P. C. (1947)** [Ancient Indian Chronology. Univ. of Calcutta.](https://indianculture.gov.in/ebooks/ancient-indian-chronology-illustrating-some-most-important-astronomical-methods)
11|**Srinivas M.D. (2019)** [The Untapped Wealth of Manuscripts on Indian Astronomy and Mathematics Indian Journal of History of Science, 54.3, 243-268.](https://www.researchgate.net/profile/M-Srinivas/publication/336438227_The_Untapped_Wealth_of_Manuscripts_on_Indian_Astronomy_and_Mathematics/links/602b2bd94585158939a94482/)
12|**Thompson R. L. (2007)** [The Cosmology of the Bhāgavata Purāṇa (Indian Edn.) Motilal Banarsidass, Delhi.](https://www.motilalbanarsidass.com/products/the-cosmology-of-the-bhagavata-purana-mysteries-of-the-sacred-universe)

---

## Backup Slides from Here

---

<!-- <div class=page-break style="page-break-before:always"></div> <p></p> -->

<style scoped>

{
    transform:  scale(.8) rotate(5deg) translate(0%, 0%);
    opacity: 0.4;
    border: 2px dashed red;
}

h2::after {
    content: "Skip";
    position: absolute;
    top: 0%;
    left: 0%;
    transform: translateY(0%) rotate(-5deg) scale(.5);
    opacity: 0.35;
    font-size: 15em;
}

img { filter: invert(100%); height: 90px; xwidth: 390px; }
{ font-size: 14px;}
table { position: absolute; transform: translate(0%, 0%); z-index: -1;  border: 0px solid black; width: 50% ; }
li { font-size: 16.5px; margin-left: 480px}

li:nth-child(n+3) { color: seagreen}
li:nth-child(n+4) { color: blue}
li:nth-child(n+6) { color: maroon; font-family:monospace; border: 0px solid black; padding: 5px; background-color: rgba(255,0,0,0.1); }
h3 {  margin-bottom: -5px; text-align: center; font-size: 20px; }
h2 { margin-top: -50px; margin-bottom: -10px;  }
</style>



##  [Ayana](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-ayana.gif), Rtu, Nakṣatra, [Precession](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-precession.gif) 


|view of sunrise | surise location|sunrise (day) count|
|--|:--:|:--:|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-01-ss.jpg)| north east|1|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-02-ae.jpg) | true east|92|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-03-ws.jpg) | south east|183|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-04-se.jpg) | true east|274|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-01-ss.jpg) | north east|367 <br><br> 1 of next cycle|

- The sunrise horizon point moves from north east to south east and back to same north east point after 366 sunrises - a solar year.
- The north east to south east journey is called **dakṣiṇāyana** and the reverse is  **uttarāyaṇa**
- In addition the sun cycles through six ṛtu-s in a year - **śiśira, vasanta, grīṣma, varṣā, śarad, hemanta** - each of 61 sunrises.
- Specific background stars can be observed just before each sunrise. These stars are called **nakṣatra-s** , 27 in number.
- Each of the 2 ayana-s and 6 ṛtu-s are associated with specfic nakṣatra-s.
- Over ages this ayana/ṛtu-nakṣatra association changes due to the **precession** phenomenon. 
- This change is used to date the ancient texts.




## Observational Astronomy of the Sun


### Sun, Ayanas and Ṛtus
<style scoped>
   table { font-size: 14px; }
   p { font-size: 14px; }
</style>
An observer noticing the sunrise point of the eastern horizon will notice the point oscillate between north-east in the summer to south-east in the winter and back to north-east in the summer - much like a swing.

The extreme north and south points are the dakṣiṇāyana  and uttarāyaṇa start   - the winter and summer solstices respectively. The points in between are called the viṣuvat - spring and autumn equinoxes.

One full swing of the sun lasts 366 days and is made of two ayanas the dakṣiṇāyana and uttarāyaṇa each of 183 days

In one full swing from uttarāyaṇa, the sun traverses through six ṛtus (seasons) in order -  namely varṣā, śarad, hemanta, śiśira, vasanta, grīṣma,- each ṛtu is of 61 days.

Just as a swing appears to be stationary at the extreme points, the sun appears to be stationary at the uttarāyaṇa and dakṣiṇāyana start points before resuming its oscillation. An observer will notice that the sun is stationary at the uttarāyaṇa and dakṣiṇāyana start points for about 14 sunrises each.

The period from one  sunrise to another is called a ahorāṭra/day. A ṛtu is made of 61 ahorāṭras/days. An ayana is made of 183 ahorāṭras/days.One swing of the sun with 366 ahorāṭras/days is samvatsara/year.

| | ahorāṭra | ṛtu | ayana |samvatsara |
|---|---|---|---|---|
| ahorāṭra| 1 |  |  | |
| ṛtu | 61 | 1 | |  |
| ayana | 183 | 3 | 1 |  |
| samvatsara | 366 | 6 | 2 | 1 |





---
<style scoped>

    {
        transform:  scale(.8) rotate(5deg) translate(0%, 0%);
        opacity: 0.4;
        border: 2px dashed red;
    }

    h2::after {
        content: "Skip";
        position: absolute;
        top: 0%;
        left: 0%;
        transform: translateY(0%) rotate(-5deg) scale(.5);
        opacity: 0.35;
        font-size: 15em;
    }

    li {font-size: 19px; padding-bottom: 14px}
    table th { display: none; }
    em { background-color: rgba(255,0,0,0.1); }
</style>


## From these MAU, NS and BP passages

1. Sun spends *13 and 5/9 days equally* with each naḳsatra of 4 amṣa . The sun completes one trip through the 27 nakṣatras in 366 days
2. The *sun is at Maghādi at start of dakṣiṇāyana*. (Further Mahāsaliaṃ chapter of Vṛddagārgīya Jyotiṣa (VGJ) states Maghā to be the first among the solar nakṣatras.) 
3. The equality of the 27 nakṣatras and the start of sequence at at Maghā help allocate the day numbers to each nakṣatra sector.
4. *The **BP** verses specify the spring and autumnal equinoctial full moons at 1/4 Kṛttikā and 3/4 Viśākhā nakṣatras. This information enables us to date the verses.*
5. We mark the **Kṛttikā and Viśākhā sectors** such that equinoxes are at ¼ kṛttikā and ¾ viśākhā. 
6. We collect the **visible Kṛttikā(η Tau) and Viśākhā(α Lib)** longitudes adjusted for precession from 2400BCE to 0BCE.
7. We programatically collect all full moon longitudes that occur near the equinoxes from 2400BCE to 0BCE, using astropy library. There are about 7 such events each century for each equinox. *The **equinoctial full moons** are marked in the chart that follows.*

---

## A tech note  - Collecting full moons programatically

<style scoped>

    {
        transform:  scale(.8) rotate(5deg) translate(0%, 0%);
        opacity: 0.4;
        border: 2px dashed red;
    }

    h2::after {
        content: "Skip";
        position: absolute;
        top: 0%;
        left: 0%;
        transform: translateY(0%) rotate(-5deg) scale(.5);
        opacity: 0.5;
        font-size: 15em;
    }

    img:nth-child(1) { position: absolute; 
    transform: scaleX(.8) scaleY(.91) translate(55%, -108%); 
    z-index: -1;  border: 0px solid black; }
    li { font-size:15px; margin-left: -20px; width: 50% ; }
    p { font-size: 17px;  width: 50%;  }

    /* all p elements after 2nd child are red*/
    p:nth-child(4) { font-family: monospace; margin-top:0px }
    p:nth-child(n+5) { color: blue;   width: 45%; font-family: monospace; margin-top:8px }
    h2 { font-size: 30px; margin-top: -50px; margin-bottom: -10px;  }

</style>

The **Astropy** library, that uses **Meeus algos**, is used to collect the full moon longitudes **programmatically**.

1. Start at an ancient date - 2400-03-21 BCE
2. Computed the full moon longitude for the date
3. If sun and moon longitudes are within 180°+ $\epsilon$ 
  -- a FM found, collect it
  -- step up the date by 28 days and repeat
1. If not nudge the date by difference of sun and moon longitudes  
2. Repeat 2 onwards till 0 BCE

**Meeus, J., Astronomical Algorithms, 2nd ed, p337, p357**

$\lambda_{moon} = 218.3164477+481267.88123421T$ 

$-0.0015786T^2$

$+ \frac{1}{538,841}T^3$ 

$- \frac{1}{65,194,000}T^4$

$+ \frac{1}{1{,}000{,}000}\sum l$

$T = \frac{FMJD - 2451545.0}{36525}$

$FMJD$ is Julian Day number of Full Moon

![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/collect-full-moons.jpg)

---   
<style scoped>

    {
        transform:  scale(.8) rotate(5deg) translate(0%, 0%);
        opacity: 0.34;
        border: 2px dashed red;
    }

    h2::after {
        content: "Skip";
        position: absolute;
        top: 0%;
        left: 0%;
        transform: translateY(0%) rotate(-5deg) scale(.5);
        opacity: 0.55;
        font-size: 15em;
    }

    img:nth-child(1) { position: absolute; 
    transform: scaleX(.55) scaleY(.7) translate(30%, -25%);
    z-index: -1;  border: 0px solid black; }
    table th { display: none; }
    li { font-size: 19px; margin-left: -20px; width: 45% ; }
    li:nth-child(1) em { background-color: rgba(255,0,0,0.2); }
    li:nth-child(2) em { background-color: rgba(0,255,0,0.2); }
    li:nth-child(3) em { background-color: rgba(255,255,0,0.6); }
    li:nth-child(4) em { background-color: rgba(255,255,0,0.6); }
    li li { font-size: 14px; margin-left: -20px; width: 105% ; color: blue; margin-left:-40px}
    p { font-size: 13px;  width: 55%;  color: blue; }
    h2 {  margin-top: -60px; margin-bottom: 20px;  }
</style>

## Computing the information of BP

![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/bp-bar-chart-fm-efm-kv.jpg)

- Get full moon timeseries from 2400BCE to 800BCE. There are about *1237 FM per century - the top chart* <br><br><br>
- The series is then filtered for *Equinoctial Full Moons - the mid chart*<br><br><br><br><br>
- The series is further filtered for *EFM near kṛttikā and viśākhā - the bottom chart*
- The *yellow region* shows the epoch when the visible kṛttikā and viśākhā are contained in their respective sectors - **2000BCE to 1600BCE**
<!-- -  $$\lambda = L' + \frac{\sum l}{1{,}000{,}000};  \beta =  \frac{\sum b}{1{,}000{,}000}$$ -->
<!-- $$\lambda = 218.3164477+481267.88123421T -0.0015786T^2$$ 
$$+ \frac{1}{538841}T^3 - \frac{1}{65194000}T^4 + \frac{\sum l}{1{,}000{,}000}$$ -->



---   
<style scoped>

    {
        transform:  scale(.8) rotate(5deg) translate(0%, 0%);
        opacity: 0.4;
        border: 2px dashed red;
    }

    h2::after {
        content: "Skip";
        position: absolute;
        top: 0%;
        left: 0%;
        transform: translateY(0%) rotate(-5deg) scale(.5);
        opacity: 0.35;
        font-size: 15em;
    }

    img { height:240px; width:720px;margin-left: auto; margin-right: auto; }
    table th { display: none; }
    td { font-size: 13px; }
    table:nth-child(3) { margin-top:-3px; color: grey; }
    table:nth-child(4) { color: blue; margin-top:40px  } 
    h2 { font-size: 30px; margin-top: -50px; margin-bottom: -10px;  }
</style>

## Inferring the BP epoch

||
|--|
![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/bp-equinoctial-full-moon-better.jpg)

|||
|--:|:--|
Axes | BCE years on the x-axis and longitudes/nakṣatra sectors on the y-axis
Green Dots | **Equinoctial Full Moons**  
Red Sector | Extent of **Kṛttikā sector** containing SE *(Sun at 0°)* in its 1st amśa
Blue Sector | Extent of **Viśākhā sector** containing AE *(Sun at 180°)* in its 3rd amśa
Sloping Red/Blue| **Visible Kṛttikā/Viśākhā longitudes** adjusted for *precession*
Light Gray Band | Epoch when  **visible Kṛttikā/Viśākhā** are in **their respective sectors** ~*1980-1610 BCE*
Dark Gray Band| Epoch for **AE FM at 4th amśa of Viśākhā closest to visble Viśākhā** ~*1700-1610 BCE*

|||
|--|--|
**1980-1610 BCE** | The *visible Kṛttikā & Viśākhā* are *contained in their respective sectors* 
**1700-1610 BCE** | The equinoctial *FM  at ¾ viṣākhā sector is nearest to visible viśākhā* 
**Maghādi scheme** | The Maghādi scheme of MAU is consistent with the equinoctial full moon scheme of BP

---
<!-- <div class=page-break style="page-break-before:always"></div> <p></p> -->

Assuming the dakṣiṇāyana point to be the day 1 of the 366 day cycle, the following table shows the day number of the start of each ṛtu and ayanas.

<style scoped>
img { filter: invert(100%); height: 60px; }
{ font-size: 14px;}

/* td:nth-child(1) { width: 5%; }
td:nth-child(2) { width: 15%; }
td:nth-child(3) { width: 15%; }
td:nth-child(4) { width: 10%; }
td:nth-child(5) { width: 30%; } */
</style>

|day num | ṛtu | ayana | equinox/ solstice | sunrise image as seen by an observer |
|--:|---|---|---|:---|
|1| varṣā start | **dakṣiṇāyana start** | summer solstice | ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-01-ss.jpg) <br>sun rises north east
|62| śarad start| dakṣiṇāyana | - | -
|92 |śarad mid | **viṣuvat** | autumn equinox | ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-02-ae.jpg)  <br> sun rises true east
|123 | hemanta start  | dakṣiṇāyana | - |
|183<br>184 | śiśira start  | **dakṣiṇāyana end**<br> **uttarāyaṇa start**| winter solstice | ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-03-ws.jpg) <br> sun rises south east
|245 | vasanta start | uttarāyaṇa | - | -
|274 | vasanta mid | **viṣuvat** | spring equinox |  ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-04-se.jpg) <br> sun rises true east
|306 | grīṣma start | uttarāyaṇa | - | -
|366 | grīṣma-end | **uttarāyaṇa end**<br>**dakṣiṇāyana start**  | summer solstice | ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-01-ss.jpg)  <br> sun rises north east


---

<style scoped>
    img { filter: invert(100%); transform: translate(-36%, -35%) scale(.30); border: 15px solid green; }
    li { font-size: 180%}
    li li { font-size: 100%}
    a::after { content: " 🔗"; }
</style>

## [Sun's annual cycle](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-ayana.gif)

- The sunrise point at horizon moves/swings from
    - north east to south east called **dakṣiṇāyana**
    - back to same north east called **uttarāyaṇa**
-   **366 sunrises** makes a cycle - a solar year
-   The sunrises are associated with specific background stars called **nakṣatra-s**
   
![(animation link for pdf)](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-ayana.gif)



---

## Sun and Nakṣatras

We noted that each of the 366 sunrises occurs at different points on the eastern horizon due to the sun's swing. In addition, the stars that are visible just prior to each sunrise at the sunrise point also change. The stars that are visible just prior to sunrise are said to belong to the nakṣatra of that day.  

During uttarāyaṇa and dakṣiṇāyana the sun seems to rise at a stationary point for about 14 days. The stars visible prior to sunrise for these two stationary points define the sector/span of a nakṣatra - of about 14 days - more precisely 13<sup>5</sup>/<sub>9</sub> days.

A nakṣatra is a span of time of about 14 days and contains the stars that are visible at sunrise in its time span. There are 27 such equal nakṣatra spans in a 366 day cycle. Each of the 27 nakṣtra while of equal time span contains varying counts of stars -  between 1 and 6 - totaling 83 stars. The 27 nakṣatra are named in a fixed cyclical order.

The current order starting from Aśvinī along with their star count listed below, is an inherited order from around 1500 years ago. The order of the nakṣatra begins with Kṛttikā and ends with Revatī in more ancient texts.

<style scoped>
    p { font-size: 13.8px; }
    table td {
        border: 1px dotted black;
        text-align: center;
        font-weight: bold;
        color: black;
        width: 14%;
        position: relative;
    }

    #never
    , table tr:nth-child(1) td:nth-child(6)
    , table tr:nth-child(1) td:nth-child(8)
    , table tr:nth-child(2) td:nth-child(5)
    , table tr:nth-child(2) td:nth-child(6)
    , table tr:nth-child(3) td:nth-child(6)
    , table tr:nth-child(3) td:nth-child(9)
    { background-color: rgba(255,0,0,0.1); font-size: 11px; }

    #never
    , table tr:nth-child(1) td:nth-child(7)
    , table tr:nth-child(2) td:nth-child(2)
    , table tr:nth-child(2) td:nth-child(3)
    , table tr:nth-child(2) td:nth-child(7)
    , table tr:nth-child(3) td:nth-child(7)
    , table tr:nth-child(3) td:nth-child(8)
    { background-color: rgba(255,0,0,0.3); font-size: 12px; }

    #never
    , table tr:nth-child(1) td:nth-child(1)
    , table tr:nth-child(1) td:nth-child(2)
    , table tr:nth-child(1) td:nth-child(5)
    , table tr:nth-child(2) td:nth-child(9)
    , table tr:nth-child(3) td:nth-child(4)
    { background-color: rgba(255,0,0,0.5); font-size: 13px; }

    #never
    , table tr:nth-child(2) td:nth-child(8)
    , table tr:nth-child(3) td:nth-child(1)
    , table tr:nth-child(3) td:nth-child(2)
    , table tr:nth-child(3) td:nth-child(3)
    , table tr:nth-child(3) td:nth-child(5)
    { background-color: rgba(255,0,0,0.6); font-size: 14px; }


    #never
    , table tr:nth-child(1) td:nth-child(4)
    , table tr:nth-child(2) td:nth-child(4)
    { background-color: rgba(255,0,0,0.8); font-size: 15px; }
    
    #never
    , table tr:nth-child(1) td:nth-child(3)
    , table tr:nth-child(1) td:nth-child(9)
    , table tr:nth-child(2) td:nth-child(1)
    { background-color: rgba(255,0,0,1); font-size: 16px; }

</style>


||||||||||
|--|--|--|--|--|--|--|--|--|
|Aśvinī<br>3|Bharaṇī<br>3|Kṛttikā<br>6|Rohiṇī<br>5|Mṛgaśiras<br>3|Ārdrā<br>1|Punarvasu<br>2|Puṣya<br>1|Aśleṣā<br>6|
|Maghā<br>6|Pūrva<br>Phalgunī<br>2|Uttara<br>Phalgunī<br>2|Hasta<br>5|Citrā<br>1|Svātī<br>1|Viśākhā<br>2|Anurādhā<br>4|Jyeṣṭhā<br>3|
|Mūla<br>4|Pūrva<br>Aṣāḍhā<br>4|Uttara<br>Aṣāḍhā<br>4|Śravaṇa<br>3|Śraviṣṭhā<br>4|Śatabhiṣā<br>1|Pūrva<br>Bhādrapadā<br>2|Uttara<br>Bhādrapadā<br>2|Revatī<br>1|:


The choice of the first nakṣatra to start the cycle contains information on the epoch and the convention for the year start.

There are texts that associate specific nakṣatras with the ṛtus - seasonal naḳsatras .  Such seasonal naḳsatras also contain vital information on the epoch of the text.

---

<style scoped>
    img { filter: invert(%); zoom: 20%; float: right; }
    p, li{ font-size: large;  }
    p { font-size: 150%; font-weight: bold; margin-top: 30px   }
</style>

## Nakṣatra-s starting from Maghā at day 1


![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/daynum-dial-season-1700-bce.jpg)

<!-- |#|nakṣatra | day span | number of stars | cumulative stars |
|-:|---:|:---:|:---|--|
 1|Maghā            |  1-14 | 6 | 6
 2|Pūrva Phalgunī   | 14-28 | 2 | 8
 3|Uttara Phalgunī  | 27-41 | 2 | 10
 4|Hasta            | 40-55 | 5 | 15
 5|Citrā            | 54-68 | 1 | 16
 6|Svātī            | 67-82 | 1 | 17
 7|Viśākhā          | 81-95 | 2 | 19
 8|Anurādhā         | 94-109| 4 | 23
 9|Jyeṣṭhā          |109-123| 3 | 26
10|Mūla             |123-136| 6 | 32
11|Pūrva Aṣāḍhā     |136-150| 4 | 36
12|Uttara Aṣāḍhā    |150-163| 4 | 40
13|Śravaṇa          |163-177| 3 | 43
14|Śraviṣṭhā        |177-190| 4 | 47
15|Śatabhiṣā        |190-204| 1 | 48
16|Pūrva Bhādrapadā |204-217| 2 | 50
17|Uttara Bhādrapadā|217-231| 2 | 52
18|Revatī           |231-245| 1 | 53
19|Aśvinī           |245-258| 3 | 56
20|Bharaṇī          |258-272| 3 | 59
21|Kṛttikā          |272-285| 6 | 65
22|Rohiṇī           |285-299| 5 | 70
23|Mṛgaśiras        |299-312| 3 | 73
24|Ārdrā            |312-326| 1 | 74
25|Punarvasu        |326-339| 2 | 76
26|Puṣya            |339-353| 1 | 77
27|Aśleṣā           |353-366| 6 | 83 -->


In this Maghādi epoch day 1 of dakṣiṇāyana is at Maghā start. 
  - The sun traverses through the 27 nakṣatras in order and returns to Maghā start at the end of the 366 day cycle.
  - The  1st and 367th sunrise are at
    - the same nakṣatra/star - Maghā/ε-Leonis
    - the same point on the horizon and
  
Over 100's of years, 
- the nakṣatra/star to shift by about 1 day in about 72 years. 
-  This shift is called the ayanāṃśa/precession.


---

<style scoped>
    img { filter: invert(%); zoom: 20%; float: right; }
    { font-size: 15px;}
    em { background-color: rgba(255,0,0,0.1); }
</style>

## Precession and its effects

![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/sun-moon-season-precession-dial.jpg)
We see the start of Maghā nakṣatra on day 1 of dakṣiṇāyana in the chart above. This is true for a certain epoch. After about a 1000 years, the start of Maghā nakṣatra will be on day 14 of dakṣiṇāyana. Equivalently day 1 of dakṣiṇāyana will move to Āśleṣā start. 

*The precession is a slow process and takes about 25,800 years to complete one cycle. That is the sunrise point will return to the same nakṣatra/star for the same ṛtu after **25,800 years.***

Precession causes the seasonal nakṣatras to drift with time.  Many ancient text associate nakṣhatras with seasons - this association contains vital information on the epoch of the text.

The direction of precession is opposite to the direction of the  sun's annual transit through the nakshatras. Incidentally the moon also transits through the nakṣatras in the same direction as the sun. The moon's transit through the nakṣatras is called the lunar month of about 27 days.

---

## Effect of precession over millennia
<style scoped>
    li { font-size: 14px;} */
</style>

-   About every 1000 years the start of season move backwark by one naḳsatra. In addition the precession causes the pole star to change. 

-   The following table/pictures shows the start of the spring equinox seasonal naḳsatra and the pole star for the last 5000 years.


<style scoped>
    th:nth-child(6) { display: none; }
    td:nth-child(6) { display: none; }
    img { filter: invert(100%); height: 240px; }
    table tr:nth-child(1) td:nth-child(1) img { filter: invert(80%); }
</style>

|Epoch|Spring Equinox|Dakṣiṇāyana|Uttaryāṇa | Pole Star|Image|
|---|---|---|---|---|--|
|Present|Uttara Bhādrapadā|Ārdrā|Mūla|Polaris|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-01-2000-ce.jpg)
|1000 years ago|Revatī|Punarvasu|Pūrva Aṣāḍhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-02-1000-ce.jpg)
|2000 years ago|Aṡvinī|Puṣya|Uttara Aṣāḍhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-03-0000-ce.jpg)
|3000 years ago|Bharanī|Aśleṣā|Śravaṇa|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-04-1000-bce.jpg)
|4000 years ago|Kṛttikā|Maghā|Śraviṣṭhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-05-2000-bce.jpg)
|5000 years ago|Rohiṇī|Pūrva Phalgunī |Śatabhiṣā|Thuban|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-06-3000-bce.jpg)

|||
|:---:|:--:|
|Present Day <br> ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-01-2000-ce.jpg) | 5000 years ago <br> ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-06-3000-bce.jpg)|


---
<style scoped>
    img { filter: invert(100%); transform: scale(0.30);  transform-origin: 0 0; }
    a::after { content: " 🔗"; }
</style>

## [Precession over 5000 years](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-precession.gif)



![Precession over 5000 years](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-precession.gif)


<style scoped>
    /* place text at the bottom of the slide */
    p { position: absolute; bottom: 60px; width: 100%;  font-size:20px; margin-left: -80px; }
    li { list-style-type: none; }
    
    /* place text at the bottom of the slide */
</style>

## Nakṣatra solar zodiac

![bg fit width 100%](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/sun-moon-season-precession-dial.jpg)
![bg fit width 90%](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-nakshatra-table.png)

- The **Sun** completes one circuit in **366 days** in **clockwise** direction<br><br>
- The **ṛtu-s** complete one circuit in ~**25,800 years** in **anticlockwise** direction

-

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    li { font-size: 16px;  margin-left: -30px; }
</style>

![bg right:60% fit ](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/02_precession-movie.gif)
## [The Drift of the Seasonal Nakṣatras](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/02_precession-movie.mp4)

- Video of ~2½ minutes shows,
- **Over millenia**,
  - the nakṣatra-s drift slowly due to precession  
  - This change is used to date the ancient texts

- **Epochs of Ancient passages using Seasonal Nakṣatra-s**
  - Brahmāṇḍa Purāṇa (BP)
  - Vṛddagārgīya Jyotiṣa (VGJ)
  - Parāśaratantra (PT)
  - Maitrāyaṇīya Āraṇyaka Upaniṣat (MAU)
  - Nidānasūtra (NS)
  - Lagadha Jyotiṣa (LJ)
  - Others ...
  
---
#
# The Maghādi/dakṣināyaṇa epoch  - BP, MAU, NS passages

---
<style scoped>
    p, li {font-size: 20px; color:blue;}
    th { display: none; }
    table td:nth-child(2)  { display:none }
    table td { font-size: 19px; }
    table { margin-left: 25px; font-size: 15px;  margin-top: 30px; }
    th { display: none; }
</style>

## The Maghādi/dakṣināyaṇa epoch

### [Brahmāṇḍa Purāṇa *BP 21.143-149*](https://raw.githubusercontent.com/cahcblr/sanchaya/main/Puranani/brahmanda%20purana.txt)

- This BP passage defines visuvat to be of equal day and night duration of 15 muhūrtas each - equinox - in the mid of vasanta and śarat ṛtus.

- The passage further states the nakṣatra location at an aṃsa grain for equinoctal sun and moon at spring and autumn equinoxes.

- It turns out the sun and moon locus at each of the equinox are diametrically opposite - at 1/4 kṛttikā and  3/4 viśākhā,  indicating the description are of the **equinoctial full moon**. 

|||
|--|--|
| **शरद्वसंतयोर्मध्ये मध्यमां गतिमास्थितः । अतस्तुल्यमहोरात्रं करोति तिमिरापहः ॥** | In *mid autumn and spring* having attained moderate pace, *the sun*, remover of darkness, therefore *makes day and night equal*. 
| हरिताश्च हया दिव्यास्तस्य युक्ता महारथे । अनुलिप्ता इवाभान्ति पद्मरक्तैर्गभस्तिभिः ॥ | The divine yellow horses, yoked to his great chariot, shine like covered with the lotus-red rays.
| मेषान्ते च तुलान्ते च भास्करोदयतः स्मृताः । **मुहूर्त्ता दश पञ्चैव अहो रात्रिश्च तावती** ॥ | The hours of the day and night are each reckoned as ten and five muhūrtas from the rising of the sun at the end of meshā and tulā
| **कृत्तिकानां यदा सूर्यः प्रथमांशगतो भवेत् । विशाखानां तदा ज्ञेयश्चतुर्थांश निशाकरः** ॥  | When the *sun is in the first part of kṛttikā*, know the *moon is in the fourth part of viśākhā*
| **विशाखानां यदा सूर्यश्चरतेंशं तृतीयकम् । तदा चन्द्रं विजानीयात्कृत्तिकाशिरसि स्थितम्** ॥ | When the *sun is in the third part of viśākhā*, know the *moon is in the head of kṛttikā*
| विषुवं तं विजानीयादेवमाहुर्महर्षयः । सूर्येण विषुवं विद्यात्कालं सोमेन लक्षयेत् ॥ | It is then understood to be equinox - so say the maharishis. Equinox is known through the sun and time by the moon
| समा रात्रिरहश्चैव यदा तद्विषुवं भवेत् । तदा दानानि देयानि पितृभ्यो विषुवेषु च ॥ | *When equinox occurs, night and day are equal*. Then during equinoxes offerings are made to piṭṛs 

---
<style scoped>
    li, p {font-size:20px;  color: blue}
    th { display: none; }
    table td:nth-child(2) { display:none }
    table { margin-left:15px;  margin-top: 0px; }
    table td { font-size: 16px; }
    h3:nth-child(1) { margin-top: -50px; margin-bottom: -10px; text-align: left; }
</style>


### [Maitrāyaṇīya Āraṇyaka Upaniṣat *MAU 6.14*](https://github.com/cahcblr/sanchaya/blob/647880cd98978d739d122a9a6b7069a4d56c6f3d/Vedic%20texts/YV/MAU-text.txt#L2)

- The year commences in Maghādi (at dakṣiṇāyana).
- A year has 12 parts and each part has 9 amṣa.
- The year's first half , Āgneya,is from **Maghādi** to Śraviṣṭhārdha and 
- The second half , Vāruṇa, is from Sārpādi to Śraviṣṭhārdha in reverse order.

|||
|--|--|
|सूर्यो योनिः कालस्य तस्य एतद्रूपं । | Sun and Time are contemporaries
|यन्निमेषादि कालात्संभृतं द्वादशात्मकं वत्सरम् । | वत्सरः(year) has 12 parts and <br> is filled with time units starting with निमेषा(eye wink)
|एतस्याग्नेयमर्धमर्धं वारुणम् । | Year's first half is आग्नेयः(Āgneya) and <br>the second half is वारुणः(Varuṇa)
| **मघाद्यं** श्रविष्ठार्धमाग्नेयं क्रमेणोत्क्रमेण सार्पाद्यं श्रविष्ठार्धान्तं सौम्यम् ।  | *Āgneya - from मघादि (Maghā start) to श्रविष्ठार्धः(half of Śraviṣṭhā)* <br> Varuṇa - from सार्पादि(Sārpā start) to श्रविष्ठार्धान्तः(end of half of Śraviṣṭhā) in counter order
|तत्र एकमात्मनो *नवांशकं* सचारकविधम् । | In each part, the Sun traverses 9 amṣa( portions) in order <br>**9 amṣa(portion) for each of the 12 year parts implies each nākshatra has 4 amṣa** 


<!-- <style scoped>
    p,  li {font-size: 20px;}
    table td:nth-child(2) , em { display:none }
    table td { font-size: 30px; }
    th { display: none; }
    table { margin-left: 25px;  margin-top: 30px; }

</style> -->

### [Nidānasūtra  *NS 5.12*](https://archive.org/details/in.ernet.dli.2015.408135/page/n173/mode/2up?view=theater)
- Sun traverses 13 and an additional 5/9 ahorāṭras in each nakṣatra. 
- To cover 27 nakṣatras the sun takes 366 ahorāṭras/days. 

|||
|--|--|
स एष नाक्षत्रः आदित्यसंवत्सरो । *सः एषः नाक्षत्रः आदित्यसंवत्सरः ।* | This is the nakṣatra year of the sun
आदित्यः खलु शश्वदेतावद्भिरहोभिर्नक्षत्राणि समवैति । *आदित्यः खलु शश्वत्  एतावत्भिः अहोर्भिः नक्षात्राणि समवैति ।* | The sun, indeed, with these many days, stays with each nakṣatras
त्रयोदशाहं त्रयोदशाहमेकैकं नक्षत्रमुपतिष्ठति। *त्रयोदशाहं त्रयोदशाहम  एकैकं नक्षत्रम् उपतिष्ठति ।* | The sun spends **13 days** with each nakṣatra  
अहस्तृतीयं च नवधा कृतयोरहोरात्रयोर्द्वे द्वे कले चेति संवत्सराः। *अहः तृतीयं च नवधा कृतयोः अहोरात्रयोः  द्वे द्वे कले चेति संवत्सराः ।* | अहोरात्रि/3 + (2* अहः +  2* रात्रि)/9 =  **5 अहोरात्रि/9**  *13 and 5/9 days with each nakṣatra*
ताश्चत्वारिंशच्चतुःपञ्चाशतं कलाः। *ताः चत्वारिंशत् चतुःपञ्चाशतं कलाः ।* | ???? Those are 40 and/times 54 kalās
ते षण्णववर्गाःसषट्षष्टित्रिशतः ॥ *ते षट् नव वर्गाः सः षट्षष्टिः त्रिशतः ॥* | ???? These are 6*9 vargās and 366

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    li { font-size: 20px;  margin-left: -50px; margin-top: 10px; }
    h2 { scale: .6; margin-top: -80px; margin-left: -50px; }
</style>

![bg right:60% fit](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/05_brahmanda-movie.gif)
## [The **Epoch of Brahmāṇḍa Purāṇa** passages 21.143-149](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/05_brahmanda-movie.mp4)
- Video of ~1½ minutes shows,
- **The BP** verses specify the spring and autumnal equinoctial full moons at 1/4 Kṛttikā and 3/4 Viśākhā nakṣatras. 
- This places these observations to ~1800BCE (± 100 years)
    



---

<style scoped>
    li{font-size: 22px; margin-left: -20px;}
    em { background-color: rgba(255,0,0,0.1); }
</style>

## Nakṣatra Chart 1800BCE (± 100) - Maghādi epoch

- The *equinoctial full moons of BP*
  - ¼ kṛttikā sector
  - ¾ viśākhā sector
  - SE-AE axis of the chart
- *aligns with maghādi of MAU*
  - when maghādi (SS 1) is at 
    - start of dakṣiṇāyana
- *around 1800 BCE (± 100)*

<!-- Computatonally, the alignment is found to be
  - when the visible kṛttikā and viśākhā are 
    - *contained in their respective sectors*
  - when the equinoctial full moon at 
    - ¾ viśākhā sector is 
    - nearest to visible viśākhā -->z
  

![bg fit right 100%](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/daynum-dial-season-fm-1700-bce.jpg)

---


#
# The Śraviṣṭhādi/uttarāyaṇa epoch - VGJ/11 and PT passages

---


## Śraviṣṭhādi/ uttarāyaṇa epoch - VGJ/11 Ādityachāra and Parāśharatantra


<style scoped>
    table { margin-left: -25px; font-size: 12px; width: 120%}
    table td:nth-child(2) { width: 10px; }
    table td:nth-child(3) { width: 10px; }
    table th:nth-child(3) { display: none; }
    table td:nth-child(5) { display: none; }
    li { font-size: 13px; margin-left: -50px}
    h2 { scale: .7; margin-bottom: -40px; }
</style>

- Ādityachāra, section 11 of VGJ, describes the transit of Sun through 9 seasonal nakṣatras . 
- Similar information is presented in PT in prose.
- The Ādityachāra passage is shown below.
- Passage maps 6 ṛtus mapped to 9 seasonal nakṣatras  
- Mapping enables passage dating

|Verse|From|To|Ṛtu|Span|
|:---|:---:|:---:|:---:|:--:|
**श्रविष्ठादीनि** चत्वारि **पौष्णार्धञ्च*** दिवाकरः  ।<br>  वर्धयन् सरसस्तिक्तं मासौ तपति **शैशिरे**  ॥ 47 | श्रविष्ठा begin | रेवती mid | शिशिर | 270°-330° |
**रोहिण्यन्तानि** विचरन् **पौष्णार्धाद्याच्च** भानुमान् ।<br> मासौ तपति **वासन्तौ** कषायं वर्धयन् रसम्॥ 48 | रेवती mid | रोहिणी end | वसन्त|330°-30°|
**सार्पार्धान्तानि** विचरन् **सौम्याद्यानि** तु भानुमान् ।<br> **ग्रैष्मिकौ** तपते मासौ कटुकं वर्धयन् रसम्॥ 52 | मृगशिरा begin | आश्लेषा mid | ग्रीष्म| 30°-90°|
**सावित्रान्तानि** विचरन् **सार्पार्धाद्यानि** भास्करः ।<br> **वार्षिकौ** तपते मासौ रसमम्लं विवर्धयन्॥ 53 |आश्लेषा mid | हस्ता end | वर्षा| 90°-150°|
**चित्रादीन्यथ** चत्वारि **ज्येष्ठार्धञ्च** दिवाकरः।<br> **शारदौ** लवणाख्यं च तपत्याप्याययन् रसम्॥ 54 | चित्रा begin | ज्येष्ठा mid | शरद्|150°-210°|
**ज्येष्ठार्धादीनि** चत्वारि **वैष्णवान्तानि** भास्करः ।<br> **हेमन्ते** तपते मासौ मधुरं वर्धयन् रसम् ॥ 55 | ज्येष्ठा mid | श्रवण end | हेमन्त|210°-270°|

  
![bg fit right:50%](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-adityacara-seasons.png)

---

## Dating Ādityachāra - by minimizing error
<style scoped>
    li { font-size: 22px; margin-left: -20px ; width: 300px; margin-top:10px}
    li li { scale : 0.9;  margin-top: 10px; color: navy;}
    h2 { scale: .8; margin-bottom: 20px; }
</style>

![bg fit right:55%](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-adityacara-charts.png)

- The text specifies 9 **seasonal nakṣatra-s** 
- For each epoch from -2500 to 500 in 50 year steps
  - Measures an **error** of the 9 nakṣatra-s from their prescribed season
  - The epoch with **lowest error** is the best epoch **$\mathbb{B}_{epoch}$**

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    li { font-size: 20px;  margin-left: -20px; margin-top: 20px}
    h2 { scale: .8; width: 110%;}
</style>


![bg right:60% fit](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/04_adityacara-movie.gif)
## [The Epoch of Ādityachāra passages in VGJ & PT ](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/04_adityacara-movie.mp4)
- Video of ~1½ minutes shows,
- **The PT and VGJ** verses that specify 9 seasonal nakṣatras
- This information places these observations to ~1300BCE (± 100 years)

---

#
# The Śravaṇādi/uttarāyaṇa epoch - VGJ/59 Ṛtusvabhāva

---

## The Śravaṇādi epoch  - VGJ/59 Ṛtusvabhāva

<style scoped>
    /* table { margin-left: -25px; font-size: 15px; }
    table td:nth-child(2) { width: 10px; }
    table td:nth-child(3) { width: 10px; }
    table th:nth-child(3) { display: none; }
    table td:nth-child(5) { display: none; }
    img { filter: invert(5%); height: 520px;  position: absolute; transform: translate(56%, -5%); z-index: -1;  border: 0px solid black; } */
    li { font-size:15px; margin-left: -30px ; width: 300px}
    h2 { scale: .8; }
    li:nth-child(2) li:nth-child(3) { color: blue; }
    li:nth-child(3) li:nth-child(2) { color: blue; }
</style>

![bg  fit right:55% ](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/sun-transit-rtusvabhava-charts-rni.jpg)

- Ṛtusvabhāva dates to **~500 BCE**
<br>
- This is different from आदित्यचारः
	- Ṛtu sequence begins with वसन्त not शिशिर
	- Ṛtu are related to months, not  *nakṣatra* span & boundaries
	- A 12 month **solar zodiac**, obviating intercalation, emerges
<br>
- It describes Sun's path through
	- 6 seasons and their months
	- 12  **vaidika** and equivalent **laukika** months and  12  *nakṣatra-s* for each of these months - ~30° apart

---

<style scoped>
    {
        transform:  scale(1) rotate(0deg) translate(0%, 0%);
        border: 10px solid gray; border-radius: 10px;
    }
    h2 { scale: .8; align: left; margin-left: -50px; }
    li { font-size: 20px;  margin-left: -50px; margin-top: 20px}
</style>


![bg right:60% fit](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/03_rtusvabhava_movie.gif)
## [The Epoch of VGJ Ṛtusvabhāva passages](https://cahc.jainuniversity.ac.in/assets/talks/2024-03-17-mythic/03_rtusvabhava_movie.mp4)
- Video of ~1½ minutes shows,
- **The VGJ** verse information that specify 12 seasonal nakṣatras
- This information places these observations to ~500BCE (± 100 years)

---

## A chronology of Solar transits  

<style scoped>
   table { font-size: 23px; }
   table td:nth-child(4) { width:23% }
   p { font-size: 32px; }
</style>

|Epoch|Scheme|Start|Season|
|--:|:--:|--:|--|
earlier | **2 Ayana/6 Ṛtu** based sun transit   |
~1800 BCE | **MAU/BP**  Equinoctial full moon scheme | Maghādi |dakṣināyaṇa 
~1300 BCE  | **VGJ/ādityacāra** and **PT**  with *4½ nakṣatra-s* per season | Śraviṣṭhādi |uttarāyaṇa
~500 BCE  | **VGJ/ṛtusvabhāva**  with *12 solar months* | Śravaṇādi<br><br>*Revatyādi<Br>Bharaṇyādi*| uttarāyaṇa<br><br>*vasanta<br>spring equinox*

**Solar zodiac** is certainly part of original Indian knowledge - that has been recorded and evolved over time.

---

# Q & A

## References

<style scoped>
    table { font-size: 14px; }
    strong { float : right; }
    th { display: none; }
    h2 { margin-top: 20px; margin-bottom: -20px; }
    h1 { border: 4px solid rgba(0,0,0,0.1); border-radius: 10px; padding: 10px; }

    tr:nth-child(6) a:nth-child(2) { font-weight: bold; color: brown; }
    tr:nth-child(7) a:nth-child(2) { font-weight: bold; color: brown; }

</style>


|  | |
|---:|---|
1|**Abhyankar, K. D. (1991)**[Misidentification of some Indian nakṣatras. Indian Journal of History of Science, 26(1), 1–10.](https://github.com/suchakr/cahc-utils/blob/main/papers/naks/naks-1991-abyn-misidentified-naks.pdf)
2|**Das P. (2018)** [Bhāgavata Cosmology; Vedic Alternative to Modern Cosmology, Tulsi Books, Mumbai.](https://tulsibooks.com/product/bhagavata-cosmology-vedic-alternative-to-modern-cosmology/)
3|**Gondalekhar, P. (2013)** [The time keepers of the Vedas. Manohar. [ISBN 978-81-7304-969- 9].](https://www.amazon.in/Time-Keepers-Vedas-History-Calendar/dp/8173049696)
4|**Iyengar, R. N. (2013)** [Parāśara Tantra (Ed. Trans & Notes). Jain University Press. [ISBN 978-81-9209-924-8].](https://www.amazon.in/Time-Keepers-Vedas-History-Calendar/dp/8173049696)
5|**Iyengar R.N. (2016)** Astronomy in Vedic texts,(Book Chapter pp.107-169).<br>History of Indian Astronomy A Handbook, (Ed. K.Ramsubramanian, A.Sule &M. Vahia)<br> Publn. by IITB and TIFR, Mumbai.
6|**Iyengar R.N. and <br>Chakravarty, S (2023)** [Equinoctial full moon of the Brahmāṇḍa Purāṇa and the nakṣatra](http://cahc.jainuniversity.ac.in/assets/ijhs/rni-maghadi-2023.pdf)
7|**Iyengar R.N. and <br>Chakravarty, S (2021)** [Transit of sun through the seasonal nakṣatra cycle in the Vṛddha‐Gārgīya Jyotiṣa, Indian Journal of History of Science 56:159–170.](https://github.com/suchakr/cahc-utils/blob/main/papers/vgj/vgj-2022-01-rni-sc-sun-transit.pdf)
8|**Koch D. (2014)** [Astronomical dating of the Mahābhārata war. Erlenbach, Switzerland](https://www.gilgamesh.ch/KochMahabharata6x9_V1.00.pdf)
9|**Sastry T. S. K. (1984)** [Vedāṅga Jyotiṣa of Lagadha. Indian Journal of History of Science, 19 (4), l–74.](https://github.com/suchakr/cahc-utils/blob/main/papers/lvj/lvj-1984-kuppanna.pdf)
10|**Sengupta, P. C. (1947)** [Ancient Indian Chronology. Univ. of Calcutta.](https://indianculture.gov.in/ebooks/ancient-indian-chronology-illustrating-some-most-important-astronomical-methods)
11|**Srinivas M.D. (2019)** [The Untapped Wealth of Manuscripts on Indian Astronomy and Mathematics Indian Journal of History of Science, 54.3, 243-268.](https://www.researchgate.net/profile/M-Srinivas/publication/336438227_The_Untapped_Wealth_of_Manuscripts_on_Indian_Astronomy_and_Mathematics/links/602b2bd94585158939a94482/)
12|**Thompson R. L. (2007)** [The Cosmology of the Bhāgavata Purāṇa (Indian Edn.) Motilal Banarsidass, Delhi.](https://www.motilalbanarsidass.com/products/the-cosmology-of-the-bhagavata-purana-mysteries-of-the-sacred-universe)

---

## Backup Slides from Here

---

<!-- <div class=page-break style="page-break-before:always"></div> <p></p> -->

<style scoped>

{
    transform:  scale(.8) rotate(5deg) translate(0%, 0%);
    opacity: 0.4;
    border: 2px dashed red;
}

h2::after {
    content: "Skip";
    position: absolute;
    top: 0%;
    left: 0%;
    transform: translateY(0%) rotate(-5deg) scale(.5);
    opacity: 0.35;
    font-size: 15em;
}

img { filter: invert(100%); height: 90px; xwidth: 390px; }
{ font-size: 14px;}
table { position: absolute; transform: translate(0%, 0%); z-index: -1;  border: 0px solid black; width: 50% ; }
li { font-size: 16.5px; margin-left: 480px}

li:nth-child(n+3) { color: seagreen}
li:nth-child(n+4) { color: blue}
li:nth-child(n+6) { color: maroon; font-family:monospace; border: 0px solid black; padding: 5px; background-color: rgba(255,0,0,0.1); }
h3 {  margin-bottom: -5px; text-align: center; font-size: 20px; }
h2 { margin-top: -50px; margin-bottom: -10px;  }
</style>



##  [Ayana](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-ayana.gif), Rtu, Nakṣatra, [Precession](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-precession.gif) 


|view of sunrise | surise location|sunrise (day) count|
|--|:--:|:--:|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-01-ss.jpg)| north east|1|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-02-ae.jpg) | true east|92|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-03-ws.jpg) | south east|183|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-04-se.jpg) | true east|274|
|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-01-ss.jpg) | north east|367 <br><br> 1 of next cycle|

- The sunrise horizon point moves from north east to south east and back to same north east point after 366 sunrises - a solar year.
- The north east to south east journey is called **dakṣiṇāyana** and the reverse is  **uttarāyaṇa**
- In addition the sun cycles through six ṛtu-s in a year - **śiśira, vasanta, grīṣma, varṣā, śarad, hemanta** - each of 61 sunrises.
- Specific background stars can be observed just before each sunrise. These stars are called **nakṣatra-s** , 27 in number.
- Each of the 2 ayana-s and 6 ṛtu-s are associated with specfic nakṣatra-s.
- Over ages this ayana/ṛtu-nakṣatra association changes due to the **precession** phenomenon. 
- This change is used to date the ancient texts.




## Observational Astronomy of the Sun


### Sun, Ayanas and Ṛtus
<style scoped>
   table { font-size: 14px; }
   p { font-size: 14px; }
</style>
An observer noticing the sunrise point of the eastern horizon will notice the point oscillate between north-east in the summer to south-east in the winter and back to north-east in the summer - much like a swing.

The extreme north and south points are the dakṣiṇāyana  and uttarāyaṇa start   - the winter and summer solstices respectively. The points in between are called the viṣuvat - spring and autumn equinoxes.

One full swing of the sun lasts 366 days and is made of two ayanas the dakṣiṇāyana and uttarāyaṇa each of 183 days

In one full swing from uttarāyaṇa, the sun traverses through six ṛtus (seasons) in order -  namely varṣā, śarad, hemanta, śiśira, vasanta, grīṣma,- each ṛtu is of 61 days.

Just as a swing appears to be stationary at the extreme points, the sun appears to be stationary at the uttarāyaṇa and dakṣiṇāyana start points before resuming its oscillation. An observer will notice that the sun is stationary at the uttarāyaṇa and dakṣiṇāyana start points for about 14 sunrises each.

The period from one  sunrise to another is called a ahorāṭra/day. A ṛtu is made of 61 ahorāṭras/days. An ayana is made of 183 ahorāṭras/days.One swing of the sun with 366 ahorāṭras/days is samvatsara/year.

| | ahorāṭra | ṛtu | ayana |samvatsara |
|---|---|---|---|---|
| ahorāṭra| 1 |  |  | |
| ṛtu | 61 | 1 | |  |
| ayana | 183 | 3 | 1 |  |
| samvatsara | 366 | 6 | 2 | 1 |





---
<style scoped>

    {
        transform:  scale(.8) rotate(5deg) translate(0%, 0%);
        opacity: 0.4;
        border: 2px dashed red;
    }

    h2::after {
        content: "Skip";
        position: absolute;
        top: 0%;
        left: 0%;
        transform: translateY(0%) rotate(-5deg) scale(.5);
        opacity: 0.35;
        font-size: 15em;
    }

    li {font-size: 19px; padding-bottom: 14px}
    table th { display: none; }
    em { background-color: rgba(255,0,0,0.1); }
</style>


## From these MAU, NS and BP passages

1. Sun spends *13 and 5/9 days equally* with each naḳsatra of 4 amṣa . The sun completes one trip through the 27 nakṣatras in 366 days
2. The *sun is at Maghādi at start of dakṣiṇāyana*. (Further Mahāsaliaṃ chapter of Vṛddagārgīya Jyotiṣa (VGJ) states Maghā to be the first among the solar nakṣatras.) 
3. The equality of the 27 nakṣatras and the start of sequence at at Maghā help allocate the day numbers to each nakṣatra sector.
4. *The **BP** verses specify the spring and autumnal equinoctial full moons at 1/4 Kṛttikā and 3/4 Viśākhā nakṣatras. This information enables us to date the verses.*
5. We mark the **Kṛttikā and Viśākhā sectors** such that equinoxes are at ¼ kṛttikā and ¾ viśākhā. 
6. We collect the **visible Kṛttikā(η Tau) and Viśākhā(α Lib)** longitudes adjusted for precession from 2400BCE to 0BCE.
7. We programatically collect all full moon longitudes that occur near the equinoxes from 2400BCE to 0BCE, using astropy library. There are about 7 such events each century for each equinox. *The **equinoctial full moons** are marked in the chart that follows.*

---

## A tech note  - Collecting full moons programatically

<style scoped>

    {
        transform:  scale(.8) rotate(5deg) translate(0%, 0%);
        opacity: 0.4;
        border: 2px dashed red;
    }

    h2::after {
        content: "Skip";
        position: absolute;
        top: 0%;
        left: 0%;
        transform: translateY(0%) rotate(-5deg) scale(.5);
        opacity: 0.5;
        font-size: 15em;
    }

    img:nth-child(1) { position: absolute; 
    transform: scaleX(.8) scaleY(.91) translate(55%, -108%); 
    z-index: -1;  border: 0px solid black; }
    li { font-size:15px; margin-left: -20px; width: 50% ; }
    p { font-size: 17px;  width: 50%;  }

    /* all p elements after 2nd child are red*/
    p:nth-child(4) { font-family: monospace; margin-top:0px }
    p:nth-child(n+5) { color: blue;   width: 45%; font-family: monospace; margin-top:8px }
    h2 { font-size: 30px; margin-top: -50px; margin-bottom: -10px;  }

</style>

The **Astropy** library, that uses **Meeus algos**, is used to collect the full moon longitudes **programmatically**.

1. Start at an ancient date - 2400-03-21 BCE
2. Computed the full moon longitude for the date
3. If sun and moon longitudes are within 180°+ $\epsilon$ 
  -- a FM found, collect it
  -- step up the date by 28 days and repeat
1. If not nudge the date by difference of sun and moon longitudes  
2. Repeat 2 onwards till 0 BCE

**Meeus, J., Astronomical Algorithms, 2nd ed, p337, p357**

$\lambda_{moon} = 218.3164477+481267.88123421T$ 

$-0.0015786T^2$

$+ \frac{1}{538,841}T^3$ 

$- \frac{1}{65,194,000}T^4$

$+ \frac{1}{1{,}000{,}000}\sum l$

$T = \frac{FMJD - 2451545.0}{36525}$

$FMJD$ is Julian Day number of Full Moon

![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/collect-full-moons.jpg)

---   
<style scoped>

    {
        transform:  scale(.8) rotate(5deg) translate(0%, 0%);
        opacity: 0.34;
        border: 2px dashed red;
    }

    h2::after {
        content: "Skip";
        position: absolute;
        top: 0%;
        left: 0%;
        transform: translateY(0%) rotate(-5deg) scale(.5);
        opacity: 0.55;
        font-size: 15em;
    }

    img:nth-child(1) { position: absolute; 
    transform: scaleX(.55) scaleY(.7) translate(30%, -25%);
    z-index: -1;  border: 0px solid black; }
    table th { display: none; }
    li { font-size: 19px; margin-left: -20px; width: 45% ; }
    li:nth-child(1) em { background-color: rgba(255,0,0,0.2); }
    li:nth-child(2) em { background-color: rgba(0,255,0,0.2); }
    li:nth-child(3) em { background-color: rgba(255,255,0,0.6); }
    li:nth-child(4) em { background-color: rgba(255,255,0,0.6); }
    li li { font-size: 14px; margin-left: -20px; width: 105% ; color: blue; margin-left:-40px}
    p { font-size: 13px;  width: 55%;  color: blue; }
    h2 {  margin-top: -60px; margin-bottom: 20px;  }
</style>

## Computing the information of BP

![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/bp-bar-chart-fm-efm-kv.jpg)

- Get full moon timeseries from 2400BCE to 800BCE. There are about *1237 FM per century - the top chart* <br><br><br>
- The series is then filtered for *Equinoctial Full Moons - the mid chart*<br><br><br><br><br>
- The series is further filtered for *EFM near kṛttikā and viśākhā - the bottom chart*
- The *yellow region* shows the epoch when the visible kṛttikā and viśākhā are contained in their respective sectors - **2000BCE to 1600BCE**
<!-- -  $$\lambda = L' + \frac{\sum l}{1{,}000{,}000};  \beta =  \frac{\sum b}{1{,}000{,}000}$$ -->
<!-- $$\lambda = 218.3164477+481267.88123421T -0.0015786T^2$$ 
$$+ \frac{1}{538841}T^3 - \frac{1}{65194000}T^4 + \frac{\sum l}{1{,}000{,}000}$$ -->



---   
<style scoped>

    {
        transform:  scale(.8) rotate(5deg) translate(0%, 0%);
        opacity: 0.4;
        border: 2px dashed red;
    }

    h2::after {
        content: "Skip";
        position: absolute;
        top: 0%;
        left: 0%;
        transform: translateY(0%) rotate(-5deg) scale(.5);
        opacity: 0.35;
        font-size: 15em;
    }

    img { height:240px; width:720px;margin-left: auto; margin-right: auto; }
    table th { display: none; }
    td { font-size: 13px; }
    table:nth-child(3) { margin-top:-3px; color: grey; }
    table:nth-child(4) { color: blue; margin-top:40px  } 
    h2 { font-size: 30px; margin-top: -50px; margin-bottom: -10px;  }
</style>

## Inferring the BP epoch

||
|--|
![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/bp-equinoctial-full-moon-better.jpg)

|||
|--:|:--|
Axes | BCE years on the x-axis and longitudes/nakṣatra sectors on the y-axis
Green Dots | **Equinoctial Full Moons**  
Red Sector | Extent of **Kṛttikā sector** containing SE *(Sun at 0°)* in its 1st amśa
Blue Sector | Extent of **Viśākhā sector** containing AE *(Sun at 180°)* in its 3rd amśa
Sloping Red/Blue| **Visible Kṛttikā/Viśākhā longitudes** adjusted for *precession*
Light Gray Band | Epoch when  **visible Kṛttikā/Viśākhā** are in **their respective sectors** ~*1980-1610 BCE*
Dark Gray Band| Epoch for **AE FM at 4th amśa of Viśākhā closest to visble Viśākhā** ~*1700-1610 BCE*

|||
|--|--|
**1980-1610 BCE** | The *visible Kṛttikā & Viśākhā* are *contained in their respective sectors* 
**1700-1610 BCE** | The equinoctial *FM  at ¾ viṣākhā sector is nearest to visible viśākhā* 
**Maghādi scheme** | The Maghādi scheme of MAU is consistent with the equinoctial full moon scheme of BP

---
<!-- <div class=page-break style="page-break-before:always"></div> <p></p> -->

Assuming the dakṣiṇāyana point to be the day 1 of the 366 day cycle, the following table shows the day number of the start of each ṛtu and ayanas.

<style scoped>
img { filter: invert(100%); height: 60px; }
{ font-size: 14px;}

/* td:nth-child(1) { width: 5%; }
td:nth-child(2) { width: 15%; }
td:nth-child(3) { width: 15%; }
td:nth-child(4) { width: 10%; }
td:nth-child(5) { width: 30%; } */
</style>

|day num | ṛtu | ayana | equinox/ solstice | sunrise image as seen by an observer |
|--:|---|---|---|:---|
|1| varṣā start | **dakṣiṇāyana start** | summer solstice | ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-01-ss.jpg) <br>sun rises north east
|62| śarad start| dakṣiṇāyana | - | -
|92 |śarad mid | **viṣuvat** | autumn equinox | ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-02-ae.jpg)  <br> sun rises true east
|123 | hemanta start  | dakṣiṇāyana | - |
|183<br>184 | śiśira start  | **dakṣiṇāyana end**<br> **uttarāyaṇa start**| winter solstice | ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-03-ws.jpg) <br> sun rises south east
|245 | vasanta start | uttarāyaṇa | - | -
|274 | vasanta mid | **viṣuvat** | spring equinox |  ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-04-se.jpg) <br> sun rises true east
|306 | grīṣma start | uttarāyaṇa | - | -
|366 | grīṣma-end | **uttarāyaṇa end**<br>**dakṣiṇāyana start**  | summer solstice | ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/swing-01-ss.jpg)  <br> sun rises north east


---

<style scoped>
    img { filter: invert(100%); transform: translate(-36%, -35%) scale(.30); border: 15px solid green; }
    li { font-size: 180%}
    li li { font-size: 100%}
    a::after { content: " 🔗"; }
</style>

## [Sun's annual cycle](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-ayana.gif)

- The sunrise point at horizon moves/swings from
    - north east to south east called **dakṣiṇāyana**
    - back to same north east called **uttarāyaṇa**
-   **366 sunrises** makes a cycle - a solar year
-   The sunrises are associated with specific background stars called **nakṣatra-s**
   
![(animation link for pdf)](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-ayana.gif)



---

## Sun and Nakṣatras

We noted that each of the 366 sunrises occurs at different points on the eastern horizon due to the sun's swing. In addition, the stars that are visible just prior to each sunrise at the sunrise point also change. The stars that are visible just prior to sunrise are said to belong to the nakṣatra of that day.  

During uttarāyaṇa and dakṣiṇāyana the sun seems to rise at a stationary point for about 14 days. The stars visible prior to sunrise for these two stationary points define the sector/span of a nakṣatra - of about 14 days - more precisely 13<sup>5</sup>/<sub>9</sub> days.

A nakṣatra is a span of time of about 14 days and contains the stars that are visible at sunrise in its time span. There are 27 such equal nakṣatra spans in a 366 day cycle. Each of the 27 nakṣtra while of equal time span contains varying counts of stars -  between 1 and 6 - totaling 83 stars. The 27 nakṣatra are named in a fixed cyclical order.

The current order starting from Aśvinī along with their star count listed below, is an inherited order from around 1500 years ago. The order of the nakṣatra begins with Kṛttikā and ends with Revatī in more ancient texts.

<style scoped>
    p { font-size: 13.8px; }
    table td {
        border: 1px dotted black;
        text-align: center;
        font-weight: bold;
        color: black;
        width: 14%;
        position: relative;
    }

    #never
    , table tr:nth-child(1) td:nth-child(6)
    , table tr:nth-child(1) td:nth-child(8)
    , table tr:nth-child(2) td:nth-child(5)
    , table tr:nth-child(2) td:nth-child(6)
    , table tr:nth-child(3) td:nth-child(6)
    , table tr:nth-child(3) td:nth-child(9)
    { background-color: rgba(255,0,0,0.1); font-size: 11px; }

    #never
    , table tr:nth-child(1) td:nth-child(7)
    , table tr:nth-child(2) td:nth-child(2)
    , table tr:nth-child(2) td:nth-child(3)
    , table tr:nth-child(2) td:nth-child(7)
    , table tr:nth-child(3) td:nth-child(7)
    , table tr:nth-child(3) td:nth-child(8)
    { background-color: rgba(255,0,0,0.3); font-size: 12px; }

    #never
    , table tr:nth-child(1) td:nth-child(1)
    , table tr:nth-child(1) td:nth-child(2)
    , table tr:nth-child(1) td:nth-child(5)
    , table tr:nth-child(2) td:nth-child(9)
    , table tr:nth-child(3) td:nth-child(4)
    { background-color: rgba(255,0,0,0.5); font-size: 13px; }

    #never
    , table tr:nth-child(2) td:nth-child(8)
    , table tr:nth-child(3) td:nth-child(1)
    , table tr:nth-child(3) td:nth-child(2)
    , table tr:nth-child(3) td:nth-child(3)
    , table tr:nth-child(3) td:nth-child(5)
    { background-color: rgba(255,0,0,0.6); font-size: 14px; }


    #never
    , table tr:nth-child(1) td:nth-child(4)
    , table tr:nth-child(2) td:nth-child(4)
    { background-color: rgba(255,0,0,0.8); font-size: 15px; }
    
    #never
    , table tr:nth-child(1) td:nth-child(3)
    , table tr:nth-child(1) td:nth-child(9)
    , table tr:nth-child(2) td:nth-child(1)
    { background-color: rgba(255,0,0,1); font-size: 16px; }

</style>


||||||||||
|--|--|--|--|--|--|--|--|--|
|Aśvinī<br>3|Bharaṇī<br>3|Kṛttikā<br>6|Rohiṇī<br>5|Mṛgaśiras<br>3|Ārdrā<br>1|Punarvasu<br>2|Puṣya<br>1|Aśleṣā<br>6|
|Maghā<br>6|Pūrva<br>Phalgunī<br>2|Uttara<br>Phalgunī<br>2|Hasta<br>5|Citrā<br>1|Svātī<br>1|Viśākhā<br>2|Anurādhā<br>4|Jyeṣṭhā<br>3|
|Mūla<br>4|Pūrva<br>Aṣāḍhā<br>4|Uttara<br>Aṣāḍhā<br>4|Śravaṇa<br>3|Śraviṣṭhā<br>4|Śatabhiṣā<br>1|Pūrva<br>Bhādrapadā<br>2|Uttara<br>Bhādrapadā<br>2|Revatī<br>1|:


The choice of the first nakṣatra to start the cycle contains information on the epoch and the convention for the year start.

There are texts that associate specific nakṣatras with the ṛtus - seasonal naḳsatras .  Such seasonal naḳsatras also contain vital information on the epoch of the text.

---

<style scoped>
    img { filter: invert(%); zoom: 20%; float: right; }
    p, li{ font-size: large;  }
    p { font-size: 150%; font-weight: bold; margin-top: 30px   }
</style>

## Nakṣatra-s starting from Maghā at day 1


![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/daynum-dial-season-1700-bce.jpg)

<!-- |#|nakṣatra | day span | number of stars | cumulative stars |
|-:|---:|:---:|:---|--|
 1|Maghā            |  1-14 | 6 | 6
 2|Pūrva Phalgunī   | 14-28 | 2 | 8
 3|Uttara Phalgunī  | 27-41 | 2 | 10
 4|Hasta            | 40-55 | 5 | 15
 5|Citrā            | 54-68 | 1 | 16
 6|Svātī            | 67-82 | 1 | 17
 7|Viśākhā          | 81-95 | 2 | 19
 8|Anurādhā         | 94-109| 4 | 23
 9|Jyeṣṭhā          |109-123| 3 | 26
10|Mūla             |123-136| 6 | 32
11|Pūrva Aṣāḍhā     |136-150| 4 | 36
12|Uttara Aṣāḍhā    |150-163| 4 | 40
13|Śravaṇa          |163-177| 3 | 43
14|Śraviṣṭhā        |177-190| 4 | 47
15|Śatabhiṣā        |190-204| 1 | 48
16|Pūrva Bhādrapadā |204-217| 2 | 50
17|Uttara Bhādrapadā|217-231| 2 | 52
18|Revatī           |231-245| 1 | 53
19|Aśvinī           |245-258| 3 | 56
20|Bharaṇī          |258-272| 3 | 59
21|Kṛttikā          |272-285| 6 | 65
22|Rohiṇī           |285-299| 5 | 70
23|Mṛgaśiras        |299-312| 3 | 73
24|Ārdrā            |312-326| 1 | 74
25|Punarvasu        |326-339| 2 | 76
26|Puṣya            |339-353| 1 | 77
27|Aśleṣā           |353-366| 6 | 83 -->


In this Maghādi epoch day 1 of dakṣiṇāyana is at Maghā start. 
  - The sun traverses through the 27 nakṣatras in order and returns to Maghā start at the end of the 366 day cycle.
  - The  1st and 367th sunrise are at
    - the same nakṣatra/star - Maghā/ε-Leonis
    - the same point on the horizon and
  
Over 100's of years, 
- the nakṣatra/star to shift by about 1 day in about 72 years. 
-  This shift is called the ayanāṃśa/precession.


---

<style scoped>
    img { filter: invert(%); zoom: 20%; float: right; }
    { font-size: 15px;}
    em { background-color: rgba(255,0,0,0.1); }
</style>

## Precession and its effects

![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/sun-moon-season-precession-dial.jpg)
We see the start of Maghā nakṣatra on day 1 of dakṣiṇāyana in the chart above. This is true for a certain epoch. After about a 1000 years, the start of Maghā nakṣatra will be on day 14 of dakṣiṇāyana. Equivalently day 1 of dakṣiṇāyana will move to Āśleṣā start. 

*The precession is a slow process and takes about 25,800 years to complete one cycle. That is the sunrise point will return to the same nakṣatra/star for the same ṛtu after **25,800 years.***

Precession causes the seasonal nakṣatras to drift with time.  Many ancient text associate nakṣhatras with seasons - this association contains vital information on the epoch of the text.

The direction of precession is opposite to the direction of the  sun's annual transit through the nakshatras. Incidentally the moon also transits through the nakṣatras in the same direction as the sun. The moon's transit through the nakṣatras is called the lunar month of about 27 days.

---

## Effect of precession over millennia
<style scoped>
    li { font-size: 14px;} */
</style>

-   About every 1000 years the start of season move backwark by one naḳsatra. In addition the precession causes the pole star to change. 

-   The following table/pictures shows the start of the spring equinox seasonal naḳsatra and the pole star for the last 5000 years.


<style scoped>
    th:nth-child(6) { display: none; }
    td:nth-child(6) { display: none; }
    img { filter: invert(100%); height: 240px; }
    table tr:nth-child(1) td:nth-child(1) img { filter: invert(80%); }
</style>

|Epoch|Spring Equinox|Dakṣiṇāyana|Uttaryāṇa | Pole Star|Image|
|---|---|---|---|---|--|
|Present|Uttara Bhādrapadā|Ārdrā|Mūla|Polaris|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-01-2000-ce.jpg)
|1000 years ago|Revatī|Punarvasu|Pūrva Aṣāḍhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-02-1000-ce.jpg)
|2000 years ago|Aṡvinī|Puṣya|Uttara Aṣāḍhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-03-0000-ce.jpg)
|3000 years ago|Bharanī|Aśleṣā|Śravaṇa|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-04-1000-bce.jpg)
|4000 years ago|Kṛttikā|Maghā|Śraviṣṭhā|-|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-05-2000-bce.jpg)
|5000 years ago|Rohiṇī|Pūrva Phalgunī |Śatabhiṣā|Thuban|![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-06-3000-bce.jpg)

|||
|:---:|:--:|
|Present Day <br> ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-01-2000-ce.jpg) | 5000 years ago <br> ![](https://cahc.jainuniversity.ac.in/assets/talks/2023-12-05-iks-cahc/maghaadi/prec-06-3000-bce.jpg)|


---
<style scoped>
    img { filter: invert(100%); transform: scale(0.30);  transform-origin: 0 0; }
    a::after { content: " 🔗"; }
</style>

## [Precession over 5000 years](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-precession.gif)



![Precession over 5000 years](https://cahc.jainuniversity.ac.in/assets/talks/bihs/sun-transit/sun-transit-precession.gif)
