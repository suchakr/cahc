<h2> Indian Journal of History of Science - Classified Papers</h2>

<script>
function highlightText(text, filter) {
    if (!filter) return text;
    const regex = new RegExp(`(${filter})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

function filterTable() {
    const input = document.getElementById("searchInput");
    const filter = input.value.toLowerCase();
    const table = document.getElementById("papers");
    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName("td");
        let show = false;
        let rowHtml = '';
        
        for (let j = 0; j < cells.length; j++) {
            const cell = cells[j];
            const text = cell.textContent || cell.innerText;
            
            if (text.toLowerCase().includes(filter)) {
                show = true;
            }
            
            // For cells with links, preserve the link while highlighting
            if (cell.getElementsByTagName("a").length > 0) {
                const link = cell.getElementsByTagName("a")[0];
                const href = link.getAttribute("href");
                rowHtml += `<td><a href="${href}">${highlightText(text, filter)}</a></td>`;
            } else {
                rowHtml += `<td>${highlightText(text, filter)}</td>`;
            }
        }
        
        if (show) {
            rows[i].style.display = "";
            rows[i].innerHTML = rowHtml;
        } else {
            rows[i].style.display = "none";
        }
    }
}

// Debounce helper function
function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

// Debounced filter function
const debouncedFilter = debounce(filterTable, 500 );

// Clear search box on page load
window.onload = function() {
    document.getElementById("searchInput").value = "";
    filterTable();
}
</script>

<input type="text" id="searchInput" placeholder="Search..." style="width: 100%; padding: 12px 20px; margin: 8px 0; box-sizing: border-box;" onkeyup="debouncedFilter()">


<table id="papers">
<tr>
<th>#</th>
<th>Journal</th>
<th>Subject</th>
<th>Category</th>
<th>Paper</th>
<th>Author</th>
<th>Size (KB)</th>
</tr>
<tr>
<td>1</td>
<td>IJHS-1-1966-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_1_PRay.pdf'>The Theory of Chemical Combination in Ancient Indian Philosophies </a></td>
<td> Priyadaranjan Ray</td>
<td>272</td>
</tr>
<tr>
<td>2</td>
<td>IJHS-1-1966-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_2_JRRavetz.pdf'>What was ‘The Scientific Revolution’ ? </a></td>
<td> J R Ravetz</td>
<td>133</td>
</tr>
<tr>
<td>3</td>
<td>IJHS-1-1966-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_3_MHoskin.pdf'>Stellar Distances: Galileo's Method and Its Subsequent History </a></td>
<td> Michael Hoskin</td>
<td>189</td>
</tr>
<tr>
<td>4</td>
<td>IJHS-1-1966-Issue-1</td>
<td>Math</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_4_DJDSPrice.pdf'>A Survival of Babylonian Arithmetic in ew Guinea? </a></td>
<td> Derek J De Solla Price</td>
<td>80</td>
</tr>
<tr>
<td>5</td>
<td>IJHS-1-1966-Issue-1</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_5_SNSen.pdf'>The Impetus Theory of the Vaisesikas </a></td>
<td> S N Sen</td>
<td>261</td>
</tr>
<tr>
<td>6</td>
<td>IJHS-1-1966-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_6_VRonchi.pdf'>New History of Optical Microscope </a></td>
<td> Vasco Ronchi</td>
<td>275</td>
</tr>
<tr>
<td>7</td>
<td>IJHS-1-1966-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_7_VSubbarayappa.pdf'>The Indian Doctrine of Five Elemnets </a></td>
<td> V Subbarayappa</td>
<td>174</td>
</tr>
<tr>
<td>8</td>
<td>IJHS-1-1966-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_8_AKBag.pdf'>Binomial Theorem in Ancient India </a></td>
<td> Amulya Kumar Bag</td>
<td>134</td>
</tr>
<tr>
<td>9</td>
<td>IJHS-1-1966-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_1_9_BRensch.pdf'>Problems of Biological Philisophy with regard to the Philosophy of the Upanisads </a></td>
<td> Bernhard Rensch</td>
<td>147</td>
</tr>
<tr>
<td>10</td>
<td>IJHS-1-1966-Issue-2</td>
<td>Astronomy</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_1_WPetri.pdf'>Uigur and Tibetian Lists of the Indian Lunar Mansions </a></td>
<td> Winfried Petri</td>
<td>187</td>
</tr>
<tr>
<td>11</td>
<td>IJHS-1-1966-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_2_MRoy.pdf'>Methods of Sterilization and Sex– Determinaton in the Arthava–Veda and in the Brhad–Aranyakopanishad </a></td>
<td> Mira Roy</td>
<td>171</td>
</tr>
<tr>
<td>12</td>
<td>IJHS-1-1966-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_3_AKBag.pdf'>Trigonometrical Series in the Karanapaddhati and the Probable Date of the Text </a></td>
<td> A K Bag</td>
<td>174</td>
</tr>
<tr>
<td>13</td>
<td>IJHS-1-1966-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_4_SPRaychaudhuri.pdf'>Land Classification in Ancient India </a></td>
<td> S P Raychaudhuri</td>
<td>117</td>
</tr>
<tr>
<td>14</td>
<td>IJHS-1-1966-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_5_SNSen.pdf'>Introduction of Western Science in India </a></td>
<td> S N Sen</td>
<td>284</td>
</tr>
<tr>
<td>15</td>
<td>IJHS-1-1966-Issue-2</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_6_MTanaka.pdf'>Characteristics of the History of Science and Technology of Modern Japan </a></td>
<td> Minoru Tanaka</td>
<td>245</td>
</tr>
<tr>
<td>16</td>
<td>IJHS-1-1966-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_7_SAKGhori.pdf'>Paper Technology in Medieval India </a></td>
<td> S A K Ghori and A Rahman</td>
<td>314</td>
</tr>
<tr>
<td>17</td>
<td>IJHS-1-1966-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_8_RKGupta.pdf'>Botanical Explorations of Victor Jacquemont </a></td>
<td> Raj Kumar Gupta</td>
<td>239</td>
</tr>
<tr>
<td>18</td>
<td>IJHS-1-1966-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol01_2_9_Notes.pdf'>Notes </a></td>
<td> </td>
<td>84</td>
</tr>
<tr>
<td>19</td>
<td>IJHS-2-1967-Issue-1</td>
<td>Metallurgy</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_1_1_PRay.pdf'>Origin and Tradition of Alchemy </a></td>
<td> Priyadaranjan Ray</td>
<td>426</td>
</tr>
<tr>
<td>20</td>
<td>IJHS-2-1967-Issue-1</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_1_2_BVSubbarayappa.pdf'>An Estimate of the Vaisesika Sutra in the History of Science </a></td>
<td> B V Subbarayappa</td>
<td>286</td>
</tr>
<tr>
<td>21</td>
<td>IJHS-2-1967-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_1_3_MRoy.pdf'>Anatomy in the Vedic Literature </a></td>
<td> Mira Roy</td>
<td>263</td>
</tr>
<tr>
<td>22</td>
<td>IJHS-2-1967-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_1_4_BMohan.pdf'>History of Plus and Minus Signs </a></td>
<td> Brij Mohan</td>
<td>108</td>
</tr>
<tr>
<td>23</td>
<td>IJHS-2-1967-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_1_5_MChowdhury.pdf'>The Embryonic Development and the Human Body in the Yajnavalkya Smrti </a></td>
<td> Mamata Choudhury</td>
<td>176</td>
</tr>
<tr>
<td>24</td>
<td>IJHS-2-1967-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_1_6_Reviews.pdf'>Reviews </a></td>
<td> </td>
<td>207</td>
</tr>
<tr>
<td>25</td>
<td>IJHS-2-1967-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_2_1_VDMarza.pdf'>The Problem of the Fertilization and Evolution of Phanerogams in Darwin’s Work: A Critical Study </a></td>
<td> Vasile D Marza and Ion T Tarnavschi</td>
<td>841</td>
</tr>
<tr>
<td>26</td>
<td>IJHS-2-1967-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_2_2_HIJhala.pdf'>WMW Haffkine‚ Bacteriologist—A Great Saviour of Mankind </a></td>
<td> H I Jhala</td>
<td>394</td>
</tr>
<tr>
<td>27</td>
<td>IJHS-2-1967-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_2_3_RCGupta.pdf'>Bhaskara I’s Approximation to Sine </a></td>
<td> R C Gupta</td>
<td>246</td>
</tr>
<tr>
<td>28</td>
<td>IJHS-2-1967-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_2_4_Notes.pdf'>Notes: Rasarnavakalpa of Rudrayamala Tantra </a></td>
<td> Mira Roy</td>
<td>99</td>
</tr>
<tr>
<td>29</td>
<td>IJHS-2-1967-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_2_5_News.pdf'>News </a></td>
<td> </td>
<td>18</td>
</tr>
<tr>
<td>30</td>
<td>IJHS-2-1967-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol02_2_6_Review.pdf'>Review </a></td>
<td> P Ray</td>
<td>51</td>
</tr>
<tr>
<td>31</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_1_AKBag.pdf'>Source Materials Concerning Astronomy and Mathematics </a></td>
<td> A K Bag</td>
<td>85</td>
</tr>
<tr>
<td>32</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Agriculture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_2_KAChowdhury.pdf'>Archaeological Plant Remainsfrom Pre– and Proto–Historic Periods as a Source of Historyof Sciences </a></td>
<td> K A Chowdhury</td>
<td>117</td>
</tr>
<tr>
<td>33</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_3_GSDikshit.pdf'>The Sivatattvratnakara as a Source for Sciences in Ancient and Medieval India </a></td>
<td> G S Dikshit</td>
<td>81</td>
</tr>
<tr>
<td>34</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_4_CGKashikar.pdf'>Pottery in the Vedic Literature </a></td>
<td> C G Kashikar</td>
<td>245</td>
</tr>
<tr>
<td>35</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_5_TMPMahadevan.pdf'>Philosophical Trends viz History of Sciences of India — Orthodox Systems </a></td>
<td> T M P Mahadevan</td>
<td>306</td>
</tr>
<tr>
<td>36</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_6_GCPande.pdf'>Philosophical Trends and the History of Science in India— Heterodox Trends </a></td>
<td> G C Pande</td>
<td>200</td>
</tr>
<tr>
<td>37</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_7_SGopal.pdf'>Social Set–Up of Science and Technology in Mughal India </a></td>
<td> Surendra Gopal</td>
<td>158</td>
</tr>
<tr>
<td>38</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_8_TASaraswathi.pdf'>Development of Mathematical Ideas in India </a></td>
<td> T A Saraswathi</td>
<td>421</td>
</tr>
<tr>
<td>39</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_9_AKBag.pdf'>Sine Table in Ancient India </a></td>
<td> AK Bag</td>
<td>133</td>
</tr>
<tr>
<td>40</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_10_RCGupta.pdf'>Second Order Interpolation in Indian Mathematics Up To the Fifteenth Century </a></td>
<td> B C Gupta</td>
<td>233</td>
</tr>
<tr>
<td>41</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_11_KSShukla.pdf'>Astronomy in Ancient and Medieval India </a></td>
<td> K S Shukla</td>
<td>146</td>
</tr>
<tr>
<td>42</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_12_TSKShastri.pdf'>A Historical Development of Certain Hindu Astronomical Processes </a></td>
<td> T S K Shastri</td>
<td>482</td>
</tr>
<tr>
<td>43</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_13_TSKShastri.pdf'>The System of the Vatesvara Siddhanta </a></td>
<td> T S K Shastri</td>
<td>189</td>
</tr>
<tr>
<td>44</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_14_SPBhattacharyya.pdf'>Ahargana In Hindu Astronomy </a></td>
<td> S P Bhattacharyya</td>
<td>221</td>
</tr>
<tr>
<td>45</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_15_News.pdf'>News </a></td>
<td> </td>
<td>36</td>
</tr>
<tr>
<td>46</td>
<td>IJHS-4-1969-Issue-1&2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol04_1And2_16_Review.pdf'>Book Review: Digestion and Metabolism in Ayurveda by C Dwarkanath </a></td>
<td> P V Sharma</td>
<td>57</td>
</tr>
<tr>
<td>47</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_1_CDwarkanath.pdf'>Some Significant Aspects of The Origin and Development of Medicine in Ancient India </a></td>
<td> C Dwarkanath</td>
<td>325</td>
</tr>
<tr>
<td>48</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_2_PJDeshpande.pdf'>Contribution to the Fundamentala of Orthopaedic Surgery </a></td>
<td> P J Deshpande</td>
<td>525</td>
</tr>
<tr>
<td>49</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_3_LMSingh.pdf'>Susruta’s Contributions to the Fundamentals of Surgery </a></td>
<td> L M Singh</td>
<td>366</td>
</tr>
<tr>
<td>50</td>
<td>IJHS-5-1970-Issue-1</td>
<td>nan</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_4_DSGaur.pdf'>The Theory of Pancamahabhuta with Special Reference to Ayurveda </a></td>
<td> D S Gaur</td>
<td>422</td>
</tr>
<tr>
<td>51</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_5_JMitra.pdf'>Methodology for Experimental Research In Ancient India </a></td>
<td> Jyotir Mitra</td>
<td>215</td>
</tr>
<tr>
<td>52</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_6_SGurumurthy.pdf'>Medical Science and Dispensaries in Ancient South India as Gleaned From Epigraphy </a></td>
<td> S Gurumurthy</td>
<td>97</td>
</tr>
<tr>
<td>53</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_7_RSSMurthy.pdf'>The Brahmanas on Medicine and Biological Sciences </a></td>
<td> R S Shivaganesha Murthy</td>
<td>116</td>
</tr>
<tr>
<td>54</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_8_PRay.pdf'>Medicine—As it Evolved in Ancient and Medieval India </a></td>
<td> Priyadaranjan Ray</td>
<td>289</td>
</tr>
<tr>
<td>55</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_9_BBMishra.pdf'>Human Anatomy According to the Agni Purana </a></td>
<td> B B Mishra</td>
<td>219</td>
</tr>
<tr>
<td>56</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_10_RCChakravorty.pdf'>Surgical Principles in the Sutrasthanam of the Susruta Samhita </a></td>
<td> R C Chakravorty</td>
<td>109</td>
</tr>
<tr>
<td>57</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_11_RNKapil.pdf'>Biology in Ancient and Medieval India </a></td>
<td> R N Kapil</td>
<td>463</td>
</tr>
<tr>
<td>58</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_12_KAChowdhury.pdf'>Wood and its Use During Pre–and Proto–Historic Time </a></td>
<td> K A Chowdhury</td>
<td>53</td>
</tr>
<tr>
<td>59</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_13_VMittre.pdf'>Biological Concepts and Agriculture in Ancient India </a></td>
<td> Vishnu Mittre</td>
<td>352</td>
</tr>
<tr>
<td>60</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_14_MRoy.pdf'>Family Relations of Some Plants in The Atharvaveda </a></td>
<td> Mira Roy</td>
<td>351</td>
</tr>
<tr>
<td>61</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_15_SPRaychaudhuri.pdf'>History of Land Use in India </a></td>
<td> S P Raychaudhuri</td>
<td>29</td>
</tr>
<tr>
<td>62</td>
<td>IJHS-5-1970-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_1_16_MSShukla.pdf'>Arbori–Horticulture in Ancient India </a></td>
<td> M S Shukla</td>
<td>83</td>
</tr>
<tr>
<td>63</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_1_JCSikdar.pdf'>Jaina Atomic Theory </a></td>
<td> J C Sikdar</td>
<td>488</td>
</tr>
<tr>
<td>64</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_2_GNChakravarthy.pdf'>Concept of The Structure of Space–Time </a></td>
<td> G N Chakravarthy</td>
<td>216</td>
</tr>
<tr>
<td>65</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_3_HCBhardwaj.pdf'>Problem of Advent of Copper in India </a></td>
<td> H C Bhardwaj</td>
<td>180</td>
</tr>
<tr>
<td>66</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_4_DPAgrawal.pdf'>Metal Technology of The Harappa Culture and Its Socio–Economic Implications </a></td>
<td> D P Agrawal</td>
<td>236</td>
</tr>
<tr>
<td>67</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_5_BKGRao.pdf'>Development of Technology During The Iron Age in South India </a></td>
<td> B K Gururaja Rao</td>
<td>388</td>
</tr>
<tr>
<td>68</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_6_MChoudhury.pdf'>The Techniques of Colouring Glass and Ceramic Materials in Ancient and Medieval India </a></td>
<td> Mamata Chowdhury</td>
<td>230</td>
</tr>
<tr>
<td>69</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_7_VGovind.pdf'>Some Aspects of Glass Manufacturing in Ancient India </a></td>
<td> Vijay Govind</td>
<td>521</td>
</tr>
<tr>
<td>70</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_8_TVMahalingam.pdf'>The South Indian Temple– Medium of Construction </a></td>
<td> T V Mahalingam</td>
<td>127</td>
</tr>
<tr>
<td>71</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_9_TMSrinivasan.pdf'>A Brief Account of the Ancient Irrigation Engineering Systems Prevalent in South India </a></td>
<td> T M Srinivasan</td>
<td>216</td>
</tr>
<tr>
<td>72</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_10_JFilliozat.pdf'>Influence of Mediterranean Culture Areas on Indian Science </a></td>
<td> Jean Filliozat</td>
<td>123</td>
</tr>
<tr>
<td>73</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_11_SNSen.pdf'>Influence of Indian Science on Other Culture Areas </a></td>
<td> S N Sen</td>
<td>358</td>
</tr>
<tr>
<td>74</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_12_RLVerma.pdf'>The Growth of Greco–Arabian Medicine in Medieval India </a></td>
<td> R L Verma</td>
<td>402</td>
</tr>
<tr>
<td>75</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_13_PVSharma.pdf'>The Date of Dhanvantari Nighantu </a></td>
<td> P V Sharma</td>
<td>154</td>
</tr>
<tr>
<td>76</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_14_HCShukla.pdf'>Ideas of Scientific Measurement in Basic Principkles of Ayurveda with Special Reference to Somatometry </a></td>
<td> H C Shukla</td>
<td>160</td>
</tr>
<tr>
<td>77</td>
<td>IJHS-5-1970-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol05_2_15_TMSrinivasan.pdf'>Water–Lifting Devices in Ancient India: Their Origin and Mechanisms </a></td>
<td> T M Srinivasan</td>
<td>161</td>
</tr>
<tr>
<td>78</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_1_MNDeshpande.pdf'>Archaeological Sources for the Reconstruction of The History of Sciences of India </a></td>
<td> M N Deshpande</td>
<td>433</td>
</tr>
<tr>
<td>79</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_2_RSengupta.pdf'>Inluence of Certain Harappan Architectural Features on Some Texts of Early–Historical Period </a></td>
<td> R Sengupta</td>
<td>94</td>
</tr>
<tr>
<td>80</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vo0l6_1_3_RNRai.pdf'>Karanasara of Vatesvara </a></td>
<td> RN Rai</td>
<td>177</td>
</tr>
<tr>
<td>81</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_4_NKPanikkar.pdf'>The Concept of Tides in Ancient India </a></td>
<td> N K Panikkar</td>
<td>335</td>
</tr>
<tr>
<td>82</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_5_RCGupta.pdf'>Fractional Parts of Aryabhata's Sines and Certain Rules </a></td>
<td> R C Gupta</td>
<td>149</td>
</tr>
<tr>
<td>83</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_6_AVCarozzi.pdf'>Lucien Cayeux: A Challenger of the Principle of Uniformity in Geology? </a></td>
<td> Albert V Carozzi</td>
<td>124</td>
</tr>
<tr>
<td>84</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_7_PVSharma.pdf'>Triamlla Bhatta: His Date and Works in 100 Verses </a></td>
<td> P V Sharma</td>
<td>172</td>
</tr>
<tr>
<td>85</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_8_VMukherji.pdf'>A Short History of the Meson Theory from 1935 to 1943_I </a></td>
<td> V Mukherji</td>
<td>521</td>
</tr>
<tr>
<td>86</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_9_BMChintamani.pdf'>Histrory of Sciences in india: Pali Sources </a></td>
<td> B M Chintamani and B V Subbarayyapa</td>
<td>195</td>
</tr>
<tr>
<td>87</td>
<td>IJHS-6-1971-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_1_10_BookReviews.pdf'>Book Review </a></td>
<td> </td>
<td>63</td>
</tr>
<tr>
<td>88</td>
<td>IJHS-6-1971-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_2_1_VMukherji.pdf'>A Short History of the Meson Theory from 1935 to 1943_II </a></td>
<td> V Mukherji</td>
<td>354</td>
</tr>
<tr>
<td>89</td>
<td>IJHS-6-1971-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_2_2_RNRai.pdf'>The Extant Siddhanta Sekhra: An Error in one of its Sine Values </a></td>
<td> R N Rai</td>
<td>70</td>
</tr>
<tr>
<td>90</td>
<td>IJHS-6-1971-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_2_3_EGKRao.pdf'>Exploration of Underground Water Springs According to the Ancient Hindus </a></td>
<td> E G K Rao</td>
<td>165</td>
</tr>
<tr>
<td>91</td>
<td>IJHS-6-1971-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_2_4_RNRai.pdf'>The Ardharatrika System of Aryabhata I </a></td>
<td> R N Rai</td>
<td>123</td>
</tr>
<tr>
<td>92</td>
<td>IJHS-6-1971-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_2_5_GPSharma.pdf'>Sivadasa Sen— A Scholar Commentator on Indian Medicine of Later Medieval Period </a></td>
<td> G P Sharma and P V Sharma</td>
<td>278</td>
</tr>
<tr>
<td>93</td>
<td>IJHS-6-1971-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol06_2_6_BMChintamani.pdf'>Notices of Thirteen Mss. In Prakrit </a></td>
<td> B M Chintamani</td>
<td>111</td>
</tr>
<tr>
<td>94</td>
<td>IJHS-7-1972-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_1_1_RNRai.pdf'>Sine Values of the Vatesvara Siddhanta </a></td>
<td> R N Rai</td>
<td>252</td>
</tr>
<tr>
<td>95</td>
<td>IJHS-7-1972-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_1_2_NKPanikkar.pdf'>Kappal Sattiram: A Tamil Treatise on Shipbuilding During the Seventeenth Century AD </a></td>
<td> N K Panikkar and T M Srinivasan</td>
<td>216</td>
</tr>
<tr>
<td>96</td>
<td>IJHS-7-1972-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_1_3_RNRai.pdf'>Calculation of Ahargana in the Vatesvara Siddhanta </a></td>
<td> R N Rai</td>
<td>311</td>
</tr>
<tr>
<td>97</td>
<td>IJHS-7-1972-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_1_4_ALSharma.pdf'>Botany in the Vedas (Part I) </a></td>
<td> A L Sharma‚ A B Seerwani and V R Shastry</td>
<td>134</td>
</tr>
<tr>
<td>98</td>
<td>IJHS-7-1972-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_1_5_SNSen.pdf'>Scientific Works in Sanskrit‚ Translated into Foreign Languages and Vice–Versa in the 18th and 19th Century AD </a></td>
<td> S N Sen</td>
<td>531</td>
</tr>
<tr>
<td>99</td>
<td>IJHS-7-1972-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_1_6_Notes_AKBag.pdf'>Notes: The Sine Table in Ancient India </a></td>
<td> A K Bag</td>
<td>66</td>
</tr>
<tr>
<td>100</td>
<td>IJHS-7-1972-Issue-1</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_1_7_News.pdf'>News: Symposium on Al–Biruni and the Indian Sciences </a></td>
<td> B V Subbarayappa</td>
<td>62</td>
</tr>
<tr>
<td>101</td>
<td>IJHS-7-1972-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_1_8_BookReview.pdf'>Book Review: Teaching the History of Chemistry </a></td>
<td> A Rehman</td>
<td>37</td>
</tr>
<tr>
<td>102</td>
<td>IJHS-7-1972-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_2_1_RCGupta.pdf'>Early Indians on Second Order Sine Differences </a></td>
<td> R C Gupta</td>
<td>132</td>
</tr>
<tr>
<td>103</td>
<td>IJHS-7-1972-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_2_2_PVSharma.pdf'>Jejatta (9th Century AD) and his Informations about Indian Drugs </a></td>
<td> P V Sharma and G P Sharma</td>
<td>237</td>
</tr>
<tr>
<td>104</td>
<td>IJHS-7-1972-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_2_3_TKBiswas.pdf'>Asoka (Saraca Indica Linn)— A Cultural and Scientific Evaluation </a></td>
<td> T K Biswas and P K Debnath</td>
<td>372</td>
</tr>
<tr>
<td>105</td>
<td>IJHS-7-1972-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_2_4_SDSharma.pdf'>Maxima and Minima of Tithis </a></td>
<td> S D Sharma</td>
<td>98</td>
</tr>
<tr>
<td>106</td>
<td>IJHS-7-1972-Issue-2</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_2_5_VVRaman.pdf'>Relativity in the Early Twenties: Many–Sided Reactions to a Great Theory </a></td>
<td> V V Raman</td>
<td>600</td>
</tr>
<tr>
<td>107</td>
<td>IJHS-7-1972-Issue-2</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_2_6_Notes_VMukherjee.pdf'>Notes: An Historical Note: The Meson Mass Value in the History of Yukawa Theory </a></td>
<td> V Mukherji</td>
<td>165</td>
</tr>
<tr>
<td>108</td>
<td>IJHS-7-1972-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_2_7_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>46</td>
</tr>
<tr>
<td>109</td>
<td>IJHS-7-1972-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol07_2_8_News.pdf'>News </a></td>
<td> </td>
<td>24</td>
</tr>
<tr>
<td>110</td>
<td>IJHS-8-1973-Issue-1&2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol08_1and2_1_LCJain.pdf'>Set Theory in Jaina School of Mathematics </a></td>
<td> L C Jain</td>
<td>570</td>
</tr>
<tr>
<td>111</td>
<td>IJHS-8-1973-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol08_1and2_2_KDSwaminathan.pdf'>Jyotisa in Kerala </a></td>
<td> K D Swaminathan</td>
<td>185</td>
</tr>
<tr>
<td>112</td>
<td>IJHS-8-1973-Issue-1&2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol08_1and2_3_JNSharma.pdf'>Arthritis in Ancient Indian Literature </a></td>
<td> J N Sharma‚ Jagadish N Sharma and R B Arora</td>
<td>131</td>
</tr>
<tr>
<td>113</td>
<td>IJHS-8-1973-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol08_1and2_4_KSShukla.pdf'>Use of Hypotenuse in the Computation of the Equation of the Centre under the Epicyclic Theory in the School of Aryabhatta I??? </a></td>
<td> K S Shukla</td>
<td>316</td>
</tr>
<tr>
<td>114</td>
<td>IJHS-8-1973-Issue-1&2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol08_1and2_5_KKTiwari.pdf'>A Thirteenth Century Indian Reference to Plant Nematodes </a></td>
<td> K K Tiwari and T R Mitra</td>
<td>63</td>
</tr>
<tr>
<td>115</td>
<td>IJHS-8-1973-Issue-1&2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol08_1and2_6_BGLSwamy.pdf'>Sources for a History of Plant Sciences in India </a></td>
<td> B G L Swamy</td>
<td>769</td>
</tr>
<tr>
<td>116</td>
<td>IJHS-8-1973-Issue-1&2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol08_1and2_7_KRAlur.pdf'>The Faunal Studies in Archaeology </a></td>
<td> K R Alur</td>
<td>577</td>
</tr>
<tr>
<td>117</td>
<td>IJHS-8-1973-Issue-1&2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol08_1and2_8_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>231</td>
</tr>
<tr>
<td>118</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_6_TSKuppannasastry.pdf'>The Main Characteristics of Hindu Astronomy in the Period Corresponding to Pre-Copernican.. </a></td>
<td> T S Kuppannasastry</td>
<td>261</td>
</tr>
<tr>
<td>119</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol09_1_1_EKKharadze.pdf'>Copernicus and Modern Science </a></td>
<td> Eugene K Kharadze</td>
<td>110</td>
</tr>
<tr>
<td>120</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol09_1_2_JSmak.pdf'>Copernicus and His Theory </a></td>
<td> Jozef Smak</td>
<td>41</td>
</tr>
<tr>
<td>121</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol09_1_3_ATrautman.pdf'>Copernicus and Modern Physics and Cosmology </a></td>
<td> Andrzej Trautman</td>
<td>44</td>
</tr>
<tr>
<td>122</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol09_1_4_SCJoshi.pdf'>Nicolaus Copernicus and the Commentariolus </a></td>
<td> S C Joshi</td>
<td>172</td>
</tr>
<tr>
<td>123</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol09_1_5_SKGhosh.pdf'>Nicolaus Copernicus and His Heliocentric Theory </a></td>
<td> Samir Kumar Ghosh</td>
<td>106</td>
</tr>
<tr>
<td>124</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol09_1_6_TSKuppannasastry.pdf'>The Main Characteristics of Hindu Astronomy in the Period Corresponding to Pre–Copernican European Astronomy </a></td>
<td> T S Kuppannasastry</td>
<td>261</td>
</tr>
<tr>
<td>125</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_7_RNRai.pdf'>The Prime Meridian in Indian Astronomy </a></td>
<td> R N Rai</td>
<td>107</td>
</tr>
<tr>
<td>126</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_8_BChatterjee.pdf'>A Glimpse of Aryabhata’s Theory of Rotation of Earth </a></td>
<td> Bina Chatterjee</td>
<td>106</td>
</tr>
<tr>
<td>127</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_9_CGPendse.pdf'>Copernican Heliocentric Theory and Indian Astronomy (AD 1500) </a></td>
<td> C G Pendse</td>
<td>403</td>
</tr>
<tr>
<td>128</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_11_DGDhavale.pdf'>The Kapitthaka of Varahamihira </a></td>
<td> D G Dhavale</td>
<td>53</td>
</tr>
<tr>
<td>129</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_13_RCGupta.pdf'>Solution of the Astronomical Triangle as found in the Tantrasamgraha </a></td>
<td> Radha Charan Gupta</td>
<td>200</td>
</tr>
<tr>
<td>130</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_14_GSundaramurthy.pdf'>The Contribution of the Cult of Sacrifice to the Development of Indian Astronomy </a></td>
<td> G Sundaramoorthy</td>
<td>130</td>
</tr>
<tr>
<td>131</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_15_SNSen.pdf'>Epicyclic Eccentric Planetary Theories in Ancient and Medieval Indian Astronomy </a></td>
<td> S N Sen</td>
<td>291</td>
</tr>
<tr>
<td>132</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_16_SMRAnsari.pdf'>Arab Antecedents of Copernican Method </a></td>
<td> S M R Ansari</td>
<td>20</td>
</tr>
<tr>
<td>133</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_17_MCPande.pdf'>Pre–Copernican Astronomy in Europe </a></td>
<td> M C Pande</td>
<td>295</td>
</tr>
<tr>
<td>134</td>
<td>IJHS-9-1974-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_18_DRKaprekar.pdf'>The Copernicus Magic Square </a></td>
<td> D R Kaprekar</td>
<td>28</td>
</tr>
<tr>
<td>135</td>
<td>IJHS-9-1974-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_1_19_Discussions.pdf'>Discussions </a></td>
<td> </td>
<td>88</td>
</tr>
<tr>
<td>136</td>
<td>IJHS-9-1974-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_2_1_RCGupta.pdf'>Sines and Cosines of Multiple Arcs as given by Kamalakara </a></td>
<td> Radha Charan Gupta</td>
<td>192</td>
</tr>
<tr>
<td>137</td>
<td>IJHS-9-1974-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_2_2_JVNarlikar.pdf'>Copernicus and Modern Astronomy </a></td>
<td> J V Narlikar</td>
<td>143</td>
</tr>
<tr>
<td>138</td>
<td>IJHS-9-1974-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_2_3_RPKulkarni.pdf'>A Note on the Examination of Soil for Foundation of Buildings and of Townships in Ancient/Medieval India </a></td>
<td> R P Kulkarni</td>
<td>184</td>
</tr>
<tr>
<td>139</td>
<td>IJHS-9-1974-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_2_4_RCGupta.pdf'>Addition and Subtraction Theorems for the Sine and the Cosine in Medieval India </a></td>
<td> Radha Charan Gupta</td>
<td>344</td>
</tr>
<tr>
<td>140</td>
<td>IJHS-9-1974-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_2_5_AKMishra.pdf'>Consciousness in Plants </a></td>
<td> Arun Kumar Misra</td>
<td>215</td>
</tr>
<tr>
<td>141</td>
<td>IJHS-9-1974-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_2_6_VDMarza.pdf'>Darwin’s Theory of Unity of Reacting Mechanisms in Plants and Animals: Its Present Day Importance </a></td>
<td> Vasile D Marza and Ion T Tarnavschi</td>
<td>1009</td>
</tr>
<tr>
<td>142</td>
<td>IJHS-9-1974-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_2_7_MNChannabasappa.pdf'>A Note on Colebrooke’s Translation of a Stanza from Bhaskara’s Lilavati </a></td>
<td> M N Channabasappa</td>
<td>80</td>
</tr>
<tr>
<td>143</td>
<td>IJHS-9-1974-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol09_2_8_Reviews.pdf'>Reviews </a></td>
<td> </td>
<td>100</td>
</tr>
<tr>
<td>144</td>
<td>IJHS-10-1975-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_1_1_PVSharma.pdf'>The Pseudo– Harita Samhita </a></td>
<td> P V Sharma</td>
<td>149</td>
</tr>
<tr>
<td>145</td>
<td>IJHS-10-1975-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_1_2_RPKulkarni.pdf'>Soil Stabilization by Early Indian Methods </a></td>
<td> R P Kulkarni</td>
<td>214</td>
</tr>
<tr>
<td>146</td>
<td>IJHS-10-1975-Issue-1</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_1_3_VVRaman.pdf'>The Permeation of Thermodynamics into Nineteenth Century Chemistry </a></td>
<td> V V Raman</td>
<td>573</td>
</tr>
<tr>
<td>147</td>
<td>IJHS-10-1975-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_1_4_RCGupta.pdf'>Circumference of the Jambudvipa in Jaina Cosmography </a></td>
<td> Radha Charan Gupta</td>
<td>357</td>
</tr>
<tr>
<td>148</td>
<td>IJHS-10-1975-Issue-1</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_1_5_SMRAnsari.pdf'>Quinquecentenary of Nicolaus Copernicus— A Report </a></td>
<td> S M R Ansari</td>
<td>192</td>
</tr>
<tr>
<td>149</td>
<td>IJHS-10-1975-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_1_6_Announcement.pdf'>Announcement </a></td>
<td> </td>
<td>57</td>
</tr>
<tr>
<td>150</td>
<td>IJHS-10-1975-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_1_7_BookReviews.pdf'>Book Review </a></td>
<td> </td>
<td>741</td>
</tr>
<tr>
<td>151</td>
<td>IJHS-10-1975-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_1_WelcomeSpeech_AGJhingran.pdf'>Welcome Speech </a></td>
<td> A G Jhingran</td>
<td>31</td>
</tr>
<tr>
<td>152</td>
<td>IJHS-10-1975-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_2_IntroductoryRemarks_FCAuluck.pdf'>Introductory Remarks </a></td>
<td> F C Auluck</td>
<td>43</td>
</tr>
<tr>
<td>153</td>
<td>IJHS-10-1975-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_3_InauguralSpeech_BRSeshachar.pdf'>Inaugural Speech </a></td>
<td> B R Seshachar</td>
<td>58</td>
</tr>
<tr>
<td>154</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_4_MAhmad.pdf'>Al–Biruni: An Introduction to his Life and Writings on the Indian Sciences </a></td>
<td> Maqbul Ahmad, ram Behari and B V Subbarayappa</td>
<td>242</td>
</tr>
<tr>
<td>155</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_5_AMShastri.pdf'>Sanskrit Literature known to Al–Biruni </a></td>
<td> Ajay Mitra Shastri</td>
<td>553</td>
</tr>
<tr>
<td>156</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_6_Ghayasuddin.pdf'>Varahamihira, The Best Sanskrit source of Al–Biruni on Indian Jyotisa </a></td>
<td> Ghayasuddin</td>
<td>559</td>
</tr>
<tr>
<td>157</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_7_BKNayar.pdf'>Al–Biruni and the Authorities on Sanskrit Prosody </a></td>
<td> Balkrishna K Nayar</td>
<td>110</td>
</tr>
<tr>
<td>158</td>
<td>IJHS-10-1975-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_8_SessionIDiscussion.pdf'>Session I: Discussion </a></td>
<td> </td>
<td>41</td>
</tr>
<tr>
<td>159</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Math</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_9_BChatterjee.pdf'>Al–Biruni and Brahmagupta </a></td>
<td> Bina Chatterjee</td>
<td>98</td>
</tr>
<tr>
<td>160</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_10_RNRai.pdf'>Al–Biruni and Indian Eras </a></td>
<td> R N Rai</td>
<td>156</td>
</tr>
<tr>
<td>161</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Math</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_11_AKBag.pdf'>Al–Biruni on Indian Arithmetic </a></td>
<td> A K Bag</td>
<td>182</td>
</tr>
<tr>
<td>162</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_12_SNSen.pdf'>Al–Biruni on determination of Latitudes and Longitudes in India </a></td>
<td> S N Sen</td>
<td>253</td>
</tr>
<tr>
<td>163</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_13_SMRAnsari.pdf'>On Physical Researches of Al–Biruni </a></td>
<td> S M R Ansari</td>
<td>388</td>
</tr>
<tr>
<td>164</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_14_SRoy.pdf'>Al–Biruni And Hindu Speculations on Gravitation </a></td>
<td> Sourin Roy</td>
<td>138</td>
</tr>
<tr>
<td>165</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Metallurgy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_15_VBMainkar.pdf'>Metrology in Al–Biruni’s India </a></td>
<td> V B Mainkar</td>
<td>111</td>
</tr>
<tr>
<td>166</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_16_SMZAlavi.pdf'>Al–Biruni’s Contribution to Physical Geography </a></td>
<td> S M Ziauddin Alavi</td>
<td>94</td>
</tr>
<tr>
<td>167</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_17_NKPanikkar.pdf'>Al–Biruni and The Theory of Tides </a></td>
<td> N K Panikkar</td>
<td>129</td>
</tr>
<tr>
<td>168</td>
<td>IJHS-10-1975-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_18_SessionIIDiscussion.pdf'>Session II Discussion </a></td>
<td> </td>
<td>35</td>
</tr>
<tr>
<td>169</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_19_SMAhmad.pdf'>Al–Biruni as a Synthesizer and Transmitter of Scientific Knowledge </a></td>
<td> S Maqbul Ahmad</td>
<td>106</td>
</tr>
<tr>
<td>170</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_20_BKNayar.pdf'>Al–Biruni and Science Communication in Sanskrit </a></td>
<td> B K Nayar</td>
<td>67</td>
</tr>
<tr>
<td>171</td>
<td>IJHS-10-1975-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_21_SessionIIIDiscussion.pdf'>Session III Discussion </a></td>
<td> </td>
<td>14</td>
</tr>
<tr>
<td>172</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_22_MSAsimov.pdf'>Al–Biruni’s Astronomical Treatise in The Dari Language </a></td>
<td> M S Asimov</td>
<td>56</td>
</tr>
<tr>
<td>173</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_23_AHHabibi.pdf'>Where was Al–Birun Situated? </a></td>
<td> Abdul H Habibi</td>
<td>32</td>
</tr>
<tr>
<td>174</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Math</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_24_BKNayar.pdf'>Al–Biruni and The Arithmetical Sequence of the Sanskrit Ganas </a></td>
<td> B K Nayar</td>
<td>172</td>
</tr>
<tr>
<td>175</td>
<td>IJHS-10-1975-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_25_MRBhat.pdf'>Al–Biruni’s Treatment of the Laghujataka and Comets: A Critique </a></td>
<td> M Ramakrishna Bhat</td>
<td>124</td>
</tr>
<tr>
<td>176</td>
<td>IJHS-10-1975-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol10_2_26_SessionIVDiscussion.pdf'>Session IV: Discussion </a></td>
<td> </td>
<td>26</td>
</tr>
<tr>
<td>177</td>
<td>IJHS-11-1976-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_1_1_RCGupta.pdf'>Sine of Eighteen Degrees in India Upto the Eighteenth Century </a></td>
<td> Radha Charan Gupta</td>
<td>159</td>
</tr>
<tr>
<td>178</td>
<td>IJHS-11-1976-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_1_2_BGLSwamy.pdf'>Sources for a History of Plant Sciences in India (II) </a></td>
<td> B G L Swamy</td>
<td>450</td>
</tr>
<tr>
<td>179</td>
<td>IJHS-11-1976-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_1_3_BGLSwamy.pdf'>Sources for a History of Plant Sciences in India (III) </a></td>
<td> B G L Swamy</td>
<td>325</td>
</tr>
<tr>
<td>180</td>
<td>IJHS-11-1976-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_1_4_RNRai.pdf'>Some Observations on Vrddha–Vasistha Siddhanta </a></td>
<td> R N Rai</td>
<td>95</td>
</tr>
<tr>
<td>181</td>
<td>IJHS-11-1976-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_1_5_AKBag.pdf'>Madhava’s Sine and Cosine Series </a></td>
<td> A K Bag</td>
<td>87</td>
</tr>
<tr>
<td>182</td>
<td>IJHS-11-1976-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_1_6_LCJain.pdf'>The Kinematic Motion of Astral Real and Counter Bodies in Trilokasara </a></td>
<td> L C Jain</td>
<td>362</td>
</tr>
<tr>
<td>183</td>
<td>IJHS-11-1976-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_1_7_RHSingh.pdf'>Ayurvedic Concept of the Psychosomatic Basis of Health and Disease </a></td>
<td> R H Singh and B N Sinha</td>
<td>187</td>
</tr>
<tr>
<td>184</td>
<td>IJHS-11-1976-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_2_1_LCJain.pdf'>On Certain Mathematical Topics of the Dhavala Texts </a></td>
<td> L C Jain</td>
<td>481</td>
</tr>
<tr>
<td>185</td>
<td>IJHS-11-1976-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_2_2_MNChannabasappa.pdf'>On the Square Root Formula in the Bakhshali Manuscript </a></td>
<td> M N Channabasappa</td>
<td>267</td>
</tr>
<tr>
<td>186</td>
<td>IJHS-11-1976-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_2_3_RMitra.pdf'>Kamala—The National Flower of India: Its Ancient History and Uses in Indian Medicine </a></td>
<td> R Mitra and L D Kapoor</td>
<td>179</td>
</tr>
<tr>
<td>187</td>
<td>IJHS-11-1976-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_2_4_DPAgarwal.pdf'>Ancient Copper Workings: Some New C–14 Dates </a></td>
<td> D P Agrawal‚ C Margabandhu and N C Shekar</td>
<td>75</td>
</tr>
<tr>
<td>188</td>
<td>IJHS-11-1976-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_2_5_MChaudhuri.pdf'>Ship–Building in the Yuktikalpataru and Samarangana Sutradhara </a></td>
<td> Mamata Chaudhuri</td>
<td>236</td>
</tr>
<tr>
<td>189</td>
<td>IJHS-11-1976-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol11_2_6_TMSrinivasan.pdf'>Measurement of Rainfall in Ancient India </a></td>
<td> T M Srinivasan</td>
<td>254</td>
</tr>
<tr>
<td>190</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_1_PKMajumdar.pdf'>Ganita Kaumudi and the Continued Fraction </a></td>
<td> Pradip Kumar Majumdar</td>
<td>75</td>
</tr>
<tr>
<td>191</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_2_PKMajumdar.pdf'>The Extant of Siddhanta Sarvabhauma— An error in the Sine of One–third of Part of an Ang </a></td>
<td> Pradip Kumar Majumdar</td>
<td>75</td>
</tr>
<tr>
<td>192</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_3_PKMajumdar.pdf'>A Rationale of Bhaskara I's Method </a></td>
<td> Pradip Kumar Majumdar</td>
<td>87</td>
</tr>
<tr>
<td>193</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_4_SRNMurthy.pdf'>Geological Evidences in Support of the Antiquity of Some Ancient Indian Events </a></td>
<td> S R N Murthy</td>
<td>100</td>
</tr>
<tr>
<td>194</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_5_HGershenowitz.pdf'>Gavin De Beer and the Neo–Lamarckians </a></td>
<td> Harry Gershenowitz</td>
<td>99</td>
</tr>
<tr>
<td>195</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_6_PKSrivastava.pdf'>Nephrology in Ancient Indian System of Medicine </a></td>
<td> R H Singh and P K Srivastava</td>
<td>77</td>
</tr>
<tr>
<td>196</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_7_RPKulkarni.pdf'>The Value of Π Known to Sulbasutrakaras </a></td>
<td> R P Kulkarni</td>
<td>158</td>
</tr>
<tr>
<td>197</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_8_LCJain.pdf'>On the Spiro–Elliptic Motion of the Sun implicit in the Tiloyapannatti </a></td>
<td> L C Jain</td>
<td>146</td>
</tr>
<tr>
<td>198</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_9_SMahdihassan.pdf'>Triphala and its Arabic and Chinese Synonyms </a></td>
<td> S Mahdihassan</td>
<td>174</td>
</tr>
<tr>
<td>199</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_10_HGershenowitz.pdf'>George Gaylord Simpson and Lamarck </a></td>
<td> Harry Gershenowitz</td>
<td>124</td>
</tr>
<tr>
<td>200</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_11_SMRAnsari.pdf'>The Establishment of Observatories </a></td>
<td> S M R Ansari</td>
<td>187</td>
</tr>
<tr>
<td>201</td>
<td>IJHS-13-1978-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_1_12_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>80</td>
</tr>
<tr>
<td>202</td>
<td>IJHS-13-1978-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_2_1_SRNMurthy.pdf'>A Critical Evaluation of Mineralogical Aspects of Some Sanskrit Texts </a></td>
<td> S R N Murthy</td>
<td>131</td>
</tr>
<tr>
<td>203</td>
<td>IJHS-13-1978-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_2_2_MRoy.pdf'>Dyes in Ancient and Medieval India </a></td>
<td> Meera Roy</td>
<td>542</td>
</tr>
<tr>
<td>204</td>
<td>IJHS-13-1978-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_2_3_KNPrasad.pdf'>Dating the Quaternary and Human Civilization </a></td>
<td> K N Prasad and S R N Murthy</td>
<td>90</td>
</tr>
<tr>
<td>205</td>
<td>IJHS-13-1978-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_2_4_RPKulkarni.pdf'>Geometry as known to the People of Indus Civilization </a></td>
<td> R P Kulkarni</td>
<td>129</td>
</tr>
<tr>
<td>206</td>
<td>IJHS-13-1978-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_2_5_RCGupta.pdf'>Indian Values of the Sinus Totus </a></td>
<td> Radha Charan Gupta</td>
<td>371</td>
</tr>
<tr>
<td>207</td>
<td>IJHS-13-1978-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_2_6_HGershenowitz.pdf'>The Treatment of Lamarckism as found in Forty–one College Textbooks </a></td>
<td> Harry Gershenowitz</td>
<td>152</td>
</tr>
<tr>
<td>208</td>
<td>IJHS-13-1978-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_2_7_TSKShastri.pdf'>The Epoch of the Romaka Siddhanta </a></td>
<td> T S Kuppana Shastri</td>
<td>173</td>
</tr>
<tr>
<td>209</td>
<td>IJHS-13-1978-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol13_2_8_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>57</td>
</tr>
<tr>
<td>210</td>
<td>IJHS-14-1979-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_1_1_SSLishk.pdf'>Zodiac Circumference as Graduated in Jaina Astronomy </a></td>
<td> Sajjan Singh Lishk and S D Sharma</td>
<td>282</td>
</tr>
<tr>
<td>211</td>
<td>IJHS-14-1979-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_1_2_HGershenowitz.pdf'>Chauncey Wright’s Views on Lamarck </a></td>
<td> Harry Gershenowitz</td>
<td>157</td>
</tr>
<tr>
<td>212</td>
<td>IJHS-14-1979-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_1_3_HGershenowitz.pdf'>George Henslow: True Darwinist </a></td>
<td> Harry Gershenowitz</td>
<td>128</td>
</tr>
<tr>
<td>213</td>
<td>IJHS-14-1979-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_1_4_LCJain.pdf'>System Theory in Jaina School of Mathematics </a></td>
<td> L C Jain</td>
<td>575</td>
</tr>
<tr>
<td>214</td>
<td>IJHS-14-1979-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_1_5_RCGupta.pdf'>Munisvara’s Modification of Brahmagupta's Rule for Second Order Interpolation </a></td>
<td> R C Gupta</td>
<td>113</td>
</tr>
<tr>
<td>215</td>
<td>IJHS-14-1979-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_1_6_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>85</td>
</tr>
<tr>
<td>216</td>
<td>IJHS-14-1979-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_1_7_News.pdf'>News </a></td>
<td> </td>
<td>84</td>
</tr>
<tr>
<td>217</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_1_SRNMurthy.pdf'>An Occurrence of Cinnabar in Rasarnavakalpa </a></td>
<td> S R N Murthy</td>
<td>73</td>
</tr>
<tr>
<td>218</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_2_VMukherji.pdf'>Some Historical Aspects of Jagadis Chandra Bose’s Microwave Research During 1895–1900 </a></td>
<td> Visvapriya Mukherji</td>
<td>423</td>
</tr>
<tr>
<td>219</td>
<td>IJHS-14-1979-Issue-2</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_3_HGershenowitz.pdf'>The Influence of Lamarckism on the Development of Freud’s Psychoanalytic Theory </a></td>
<td> Harry Gershenowitz</td>
<td>202</td>
</tr>
<tr>
<td>220</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_4_HGershenowitz.pdf'>John Burroughs: Right Wing Neo–Lamarckian </a></td>
<td> Harry Gershenowitz</td>
<td>149</td>
</tr>
<tr>
<td>221</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_5_JCSikdar.pdf'>Indian Concepts of Matter Part–I </a></td>
<td> J C Sickdar</td>
<td>243</td>
</tr>
<tr>
<td>222</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_6_SRNMurthy.pdf'>Vagbhata on Medicinal Uses of Gems </a></td>
<td> S R N Murthy</td>
<td>89</td>
</tr>
<tr>
<td>223</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_7_RSSingh.pdf'>Botanical Identity and a Critical Appreciation of Maluva Lata as Evinced in the Buddhistic Pali Literature </a></td>
<td> R S Singh</td>
<td>94</td>
</tr>
<tr>
<td>224</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_8_SRNMurthy.pdf'>On Some Geological Aspects of the Suryasiddhanta </a></td>
<td> S R N Murthy</td>
<td>119</td>
</tr>
<tr>
<td>225</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_9_TSKSastry.pdf'>The Vasistha–Paulisa Venus in the Pancasiddhantika of Varahamihira </a></td>
<td> T S Kuppanna Sastry</td>
<td>104</td>
</tr>
<tr>
<td>226</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_10_SSKamavisdar.pdf'>Evidences of the Inorganic Subtances in Amalgamation Process During Indian Alchemy </a></td>
<td> S S Kamavisdar</td>
<td>32</td>
</tr>
<tr>
<td>227</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_11_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>70</td>
</tr>
<tr>
<td>228</td>
<td>IJHS-14-1979-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol14_2_12_News.pdf'>News </a></td>
<td> </td>
<td>42</td>
</tr>
<tr>
<td>229</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_4_SBagchi.pdf'>History of Mining in India—Circa 1400–1800 and Technology Status </a></td>
<td> S Bagchi and A K Ghose</td>
<td>104</td>
</tr>
<tr>
<td>230</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_6_RCGupta.pdf'>The Marici Commentary on the Jyotpatti </a></td>
<td> R C Gupta</td>
<td>112</td>
</tr>
<tr>
<td>231</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_8_HKNaqvi.pdf'>Colour Making and Dyeing of Cotton Textiles in Medieval Hindustan </a></td>
<td> Hamida Khatoon Naqvi</td>
<td>285</td>
</tr>
<tr>
<td>232</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_9_RLVerma.pdf'>Medical Trends in Kashmir During Zain–ul–Abidin’s Reign </a></td>
<td> R L Verma</td>
<td>218</td>
</tr>
<tr>
<td>233</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_10_AKBag.pdf'>Indian Literature on Mathematics During 1400–1800 AD </a></td>
<td> A K Bag</td>
<td>325</td>
</tr>
<tr>
<td>234</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_11_KBehari.pdf'>A Survey of Historical Astrolables of Delhi </a></td>
<td> Kailash Behari and Vijai Govind</td>
<td>222</td>
</tr>
<tr>
<td>235</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_12_DKumar.pdf'>Patterns of Colonial Science in India </a></td>
<td> Deepak Kumar</td>
<td>189</td>
</tr>
<tr>
<td>236</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_1_INVerma.pdf'>Calico Printing in India </a></td>
<td> I N Verma</td>
<td>128</td>
</tr>
<tr>
<td>237</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_2_JCSikdar.pdf'>Jaina Alchemy </a></td>
<td> J C Sikdar</td>
<td>254</td>
</tr>
<tr>
<td>238</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_3_TSiddiqi.pdf'>Unani Medicine in India during the Delhi Sultanate </a></td>
<td> Tazimuddin Siddiqi</td>
<td>137</td>
</tr>
<tr>
<td>239</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_5_SPSangar.pdf'>Indian Silk fabrics in  the Seventeenth Century </a></td>
<td> S P Sangar</td>
<td>250</td>
</tr>
<tr>
<td>240</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_7_SAKGhori.pdf'>The Impact of Modern European Astronomy on Raja Jai Singh </a></td>
<td> S A Khan Ghori</td>
<td>174</td>
</tr>
<tr>
<td>241</td>
<td>IJHS-15-1980-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_1_13_HGershenowitz.pdf'>Monsieur Poliakov’s Recent Attack Upon Lamarck </a></td>
<td> Harry Gershenowitz</td>
<td>127</td>
</tr>
<tr>
<td>242</td>
<td>IJHS-15-1980-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_2_4_HGershenowitz.pdf'>Napoleon and Lamarck </a></td>
<td> Harry Gershenowitz</td>
<td>137</td>
</tr>
<tr>
<td>243</td>
<td>IJHS-15-1980-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_2_5_SSKamavisdar.pdf'>Analytical Studies in the Evidences Regarding Chemico–Culture in the History of Indian Medicine in Ancient Period—Allium Series </a></td>
<td> S S Kamavisdar</td>
<td>306</td>
</tr>
<tr>
<td>244</td>
<td>IJHS-15-1980-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_2_6_SMahadihassan.pdf'>A Comparitive Study of the Early System of Indian Cosmology and the Tridosa Humoral Doctrine </a></td>
<td> S Mahdihassan</td>
<td>157</td>
</tr>
<tr>
<td>245</td>
<td>IJHS-15-1980-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_2_1_KSShukla.pdf'>Hindu Geometry </a></td>
<td> Bibhutibhusan Datta and Avadhesh Narayan Singh; Revised by Kripa Shankar Shukla</td>
<td>1304</td>
</tr>
<tr>
<td>246</td>
<td>IJHS-15-1980-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_2_2_SRNMurthy.pdf'>The Vedic River Saraswati A Myth or Fact – A Geological Approach </a></td>
<td> S R N Murthy</td>
<td>106</td>
</tr>
<tr>
<td>247</td>
<td>IJHS-15-1980-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol15_2_3_SSLishk.pdf'>Standardization of Time–Unit Muhurta Through the Science of Sciatherics in Atharva Vedanga Jyotisa </a></td>
<td> Sajjan Singh Lishk and S D Sharma</td>
<td>267</td>
</tr>
<tr>
<td>248</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_2_KKThakral.pdf'>Techniques for Extraction of Foreign Bodies From war wounds In Medieval India </a></td>
<td> K K Thakral</td>
<td>97</td>
</tr>
<tr>
<td>249</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_4_TSiddiqi.pdf'>Unani Medicine in India 1524 to 1605 AD </a></td>
<td> T Siddiqi</td>
<td>68</td>
</tr>
<tr>
<td>250</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_6_GNChaturvedi.pdf'>Medicinal Use of Opium And Cannabis in Medieval India </a></td>
<td> G N Chaturvedi</td>
<td>90</td>
</tr>
<tr>
<td>251</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_7_SKMishra.pdf'>Ideas of Integration as a Process of Evolution of Indian System of Medicine in the Medieval Period </a></td>
<td> S K Mishra</td>
<td>98</td>
</tr>
<tr>
<td>252</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_8_RSSingh.pdf'>Contribution of Unani Materia Medicas to the Identification of Vedic Plants with Special Reference to Usana </a></td>
<td> R S singh</td>
<td>121</td>
</tr>
<tr>
<td>253</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Metallurgy</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_11_SMahdihassan.pdf'>Alchemy and its Fundamental Terms in Greek‚ Arabic‚ Sanskrit and Chinese </a></td>
<td> S Mahdihassan</td>
<td>278</td>
</tr>
<tr>
<td>254</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_12_NPRai.pdf'>The Origin and Development of Pulse Examination in Medieval India </a></td>
<td> N P Rai</td>
<td>246</td>
</tr>
<tr>
<td>255</td>
<td>IJHS-16-1981-Issue-1</td>
<td>MindSciences</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_15_AKBose.pdf'>Aphrodisiacs– A Psychosocial Perspective </a></td>
<td> A K Bose</td>
<td>75</td>
</tr>
<tr>
<td>256</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_16_CBDube.pdf'>Diseases Due to Deficiencies of Vital Principles in the Body </a></td>
<td> C B Dube</td>
<td>67</td>
</tr>
<tr>
<td>257</td>
<td>IJHS-16-1981-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol_16_1_0_Address.pdf'>Inaugural Address </a></td>
<td> V Ramalingaswami</td>
<td>32</td>
</tr>
<tr>
<td>258</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_1_PVSharma.pdf'>Contributions of Sarngadhara in the Field of Materia Medica and Phamacy </a></td>
<td> P V Sharma</td>
<td>145</td>
</tr>
<tr>
<td>259</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_3_RNSingh.pdf'>Contribution of Medieval India to Ayurvedic Materia Medica </a></td>
<td> D K S Chauhan</td>
<td>106</td>
</tr>
<tr>
<td>260</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_5_TSiddiqi.pdf'>Two Eminent Physicians of Unani Medicine During Shah Jahan’s Reign </a></td>
<td> T Siddiqi</td>
<td>92</td>
</tr>
<tr>
<td>261</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_9_MSKhan.pdf'>An Arabic Source for the History of Ancient Indian Medicine </a></td>
<td> M S Khan</td>
<td>223</td>
</tr>
<tr>
<td>262</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_10_ABKhan.pdf'>Poisons and Antidotes in Unani Systemof Medicine </a></td>
<td> A B Khan</td>
<td>126</td>
</tr>
<tr>
<td>263</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_13_BNSingh.pdf'>The Contribution of Madanapala Nighantu to the Knowledge of Indian Materia Medica with Particular Reference to Fig (Anjira) </a></td>
<td> B N Singh</td>
<td>138</td>
</tr>
<tr>
<td>264</td>
<td>IJHS-16-1981-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_1_14_AHIsraili.pdf'>Humoral Theory of Unani Tibb </a></td>
<td> A H Israili</td>
<td>95</td>
</tr>
<tr>
<td>265</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_4_AJKhan.pdf'>A Survey of the Concepts and Measures Developed by the Greco–Arab Physicians Related with The Prevention and Treatment of the Infections and Epidemic Diseases </a></td>
<td> A J Khan</td>
<td>117</td>
</tr>
<tr>
<td>266</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_6_JLSanchez.pdf'>Carlos J Finlay and the Conception of Contagion </a></td>
<td> J L Sanchez</td>
<td>244</td>
</tr>
<tr>
<td>267</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_9_KTMHegde.pdf'>Scientific Basis and Technology of Ancient Indian Copper and Iron Metallurgy </a></td>
<td> K T M Hegde</td>
<td>301</td>
</tr>
<tr>
<td>268</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_10_SPSangar.pdf'>Intoxicants in Mughal India </a></td>
<td> S P Sangar</td>
<td>254</td>
</tr>
<tr>
<td>269</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_11_GAbraham.pdf'>The Gnomon in Early Indian Astronomy </a></td>
<td> George Abraham</td>
<td>64</td>
</tr>
<tr>
<td>270</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_12_RSSingh.pdf'>On the Identity and Economico Medicinal uses of Hastikarnapalasa as Evinced in the Ancient (Sanskrit) Texts and Traditions </a></td>
<td> R S Singh</td>
<td>94</td>
</tr>
<tr>
<td>271</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_1_PKMajumdar.pdf'>The Rationale of Brahmagupta’s Method of Solving ax—c=by </a></td>
<td> P K Majumdar</td>
<td>85</td>
</tr>
<tr>
<td>272</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_2_SDSharma.pdf'>Pluto and a Transplutonian Planet as Predicted by Venkatesha Ketakara </a></td>
<td> S D Sharma</td>
<td>221</td>
</tr>
<tr>
<td>273</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_3_HGershenowitz.pdf'>John Wesley Powell: Staunch Neo–Lamarckian </a></td>
<td> H Gershenowitz</td>
<td>184</td>
</tr>
<tr>
<td>274</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Medicine</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_5_NKGarg.pdf'>Interaction in Chemistry and Medicine Between India and Europe in 18th–19th Century </a></td>
<td> N K Garg</td>
<td>201</td>
</tr>
<tr>
<td>275</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_7_RMitra.pdf'>Bakula– A Reputed Drug of Ayurveda ‚its History‚ Uses in Indian Medicine </a></td>
<td> Roma Mitra</td>
<td>277</td>
</tr>
<tr>
<td>276</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_8_DGThatte.pdf'>Techniques of Venupuncture (Siravedha) in India in the 18th Century </a></td>
<td> D G Thatte</td>
<td>174</td>
</tr>
<tr>
<td>277</td>
<td>IJHS-16-1981-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol16_2_13_SMahdihassan.pdf'>Parisrut The Earliest Distilled Liquor of Vedic Times or of About 1500BC </a></td>
<td> S Mahdihassan</td>
<td>154</td>
</tr>
<tr>
<td>278</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_2_RDRoy.pdf'>An Outline Survey of Some Aspects of Technology in India, 1750–1900 and its Legacy </a></td>
<td> Rama Deb roy</td>
<td>197</td>
</tr>
<tr>
<td>279</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_4_MJMehta.pdf'>Indigenous Paper Industry and Muslim Entrepreneurship </a></td>
<td> Makrand J Mehta</td>
<td>361</td>
</tr>
<tr>
<td>280</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_7_AKBag.pdf'>Technology in India in the Eighteenth–Ninteenth Century </a></td>
<td> A K Bag</td>
<td>180</td>
</tr>
<tr>
<td>281</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_12_KSMurty.pdf'>Geological Sciences in India in the 18th–19th Century </a></td>
<td> K S Murty</td>
<td>282</td>
</tr>
<tr>
<td>282</td>
<td>IJHS-17-1982-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_13_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>127</td>
</tr>
<tr>
<td>283</td>
<td>IJHS-17-1982-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_14_News.pdf'>News </a></td>
<td> </td>
<td>106</td>
</tr>
<tr>
<td>284</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_1_SNSen.pdf'>Tieffenthaler on Latitudes and Longitudes in India— An Eighteenth Century Study of Geographical Coordinates </a></td>
<td> S N Sen</td>
<td>315</td>
</tr>
<tr>
<td>285</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Agriculture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_3_RPKulkarni.pdf'>Irrigation Engineering in India </a></td>
<td> R P Kulkarni</td>
<td>274</td>
</tr>
<tr>
<td>286</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_5_HKNaqvi.pdf'>Technology and Process of Some of the Principal Industries of Eighteenth Century Hindustan </a></td>
<td> Hamida Khatoon Naqvi</td>
<td>122</td>
</tr>
<tr>
<td>287</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Culture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_6_HCBhardwaj.pdf'>Indian Dyes and Dyeing Industry during 18–19 Century </a></td>
<td> H C Bhardwaj and Kamal K Jain</td>
<td>215</td>
</tr>
<tr>
<td>288</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Culture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_8_EGKRao.pdf'>Development of Banking Institutions in India in the Eighteenth–Ninteenth Century </a></td>
<td> E G K Rao</td>
<td>433</td>
</tr>
<tr>
<td>289</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Medicine</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_10_JCSikdar.pdf'>Phirangiroga (Syphilis) and its Management </a></td>
<td> J C Sikdar</td>
<td>493</td>
</tr>
<tr>
<td>290</td>
<td>IJHS-17-1982-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_1_11_NGangadharan.pdf'>The State of Ayurveda in Eighteenth & Ninteenth Centuries </a></td>
<td> N Gangadharan</td>
<td>198</td>
</tr>
<tr>
<td>291</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Agriculture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_1_SSingh.pdf'>Agricultural Science and Technology in Punjab in the Ninteenth Century </a></td>
<td> Sukhwant Singh</td>
<td>283</td>
</tr>
<tr>
<td>292</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_3_HCBhardwaj.pdf'>Development of Iron and Steel Technology in India during 18th and 19th Centuries </a></td>
<td> H C Bhardwaj</td>
<td>192</td>
</tr>
<tr>
<td>293</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_5_MLSharma.pdf'>Jagannath Samrats Outstanding Contribution to Indian Astronomy in Eighteenth Century AD </a></td>
<td> M L Sharma</td>
<td>150</td>
</tr>
<tr>
<td>294</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_10_DKumar.pdf'>Economic Compulsions and the Geological Survey of India </a></td>
<td> Deepak kumar</td>
<td>212</td>
</tr>
<tr>
<td>295</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_11_SKhatun.pdf'>Impact of European Science and Technology on Bengal </a></td>
<td> Sharifa Khatun</td>
<td>198</td>
</tr>
<tr>
<td>296</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Medicine</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_13_AKBasu.pdf'>Some Perspectives of the Cultural imapct of European Medical Scienec on the Development Scientific Medicine in India </a></td>
<td> A K basu</td>
<td>139</td>
</tr>
<tr>
<td>297</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_15_VNSharma.pdf'>The Impact of Eighteenth Century Jesuit Astronomers on the Astronomy of India and China </a></td>
<td> Virendra Nath Sharma</td>
<td>157</td>
</tr>
<tr>
<td>298</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Biology</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_16_KMMatthew.pdf'>Botany and its Technologies in Peninsular India in the Eighteenth and Ninteenth Centuries </a></td>
<td> K M Matthew</td>
<td>231</td>
</tr>
<tr>
<td>299</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_18_DPJha.pdf'>Science and Technology (Coal Mining) in India in Eighteenth–Ninteenth Century </a></td>
<td> D P Jha</td>
<td>242</td>
</tr>
<tr>
<td>300</td>
<td>IJHS-17-1982-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_19_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>68</td>
</tr>
<tr>
<td>301</td>
<td>IJHS-17-1982-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_20_Announcement.pdf'>Announcement </a></td>
<td> </td>
<td>29</td>
</tr>
<tr>
<td>302</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_2_RDSingh.pdf'>Development of Mining Technology during the Ninteenth Century in India </a></td>
<td> R D Singh</td>
<td>476</td>
</tr>
<tr>
<td>303</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_4_EGForbes.pdf'>European Astronomical Tradition: Transmission into India </a></td>
<td> Eric G Forbes</td>
<td>224</td>
</tr>
<tr>
<td>304</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_6_AKMehra.pdf'>Solar Eclipse Theory and observations in the 18th Century India </a></td>
<td> Anjani Kumar Mehra</td>
<td>128</td>
</tr>
<tr>
<td>305</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_7_MNMadhyastha.pdf'>Brief History of Scientific Progress of South Kanara </a></td>
<td> M N Madhyastha, M Abdul Rahiman and K M Kaveriappa</td>
<td>141</td>
</tr>
<tr>
<td>306</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_8_KNobuo.pdf'>The Characteristic Features of Japanese Culture in the Field of Science Eighteenth–Ninteenth Century </a></td>
<td> Kawajiri Nobuo</td>
<td>185</td>
</tr>
<tr>
<td>307</td>
<td>IJHS-17-1982-Issue-2</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_9_JTBlackmore.pdf'>The Rise and Fall of Three Fashionable Expectations </a></td>
<td> John T Blackmore</td>
<td>174</td>
</tr>
<tr>
<td>308</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_12_GSingh.pdf'>Impact of European Science and Technology on the development of Modern Ayurveda during 19th Century </a></td>
<td> Gurdip Singh and P D Joshi</td>
<td>225</td>
</tr>
<tr>
<td>309</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_14_VNSharma.pdf'>Jai Singh‚ His European Astronomers and the Copernican Revolution </a></td>
<td> Virendra Nath Sharma</td>
<td>228</td>
</tr>
<tr>
<td>310</td>
<td>IJHS-17-1982-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol17_2_17_PKBhattacharyya.pdf'>Beginning of Modern Botany in India by Dutch in 16th–18th Century (Basic Features and Characteristics) </a></td>
<td> P K Bhattacharyya</td>
<td>364</td>
</tr>
<tr>
<td>311</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_1_HGershenowitz.pdf'>Arthur Koestler’s Osculation with Lamarckism and Neo–Lamarckism </a></td>
<td> Harry Gershenowitz</td>
<td>179</td>
</tr>
<tr>
<td>312</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_3_HGershenowitz.pdf'>Georges Clemenceau: Traditional Lamarckian </a></td>
<td> Harry Gershenowitz</td>
<td>183</td>
</tr>
<tr>
<td>313</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_5_BDatta.pdf'>Hindu Trignometry </a></td>
<td> Bibhutibhusan Datta and Avadhesh Narayan Singh</td>
<td>1010</td>
</tr>
<tr>
<td>314</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_7_HKNaqvi.pdf'>Some Varieties of Indian Silken Stuffs in Persian Sources C 1200–1700 </a></td>
<td> Hamida Khatoon Naqvi</td>
<td>284</td>
</tr>
<tr>
<td>315</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_8_SMahdihassan.pdf'>The Etymology of Kim–Purusa </a></td>
<td> S Mahdihassan</td>
<td>29</td>
</tr>
<tr>
<td>316</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_9_Bookreview.pdf'>Book Reviews </a></td>
<td> </td>
<td>66</td>
</tr>
<tr>
<td>317</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_2_VKJoshi.pdf'>Evolution of the Concept of Astavarga </a></td>
<td> V K Joshi</td>
<td>116</td>
</tr>
<tr>
<td>318</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_4_RCGupta.pdf'>Spread and Triumph of Indian Numerals </a></td>
<td> R C Gupta</td>
<td>306</td>
</tr>
<tr>
<td>319</td>
<td>IJHS-18-1983-Issue-1</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_1_6_PRamakrishnan.pdf'>History of Powder Metallurgy </a></td>
<td> P Ramakrishnan</td>
<td>157</td>
</tr>
<tr>
<td>320</td>
<td>IJHS-18-1983-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_3_RSSingh.pdf'>The Identity and Critical Appraisal of the Basis of Nomenclature and Ancient Socio–Cultural and Geographico–Historical Reflections Evinced with the Paninian Perfume Plant ⁄ Plant Part–Kisara </a></td>
<td> R S Singh and V D Vyas</td>
<td>145</td>
</tr>
<tr>
<td>321</td>
<td>IJHS-18-1983-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_4_ANSingh.pdf'>On the Identity of and Indo–Greek Relation Reflected in the Plant–Names and Uses Evinced in the Kautilya Arthasastra with Particular Reference to ‘Kiratatikta’ of ‘Katuvarga’ </a></td>
<td> A N Singh and R S Singh</td>
<td>107</td>
</tr>
<tr>
<td>322</td>
<td>IJHS-18-1983-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_7_PKMajumdar.pdf'>A Rationale of Bhatta Govinda’s Method for Solving the Equation ax—c=by and a Comparitive Study of the Determination of ‘Mati’ as Given by Bhaskara I and Bhatta Govinda </a></td>
<td> Pradip Kumar Majumdar</td>
<td>88</td>
</tr>
<tr>
<td>323</td>
<td>IJHS-18-1983-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_9_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>120</td>
</tr>
<tr>
<td>324</td>
<td>IJHS-18-1983-Issue-2</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_1_HGershenowitz.pdf'>Why Did Gregory Bateson Overlook Some Basic Lamarckian Tenets </a></td>
<td> Harry Gershenowitz</td>
<td>367</td>
</tr>
<tr>
<td>325</td>
<td>IJHS-18-1983-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_2_HGershenowitz.pdf'>Encyclopedias and Lamarck </a></td>
<td> Harry Gershenowitz</td>
<td>250</td>
</tr>
<tr>
<td>326</td>
<td>IJHS-18-1983-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_5_NCShekar.pdf'>Antiquity of Mining and Metallurgical Activities at Ambaji‚ Kumbaria and Deri </a></td>
<td> N C Shekar</td>
<td>144</td>
</tr>
<tr>
<td>327</td>
<td>IJHS-18-1983-Issue-2</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_6_VSKirsanov.pdf'>The Characteristic Features of Development of Science and Technology in Europe in the 18–19th Centuries </a></td>
<td> V S Kirsanov</td>
<td>329</td>
</tr>
<tr>
<td>328</td>
<td>IJHS-18-1983-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol18_2_8_MChaudhuri.pdf'>The Technique of Glass Making in India (1400–1800 AD) </a></td>
<td> Mamata Chaudhuri</td>
<td>344</td>
</tr>
<tr>
<td>329</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_3_SAParamhans.pdf'>Units of Measurements in Medieval India and their Modern Equivalents </a></td>
<td> S A Paramhans</td>
<td>122</td>
</tr>
<tr>
<td>330</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_4_NBhatla.pdf'>Plants: Traditional Worshipping </a></td>
<td> N Bhatla‚ T Mukherjee and G Singh</td>
<td>102</td>
</tr>
<tr>
<td>331</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_5_KHKrishnamurthy.pdf'>Siddha System of Medicine: A Historical Appraisal </a></td>
<td> K H Krishnamurthy and G C Mouli</td>
<td>181</td>
</tr>
<tr>
<td>332</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_8_Smahdihassan.pdf'>The Chinese Origin of the Sanskrit Word for Wheat </a></td>
<td> S Mahadihassan</td>
<td>44</td>
</tr>
<tr>
<td>333</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_10_SAHRizvi.pdf'>On Trisection of an Angle Leading to the Derivation of a Cubic Equation and Computation of Value of Sine </a></td>
<td> S A H Rizvi</td>
<td>103</td>
</tr>
<tr>
<td>334</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_11_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>44</td>
</tr>
<tr>
<td>335</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_12_Report.pdf'>Report: History of Science in USSR </a></td>
<td> A K Bag</td>
<td>98</td>
</tr>
<tr>
<td>336</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_1_PSingh.pdf'>Varga–Prakrtri— The Cakravala Method of its Solution and the Regular Continued–Fractions </a></td>
<td> P Singh</td>
<td>173</td>
</tr>
<tr>
<td>337</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_2_GJChhabra.pdf'>Prediction of Pluto by B Ketakar </a></td>
<td> J G Chhabra‚ S D Sharma and Manju Khanna</td>
<td>127</td>
</tr>
<tr>
<td>338</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_6_HGershenowitz.pdf'>Robert Broom’s Misinterpretation of Lamarck and Darwin </a></td>
<td> H Gershenowitz</td>
<td>174</td>
</tr>
<tr>
<td>339</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_7_AIsmail.pdf'>Surgery in the Medieval Muslim World </a></td>
<td> A Ismail and A B Khan</td>
<td>101</td>
</tr>
<tr>
<td>340</td>
<td>IJHS-19-1984-Issue-1</td>
<td>Medicine</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_1_9_Smahdihassan.pdf'>The Tridosa Doctrine and the Constituents of Chinese Humorology </a></td>
<td> S Mahadihassan</td>
<td>41</td>
</tr>
<tr>
<td>341</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_3_PDGupta.pdf'>Helminthology in India in 18th–19th Centuries with Some Remarks on its Recent Progress </a></td>
<td> P D Gupta</td>
<td>144</td>
</tr>
<tr>
<td>342</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_5_MSBhatnagar.pdf'>The Concept of Matter and its States in Indian Literature </a></td>
<td> M S Bhatnagar</td>
<td>261</td>
</tr>
<tr>
<td>343</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_8_VDeshpande.pdf'>Transmutation of Base–Metals into Gold as Described in the Text Rasarnavakalpa and its Comparison with the Parallel Chinese Methods </a></td>
<td> V Deshpande</td>
<td>104</td>
</tr>
<tr>
<td>344</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_9_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>66</td>
</tr>
<tr>
<td>345</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Other</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_10_Report.pdf'>Report: An International Islamic Science Conference </a></td>
<td> M S Khan</td>
<td>20</td>
</tr>
<tr>
<td>346</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol19_2_11_News.pdf'>News </a></td>
<td> </td>
<td>29</td>
</tr>
<tr>
<td>347</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_1_BDatta.pdf'>Use of Calculus in Hindu Mathematics </a></td>
<td> B Datta and A N Singh</td>
<td>132</td>
</tr>
<tr>
<td>348</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_2_HGershenowitz.pdf'>Encyclopaedia Judaica’s Interpretation of Neo–Lamarckism </a></td>
<td> H Gershenowitz</td>
<td>71</td>
</tr>
<tr>
<td>349</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_4_MRoy.pdf'>The Concept of Yantra in the Samarangana–Sutradharaof Bhoja </a></td>
<td> Mira Roy</td>
<td>101</td>
</tr>
<tr>
<td>350</td>
<td>IJHS-19-1984-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_2_6_RMercier.pdf'>The Astronomical Tables of Rajah Jai Singh Sawai </a></td>
<td> R Mercier</td>
<td>414</td>
</tr>
<tr>
<td>351</td>
<td>IJHS-19-1984-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_1_VVRaman.pdf'>Jean Le Rond D’Alembert 1717–1783 </a></td>
<td> V V Raman</td>
<td>235</td>
</tr>
<tr>
<td>352</td>
<td>IJHS-19-1984-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_3_VShekhawat.pdf'>Standards of Scientific Investigation: Logic and Methodology of Science in Caraka Samhita </a></td>
<td> V Shekhawat</td>
<td>509</td>
</tr>
<tr>
<td>353</td>
<td>IJHS-19-1984-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_4_DKumar.pdf'>Science in Higher Education: A Study in Victorian India </a></td>
<td> Deepak Kumar</td>
<td>137</td>
</tr>
<tr>
<td>354</td>
<td>IJHS-19-1984-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_9_Announcement.pdf'>Announcement </a></td>
<td> </td>
<td>18</td>
</tr>
<tr>
<td>355</td>
<td>IJHS-19-1984-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_10_SupplementVedangjyotishaofLagdha.pdf'>Supplement: Vedanga Jyotisa of Lagadha </a></td>
<td> S K Mukherjee</td>
<td>890</td>
</tr>
<tr>
<td>356</td>
<td>IJHS-19-1984-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_2_URBansal.pdf'>Industries in India in 18th and 19t Centuries </a></td>
<td> U R Bansal and BB Bansal</td>
<td>149</td>
</tr>
<tr>
<td>357</td>
<td>IJHS-19-1984-Issue-3</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_5_HGershenowitz.pdf'>Professor Conway Zirkle’s Vitriolic Attack on Lamarck </a></td>
<td> H Gershenowitz</td>
<td>201</td>
</tr>
<tr>
<td>358</td>
<td>IJHS-19-1984-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_6_CLYadav.pdf'>The Wonder Ayurvedic Drug Laksmana for Progeny: A Historical Appraisal </a></td>
<td> C L Yadav and  K C Chunekar</td>
<td>125</td>
</tr>
<tr>
<td>359</td>
<td>IJHS-19-1984-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_7_APKulaichev.pdf'>Sriyantra and its Mathematical Properties </a></td>
<td> A P Kulaichev</td>
<td>177</td>
</tr>
<tr>
<td>360</td>
<td>IJHS-19-1984-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_3_8_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>32</td>
</tr>
<tr>
<td>361</td>
<td>IJHS-19-1984-Issue-4</td>
<td>Biology</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_4_1_SCDey.pdf'>Ichthyological Developments in Assam in Ninteenth Century </a></td>
<td> S C Dey</td>
<td>231</td>
</tr>
<tr>
<td>362</td>
<td>IJHS-19-1984-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_4_2_DKAgarwal.pdf'>Washerman and Washing Materials in Ancient India </a></td>
<td> D K Agarwal and S C Shukla</td>
<td>118</td>
</tr>
<tr>
<td>363</td>
<td>IJHS-19-1984-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_4_6_PKChattopadhyay.pdf'>Archaeometallurgical Studies in Indian Subcontinent: A Survey on Metallography of Iron Objects </a></td>
<td> P K Chattopadhyay</td>
<td>84</td>
</tr>
<tr>
<td>364</td>
<td>IJHS-19-1984-Issue-4</td>
<td>Math</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_4_8_AKBag.pdf'>Kuttaka and Qiuyishu </a></td>
<td> A K Bag and K S Shen</td>
<td>90</td>
</tr>
<tr>
<td>365</td>
<td>IJHS-19-1984-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol19_4_9_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>128</td>
</tr>
<tr>
<td>366</td>
<td>IJHS-19-1984-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol19_4_10_NotesAndNews.pdf'>Notes and News </a></td>
<td> </td>
<td>43</td>
</tr>
<tr>
<td>367</td>
<td>IJHS-19-1984-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_4_3_MSBhatnagar.pdf'>Atom from Veda to Date </a></td>
<td> M S Bhatnagar</td>
<td>80</td>
</tr>
<tr>
<td>368</td>
<td>IJHS-19-1984-Issue-4</td>
<td>Agriculture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_4_4_HKNaqvi.pdf'>Cultivation under the Sultans of Delhi c 1206–1555 </a></td>
<td> H K Naqvi</td>
<td>192</td>
</tr>
<tr>
<td>369</td>
<td>IJHS-19-1984-Issue-4</td>
<td>Agriculture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_4_5_MMajumdar.pdf'>Risala Dar Falahat </a></td>
<td> M Majumdar</td>
<td>273</td>
</tr>
<tr>
<td>370</td>
<td>IJHS-19-1984-Issue-4</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol19_4_7_BCJoshi.pdf'>Neurology in Ancient India– Some Evidences </a></td>
<td> B C Joshi</td>
<td>354</td>
</tr>
<tr>
<td>371</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_2_KVSarma.pdf'>A Survey of Source Materials </a></td>
<td> K V Sarma</td>
<td>368</td>
</tr>
<tr>
<td>372</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_4_SNSen.pdf'>Survey of Studies in European Languages </a></td>
<td> S N Sen</td>
<td>1262</td>
</tr>
<tr>
<td>373</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_5_AKBag.pdf'>Astronomy in Indus Civilization and during Vedic Times </a></td>
<td> A K Bag</td>
<td>158</td>
</tr>
<tr>
<td>374</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_8_SDSharma.pdf'>Eclipses‚ Parallax and Precession of Equinoxes </a></td>
<td> S D Sharma</td>
<td>383</td>
</tr>
<tr>
<td>375</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_9_KSShukla.pdf'>Phases of The Moon, Rising and Setting Of Planets and Stars and Their Conjunstions </a></td>
<td> K S Shukla</td>
<td>575</td>
</tr>
<tr>
<td>376</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_12_SDSharma.pdf'>Astronomical Observatories </a></td>
<td> S D Sharma</td>
<td>481</td>
</tr>
<tr>
<td>377</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_3_SAKhan.pdf'>Development of Zij Literature in India </a></td>
<td> S A Khan</td>
<td>473</td>
</tr>
<tr>
<td>378</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_6_SDSharma.pdf'>Post–Vedic Astronomy </a></td>
<td> S D Sharma</td>
<td>235</td>
</tr>
<tr>
<td>379</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_7_ASomayaji.pdf'>The Yuga System And The Computations of Mean and True Planetary Longitudes </a></td>
<td> D Arka Somayaji</td>
<td>669</td>
</tr>
<tr>
<td>380</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_11_RNRai.pdf'>Astronomical Instruments </a></td>
<td> R N Rai</td>
<td>453</td>
</tr>
<tr>
<td>381</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_13_SMRAnsari.pdf'>Introduction of Modern western Astronomy in India During 18–19 Centuries </a></td>
<td> S M R Ansari</td>
<td>735</td>
</tr>
<tr>
<td>382</td>
<td>IJHS-20-1985-Issue-1to4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol20-1to4_14_JCBhattacharyya.pdf'>Astronomy in India in the 20th Century </a></td>
<td> J C Bhattacharyya</td>
<td>529</td>
</tr>
<tr>
<td>383</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_1_SMahdihassan.pdf'>Ephedra as Soma Meaning Hemp Fibres with Soma Later Misidentified as the Hemp Plant Itself </a></td>
<td> S Mahdihassan</td>
<td>156</td>
</tr>
<tr>
<td>384</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_2_ASRamanathan.pdf'>Contribution to ‘Weather Science in Ancient India-I’ </a></td>
<td> A S Ramanathan</td>
<td>146</td>
</tr>
<tr>
<td>385</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_3_ASRamanathan.pdf'>Contribution to ‘Weather Science in Ancient India-II’ </a></td>
<td> A S Ramanathan</td>
<td>99</td>
</tr>
<tr>
<td>386</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_4_RDRoy.pdf'>The Great Trignometrical Survey of India in a Historical Perspective </a></td>
<td> Rama Deb Roy</td>
<td>191</td>
</tr>
<tr>
<td>387</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_5_RRDaniel.pdf'>The Method of Science in Astronomy </a></td>
<td> R R Daniel</td>
<td>342</td>
</tr>
<tr>
<td>388</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_6_RCGupta.pdf'>Some Equalization Problems from the Bakshali Manuscript </a></td>
<td> R C Gupta</td>
<td>174</td>
</tr>
<tr>
<td>389</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_7_SKak.pdf'>Computational Aspects of the Aryabhata Algorithm </a></td>
<td> Subhash Kak</td>
<td>136</td>
</tr>
<tr>
<td>390</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_8_BZSzalek.pdf'>Decipherment and Interpretation of the Proto–Indian (Mohenjo–Daro and Harappa) Inscriptions </a></td>
<td> Benon Zb Szalek</td>
<td>77</td>
</tr>
<tr>
<td>391</td>
<td>IJHS-21-1986-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_9_BookReview.pdf'>Book Review </a></td>
<td> M S Khan</td>
<td>115</td>
</tr>
<tr>
<td>392</td>
<td>IJHS-21-1986-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_1_11_News.pdf'>News </a></td>
<td> </td>
<td>42</td>
</tr>
<tr>
<td>393</td>
<td>IJHS-21-1986-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_1_VShekhawat.pdf'>The Art of Theory Construction in Caraka Samhita </a></td>
<td> Virendra Shekhawat</td>
<td>276</td>
</tr>
<tr>
<td>394</td>
<td>IJHS-21-1986-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_2_PKunitzsch.pdf'>Star Catalogues and Star Tables in Medieval Oriental and European Astronomy </a></td>
<td> Paun Kunitzsch</td>
<td>232</td>
</tr>
<tr>
<td>395</td>
<td>IJHS-21-1986-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_3_PSingh.pdf'>Narayana’s Treatment of Magic Squares </a></td>
<td> Parmanand Singh</td>
<td>143</td>
</tr>
<tr>
<td>396</td>
<td>IJHS-21-1986-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_4_RCGupta.pdf'>Madhavacandra’s and Other Octagonal Derivations of the Jaina Value Π = √10 </a></td>
<td> R C Gupta</td>
<td>151</td>
</tr>
<tr>
<td>397</td>
<td>IJHS-21-1986-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_5_SAHRizvi.pdf'>Arithmetical Ratio of Diameter to its Circumference of a Circle with Special Reference to Jame–I–Bahadur Khani </a></td>
<td> Syed Aftab Husain Rizvi</td>
<td>146</td>
</tr>
<tr>
<td>398</td>
<td>IJHS-21-1986-Issue-2</td>
<td>Math</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_6_BCJoshi.pdf'>Neurology in Ancient India: Muladhara Cakra—A Physiological Reality </a></td>
<td> B C Joshi</td>
<td>597</td>
</tr>
<tr>
<td>399</td>
<td>IJHS-21-1986-Issue-2</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_7_OPUpadhyay.pdf'>Evolution of Kusta </a></td>
<td> O P upadhyay</td>
<td>244</td>
</tr>
<tr>
<td>400</td>
<td>IJHS-21-1986-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_8_SMahdihassan.pdf'>Lac and its Decolourization by Orpiment as Traced to Babylon </a></td>
<td> S Mahdihassan</td>
<td>146</td>
</tr>
<tr>
<td>401</td>
<td>IJHS-21-1986-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_9_BookReviews.pdf'>Book Review: Medical Education and Research: Western Medicine in India </a></td>
<td> S M R Ansari</td>
<td>123</td>
</tr>
<tr>
<td>402</td>
<td>IJHS-21-1986-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_10_Report.pdf'>Report: Seminar on Science‚ Technology and Social Change‚ 1900–1980 </a></td>
<td> S N Sen</td>
<td>47</td>
</tr>
<tr>
<td>403</td>
<td>IJHS-21-1986-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_11_News.pdf'>News </a></td>
<td> </td>
<td>55</td>
</tr>
<tr>
<td>404</td>
<td>IJHS-21-1986-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_2_12_Announcements.pdf'>Announcements </a></td>
<td> </td>
<td>50</td>
</tr>
<tr>
<td>405</td>
<td>IJHS-21-1986-Issue-3</td>
<td>MindSciences</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_1_ARahman.pdf'>On Relevance of Ibn Sina Today </a></td>
<td> A Rahman</td>
<td>246</td>
</tr>
<tr>
<td>406</td>
<td>IJHS-21-1986-Issue-3</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_2_MFAintabi.pdf'>Ibn Sina: Genius of Arabic–Islamic Civilization </a></td>
<td> Mahomed Fouad Aintabi</td>
<td>46</td>
</tr>
<tr>
<td>407</td>
<td>IJHS-21-1986-Issue-3</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_3_MAsimov.pdf'>The Life and Teachings of Ibn Sina </a></td>
<td> Muhamed Asimov</td>
<td>499</td>
</tr>
<tr>
<td>408</td>
<td>IJHS-21-1986-Issue-3</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_4_MMKhairullayev.pdf'>Some Treatises and Epistles of Ibn Sina </a></td>
<td> M M Khairullayev</td>
<td>141</td>
</tr>
<tr>
<td>409</td>
<td>IJHS-21-1986-Issue-3</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_5_KNPandita.pdf'>Central Asian Society in Ibn Sina’s Time </a></td>
<td> K N Pandita</td>
<td>115</td>
</tr>
<tr>
<td>410</td>
<td>IJHS-21-1986-Issue-3</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_6_MAsimov.pdf'>Poetic and Socio–Ethic Views of Ibn Sina </a></td>
<td> Muhamed Asimov</td>
<td>76</td>
</tr>
<tr>
<td>411</td>
<td>IJHS-21-1986-Issue-3</td>
<td>MindSciences</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_7_HMSaid.pdf'>Ibn Sina as a Scientist </a></td>
<td> Hakim Mohammed Said</td>
<td>182</td>
</tr>
<tr>
<td>412</td>
<td>IJHS-21-1986-Issue-3</td>
<td>MindSciences</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_8_AKBag.pdf'>Ibn Sina and Indian Science </a></td>
<td> A K Bag</td>
<td>132</td>
</tr>
<tr>
<td>413</td>
<td>IJHS-21-1986-Issue-3</td>
<td>MindSciences</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_9_SAARizvi.pdf'>Ibn Sina’s Impact on the Rational and Scientific Movements in India </a></td>
<td> S A A Rizvi</td>
<td>202</td>
</tr>
<tr>
<td>414</td>
<td>IJHS-21-1986-Issue-3</td>
<td>MindSciences</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_10_WHAbdi.pdf'>Ibn Sina’s Critique Mutakallimin’s Atomic Theory </a></td>
<td> Wazir Hsan Abdi</td>
<td>160</td>
</tr>
<tr>
<td>415</td>
<td>IJHS-21-1986-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_3_11_Report.pdf'>Report: XVII International Union for History and Philosophy of Science Congress </a></td>
<td> S K Mukherjee and A K Bag</td>
<td>79</td>
</tr>
<tr>
<td>416</td>
<td>IJHS-21-1986-Issue-4</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_4_1_SRAPerwaz.pdf'>Ibn Sina’s Medical Works </a></td>
<td> Syed Riyaz ‘Ali Perwaz</td>
<td>356</td>
</tr>
<tr>
<td>417</td>
<td>IJHS-21-1986-Issue-4</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_4_2_MSKhan.pdf'>The Section on Cardiac Diseases and Their Treatment in the Qanun of Ibn Sina </a></td>
<td> M S Khan</td>
<td>253</td>
</tr>
<tr>
<td>418</td>
<td>IJHS-21-1986-Issue-4</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_4_3_TSiddiqi.pdf'>Ibn Sina on Materia Medica </a></td>
<td> Tazimuddin Siddiqi</td>
<td>629</td>
</tr>
<tr>
<td>419</td>
<td>IJHS-21-1986-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_4_4_GNChaturvedi.pdf'>Impact of Ibn Sina on Pulse Examination and Materia Medica of Medieval Period of Ayurveda </a></td>
<td> G N Chaturvedi and K P Singh</td>
<td>125</td>
</tr>
<tr>
<td>420</td>
<td>IJHS-21-1986-Issue-4</td>
<td>MindSciences</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_4_5_MTaiyab.pdf'>Physiological Approach of Ibn Sina Towards the Science of Behaviour </a></td>
<td> M Taiyab</td>
<td>92</td>
</tr>
<tr>
<td>421</td>
<td>IJHS-21-1986-Issue-4</td>
<td>MindSciences</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_4_6_PNPushp.pdf'>Ibn Sina on Speech Articulation </a></td>
<td> P N Pushp</td>
<td>123</td>
</tr>
<tr>
<td>422</td>
<td>IJHS-21-1986-Issue-4</td>
<td>MindSciences</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_4_7_HSVirk.pdf'>Ibn Sina’s Approach to Physics </a></td>
<td> H S Virk</td>
<td>93</td>
</tr>
<tr>
<td>423</td>
<td>IJHS-21-1986-Issue-4</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol21_4_8_SShafi.pdf'>Contributions of Ibn Sina to Geographical Knowledge </a></td>
<td> M Shafi</td>
<td>98</td>
</tr>
<tr>
<td>424</td>
<td>IJHS-22-1987-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_1_ASRamanathan.pdf'>Contribution to ‘Weather Science in Ancient India’ IV </a></td>
<td> A S Ramanathan</td>
<td>121</td>
</tr>
<tr>
<td>425</td>
<td>IJHS-22-1987-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol22_1_2_VDeshpande.pdf'>Medieval Transformation of Alchemical and Chemical Ideas between India and China </a></td>
<td> Vijaya Deshpande</td>
<td>0</td>
</tr>
<tr>
<td>426</td>
<td>IJHS-22-1987-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_4_AKBiswas.pdf'>Rasa– Ratna– Samuccaya and Mineral Processing State–of–Art in the 13th Century AD India </a></td>
<td> Arun Kumar Biswas</td>
<td>410</td>
</tr>
<tr>
<td>427</td>
<td>IJHS-22-1987-Issue-1</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_5_WHAbdi.pdf'>Mulla Mahmud Jaunpuri's Theory of Moon–Spots </a></td>
<td> Wazir Hasan Abdi</td>
<td>85</td>
</tr>
<tr>
<td>428</td>
<td>IJHS-22-1987-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_6_SCKak.pdf'>On the Decipherment of the Indus Script— A Preliminary Study of its Connection with Brahmi </a></td>
<td> Subhash C Kak</td>
<td>204</td>
</tr>
<tr>
<td>429</td>
<td>IJHS-22-1987-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_7_SMahdihassan.pdf'>History of Cinnabar as Drug, The Natural Substance and Synthetic Product </a></td>
<td> S Mahdihassan</td>
<td>195</td>
</tr>
<tr>
<td>430</td>
<td>IJHS-22-1987-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_8_RKrishnamurthy.pdf'>Perfumery in Ancient India </a></td>
<td> Radha Krishnamurthy</td>
<td>187</td>
</tr>
<tr>
<td>431</td>
<td>IJHS-22-1987-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_9_SChandra.pdf'>Some Reflections from the Works of Vernadsky (1863–1945) </a></td>
<td> Sanjay Chandra</td>
<td>79</td>
</tr>
<tr>
<td>432</td>
<td>IJHS-22-1987-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_10_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>110</td>
</tr>
<tr>
<td>433</td>
<td>IJHS-22-1987-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1_11_Report.pdf'>Report </a></td>
<td> S N Sen</td>
<td>19</td>
</tr>
<tr>
<td>434</td>
<td>IJHS-22-1987-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_1-12_Announcements.pdf'>Announcements </a></td>
<td> </td>
<td>75</td>
</tr>
<tr>
<td>435</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_2_RPSTyagi.pdf'>Importnace of Studying Veterinary Science Literature in Ancient India </a></td>
<td> R P S Tyagi</td>
<td>36</td>
</tr>
<tr>
<td>436</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_3_VKSharma.pdf'>Scope of Study of Veterinary Science Literature in Ancient India </a></td>
<td> V K Sharma</td>
<td>94</td>
</tr>
<tr>
<td>437</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_4_GPrasad.pdf'>Method of Science used in Past Indian and its Relevance to Present Day Context </a></td>
<td> Gaya Prasad</td>
<td>74</td>
</tr>
<tr>
<td>438</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_5_DNGarg.pdf'>Souces of Ancient Indian Literature on Veterinary Sciences </a></td>
<td> D N Garo</td>
<td>147</td>
</tr>
<tr>
<td>439</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_6_KCSatija.pdf'>Rural Folk Prescriptions: Plea for Search of Scientific Content </a></td>
<td> K C Satija</td>
<td>140</td>
</tr>
<tr>
<td>440</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_7_RDRana.pdf'>Pharmacy in Ancient India </a></td>
<td> R D Rana</td>
<td>66</td>
</tr>
<tr>
<td>441</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_8_VMMandokhot.pdf'>Nutritional and Managerial Practices of Animals in Ancient India </a></td>
<td> V M Mandokhot</td>
<td>130</td>
</tr>
<tr>
<td>442</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_9_UMandokhot.pdf'>Breeding Practices and Selection Criteria for Domestication of Animals </a></td>
<td> Usha V Mandokhot</td>
<td>182</td>
</tr>
<tr>
<td>443</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_10_SPrasad.pdf'>Administrative Recommendation in regard to Upkeeping, Health, and Management of Animals in Ancient India </a></td>
<td> S Prasad</td>
<td>100</td>
</tr>
<tr>
<td>444</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_11_SKKalra.pdf'>Posibilities of relating Modern Veterinary Science Literature to the Growth of Relevant Knowledge in Ancient India </a></td>
<td> S K Kalra</td>
<td>325</td>
</tr>
<tr>
<td>445</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_12_RDSharma.pdf'>Historical Background and Analysis of Scientific Content of Ancient Indian Literature on Practices for the Treatment of Diseases of Domestic Animals </a></td>
<td> R D Sharma, Rakesh Kumar and Sridhar</td>
<td>126</td>
</tr>
<tr>
<td>446</td>
<td>IJHS-22-1987-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_13_SCDogra.pdf'>Antimicrobial Agents used in Ancient India </a></td>
<td> S C Dogra</td>
<td>117</td>
</tr>
<tr>
<td>447</td>
<td>IJHS-22-1987-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_2_14_News.pdf'>News </a></td>
<td> </td>
<td>59</td>
</tr>
<tr>
<td>448</td>
<td>IJHS-22-1987-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_1_ASRamanathan.pdf'>Contribution to Weather Science in Ancient India. V— Priciples of Forecasting Rainfall in Ancient India (Long Range) </a></td>
<td> A S Ramanathan</td>
<td>288</td>
</tr>
<tr>
<td>449</td>
<td>IJHS-22-1987-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_2_ASRamanathan.pdf'>Contribution to Weather Science in Ancient India. VI— Priciples of Forecasting Rainfall in Ancient India (Short and Medium Range) </a></td>
<td> A S Ramanathan</td>
<td>128</td>
</tr>
<tr>
<td>450</td>
<td>IJHS-22-1987-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_3_ASRamanathan.pdf'>Contribution to Weather Science in Ancient India. VII— A Scientific Assessment of the Rules of Rainfall Forecasting Practiced in Ancient India </a></td>
<td> A S Ramanathan</td>
<td>148</td>
</tr>
<tr>
<td>451</td>
<td>IJHS-22-1987-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_4_SCKak.pdf'>On Astronomy in Ancient India </a></td>
<td> Subhash C Kak</td>
<td>349</td>
</tr>
<tr>
<td>452</td>
<td>IJHS-22-1987-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_5_SCKak.pdf'>On the Chronology in Ancient India </a></td>
<td> Subhash C Kak</td>
<td>287</td>
</tr>
<tr>
<td>453</td>
<td>IJHS-22-1987-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_6_OPUpadhyay.pdf'>A Few Facts of Historiacl Interest Relating to Diabetes Mellitus </a></td>
<td> O P Upadhyay and D Upadhyay</td>
<td>107</td>
</tr>
<tr>
<td>454</td>
<td>IJHS-22-1987-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_7_RCGupta.pdf'>Indian Mathematical Sciences Abroad During Pre–modern Times </a></td>
<td> R C Gupta</td>
<td>173</td>
</tr>
<tr>
<td>455</td>
<td>IJHS-22-1987-Issue-3</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_8_Jlaurent.pdf'>Milgram's Shocking Experiments: A Case in Social Construction of ‘Science’ </a></td>
<td> John Laurent</td>
<td>632</td>
</tr>
<tr>
<td>456</td>
<td>IJHS-22-1987-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_9_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>57</td>
</tr>
<tr>
<td>457</td>
<td>IJHS-22-1987-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_3_10_Supplement_RasaRatnaSamuccaya.pdf'>Supplement: Rasa Ratna Samuccaya </a></td>
<td> </td>
<td>1612</td>
</tr>
<tr>
<td>458</td>
<td>IJHS-22-1987-Issue-4</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_1_ASRamanathan.pdf'>Contribution to Weather Science in Ancient India. VIII— Observation and Measurement of Meteorological Parameters in Ancient India </a></td>
<td> A S Ramanathan</td>
<td>152</td>
</tr>
<tr>
<td>459</td>
<td>IJHS-22-1987-Issue-4</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_2_SMahdihassan.pdf'>Three Important Vedic Grasses </a></td>
<td> S Mahdihassan</td>
<td>215</td>
</tr>
<tr>
<td>460</td>
<td>IJHS-22-1987-Issue-4</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_3_BCJoshi.pdf'>Neurology in Ancient India: Ajna Cakra— A Physiological Reality </a></td>
<td> B C Joshi</td>
<td>349</td>
</tr>
<tr>
<td>461</td>
<td>IJHS-22-1987-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_4_RPKulkarni.pdf'>Development of Engineering and Technology in India from 1000 BC to 1000 AD as revealed in Rajatarangini </a></td>
<td> R P Kulkarni</td>
<td>201</td>
</tr>
<tr>
<td>462</td>
<td>IJHS-22-1987-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_5_RPKulkarni.pdf'>Specifications for Brick Masonry according to Samarangana Sutradhara </a></td>
<td> R P Kulkarni</td>
<td>59</td>
</tr>
<tr>
<td>463</td>
<td>IJHS-22-1987-Issue-4</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_6_BNMehrotra.pdf'>Anthelmintic Plants in Traditional Remedies in India </a></td>
<td> Ved Prakash and B N Mehrotra</td>
<td>144</td>
</tr>
<tr>
<td>464</td>
<td>IJHS-22-1987-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_7_VSingh.pdf'>Why did the Scientific Revolution take place in Europe and not elsewhere? </a></td>
<td> Virendra Singh</td>
<td>204</td>
</tr>
<tr>
<td>465</td>
<td>IJHS-22-1987-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_8_SPGupta.pdf'>Science and Divine Philosophy in the Seventeenth Century Europe </a></td>
<td> S P Gupta</td>
<td>68</td>
</tr>
<tr>
<td>466</td>
<td>IJHS-22-1987-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol22_4_9_RKTrivedi.pdf'>Todaramala of Jaipur (A Jaina Philosopher– Mathematician) </a></td>
<td> R K Trivedi</td>
<td>395</td>
</tr>
<tr>
<td>467</td>
<td>IJHS-24-1989-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_1_1_SCKak.pdf'>Some Early Codes and Ciphers </a></td>
<td> Subhas K Kak</td>
<td>82</td>
</tr>
<tr>
<td>468</td>
<td>IJHS-24-1989-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_1_2_GArmitage.pdf'>The Schlagintweit Collections </a></td>
<td> G Armitage</td>
<td>1890</td>
</tr>
<tr>
<td>469</td>
<td>IJHS-24-1989-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_1_3_PJha.pdf'>Development of Hindu Astro–Mathematical Sciences in Mithila </a></td>
<td> Parameshwar Jha</td>
<td>153</td>
</tr>
<tr>
<td>470</td>
<td>IJHS-24-1989-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_1_4_BookReview.pdf'>Book Review </a></td>
<td> </td>
<td>29</td>
</tr>
<tr>
<td>471</td>
<td>IJHS-24-1989-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_1_5_Supplement.pdf'>Supplement: Rasa Ratna Sammuccaya </a></td>
<td> </td>
<td>684</td>
</tr>
<tr>
<td>472</td>
<td>IJHS-24-1989-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_2_1_SAHRizvi.pdf'>Seth Ward and Ghulam Husain’s Problem for Determining the Place of a Planet </a></td>
<td> Syed Aftab Husain Rizvi</td>
<td>108</td>
</tr>
<tr>
<td>473</td>
<td>IJHS-24-1989-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_2_2_SSeshan.pdf'>The History of Paper in India Upto 1948 </a></td>
<td> Sita Ramaseshan</td>
<td>582</td>
</tr>
<tr>
<td>474</td>
<td>IJHS-24-1989-Issue-2</td>
<td>Culture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_2_3_BSzalek.pdf'>Evidence for Proto–Indian Origin of the Easter Island Writing System </a></td>
<td> Benon Zb Szalek</td>
<td>185</td>
</tr>
<tr>
<td>475</td>
<td>IJHS-24-1989-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_2_4_BookReviews.pdf'>Book Review </a></td>
<td> </td>
<td>38</td>
</tr>
<tr>
<td>476</td>
<td>IJHS-24-1989-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_1_5_Supplement.pdf'>Supplement: Rasa Ratna Sammuccaya </a></td>
<td> </td>
<td>684</td>
</tr>
<tr>
<td>477</td>
<td>IJHS-24-1989-Issue-3</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_1_APKulaichev.pdf'>Sriyantra— The Ancient Intrument to Control the Psychophisiological State of Man </a></td>
<td> Alexey Pavlovich Kulaichev and Dina Mikhailovna Ramendic</td>
<td>270</td>
</tr>
<tr>
<td>478</td>
<td>IJHS-24-1989-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_2_SAParamhans.pdf'>A Fresh Glimse on the Date of Mahabharata </a></td>
<td> S A Paramhans</td>
<td>89</td>
</tr>
<tr>
<td>479</td>
<td>IJHS-24-1989-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol24_4_2_SAParamhans.pdf'>A Glance at Military Techniques in Ramayana and Mahabharata </a></td>
<td> </td>
<td>0</td>
</tr>
<tr>
<td>480</td>
<td>IJHS-24-1989-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_4BBLal.pdf'>Vedic Mathematics— Mathematical Calculations Based on the Vedic Sutras and on the Lilavati </a></td>
<td> B B Lal</td>
<td>61</td>
</tr>
<tr>
<td>481</td>
<td>IJHS-24-1989-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_5_LCJain.pdf'>System Theory in Jaina School of Mathematics–II </a></td>
<td> L C Jain</td>
<td>255</td>
</tr>
<tr>
<td>482</td>
<td>IJHS-24-1989-Issue-3</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_6_SMahadihassan.pdf'>A Comparitive Study of Chinese Cosmology–cum–Humorology with Eight Elements </a></td>
<td> S Mahdihassan</td>
<td>72</td>
</tr>
<tr>
<td>483</td>
<td>IJHS-24-1989-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_7_RKKochhar.pdf'>Transit of Mercury 1651: The Earliest Telescopic Observation in India </a></td>
<td> R K Kochhar</td>
<td>95</td>
</tr>
<tr>
<td>484</td>
<td>IJHS-24-1989-Issue-3</td>
<td>Culture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_8_AKBiswas.pdf'>History of Science in India: In the Search of a Paradigm </a></td>
<td> Sulekha Biswas and Arun Kumar Biswas</td>
<td>175</td>
</tr>
<tr>
<td>485</td>
<td>IJHS-24-1989-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_9_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>67</td>
</tr>
<tr>
<td>486</td>
<td>IJHS-24-1989-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_3_10_ProjectsRenewed.pdf'>News: Projects Reviewed and Approved duing 1988–89 </a></td>
<td> </td>
<td>43</td>
</tr>
<tr>
<td>487</td>
<td>IJHS-24-1989-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_1_5_Supplement.pdf'>Supplement: Rasa Ratna Sammuccaya </a></td>
<td> </td>
<td>684</td>
</tr>
<tr>
<td>488</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_1_KSShukla.pdf'>The Yuga of the Yavanajataka–David Pingree’s Text and Translation Reviewed </a></td>
<td> K S Shukla</td>
<td>179</td>
</tr>
<tr>
<td>489</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_2_BSen.pdf'>Development of Technical Education in India and State Policy—A Historical Perspective </a></td>
<td> Biman Sen</td>
<td>524</td>
</tr>
<tr>
<td>490</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_3_TRChandrasekhar.pdf'>Non–Euclidean Geometry from Early Times to Beltrami </a></td>
<td> T R Chandrasekhar</td>
<td>131</td>
</tr>
<tr>
<td>491</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_4_SNSen.pdf'>Madras Meridian Circle Observations of Fixed Stars during 1862–1887 </a></td>
<td> S N Sen</td>
<td>466</td>
</tr>
<tr>
<td>492</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_5_MCMallik.pdf'>A Survey of Research and Development in Electronics and Telecommunication in India Over a Century (1850–1950) </a></td>
<td> Late M C Mallick</td>
<td>712</td>
</tr>
<tr>
<td>493</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_6_ABasu.pdf'>Chemical Research in India During Nineteenth Century </a></td>
<td> Aparajito Basu</td>
<td>183</td>
</tr>
<tr>
<td>494</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_7_VLSharma.pdf'>Weighing Devices in Ancient India </a></td>
<td> Vijaya Lakshmi Sharma and H C Bhardwaj</td>
<td>129</td>
</tr>
<tr>
<td>495</td>
<td>IJHS-24-1989-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_8_SMahadihassan.pdf'>The Five Souls of Indian Medicine </a></td>
<td> S Mahdihassan</td>
<td>63</td>
</tr>
<tr>
<td>496</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_9_BookReview.pdf'>Book Review </a></td>
<td> C K Majumdar</td>
<td>47</td>
</tr>
<tr>
<td>497</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_10_Report.pdf'>Report: Seminar on Astronomy and Mathematics in Ancient and Medieval India </a></td>
<td> S N Sen</td>
<td>109</td>
</tr>
<tr>
<td>498</td>
<td>IJHS-24-1989-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol24_4_11_Supplement.pdf'>Supplement: Rasa Ratna Sammuccaya </a></td>
<td> </td>
<td>427</td>
</tr>
<tr>
<td>499</td>
<td>IJHS-25-1990-Issue-1to4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol25_1to4_1_SMahdihassan.pdf'>The Phases of Magic Square of Three </a></td>
<td> S Mahdihassan</td>
<td>52</td>
</tr>
<tr>
<td>500</td>
<td>IJHS-25-1990-Issue-1to4</td>
<td>nan</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol25_1to4_2_AKBag.pdf'>Ritual Geometry in India and its Parallelism in Other Cultures </a></td>
<td> A K Bag</td>
<td>223</td>
</tr>
<tr>
<td>501</td>
<td>IJHS-25-1990-Issue-1to4</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol25_1to4_3_MSKhan.pdf'>Ali Ibn Rabban At Tabari‚ A Ninth Century Arab Physician, on the Ayurveda </a></td>
<td> M S Khan</td>
<td>208</td>
</tr>
<tr>
<td>502</td>
<td>IJHS-25-1990-Issue-1to4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol25_1to4_4_VNSharma.pdf'>Zij–I–Muhammad and the Tables of De La Hire </a></td>
<td> Virendra Nath Sharma</td>
<td>192</td>
</tr>
<tr>
<td>503</td>
<td>IJHS-25-1990-Issue-1to4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol25_1to4_5_NewsProjectsapprovedNewpublication.pdf'>News </a></td>
<td> </td>
<td>109</td>
</tr>
<tr>
<td>504</td>
<td>IJHS-25-1990-Issue-1to4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol25_1to4_6_SupplementLaghumanasa.pdf'>Supplement—Laghumanasa of Manjula </a></td>
<td> </td>
<td>2361</td>
</tr>
<tr>
<td>505</td>
<td>IJHS-26-1991-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_1_1_KDAbhyankar.pdf'>Misidentification of some Indian Naksatras </a></td>
<td> K D Abhyankar</td>
<td>160</td>
</tr>
<tr>
<td>506</td>
<td>IJHS-26-1991-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_1_2_SMahdihassan.pdf'>The Vedic Gods Agni‚ Indra and Soma as Interrelated: A Study of Soma </a></td>
<td> S Mahadihassan</td>
<td>81</td>
</tr>
<tr>
<td>507</td>
<td>IJHS-26-1991-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_1_3_SRSarma.pdf'>The Pratyayas: Indian Contribution to Combinatorics </a></td>
<td> L Alsdorf</td>
<td>630</td>
</tr>
<tr>
<td>508</td>
<td>IJHS-26-1991-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_1_4_SAParamhans.pdf'>Astronomy in Ancient India— Its Importance‚ Insight and Prevelance </a></td>
<td> S A Paramhans</td>
<td>118</td>
</tr>
<tr>
<td>509</td>
<td>IJHS-26-1991-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_1_5_AKChakraborty.pdf'>Some Studies on Varahamihira </a></td>
<td> A K Chakravaty</td>
<td>107</td>
</tr>
<tr>
<td>510</td>
<td>IJHS-26-1991-Issue-1</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_1_6_SSangwan.pdf'>Level of Agricultural Technology in India (1757–1857) </a></td>
<td> S Sangwan</td>
<td>674</td>
</tr>
<tr>
<td>511</td>
<td>IJHS-26-1991-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_1_7_ABandyopandhyay.pdf'>Radha Gobinda Chandra— A Pioneer in Astronomical Observations in India </a></td>
<td> A Bandyopadhyay</td>
<td>175</td>
</tr>
<tr>
<td>512</td>
<td>IJHS-26-1991-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol26_1_8_BookReview.pdf'>Book Review: Vatesvara Siddhanta and Gola of Vatesvara by K S Shukla </a></td>
<td> D Pingree</td>
<td>111</td>
</tr>
<tr>
<td>513</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_1_KTAcharya.pdf'>Alcoholic Fermentation and its Products in Ancient India </a></td>
<td> K T Achaya</td>
<td>104</td>
</tr>
<tr>
<td>514</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_2_SMahdihassan.pdf'>The Word Kohala in Susruta and Term Alcool–Vini of Paracelsus </a></td>
<td> S Mahadihassan</td>
<td>34</td>
</tr>
<tr>
<td>515</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_3_MRay.pdf'>Minerals and Gems in Indian Alchemy </a></td>
<td> Mira Ray</td>
<td>313</td>
</tr>
<tr>
<td>516</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_4_MChaudhuri.pdf'>Arbori–Horticulture: As Known in the Puranas </a></td>
<td> M Chaudhuri</td>
<td>65</td>
</tr>
<tr>
<td>517</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_5_HKNaqvi.pdf'>Dyeing Agents in India A D 1200–1800 </a></td>
<td> H K Naqvi</td>
<td>272</td>
</tr>
<tr>
<td>518</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_6_KVSarma.pdf'>Yuktibhasa of Jyesthadeva </a></td>
<td> K V Sarma and S Hariharan</td>
<td>316</td>
</tr>
<tr>
<td>519</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_7_VNSharma.pdf'>The Kapala Yantras of Sawai Jai Singh </a></td>
<td> V N Sharma</td>
<td>135</td>
</tr>
<tr>
<td>520</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_8_AKSaxena.pdf'>Optical Glass: Its Manufacture in India— A Historical Perspective </a></td>
<td> A K Saxena‚ A Vagiswari and M Manjula</td>
<td>176</td>
</tr>
<tr>
<td>521</td>
<td>IJHS-26-1991-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_2_9_NewsIHCongress.pdf'>News: Seminar on Indian Astronomy and Jai Singh— A Report </a></td>
<td> S M R Ansari</td>
<td>27</td>
</tr>
<tr>
<td>522</td>
<td>IJHS-26-1991-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_3_1_PVSharma.pdf'>An Anonymous Treatise on Pathyapathya </a></td>
<td> P V Sharma</td>
<td>229</td>
</tr>
<tr>
<td>523</td>
<td>IJHS-26-1991-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_3_2_VNSharma.pdf'>Precision Instruments of Sawai Jai Singh </a></td>
<td> V N Sharma</td>
<td>508</td>
</tr>
<tr>
<td>524</td>
<td>IJHS-26-1991-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_3_3_AKarbelashvili.pdf'>Europe–India Telegraph “Bridge” via the Caucasus </a></td>
<td> A Karbelashvili</td>
<td>90</td>
</tr>
<tr>
<td>525</td>
<td>IJHS-26-1991-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_3_4_PKBasu.pdf'>Newton’s Physics in the Context of His Works on Chemistry and Alchemy </a></td>
<td> P K Basu</td>
<td>492</td>
</tr>
<tr>
<td>526</td>
<td>IJHS-26-1991-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_3_5_SupplementRasaratnasamucchaya.pdf'>Supplement: Rasa Ratna Samuccaya (Part II) </a></td>
<td> </td>
<td>386</td>
</tr>
<tr>
<td>527</td>
<td>IJHS-26-1991-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_4_1_BPrakash.pdf'>Metallurgy of Iron and Steel Making and Blacksmithy in Ancient India </a></td>
<td> B Prakash</td>
<td>449</td>
</tr>
<tr>
<td>528</td>
<td>IJHS-26-1991-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_4_2_SMahdihassan.pdf'>A Consolidated Symbol of Cosmology </a></td>
<td> S Mahadihassan</td>
<td>37</td>
</tr>
<tr>
<td>529</td>
<td>IJHS-26-1991-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_4_3_NKChandel.pdf'>A Comparative Study on Cometary Records from the Brhat Samhita and Bhadrabahu Samhita </a></td>
<td> N K Chandel and S Sharma</td>
<td>111</td>
</tr>
<tr>
<td>530</td>
<td>IJHS-26-1991-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_4_4_GAbraham.pdf'>Mean Sun and Moon in Ancient Greek and Indian Astronomy </a></td>
<td> George Abraham</td>
<td>64</td>
</tr>
<tr>
<td>531</td>
<td>IJHS-26-1991-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_4_5_SPGupta.pdf'>Realism in Science </a></td>
<td> S P Gupta</td>
<td>59</td>
</tr>
<tr>
<td>532</td>
<td>IJHS-26-1991-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol26_4_6_SupplementsPanchavimsatika.pdf'>Supplements </a></td>
<td> </td>
<td>1078</td>
</tr>
<tr>
<td>533</td>
<td>IJHS-27-1992-Issue-1</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_1_1_SMahdihassan.pdf'>The Five Elements of Chinese Cosmology in the Light of Dialectism </a></td>
<td> S Mahdihassan</td>
<td>41</td>
</tr>
<tr>
<td>534</td>
<td>IJHS-27-1992-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_1_2_KTAchaya.pdf'>Indian Oilpress (Ghani) </a></td>
<td> K T Acharya</td>
<td>131</td>
</tr>
<tr>
<td>535</td>
<td>IJHS-27-1992-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_1_3_NSaxena.pdf'>Yogaratnakara— An Important Source Book in Medicine </a></td>
<td> Nirmal Saxena</td>
<td>188</td>
</tr>
<tr>
<td>536</td>
<td>IJHS-27-1992-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_1_4_KAChowdhury.pdf'>Krsi– Parasara </a></td>
<td> Kafil Ahmed Chowdhury</td>
<td>337</td>
</tr>
<tr>
<td>537</td>
<td>IJHS-27-1992-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_1_5_BDatta.pdf'>Magic Squares in India </a></td>
<td> Bibhutibhusan Datta and Awadhesh Narayan Singh</td>
<td>1067</td>
</tr>
<tr>
<td>538</td>
<td>IJHS-27-1992-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_2_1_VDeshpande.pdf'>Vangastambhanasodhanam: A Chapter on Metallurgy of Tin in Sanskrit Alchemical Text ‘Rasopanisad’ </a></td>
<td> Vijaya Deshpande</td>
<td>158</td>
</tr>
<tr>
<td>539</td>
<td>IJHS-27-1992-Issue-2</td>
<td>Agriculture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_2_2_AJQaisar.pdf'>Horseshoeing in Mughal India </a></td>
<td> A Jan Qaisar</td>
<td>220</td>
</tr>
<tr>
<td>540</td>
<td>IJHS-27-1992-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_2_3_MMehta.pdf'>Science versus Technology: The Early Years of Kala Bhawan, Baroda 1890–1896 </a></td>
<td> Makrand Mehta</td>
<td>351</td>
</tr>
<tr>
<td>541</td>
<td>IJHS-27-1992-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_2_4_JNSinha.pdf'>Origin of India's National Science Policy: M L Sircar to M K Gandhi, 1875–1935 </a></td>
<td> Jagdish N Sinha</td>
<td>201</td>
</tr>
<tr>
<td>542</td>
<td>IJHS-27-1992-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_2_5_BookReviews.pdf'>Book Review </a></td>
<td> Deepak Kumar</td>
<td>40</td>
</tr>
<tr>
<td>543</td>
<td>IJHS-27-1992-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_2_6_NewPublications.pdf'>New Publications </a></td>
<td> </td>
<td>21</td>
</tr>
<tr>
<td>544</td>
<td>IJHS-27-1992-Issue-3</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_3_1_JCSikdar.pdf'>Fabric of Life: Paryapati Pranapana in Jaina Agama </a></td>
<td> J C Sikdar</td>
<td>107</td>
</tr>
<tr>
<td>545</td>
<td>IJHS-27-1992-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_3_2_BDatta.pdf'>Use of Permutations and Combinations in India </a></td>
<td> Bibhutibhusan Datta and Awadhesh Narayan Singh</td>
<td>217</td>
</tr>
<tr>
<td>546</td>
<td>IJHS-27-1992-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_3_3_RKrishnamurthy.pdf'>Gemmology in Ancient India </a></td>
<td> Radha Krishnamurthy</td>
<td>134</td>
</tr>
<tr>
<td>547</td>
<td>IJHS-27-1992-Issue-3</td>
<td>Metallurgy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_3_4_ASaeed.pdf'>Study of Muslim Alchemy in the Medieval Ages & some Valuable Chemicals Transmitted to Modern Chemistry </a></td>
<td> Aftab Saeed</td>
<td>233</td>
</tr>
<tr>
<td>548</td>
<td>IJHS-27-1992-Issue-3</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_3_5_DKMittra.pdf'>Role of Ram Bramha Sanyal in Initiating Zoological Researches on the Animals in Captivity </a></td>
<td> D K Mittra</td>
<td>170</td>
</tr>
<tr>
<td>549</td>
<td>IJHS-27-1992-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_3_6_AGhosh.pdf'>The First Indian Aeronaut </a></td>
<td> Amitabha Ghosh</td>
<td>319</td>
</tr>
<tr>
<td>550</td>
<td>IJHS-27-1992-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_3_7_News.pdf'>News </a></td>
<td> </td>
<td>32</td>
</tr>
<tr>
<td>551</td>
<td>IJHS-27-1992-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_3_8_Supplement_RasaRatnaSamuccaya.pdf'>Supplement: Rasa Ratna Samuccaya </a></td>
<td> D Joshi</td>
<td>616</td>
</tr>
<tr>
<td>552</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_1_SNSen.pdf'>Factors in the Develoment of Scientific Research in India between 1906 and 1930 </a></td>
<td> S N Sen</td>
<td>144</td>
</tr>
<tr>
<td>553</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_2_JNKapur.pdf'>Development of Mathematical Sciences in India during the Twentieth Century </a></td>
<td> J N Kapur</td>
<td>265</td>
</tr>
<tr>
<td>554</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_3_HNBose.pdf'>Luminescence and Allied Phenomena </a></td>
<td> H N Bose</td>
<td>165</td>
</tr>
<tr>
<td>555</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_4_CKMajumdar.pdf'>Solid State Physics: 1900–1980 </a></td>
<td> C K Majumdar</td>
<td>241</td>
</tr>
<tr>
<td>556</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_5_AKRaychaudhuri.pdf'>Pattern of Research in India on Theoritical Astronomy and Astrophysics during period 1900–1980 </a></td>
<td> A K Raychaudhuri</td>
<td>87</td>
</tr>
<tr>
<td>557</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_6_AKSaha.pdf'>Evolution of Continental Crust of India: Growth of Knowledge. 1900–1980 — A Review </a></td>
<td> A K Saha</td>
<td>48</td>
</tr>
<tr>
<td>558</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_7_SKMukherjee.pdf'>Progress in Indian Agriculture: 1900–1980 </a></td>
<td> S K Mukherjee</td>
<td>131</td>
</tr>
<tr>
<td>559</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_8_RCMehrotra.pdf'>Development of Inorganic Chemistry in India during 1900–1980 </a></td>
<td> R C Mehrotra</td>
<td>115</td>
</tr>
<tr>
<td>560</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_9_SKMukerjee.pdf'>Mineral Exploration in the Twentieth Century </a></td>
<td> S K Mukerjee</td>
<td>274</td>
</tr>
<tr>
<td>561</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_10_JDas.pdf'>Progress in Telecommunications and R & D during Post–war Years (1945–84) — A Review </a></td>
<td> J Das</td>
<td>122</td>
</tr>
<tr>
<td>562</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_11_RRDaniel.pdf'>Space Science in India </a></td>
<td> R R Daniel</td>
<td>222</td>
</tr>
<tr>
<td>563</td>
<td>IJHS-27-1992-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_12_BookReviews.pdf'>Book Review </a></td>
<td> </td>
<td>68</td>
</tr>
<tr>
<td>564</td>
<td>IJHS-27-1992-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_13_Obituary_SNSen.pdf'>Orbituary: S N Sen </a></td>
<td> </td>
<td>56</td>
</tr>
<tr>
<td>565</td>
<td>IJHS-27-1992-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_16_Erratum.pdf'>Erratum </a></td>
<td> </td>
<td>45</td>
</tr>
<tr>
<td>566</td>
<td>IJHS-27-1992-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol27_4_17_SupplementBibliographyofPhysics.pdf'>Supplement: Bibliography of Physics, Astronomy, Astrophysics and Geophysics in India </a></td>
<td> </td>
<td>521</td>
</tr>
<tr>
<td>567</td>
<td>IJHS-28-1993-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_1_1_KDAbhyankar.pdf'>A Search for the Earliest Vedic Calender </a></td>
<td> K D Abhyankar</td>
<td>209</td>
</tr>
<tr>
<td>568</td>
<td>IJHS-28-1993-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_1_2_SCKak.pdf'>Astronomy of the Satapatha Brahmana </a></td>
<td> Subhash C Kak</td>
<td>297</td>
</tr>
<tr>
<td>569</td>
<td>IJHS-28-1993-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_1_3_PVSharma.pdf'>A Fragment of the Lauhasastra of Nagarjuna </a></td>
<td> P V Sharma</td>
<td>253</td>
</tr>
<tr>
<td>570</td>
<td>IJHS-28-1993-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_1_4_VNSharma.pdf'>Pratibimba Siddhanta of Jai Singh’s Library </a></td>
<td> V N Sharma</td>
<td>82</td>
</tr>
<tr>
<td>571</td>
<td>IJHS-28-1993-Issue-1</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_1_5_SRSarma.pdf'>Two Mughal Celestial Globes </a></td>
<td> S R Sarma‚ S M R Ansari and A G Kulkarni</td>
<td>350</td>
</tr>
<tr>
<td>572</td>
<td>IJHS-28-1993-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_1_6_SChandra.pdf'>Birbal Sahni and India– Madagascar Fit </a></td>
<td> Sanjay Chandra</td>
<td>54</td>
</tr>
<tr>
<td>573</td>
<td>IJHS-28-1993-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_1_7_SupplementBibliographyofPhysics.pdf'>Supplement </a></td>
<td> </td>
<td>1873</td>
</tr>
<tr>
<td>574</td>
<td>IJHS-28-1993-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_2_1_SCKak.pdf'>The Structure of the Rgveda </a></td>
<td> Subhash C Kak</td>
<td>141</td>
</tr>
<tr>
<td>575</td>
<td>IJHS-28-1993-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_2_2_RCGupta.pdf'>Sundararaja’s Improvements of Vedic Circle–Square Conversions </a></td>
<td> R C Gupta</td>
<td>276</td>
</tr>
<tr>
<td>576</td>
<td>IJHS-28-1993-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_2_3_BDatta.pdf'>Use of Series in India </a></td>
<td> B Datta and A N Singh</td>
<td>317</td>
</tr>
<tr>
<td>577</td>
<td>IJHS-28-1993-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_2_4_VNSharma.pdf'>Sawai Jai Singh’s Hindu Astronomers </a></td>
<td> V N Sharma</td>
<td>456</td>
</tr>
<tr>
<td>578</td>
<td>IJHS-28-1993-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_2_5_RMercier.pdf'>Account by Joseph Dubois of Astronomical Work under Jai Singh Sawai </a></td>
<td> Raymond Mercier</td>
<td>169</td>
</tr>
<tr>
<td>579</td>
<td>IJHS-28-1993-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_2_6_AGhosh.pdf'>Golak Chandra: India’s Pioneer Innovator Technician </a></td>
<td> Amitabha Ghosh</td>
<td>405</td>
</tr>
<tr>
<td>580</td>
<td>IJHS-28-1993-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_2_7_BookReview.pdf'>Book Review: Glimpses of India’s Statistical Heritage by J K Ghosh‚ S K Mitra and K R Parthasarthy </a></td>
<td> J N Kapur</td>
<td>70</td>
</tr>
<tr>
<td>581</td>
<td>IJHS-28-1993-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_2_8_SupplementBiblographyofPhysics.pdf'>Supplement </a></td>
<td> </td>
<td>2214</td>
</tr>
<tr>
<td>582</td>
<td>IJHS-28-1993-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_3_1_YOhashi.pdf'>Development of Astronomical Observation in Vedic and Post–Vedic India </a></td>
<td> Yukio Ohashi</td>
<td>1027</td>
</tr>
<tr>
<td>583</td>
<td>IJHS-28-1993-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_3_2_BDatta.pdf'>Surds in Hindu Mathematics </a></td>
<td> B Datta and A N Singh</td>
<td>166</td>
</tr>
<tr>
<td>584</td>
<td>IJHS-28-1993-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_3_3_BDatta.pdf'>Approximate Values of Surds in Hindu Mathematics </a></td>
<td> B Datta and A N Singh</td>
<td>111</td>
</tr>
<tr>
<td>585</td>
<td>IJHS-28-1993-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_3_4_HSVirk.pdf'>Life and Works of Puran Singh </a></td>
<td> H S Virk</td>
<td>168</td>
</tr>
<tr>
<td>586</td>
<td>IJHS-28-1993-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol28_3_5_News.pdf'>News </a></td>
<td> </td>
<td>42</td>
</tr>
<tr>
<td>587</td>
<td>IJHS-28-1993-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_4_1_PSFilliozat.pdf'>Formalisation and Orality in Panini’s Astadhyayi </a></td>
<td> P S Filliozat</td>
<td>172</td>
</tr>
<tr>
<td>588</td>
<td>IJHS-28-1993-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_4_2_LCJain.pdf'>Constant–Set (Dhruva–Rasi) Technique in Jaina School of Astronomy </a></td>
<td> L C Jain and K P Jain</td>
<td>103</td>
</tr>
<tr>
<td>589</td>
<td>IJHS-28-1993-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_4_3_AKBiswas.pdf'>The Primacy of India in Ancient Brass and Zinc Metallurgy </a></td>
<td> A K Biwas</td>
<td>398</td>
</tr>
<tr>
<td>590</td>
<td>IJHS-28-1993-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_4_4_BookReviewsAKBiswasAndARahman.pdf'>Book Reviews </a></td>
<td> </td>
<td>72</td>
</tr>
<tr>
<td>591</td>
<td>IJHS-28-1993-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol28_4_5_SupplementBibliographyofPhysics.pdf'>Supplement </a></td>
<td> </td>
<td>2284</td>
</tr>
<tr>
<td>592</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_1_DKumar.pdf'>Calcutta: The Emergence of a Science City (1784–1856) </a></td>
<td> Deepak Kumar</td>
<td>127</td>
</tr>
<tr>
<td>593</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_2_SGhose.pdf'>William O’Shaughnessy – An Innovator and Entrepreneur </a></td>
<td> Saroj Ghose</td>
<td>226</td>
</tr>
<tr>
<td>594</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_3_MKahali.pdf'>John Henry Pratt‚ Archdeacon of Calcutta and His Theory of Isostatic Compensation </a></td>
<td> Manidipa Kahali</td>
<td>123</td>
</tr>
<tr>
<td>595</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_4_DBose.pdf'>Madhusudan Gupta </a></td>
<td> Debasis Bose</td>
<td>162</td>
</tr>
<tr>
<td>596</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_5_SNSen.pdf'>The Pioneering Role of Calcutta in Scientific and Technical Education in India </a></td>
<td> S N Sen</td>
<td>117</td>
</tr>
<tr>
<td>597</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_6_SCGhosh.pdf'>Calcutta University and Science </a></td>
<td> S C Ghosh</td>
<td>193</td>
</tr>
<tr>
<td>598</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_7_AGhosh.pdf'>Some Eminent Indian Pioneers in the Field of Technology </a></td>
<td> Amitabha Ghosh</td>
<td>243</td>
</tr>
<tr>
<td>599</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_8_AKBiswas.pdf'>Reverend Father Eugene Lafont and the Scientific Activity of St Xaviers College </a></td>
<td> Arun Kumar Biswas</td>
<td>204</td>
</tr>
<tr>
<td>600</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_9_JKGhosh.pdf'>Mahalanobis and the Art and Science of Statistics: The Early Days </a></td>
<td> J K Ghosh</td>
<td>159</td>
</tr>
<tr>
<td>601</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_10_SChatterjee.pdf'>Meghnad Saha – The Scientist and the Institution Builder </a></td>
<td> Santimay Chatterjee</td>
<td>180</td>
</tr>
<tr>
<td>602</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_11_DChattopadhyaya.pdf'>Four Calcuttans in Defence of Scientific Temper </a></td>
<td> Debiprasad Chattopadhyay</td>
<td>128</td>
</tr>
<tr>
<td>603</td>
<td>IJHS-29-1994-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_12_News.pdf'>News </a></td>
<td> </td>
<td>66</td>
</tr>
<tr>
<td>604</td>
<td>IJHS-29-1994-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_1_13_Supplement.pdf'>Supplement: On the Desirability of a National Institution for the Cultivation of the Sciences by the Natives of India (1872–1876) </a></td>
<td> Mahendralal Sircar</td>
<td>633</td>
</tr>
<tr>
<td>605</td>
<td>IJHS-29-1994-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_2_2_AKBiswas.pdf'>Vaidurya‚ Marakata and Other Beryl Family Gem Minerals: Etymology and Traditions in Ancient India </a></td>
<td> Arun Kumar Biswas</td>
<td>700</td>
</tr>
<tr>
<td>606</td>
<td>IJHS-29-1994-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_2_3_YOhashi.pdf'>Astronomical Instruments in Classical Siddhantas </a></td>
<td> Yukio Ohashi</td>
<td>2055</td>
</tr>
<tr>
<td>607</td>
<td>IJHS-29-1994-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_2_4_VDeshpande.pdf'>Sulbarakalikacchedah: Medieval Methods for Cleansing Metal Surfaces and Removing Tarnishes </a></td>
<td> Vijaya Deshpande</td>
<td>180</td>
</tr>
<tr>
<td>608</td>
<td>IJHS-29-1994-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_2_5_MFilliozat.pdf'>D’Apres De Mannevillette Captain and Hydrographer to the French East India Company (1707–1780) </a></td>
<td> Manonmani Filliozat</td>
<td>218</td>
</tr>
<tr>
<td>609</td>
<td>IJHS-29-1994-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_2_6_News.pdf'>News </a></td>
<td> </td>
<td>118</td>
</tr>
<tr>
<td>610</td>
<td>IJHS-29-1994-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_3_1_SKBhatia.pdf'>Carburisation of Iron in Ancient India </a></td>
<td> S K Bhatia</td>
<td>135</td>
</tr>
<tr>
<td>611</td>
<td>IJHS-29-1994-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_3_2_NGDongre.pdf'>Metrology and Coinage in Ancient India and Contemporary World </a></td>
<td> N G Dongre</td>
<td>161</td>
</tr>
<tr>
<td>612</td>
<td>IJHS-29-1994-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_3_3_SCKak.pdf'>Evolution of Early Writing in India </a></td>
<td> Subhash C Kak</td>
<td>219</td>
</tr>
<tr>
<td>613</td>
<td>IJHS-29-1994-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_3_4_AKBiswas.pdf'>Gem—Minerals in Pre–Modern India </a></td>
<td> Arun Kumar Biswas</td>
<td>498</td>
</tr>
<tr>
<td>614</td>
<td>IJHS-29-1994-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_3_5_VRamaswamy.pdf'>Metallurgy and Traditional Metal Crafts in Tamil Nadu </a></td>
<td> Vijaya Ramaswamy</td>
<td>193</td>
</tr>
<tr>
<td>615</td>
<td>IJHS-29-1994-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_3_6_VNSharma.pdf'>Misra Yantra of the Delhi Observatory </a></td>
<td> Virendra Nath Sharma</td>
<td>207</td>
</tr>
<tr>
<td>616</td>
<td>IJHS-29-1994-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_3_7_Obituary.pdf'>Obituary: Debiprasad Chattopadhaya </a></td>
<td> A K Chakravarty</td>
<td>56</td>
</tr>
<tr>
<td>617</td>
<td>IJHS-29-1994-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_3_8_News.pdf'>News </a></td>
<td> </td>
<td>65</td>
</tr>
<tr>
<td>618</td>
<td>IJHS-29-1994-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_4_1_DFrawley.pdf'>Planets in the Vedic Literature </a></td>
<td> Davis Frawley</td>
<td>147</td>
</tr>
<tr>
<td>619</td>
<td>IJHS-29-1994-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_4_2_SRSarma.pdf'>Indian Astronomical and Time–Measuring Instruments: A Catalogue in Preparation </a></td>
<td> Sreeramula Rajeswara Sarma</td>
<td>465</td>
</tr>
<tr>
<td>620</td>
<td>IJHS-29-1994-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_4_3_SDas.pdf'>Solutions of Linear Algebraic Equations and Sums of Fraction–Additions Using Sutra Method </a></td>
<td> S Das</td>
<td>333</td>
</tr>
<tr>
<td>621</td>
<td>IJHS-29-1994-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_4_4_VNJha.pdf'>Indeterminate Analysis in the Context of the Mahasiddhanta of Aryabhata II </a></td>
<td> V N Jha</td>
<td>152</td>
</tr>
<tr>
<td>622</td>
<td>IJHS-29-1994-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_4_5_AKBiswas.pdf'>Iron and Steel in Pre–Modern India—A Critical Review </a></td>
<td> Arun Kumar Biswas</td>
<td>423</td>
</tr>
<tr>
<td>623</td>
<td>IJHS-29-1994-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_4_6_NGDongre.pdf'>Dhvantapramapaka Yantra of Maharsi Bharadvaja </a></td>
<td> N G Dongre</td>
<td>329</td>
</tr>
<tr>
<td>624</td>
<td>IJHS-29-1994-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol29_4_9_News.pdf'>News </a></td>
<td> </td>
<td>70</td>
</tr>
<tr>
<td>625</td>
<td>IJHS-30-1995-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_1_1_JDHughes.pdf'>The Effect of Knowledge of Indian Biota on Ecological Thought </a></td>
<td> J Donald Hughes</td>
<td>163</td>
</tr>
<tr>
<td>626</td>
<td>IJHS-30-1995-Issue-1</td>
<td>Math</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_1_2_PManansala.pdf'>Sungka Mathematics ofg the Philippines </a></td>
<td> Paul Manansala</td>
<td>237</td>
</tr>
<tr>
<td>627</td>
<td>IJHS-30-1995-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_1_3_NCRana.pdf'>On The Meaning of the Mula Naksatra </a></td>
<td> N C Rana and R K Kochhar</td>
<td>65</td>
</tr>
<tr>
<td>628</td>
<td>IJHS-30-1995-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_1_4_AMukhopadhyay.pdf'>Polygonal Approximation to Circle and Madhavacarya </a></td>
<td> A Mukhopadhyay and M R Adhikari</td>
<td>170</td>
</tr>
<tr>
<td>629</td>
<td>IJHS-30-1995-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_1_5_JInsley.pdf'>Making Mountains out of Molehills? George Everest and Henry Barrow, 1830-39 </a></td>
<td> Jane Insley</td>
<td>147</td>
</tr>
<tr>
<td>630</td>
<td>IJHS-30-1995-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_1_6_LCJain.pdf'>The Method for Finding out the Number of Moons and their Families in the Tiloyapannatti </a></td>
<td> L C Jain and Kumari Prabha Jain</td>
<td>192</td>
</tr>
<tr>
<td>631</td>
<td>IJHS-30-1995-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_1_7_BookReview.pdf'>Book Review </a></td>
<td> </td>
<td>51</td>
</tr>
<tr>
<td>632</td>
<td>IJHS-30-1995-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_1_8_ReviewReport.pdf'>A National Report on Studies in HOS in India (1990-93) </a></td>
<td> </td>
<td>208</td>
</tr>
<tr>
<td>633</td>
<td>IJHS-30-1995-Issue-2to4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_2and3and4_1_APGreeshmalatha.pdf'>Kattamaran in South Kerala— A Study of Constructional Techniques </a></td>
<td> A P Greeshmalatha and G V Rajamanickam</td>
<td>562</td>
</tr>
<tr>
<td>634</td>
<td>IJHS-30-1995-Issue-2to4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_2and3and4_2_LCJain.pdf'>Certain Special Features of the Ancient Jaina Calender </a></td>
<td> L C Jain and Kumari Prabha Jain</td>
<td>459</td>
</tr>
<tr>
<td>635</td>
<td>IJHS-30-1995-Issue-2to4</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_2and3and4_3_MSKhan.pdf'>Tabaqat Al–Umam of Qadi Sai–id Al–Andalusi (1029-1070) </a></td>
<td> M S Khan</td>
<td>349</td>
</tr>
<tr>
<td>636</td>
<td>IJHS-30-1995-Issue-2to4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_2and3and4_4_AKChakravarty.pdf'>Three 19th Century Calcutta Astronomers </a></td>
<td> A K Chakravarty</td>
<td>137</td>
</tr>
<tr>
<td>637</td>
<td>IJHS-30-1995-Issue-2to4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_2and3and4_5_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>51</td>
</tr>
<tr>
<td>638</td>
<td>IJHS-30-1995-Issue-2to4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_2and3and4_6_News.pdf'>News </a></td>
<td> </td>
<td>47</td>
</tr>
<tr>
<td>639</td>
<td>IJHS-30-1995-Issue-2to4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol30_2and3and4_7_Supplementary_HistoryofMagneticStudiesinIndia.pdf'>SupplementHistory of Magnetic Studies in India 1850to1980-— A Bibliography </a></td>
<td> Jayanta Sthanapati and S N Sen</td>
<td>3495</td>
</tr>
<tr>
<td>640</td>
<td>IJHS-31-1996-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_1_1_AKChakravarty.pdf'>Evolution of Dating System </a></td>
<td> A K Charavarty</td>
<td>211</td>
</tr>
<tr>
<td>641</td>
<td>IJHS-31-1996-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_1_2_KDAbhyankar.pdf'>Kalyuga‚ Saptarsi‚ Yudhisthra and Laukika Eras </a></td>
<td> K D Abhyankar and G M Ballabh</td>
<td>262</td>
</tr>
<tr>
<td>642</td>
<td>IJHS-31-1996-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_1_3_AMShastri_vikrama.pdf'>Vikrama Era </a></td>
<td> Ajay Mitra Shastri</td>
<td>589</td>
</tr>
<tr>
<td>643</td>
<td>IJHS-31-1996-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_1_4_AMShastri_Saka.pdf'>Saka Era </a></td>
<td> Ajay Mitra Shastri</td>
<td>445</td>
</tr>
<tr>
<td>644</td>
<td>IJHS-31-1996-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_1_5_ABhattacharyya.pdf'>Bengali San </a></td>
<td> Amitabha Bhattacharyya</td>
<td>63</td>
</tr>
<tr>
<td>645</td>
<td>IJHS-31-1996-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_1_6_KVSarma.pdf'>Kollam Era </a></td>
<td> K V Sarma</td>
<td>94</td>
</tr>
<tr>
<td>646</td>
<td>IJHS-31-1996-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_1_7_NewsSeminarPublications.pdf'>News and Seminar Publications </a></td>
<td> </td>
<td>94</td>
</tr>
<tr>
<td>647</td>
<td>IJHS-31-1996-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_1_8_SupplementBibliographyon MagneticStudies.pdf'>Supplement: History of Magnetic Studies in India 1850–1980 </a></td>
<td> Jayanta Sthanapati</td>
<td>2752</td>
</tr>
<tr>
<td>648</td>
<td>IJHS-31-1996-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_2_1_PVSharma.pdf'>Original Concept of Soma </a></td>
<td> P V Sharma</td>
<td>323</td>
</tr>
<tr>
<td>649</td>
<td>IJHS-31-1996-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_2_2_KHKrishnamurthy.pdf'>A Botanical Account of Valmiki’s Pancavati </a></td>
<td> K H Krishnamurthy</td>
<td>388</td>
</tr>
<tr>
<td>650</td>
<td>IJHS-31-1996-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_2_3_VMishra.pdf'>Theorem of Square on the Diagonal in Vedic Geometry and its Application </a></td>
<td> V Mishra and S L Singh</td>
<td>104</td>
</tr>
<tr>
<td>651</td>
<td>IJHS-31-1996-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_2_4_LGopal.pdf'>Emergence of Vrksayurveda </a></td>
<td> Lallanji Gopal</td>
<td>83</td>
</tr>
<tr>
<td>652</td>
<td>IJHS-31-1996-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_2_5_DPingree.pdf'>Sanskrit Geographical Tables </a></td>
<td> David Pingree</td>
<td>460</td>
</tr>
<tr>
<td>653</td>
<td>IJHS-31-1996-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_2_6_NewsMonographPublications.pdf'>News </a></td>
<td> </td>
<td>136</td>
</tr>
<tr>
<td>654</td>
<td>IJHS-31-1996-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_3_1_HWLaale.pdf'>Embyology and Abortion in Indian Antiquity: A Brief Survey </a></td>
<td> H Willer Laale</td>
<td>477</td>
</tr>
<tr>
<td>655</td>
<td>IJHS-31-1996-Issue-3</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_3_2_MBanerjee.pdf'>Sanskrit Vastu–Works on Soil–Testing </a></td>
<td> Manabendu Banerjee</td>
<td>156</td>
</tr>
<tr>
<td>656</td>
<td>IJHS-31-1996-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_3_3_SDSharma.pdf'>Conjunction of Jupiter with δ Cancri </a></td>
<td> S D Sharma</td>
<td>70</td>
</tr>
<tr>
<td>657</td>
<td>IJHS-31-1996-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_3_4_VDeshpande.pdf'>A Note on Ancient Zinc Smelting in India and China </a></td>
<td> Vijaya Deshpande</td>
<td>76</td>
</tr>
<tr>
<td>658</td>
<td>IJHS-31-1996-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_3_5_PKMisra.pdf'>Evaluation of the Accuracy of Measurements in Indian Astronomy – I: Samanta Candrasekhara </a></td>
<td> P K Misra</td>
<td>106</td>
</tr>
<tr>
<td>659</td>
<td>IJHS-31-1996-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol31_3_6_BookReviewandNews.pdf'>Book Review and News </a></td>
<td> </td>
<td>0</td>
</tr>
<tr>
<td>660</td>
<td>IJHS-31-1996-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_4_1_MJShendge.pdf'>Beginning of Scientific Observations: Founding of Linguistic Science in India </a></td>
<td> Malati J Shendge</td>
<td>485</td>
</tr>
<tr>
<td>661</td>
<td>IJHS-31-1996-Issue-4</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_4_2_RKrishnamurthy.pdf'>Water in Ancient India </a></td>
<td> Radha Krishnamurthy</td>
<td>183</td>
</tr>
<tr>
<td>662</td>
<td>IJHS-31-1996-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_4_3_SDas.pdf'>Multiplication and Divisibility of Numbers – The Sutra Way </a></td>
<td> S Das</td>
<td>335</td>
</tr>
<tr>
<td>663</td>
<td>IJHS-31-1996-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_4_4_VJDeshpande.pdf'>Musavijnana or the Ancient Science of Crucibles </a></td>
<td> Vijaya Jayant Deshpande</td>
<td>278</td>
</tr>
<tr>
<td>664</td>
<td>IJHS-31-1996-Issue-4</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_4_5_MKChandrashekaran.pdf'>JC Bose’s Views on Biological Rhythms </a></td>
<td> M K Chandrashekaran and R Subbaraj</td>
<td>150</td>
</tr>
<tr>
<td>665</td>
<td>IJHS-31-1996-Issue-4</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol31_4_6_NCShah.pdf'>Norman Gill: The Pioneer Horticulturist of the Hills of Uttar Pradesh – A Tribute </a></td>
<td> N C Shah</td>
<td>155</td>
</tr>
<tr>
<td>666</td>
<td>IJHS-32-1997-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_1_1_BPrakash.pdf'>Use of Metals in Ayuevedic Medicine </a></td>
<td> Bhanu Prakash</td>
<td>600</td>
</tr>
<tr>
<td>667</td>
<td>IJHS-32-1997-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_1_2_GVRajamanickam.pdf'>Traditional Sea Knowledge Prevailing among Tribes of Andaman and Nicobar Islands </a></td>
<td> G V Rajamanickam</td>
<td>461</td>
</tr>
<tr>
<td>668</td>
<td>IJHS-32-1997-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_1_3_GAbraham.pdf'>Ancient and Medieval Star Catalogues </a></td>
<td> George Abraham</td>
<td>59</td>
</tr>
<tr>
<td>669</td>
<td>IJHS-32-1997-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_1_4_AMukhopadhyay.pdf'>The Concept of Cyclic Quadilaterals: Its Origin and Development in India (From the Age of Sulba Sutras to Bhaskara I) </a></td>
<td> A Mukhopadhyay and MR Adhikari</td>
<td>247</td>
</tr>
<tr>
<td>670</td>
<td>IJHS-32-1997-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_1_5_SKChatterjee.pdf'>A Note on Kali Era </a></td>
<td> S K Chatterjee</td>
<td>216</td>
</tr>
<tr>
<td>671</td>
<td>IJHS-32-1997-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_1_6_BNMukherjee.pdf'>A Note on the Vikrama and Saka Eras </a></td>
<td> B N Mukherjee</td>
<td>102</td>
</tr>
<tr>
<td>672</td>
<td>IJHS-32-1997-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_1_7_BookReview.pdf'>Book Review: Kasyapa–Samhita </a></td>
<td> S C Sankhyadhar</td>
<td>51</td>
</tr>
<tr>
<td>673</td>
<td>IJHS-32-1997-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol32_1_9_NewsandAcademyPublicationsonHOS.pdf'>News </a></td>
<td> </td>
<td>130</td>
</tr>
<tr>
<td>674</td>
<td>IJHS-32-1997-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol32_1_10_SupplementRasahrdayatantramCh1to10.pdf'>Supplement: Rasahrdayatantram </a></td>
<td> </td>
<td>2446</td>
</tr>
<tr>
<td>675</td>
<td>IJHS-32-1997-Issue-2</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_2_1_SCKak.pdf'>On th Science of Consciousness in Ancient India </a></td>
<td> Subhash C Kak</td>
<td>216</td>
</tr>
<tr>
<td>676</td>
<td>IJHS-32-1997-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_2_2_HFrost.pdf'>Stone Anchors: The Need for Methodical Recording </a></td>
<td> Honor Frost</td>
<td>102</td>
</tr>
<tr>
<td>677</td>
<td>IJHS-32-1997-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_2_3_VMishra.pdf'>First Degree Indeterminate Analysis in Ancient India and its Application by Virasena </a></td>
<td> V Mishra and S L Singh</td>
<td>80</td>
</tr>
<tr>
<td>678</td>
<td>IJHS-32-1997-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_2_4_GAbraham.pdf'>Variable Radius Epicycle Model </a></td>
<td> George Abraham</td>
<td>50</td>
</tr>
<tr>
<td>679</td>
<td>IJHS-32-1997-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_2_5_AGhosh.pdf'>Guru Jones—A Private Engineer in the Colonial Trap </a></td>
<td> Amitabha Ghosh</td>
<td>313</td>
</tr>
<tr>
<td>680</td>
<td>IJHS-32-1997-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_2_6_KVSarma.pdf'>In Quests of Early Manuscripts/ Collections Dealing with Science and Technology in India </a></td>
<td> K V Sarma</td>
<td>187</td>
</tr>
<tr>
<td>681</td>
<td>IJHS-32-1997-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_2_7_BookReview.pdf'>Book Review: Technology and the Raj by Roy McLeod and Deepak Kumar </a></td>
<td> Chittabrata Palit</td>
<td>58</td>
</tr>
<tr>
<td>682</td>
<td>IJHS-32-1997-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_2_8_NewsIndoPortuguesePublicationsonHOS.pdf'>News </a></td>
<td> </td>
<td>77</td>
</tr>
<tr>
<td>683</td>
<td>IJHS-32-1997-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_3_1_KCHari.pdf'>True Rationale of Surya Siddhanta </a></td>
<td> K Chandra Hari</td>
<td>145</td>
</tr>
<tr>
<td>684</td>
<td>IJHS-32-1997-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_3_2_SRSarma.pdf'>Some Medieval Arithmetical Tables </a></td>
<td> S R Sarma</td>
<td>125</td>
</tr>
<tr>
<td>685</td>
<td>IJHS-32-1997-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_3_3_YOhashi.pdf'>Early History of the Astrolabe in India </a></td>
<td> Yukio Ohashi</td>
<td>1491</td>
</tr>
<tr>
<td>686</td>
<td>IJHS-32-1997-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_3_4_BookReview.pdf'>Book Review: Minerals and Metals in Ancient India by A K Biswas </a></td>
<td> A M Shastri</td>
<td>89</td>
</tr>
<tr>
<td>687</td>
<td>IJHS-32-1997-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_4_1_SCKak.pdf'>Three old Indian Values of Π </a></td>
<td> Subhash C Kak</td>
<td>124</td>
</tr>
<tr>
<td>688</td>
<td>IJHS-32-1997-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_4_2_VMMallayya.pdf'>Arithmetic Operation of Division with Special Reference to Bhaskara II’s Lilavati and its Commentaries </a></td>
<td> V M Mallayya</td>
<td>182</td>
</tr>
<tr>
<td>689</td>
<td>IJHS-32-1997-Issue-4</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_4_3_SKChatterjee.pdf'>Balinese Traditional Calendar </a></td>
<td> SK Chatterjee</td>
<td>300</td>
</tr>
<tr>
<td>690</td>
<td>IJHS-32-1997-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_4_4_BRRao.pdf'>Guttur – An Iron Age Industrial Centre in Dharmapuri District </a></td>
<td> B Raghunatha Rao and B Sasisekaran</td>
<td>526</td>
</tr>
<tr>
<td>691</td>
<td>IJHS-32-1997-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_4_5_NSaxena.pdf'>Lolimbaraja and his Contribution to Medicine </a></td>
<td> Nirmal Saxena</td>
<td>181</td>
</tr>
<tr>
<td>692</td>
<td>IJHS-32-1997-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_4_6_KSMathew.pdf'>The Portugese and the Study of Medicinal Plants in India in the Sixteenth Century </a></td>
<td> K S Matthew</td>
<td>156</td>
</tr>
<tr>
<td>693</td>
<td>IJHS-32-1997-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_4_7_BookReviewaAndSRSarma.pdf'>Book Reviews </a></td>
<td> </td>
<td>61</td>
</tr>
<tr>
<td>694</td>
<td>IJHS-32-1997-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol32_4_8_NewsMagicSquare.pdf'>News </a></td>
<td> </td>
<td>36</td>
</tr>
<tr>
<td>695</td>
<td>IJHS-33-1998-Issue-1</td>
<td>Math</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_1_1_SKAdhikari.pdf'>Babylonian Mathematics </a></td>
<td> Swapan Kumar Adhikari</td>
<td>249</td>
</tr>
<tr>
<td>696</td>
<td>IJHS-33-1998-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_1_2_SCKak.pdf'>Vena‚ Veda‚ Venus </a></td>
<td> Subhash C Kak</td>
<td>85</td>
</tr>
<tr>
<td>697</td>
<td>IJHS-33-1998-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_1_3_SCKak.pdf'>Sayana’s Astronomy </a></td>
<td> Subhash C Kak</td>
<td>78</td>
</tr>
<tr>
<td>698</td>
<td>IJHS-33-1998-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_1_4_SSSarma.pdf'>Contemporaneity of the Perception on Environment in Kautilya’s Arthasastra </a></td>
<td> Sunil Sen Sarma</td>
<td>185</td>
</tr>
<tr>
<td>699</td>
<td>IJHS-33-1998-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_1_5_SKJain.pdf'>Some Aspects of Biodiversity and Indian Traditions </a></td>
<td> S K Jain</td>
<td>198</td>
</tr>
<tr>
<td>700</td>
<td>IJHS-33-1998-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_1_6_SJJKozhamthadam.pdf'>Kepler and the Origin of Modern Science </a></td>
<td> SJ Job Kozhamthadam</td>
<td>329</td>
</tr>
<tr>
<td>701</td>
<td>IJHS-33-1998-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_1_7_PublicationonHOS.pdf'>Publication on History of Science </a></td>
<td> </td>
<td>84</td>
</tr>
<tr>
<td>702</td>
<td>IJHS-33-1998-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_1_8_Supplement.pdf'>Supplement: Tantrasamgraha of Nilakantha Somayaji </a></td>
<td> K V Sarma and V S Narasimhan</td>
<td>594</td>
</tr>
<tr>
<td>703</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_1_SCKak.pdf'>Early Theories on the Distance to the Sun </a></td>
<td> Subhash C Kak</td>
<td>115</td>
</tr>
<tr>
<td>704</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_2_BNNAchar.pdf'>Enigma of the Five–Year Yuga of Vedanga Jyotisa </a></td>
<td> B N Narahari Achar</td>
<td>157</td>
</tr>
<tr>
<td>705</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_3_SMadabhushi.pdf'>Seismological Zones of Varahamihira </a></td>
<td> Srinivas Madabhushi and P Srirama Murty</td>
<td>132</td>
</tr>
<tr>
<td>706</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_4_AMukhopadhyay.pdf'>A Step Towards Incommensurability of Π and Bhaskara (I): An Episode of the Sixth Century AD </a></td>
<td> A Mukhopadhyay and M R Adhikari</td>
<td>191</td>
</tr>
<tr>
<td>707</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_5_SSarkar.pdf'>Indian Craft Technology: Static or Changing – A Case Study of the Kansari’s Craft in Bengal‚ 16th to 18th Centuries </a></td>
<td> Smritikumar Sarkar</td>
<td>255</td>
</tr>
<tr>
<td>708</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_6_SKChatterjee.pdf'>Traditional Calender of Myanmar (Burma) </a></td>
<td> S K Chatterjee</td>
<td>263</td>
</tr>
<tr>
<td>709</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_7_News.pdf'>News: A Non–Conventional Formula to Calculate the Area of Circle </a></td>
<td> R S J Reddy</td>
<td>36</td>
</tr>
<tr>
<td>710</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_8_ProjectsApproved.pdf'>Projects Approved and Renewed by the Indian National Commission for History of Science </a></td>
<td> </td>
<td>45</td>
</tr>
<tr>
<td>711</td>
<td>IJHS-33-1998-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_9_AcademyPublicationsofHOS.pdf'>Academy Publications on History of Science </a></td>
<td> </td>
<td>79</td>
</tr>
<tr>
<td>712</td>
<td>IJHS-33-1998-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_2_10_Supplement.pdf'>Supplement: Tantrasamgraha of Nilakantha Somayaji </a></td>
<td> K V Sarma and V S Narasimhan</td>
<td>611</td>
</tr>
<tr>
<td>713</td>
<td>IJHS-33-1998-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_3_1_SCKak.pdf'>The SunU+2019 ’s Orbit in the Brahmanas </a></td>
<td> Subhash C Kak</td>
<td>213</td>
</tr>
<tr>
<td>714</td>
<td>IJHS-33-1998-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_3_2_KCHari.pdf'>On the Origin of KaliyugadiU+2019 ’ Synodic Super-Conjunction </a></td>
<td> K Chandra Hari</td>
<td>114</td>
</tr>
<tr>
<td>715</td>
<td>IJHS-33-1998-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_3_3_CSRao.pdf'>Sriyantra – A Study of Spherical and Plane Forms </a></td>
<td> C S Rao</td>
<td>325</td>
</tr>
<tr>
<td>716</td>
<td>IJHS-33-1998-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_3_4_NGDongre.pdf'>Spectroscopy in Ancient India: An Application of Spectroscopy to Astrophysics </a></td>
<td> N G Dongre</td>
<td>161</td>
</tr>
<tr>
<td>717</td>
<td>IJHS-33-1998-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_3_5_ADas.pdf'>History of Science and Technology in India– Quicksands of Paradigm </a></td>
<td> Anirban Das</td>
<td>152</td>
</tr>
<tr>
<td>718</td>
<td>IJHS-33-1998-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_3_6_AcademyPublicationsofHOS.pdf'>Academy Publications on History of Science and Announcement </a></td>
<td> </td>
<td>88</td>
</tr>
<tr>
<td>719</td>
<td>IJHS-33-1998-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_3_7_Supplement.pdf'>Supplement: Tantrasamgraha of Nilakantha Somayaji </a></td>
<td> K V Sarma and V S Narasimhan</td>
<td>789</td>
</tr>
<tr>
<td>720</td>
<td>IJHS-33-1998-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_4_1_KCHari.pdf'>On the Origin of Sidereal Zodiac and Astronomy </a></td>
<td> K Chandra Hari</td>
<td>171</td>
</tr>
<tr>
<td>721</td>
<td>IJHS-33-1998-Issue-4</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_4_2_PSensarma.pdf'>Conservation of Biodiversity in Manu–Samhita </a></td>
<td> Priyadarsan Sensarma</td>
<td>120</td>
</tr>
<tr>
<td>722</td>
<td>IJHS-33-1998-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_4_3_NGDongre.pdf'>Prakasa Stambhanabhida Lauha of Maharsi Bharadvaja </a></td>
<td> N G Dongre, S K Malavia and P ramachandra Rao</td>
<td>177</td>
</tr>
<tr>
<td>723</td>
<td>IJHS-33-1998-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_4_4_CPalit.pdf'>Dr Mahendralal Sircar and Homeopathy </a></td>
<td> Chittabrata Palit</td>
<td>213</td>
</tr>
<tr>
<td>724</td>
<td>IJHS-33-1998-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_4_5_AcademysPublicationsonHOS.pdf'>Academy Publications on History of Science </a></td>
<td> </td>
<td>84</td>
</tr>
<tr>
<td>725</td>
<td>IJHS-33-1998-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_4_6_News.pdf'>News </a></td>
<td> </td>
<td>114</td>
</tr>
<tr>
<td>726</td>
<td>IJHS-33-1998-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol33_4_7_Supplement.pdf'>Supplement: The Cylindrical Sundial in India </a></td>
<td> Yukio Ohashi</td>
<td>1024</td>
</tr>
<tr>
<td>727</td>
<td>IJHS-34-1999-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_1_1_KCHari.pdf'>A Critical Study of Vedic Mathematics of Sankaracarya SriBharatiKrsna Tirthaji Maharaj </a></td>
<td> K Chandra Hari</td>
<td>288</td>
</tr>
<tr>
<td>728</td>
<td>IJHS-34-1999-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_1_2_NKumar.pdf'>Betel Vine (Piper Betle L.) Cultivation_A Unique Case of Plant Establishment under Anthropogenically Regulated Microclimatic Conditions </a></td>
<td> Nikhil Kumar</td>
<td>1167</td>
</tr>
<tr>
<td>729</td>
<td>IJHS-34-1999-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_1_3_RShrivastva.pdf'>Smelting Furnaces in Ancient India </a></td>
<td> Rina Shrivastava</td>
<td>721</td>
</tr>
<tr>
<td>730</td>
<td>IJHS-34-1999-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_1_4_AGhosh.pdf'>PreCommercial Era of Sound Recording in India </a></td>
<td> Amitabha Ghosh</td>
<td>223</td>
</tr>
<tr>
<td>731</td>
<td>IJHS-34-1999-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_1_5_RSingh.pdf'>C V Raman‚ M N Saha and The Nobel Prize for the Year 1930 </a></td>
<td> Rajinder Singh and Falk Riess</td>
<td>240</td>
</tr>
<tr>
<td>732</td>
<td>IJHS-34-1999-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_1_6_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>71</td>
</tr>
<tr>
<td>733</td>
<td>IJHS-34-1999-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_1_7_News.pdf'>News </a></td>
<td> </td>
<td>85</td>
</tr>
<tr>
<td>734</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_1_JSPettersson.pdf'>Indus Numerals on Metal Tools </a></td>
<td> J S Pettersson</td>
<td>317</td>
</tr>
<tr>
<td>735</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_2_BNNAchar.pdf'>On An Astronomical Concept in Visnupurana </a></td>
<td> B N Narahari Achar</td>
<td>104</td>
</tr>
<tr>
<td>736</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Astronomy</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_3_Skak.pdf'>The Solar Numbers in Angkor Wat </a></td>
<td> Subhash Kak</td>
<td>203</td>
</tr>
<tr>
<td>737</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_4_DKKanjilal.pdf'>A Note On The Vrksayurveda of Parasara </a></td>
<td> Dileep Kumar Kanjilal</td>
<td>101</td>
</tr>
<tr>
<td>738</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_5_KCHari.pdf'>Intricacy of The Siddhantic Solar Year </a></td>
<td> K Chandra Hari</td>
<td>193</td>
</tr>
<tr>
<td>739</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_6_SRSarma.pdf'>Yantraraja: The Astrolabe in Sanskrit </a></td>
<td> Sreeramula Rajeswara Sarma</td>
<td>368</td>
</tr>
<tr>
<td>740</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_7_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>119</td>
</tr>
<tr>
<td>741</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_8_News.pdf'>News </a></td>
<td> </td>
<td>40</td>
</tr>
<tr>
<td>742</td>
<td>IJHS-34-1999-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_2_9_AcademyPublicationsonHOS.pdf'>Academy Publications on HOS </a></td>
<td> </td>
<td>93</td>
</tr>
<tr>
<td>743</td>
<td>IJHS-34-1999-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_3_1_RShrivastva.pdf'>Mining of Copper in Ancient India </a></td>
<td> Rina Shrivastava</td>
<td>121</td>
</tr>
<tr>
<td>744</td>
<td>IJHS-34-1999-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_3_2_RNIyengar.pdf'>Earthquake History of India in Medieval Times </a></td>
<td> R N Iyengar et al.</td>
<td>909</td>
</tr>
<tr>
<td>745</td>
<td>IJHS-34-1999-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_3_3_NKMaitra.pdf'>Michael Faraday Vis–A–Vis Chandrasekhar </a></td>
<td> N K Maitra</td>
<td>72</td>
</tr>
<tr>
<td>746</td>
<td>IJHS-34-1999-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_3_4_BookReviews.pdf'>Book Review </a></td>
<td> </td>
<td>70</td>
</tr>
<tr>
<td>747</td>
<td>IJHS-34-1999-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_3_5_News.pdf'>News— Academy Publications on HOS </a></td>
<td> </td>
<td>93</td>
</tr>
<tr>
<td>748</td>
<td>IJHS-34-1999-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_4_1_BSasisekaran.pdf'>Technology of Iron and Steel in Kodumal— An Ancient Industrial Centre in Tamil Nadu </a></td>
<td> B Sasisekaran and B Raghunatha Rao</td>
<td>774</td>
</tr>
<tr>
<td>749</td>
<td>IJHS-34-1999-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_4_2_SRSarma.pdf'>Katapayadi Notation on a Sanskrit Astrolabe </a></td>
<td> Sreeramula Rajeswara Sarma</td>
<td>366</td>
</tr>
<tr>
<td>750</td>
<td>IJHS-34-1999-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_4_3_SGarg.pdf'>Dams— Engineering Analysisof Alternatives </a></td>
<td> Sandeep Garg et al.</td>
<td>388</td>
</tr>
<tr>
<td>751</td>
<td>IJHS-34-1999-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_4_4_RKKochhar.pdf'>Science in British India </a></td>
<td> R K Kochhar</td>
<td>481</td>
</tr>
<tr>
<td>752</td>
<td>IJHS-34-1999-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_4_5_BookReview.pdf'>Book Review </a></td>
<td> </td>
<td>44</td>
</tr>
<tr>
<td>753</td>
<td>IJHS-34-1999-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_4_6_News.pdf'>News </a></td>
<td> </td>
<td>109</td>
</tr>
<tr>
<td>754</td>
<td>IJHS-34-1999-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol34_4_7_Supplement_Rasendramangalam.pdf'>Supplement— Rasendramangalam of Nagarjuna </a></td>
<td> H S Sharma</td>
<td>649</td>
</tr>
<tr>
<td>755</td>
<td>IJHS-35-2000-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_1_1_BNNAchar.pdf'>On The Astronomical Basis of the Date of Satapatha Brahmana: A Re–Examination of Dikshit's Theory </a></td>
<td> B N N Achar</td>
<td>343</td>
</tr>
<tr>
<td>756</td>
<td>IJHS-35-2000-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_1_2_KCHari.pdf'>Date of the Solar Orbit of Satapatha Brahmana </a></td>
<td> K Chandra Hari</td>
<td>64</td>
</tr>
<tr>
<td>757</td>
<td>IJHS-35-2000-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_1_3_PSensarma.pdf'>Dietary Diversity in Manu–Samhita </a></td>
<td> P Sensarma</td>
<td>183</td>
</tr>
<tr>
<td>758</td>
<td>IJHS-35-2000-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_1_4_BvDalen.pdf'>Origin of the Mean Motion Tables of Jai Singh </a></td>
<td> B V Dalen</td>
<td>363</td>
</tr>
<tr>
<td>759</td>
<td>IJHS-35-2000-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_1_5_HSingh.pdf'>Pharmaceutical Society of India: The oldest Indian Pharmaceutical Organisation </a></td>
<td> H Singh</td>
<td>139</td>
</tr>
<tr>
<td>760</td>
<td>IJHS-35-2000-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_1_6_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>136</td>
</tr>
<tr>
<td>761</td>
<td>IJHS-35-2000-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_1_7_Notices.pdf'>Notices </a></td>
<td> </td>
<td>39</td>
</tr>
<tr>
<td>762</td>
<td>IJHS-35-2000-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_3_1_BNNAchar.pdf'>A Case for Revising the Date of Vedanga Jyotisa </a></td>
<td> B N N Achar</td>
<td>149</td>
</tr>
<tr>
<td>763</td>
<td>IJHS-35-2000-Issue-3</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_3_2_KDAbhyankar.pdf'>Babylonian Source of Aryabhata’s Planetary Constants </a></td>
<td> K D Abhyankar</td>
<td>62</td>
</tr>
<tr>
<td>764</td>
<td>IJHS-35-2000-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_3_3_THayashi.pdf'>Govindaswamin’s Arithmetic Rules Cited in the Kriyakramakari of Sankara and Narayana </a></td>
<td> T Hayashi</td>
<td>666</td>
</tr>
<tr>
<td>765</td>
<td>IJHS-35-2000-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_3_4_VNSharma.pdf'>Astronomical Instruments at Kota </a></td>
<td> V N Sharma</td>
<td>427</td>
</tr>
<tr>
<td>766</td>
<td>IJHS-35-2000-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_3_5_IHabib.pdf'>Joseph Needham and the History of Indian Technology </a></td>
<td> Irfan Habib</td>
<td>615</td>
</tr>
<tr>
<td>767</td>
<td>IJHS-35-2000-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_3_6_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>131</td>
</tr>
<tr>
<td>768</td>
<td>IJHS-35-2000-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_3_7_Notices.pdf'>Notices </a></td>
<td> </td>
<td>33</td>
</tr>
<tr>
<td>769</td>
<td>IJHS-35-2000-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_3_8_Conferences.pdf'>Conferences: NISTADS INSA Workshop on History of Science in India </a></td>
<td> A N Thakur</td>
<td>108</td>
</tr>
<tr>
<td>770</td>
<td>IJHS-35-2000-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_4_1_BNNAchar.pdf'>On the Caitradi Scheme </a></td>
<td> B N N Achar</td>
<td>280</td>
</tr>
<tr>
<td>771</td>
<td>IJHS-35-2000-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_4_2_HThurston.pdf'>Planetary Revolutions in Indian Astronomy </a></td>
<td> Hugh Thurston</td>
<td>121</td>
</tr>
<tr>
<td>772</td>
<td>IJHS-35-2000-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_4_3_DRaina.pdf'>Jean–Baptiste Biot on the History of Indian Astronomy (1830–1860): The Nation in the Post–Enlightenment Historiography of Science </a></td>
<td> Dhruv Raina</td>
<td>509</td>
</tr>
<tr>
<td>773</td>
<td>IJHS-35-2000-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_4_4_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>108</td>
</tr>
<tr>
<td>774</td>
<td>IJHS-35-2000-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol35_4_5_SupplementsHOSResearchProjects.pdf'>Supplements </a></td>
<td> </td>
<td>1524</td>
</tr>
<tr>
<td>775</td>
<td>IJHS-36-2001-Issue-1&2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_1and2_1_RBalasubramanian.pdf'>New Insights on the 1600 Year Old Corrosion Resistant Delhi Iron Pillar </a></td>
<td> R Balasubramaniam</td>
<td>1182</td>
</tr>
<tr>
<td>776</td>
<td>IJHS-36-2001-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_1and2_2_SRSarma.pdf'>Measuring Time With Long Syllables </a></td>
<td> S R Sarma</td>
<td>82</td>
</tr>
<tr>
<td>777</td>
<td>IJHS-36-2001-Issue-1&2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_1and2_3_AKBag.pdf'>Ahargana and Weekdays As Per Modern Suryasiddhanta </a></td>
<td> A K Bag</td>
<td>163</td>
</tr>
<tr>
<td>778</td>
<td>IJHS-36-2001-Issue-1&2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_1and2_4_BookReview.pdf'>Book Reviews </a></td>
<td> </td>
<td>152</td>
</tr>
<tr>
<td>779</td>
<td>IJHS-36-2001-Issue-1&2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_1and2_5_Notices.pdf'>Notices of Journals </a></td>
<td> </td>
<td>72</td>
</tr>
<tr>
<td>780</td>
<td>IJHS-36-2001-Issue-1&2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_1and2_6_Conferences.pdf'>Conferences </a></td>
<td> A K Bag</td>
<td>119</td>
</tr>
<tr>
<td>781</td>
<td>IJHS-36-2001-Issue-1&2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_1and2_7_Projects.pdf'>Projects Approved and Renewed by the Indian National Commission for History of Science </a></td>
<td> </td>
<td>75</td>
</tr>
<tr>
<td>782</td>
<td>IJHS-36-2001-Issue-3&4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_3and4_1_BSasisekaran.pdf'>Technology of Forge Welding Adopted at Mallappadi – An Iron Age Site in Tamil Nadu </a></td>
<td> B Sasisekaran and B raghunatha Rao</td>
<td>375</td>
</tr>
<tr>
<td>783</td>
<td>IJHS-36-2001-Issue-3&4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_3and4_2_KVSarma.pdf'>Aryabhata: His name‚ Time and Provenance </a></td>
<td> K V Sarma</td>
<td>161</td>
</tr>
<tr>
<td>784</td>
<td>IJHS-36-2001-Issue-3&4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_3and4_3_YVJeppu.pdf'>Aryabhata’s Kaliyuga Revisited: An Optimization Problem </a></td>
<td> Y V Jeppu</td>
<td>125</td>
</tr>
<tr>
<td>785</td>
<td>IJHS-36-2001-Issue-3&4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_3and4_4_KCHari.pdf'>Vakyakarana–A Study </a></td>
<td> K Chandra Hari</td>
<td>333</td>
</tr>
<tr>
<td>786</td>
<td>IJHS-36-2001-Issue-3&4</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_3and4_5_GSSodhi.pdf'>A Tale of Two Fingerprint Experts </a></td>
<td> G S Sodhi and Jasjeet Kaur</td>
<td>112</td>
</tr>
<tr>
<td>787</td>
<td>IJHS-36-2001-Issue-3&4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_3and4_6_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>138</td>
</tr>
<tr>
<td>788</td>
<td>IJHS-36-2001-Issue-3&4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_3and4_7_ProjectReport.pdf'>Project Report: Search for Ancient Indian Records of the Sighting of Supernovae </a></td>
<td> Jayant V Narlikar and Saroja Bhate</td>
<td>2133</td>
</tr>
<tr>
<td>789</td>
<td>IJHS-36-2001-Issue-3&4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol36_3and4_8_Conferences.pdf'>Conferences </a></td>
<td> S M R Ansari</td>
<td>126</td>
</tr>
<tr>
<td>790</td>
<td>IJHS-37-2002-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_1_1_RBalasubramaniam.pdf'>Studies of Ancient Indian OCP Period Copper </a></td>
<td> RBalasubramaniam‚ M N Mungole et. al</td>
<td>350</td>
</tr>
<tr>
<td>791</td>
<td>IJHS-37-2002-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_1_2_BSasisekaran.pdf'>Metallurgy and Metal Industry in Ancient Tamil Nadu— An Archaeological Study </a></td>
<td> B Sasisekaran</td>
<td>180</td>
</tr>
<tr>
<td>792</td>
<td>IJHS-37-2002-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_1_3_KDAbhyankar.pdf'>Probable Rationale for Unequal Naksatra Divisions in Jain Astronomy </a></td>
<td> K D Abhyankar</td>
<td>89</td>
</tr>
<tr>
<td>793</td>
<td>IJHS-37-2002-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_1_4_VJha.pdf'>Indigenous Colours in Mithila(North Bihar)– A Historical Perspective </a></td>
<td> Vidyanath Jha</td>
<td>288</td>
</tr>
<tr>
<td>794</td>
<td>IJHS-37-2002-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_1_5_TVVenkateswaran.pdf'>The Topography of a Changing World </a></td>
<td> T N Venkateswaran</td>
<td>370</td>
</tr>
<tr>
<td>795</td>
<td>IJHS-37-2002-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_1_6_BookReview.pdf'>Book Review </a></td>
<td> A N Thakur</td>
<td>27</td>
</tr>
<tr>
<td>796</td>
<td>IJHS-37-2002-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_1_7_Conference.pdf'>Conferences </a></td>
<td> </td>
<td>92</td>
</tr>
<tr>
<td>797</td>
<td>IJHS-37-2002-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_1_9_Supplement ScientificPeriodicals.pdf'>Supplement: Growth of Scientific Periodicals in India (1788– 1900) </a></td>
<td> B K Sen</td>
<td>629</td>
</tr>
<tr>
<td>798</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_1_BNNAchar.pdf'>Aryabhata and the table of Rsines </a></td>
<td> B N Narahari Achar</td>
<td>70</td>
</tr>
<tr>
<td>799</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_2_KCHari.pdf'>Genesis and Antecedents of Aryabhatiya </a></td>
<td> K Chandra Hari</td>
<td>218</td>
</tr>
<tr>
<td>800</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_3_RBalasubramaniam.pdf'>A New Study of Dhar Iron Pillar </a></td>
<td> R Balasubramaniam</td>
<td>1321</td>
</tr>
<tr>
<td>801</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_4_JWisniak.pdf'>Fritz Haber— A Conflicting Chemist </a></td>
<td> Jaime Wisniak</td>
<td>344</td>
</tr>
<tr>
<td>802</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_5_RSingh.pdf'>Sir C V Raman and his contacts with Hungarian Scientists </a></td>
<td> Rajinder Singh</td>
<td>388</td>
</tr>
<tr>
<td>803</td>
<td>IJHS-37-2002-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_6_BookReview.pdf'>Book Review </a></td>
<td> Kiran Arora</td>
<td>41</td>
</tr>
<tr>
<td>804</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_7_ProjectReport.pdf'>Projects Report: Minerals and Metals in Ancient India </a></td>
<td> Shabnam Shukla</td>
<td>45</td>
</tr>
<tr>
<td>805</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_8_Conferences.pdf'>Conferences: Indian History Congress </a></td>
<td> Shabnam Shukla</td>
<td>70</td>
</tr>
<tr>
<td>806</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_9_BChaki.pdf'>Conferences: National Seminar </a></td>
<td> Balai Chaki</td>
<td>50</td>
</tr>
<tr>
<td>807</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_10_INCforHOS.pdf'>Indian National Commission for History of Science: Projects Renewed and Approved </a></td>
<td> </td>
<td>44</td>
</tr>
<tr>
<td>808</td>
<td>IJHS-37-2002-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_2_11_SupplementScientificPeriodicals.pdf'>Supplement: Growth of Scientific Periodicals in India (1788– 1900) </a></td>
<td> B K Sen</td>
<td>995</td>
</tr>
<tr>
<td>809</td>
<td>IJHS-37-2002-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_1_KDAbhyankar.pdf'>On Two Important Provisions in Vedanga&ndash Jyotisa </a></td>
<td> K D Abhyankar</td>
<td>129</td>
</tr>
<tr>
<td>810</td>
<td>IJHS-37-2002-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_2_KCHari.pdf'>Date of Haridatta‚ Promulgator of the Prahita System of Astronomy in Kerala </a></td>
<td> K Chandra Hari</td>
<td>213</td>
</tr>
<tr>
<td>811</td>
<td>IJHS-37-2002-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_3_DJadhav.pdf'>Nemicandra’s Rule for the Volume of a Sphere </a></td>
<td> Dipak Jadhav</td>
<td>207</td>
</tr>
<tr>
<td>812</td>
<td>IJHS-37-2002-Issue-3</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_4_SMRAnsari.pdf'>Practical Astronomy in Indo–Persian Sources </a></td>
<td> S M R Ansari</td>
<td>156</td>
</tr>
<tr>
<td>813</td>
<td>IJHS-37-2002-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_5_RSingh.pdf'>Sir CV Raman‚ Dame Kathleen Lonsdale and their Scientific Controversy due to the Diffuse Spots in X–ray Photographs </a></td>
<td> Ravinder Singh</td>
<td>342</td>
</tr>
<tr>
<td>814</td>
<td>IJHS-37-2002-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_6_BookReview.pdf'>Book Review: Ayurvedic remedies for the whole family </a></td>
<td> N Kumar</td>
<td>185</td>
</tr>
<tr>
<td>815</td>
<td>IJHS-37-2002-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_7_ProjectReport.pdf'>Project Report: Shipping and ship building in India– Medieval Period </a></td>
<td> Shabnam Shukla</td>
<td>24</td>
</tr>
<tr>
<td>816</td>
<td>IJHS-37-2002-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_8_Obituary.pdf'>Orbituary: Apurba Kumar Chakravarty </a></td>
<td> Shabnam Shukla‚ S K Chatterjee</td>
<td>307</td>
</tr>
<tr>
<td>817</td>
<td>IJHS-37-2002-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_9_NoticeofJournals.pdf'>Notice of Journals </a></td>
<td> </td>
<td>23</td>
</tr>
<tr>
<td>818</td>
<td>IJHS-37-2002-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_3_10_SupplementScientificPeriodicalsBKSen.pdf'>Supplement: Growth of Scientific Periodicals in India (1788– 1900) </a></td>
<td> B K Sen</td>
<td>1250</td>
</tr>
<tr>
<td>819</td>
<td>IJHS-37-2002-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_1_MMishra.pdf'>The Objective Criteria in Deciphering the Indus Script </a></td>
<td> Madhusudan Mishra</td>
<td>127</td>
</tr>
<tr>
<td>820</td>
<td>IJHS-37-2002-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_2_TLaha.pdf'>Material and Electrochemical Characterization of Ancient Indian OCP Period Copper </a></td>
<td> T Laha et. al.</td>
<td>188</td>
</tr>
<tr>
<td>821</td>
<td>IJHS-37-2002-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_3_KCHari.pdf'>An Early Eclipse Record of Indian Astronomy </a></td>
<td> K Chandra Hari</td>
<td>95</td>
</tr>
<tr>
<td>822</td>
<td>IJHS-37-2002-Issue-4</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_4_NCShah.pdf'>Hugh Martin Leake: A Historical Memoir </a></td>
<td> N C Shah</td>
<td>169</td>
</tr>
<tr>
<td>823</td>
<td>IJHS-37-2002-Issue-4</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_5_SSen.pdf'>The beginning of Biochemical Researches in India— An Historical Perspective </a></td>
<td> Srabani sen</td>
<td>287</td>
</tr>
<tr>
<td>824</td>
<td>IJHS-37-2002-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_6_BookReview.pdf'>Book Review : Kautilya’s Arthasastra in the light of modern science and technology </a></td>
<td> Arun Kumar Biswas</td>
<td>115</td>
</tr>
<tr>
<td>825</td>
<td>IJHS-37-2002-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_8_ProjectReport.pdf'>Project Report: Raj Nighantu of Narhari Pandit </a></td>
<td> Shabnam Shukla</td>
<td>67</td>
</tr>
<tr>
<td>826</td>
<td>IJHS-37-2002-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_9_Obituary.pdf'>Orbituary: Shabbir Ahmad Khan Ghori </a></td>
<td> S M R Ansari</td>
<td>55</td>
</tr>
<tr>
<td>827</td>
<td>IJHS-37-2002-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol37_4_10_NoticeofJournals.pdf'>Notice of Journals </a></td>
<td> </td>
<td>45</td>
</tr>
<tr>
<td>828</td>
<td>IJHS-38-2003-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_1_1_RCGupta.pdf'>Agni–Kunda—A Negelected Area of Study in the History of Ancient Mathematics </a></td>
<td> R C Gupta</td>
<td>606</td>
</tr>
<tr>
<td>829</td>
<td>IJHS-38-2003-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_1_2_AKBag.pdf'>Luni–Solar Calender‚ Kali Ahargana and Julian Days </a></td>
<td> A K Bag</td>
<td>721</td>
</tr>
<tr>
<td>830</td>
<td>IJHS-38-2003-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_1_3_AKBag.pdf'>A Note on the Ahargana and the Weekdays as per Modern Suryasiddhanta </a></td>
<td> A K Bag</td>
<td>183</td>
</tr>
<tr>
<td>831</td>
<td>IJHS-38-2003-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_1_4_KCHari.pdf'>Eclipse Observations of Paramesvara‚ the 14–15th century Astronomer of Kerala </a></td>
<td> K Chandra Hari</td>
<td>666</td>
</tr>
<tr>
<td>832</td>
<td>IJHS-38-2003-Issue-1</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_1_5_SFTuan.pdf'>Dirac and Heisenberg in Hawaii </a></td>
<td> S F Tuan</td>
<td>373</td>
</tr>
<tr>
<td>833</td>
<td>IJHS-38-2003-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_1_6_BookReview.pdf'>Book Review: Metallurgy in Indian Archaeology </a></td>
<td> R K Dube</td>
<td>282</td>
</tr>
<tr>
<td>834</td>
<td>IJHS-38-2003-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_1_7_Obituary.pdf'>Obituary: Jagat Narain Kapur </a></td>
<td> A K Bag</td>
<td>218</td>
</tr>
<tr>
<td>835</td>
<td>IJHS-38-2003-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_1_RNIyengar.pdf'>Internal Consistency of Eclipses and Planetary Positions in Mahabharata </a></td>
<td> R N Iyengar</td>
<td>2037</td>
</tr>
<tr>
<td>836</td>
<td>IJHS-38-2003-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_2_JLCoze.pdf'>About the Signification of Wootz and Other Names Given to Steel </a></td>
<td> J Le Coze</td>
<td>458</td>
</tr>
<tr>
<td>837</td>
<td>IJHS-38-2003-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_3_KRamasubramanian.pdf'>Corrections to the Terrestrial Latitude in Tantrasangraha </a></td>
<td> K Ramasubramanian and M S Sriram</td>
<td>532</td>
</tr>
<tr>
<td>838</td>
<td>IJHS-38-2003-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_4_BRRao.pdf'>Cudamaninighantu — An Unpublished Work on Dravyaguna by Suraya </a></td>
<td> B Rama Rao</td>
<td>253</td>
</tr>
<tr>
<td>839</td>
<td>IJHS-38-2003-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_5_RSingh.pdf'>C V Raman and the American Scientists </a></td>
<td> Rajinder Singh</td>
<td>1003</td>
</tr>
<tr>
<td>840</td>
<td>IJHS-38-2003-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_6_BookReview.pdf'>Book Review: The Ganitasarasangraha of Sri Mahaviracarya </a></td>
<td> S R Sarma</td>
<td>226</td>
</tr>
<tr>
<td>841</td>
<td>IJHS-38-2003-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_7_ProjectReport.pdf'>Project Report: Botanist Jaikrishnabhai – Life and Contributions by JJ Shah </a></td>
<td> Shabnam Shukla</td>
<td>128</td>
</tr>
<tr>
<td>842</td>
<td>IJHS-38-2003-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_8_IndianNationalCommissionforHOS.pdf'>Indian National Commission for History of Science: Projects Renewed and Approved </a></td>
<td> </td>
<td>83</td>
</tr>
<tr>
<td>843</td>
<td>IJHS-38-2003-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_2_9_Conferences.pdf'>Conferences </a></td>
<td> </td>
<td>127</td>
</tr>
<tr>
<td>844</td>
<td>IJHS-38-2003-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_1_RBalasubramaniam.pdf'>Influence of Manufacturing Methodology on the Corrosion Resistance of the Delhi Iron Pillar </a></td>
<td> R Balasubramaniam</td>
<td>1411</td>
</tr>
<tr>
<td>845</td>
<td>IJHS-38-2003-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_2_BSasisekaran.pdf'>Archaeo Metallurgical Study on Select Pallava Coins </a></td>
<td> B Sasisekaran and B Raghunatha Rao</td>
<td>1104</td>
</tr>
<tr>
<td>846</td>
<td>IJHS-38-2003-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_3_KCHari.pdf'>Computation of the True Moon by Madhava of Sangama–Grama </a></td>
<td> K Chandra Hari</td>
<td>1150</td>
</tr>
<tr>
<td>847</td>
<td>IJHS-38-2003-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_4_SBRao.pdf'>Lunar Eclipse Computation in Indian Astronomy with Special Reference to Grahalaghavam </a></td>
<td> S abalachandra Rao‚ S K Uma and Padmaja Venugopal</td>
<td>747</td>
</tr>
<tr>
<td>848</td>
<td>IJHS-38-2003-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_5_IGKhan.pdf'>The Awadh Scientific Renaissance and the Role of the French: C 1750–1820 </a></td>
<td> Iqbal Ghani Khan</td>
<td>2160</td>
</tr>
<tr>
<td>849</td>
<td>IJHS-38-2003-Issue-3</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_6_BookReview.pdf'>Book Review: Science and Technology in the Islamic World </a></td>
<td> A K Bag</td>
<td>417</td>
</tr>
<tr>
<td>850</td>
<td>IJHS-38-2003-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_7_ProjectReport.pdf'>Project Report </a></td>
<td> Shabnam Shukla</td>
<td>229</td>
</tr>
<tr>
<td>851</td>
<td>IJHS-38-2003-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_8_Obituary.pdf'>Obituary: T A Sarasvati Amma </a></td>
<td> R C Gupta</td>
<td>253</td>
</tr>
<tr>
<td>852</td>
<td>IJHS-38-2003-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_3_9_Supplement.pdf'>Supplement: Brahmasphutasiddhanta </a></td>
<td> Setsuro Ikeyama</td>
<td>3824</td>
</tr>
<tr>
<td>853</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_1_PSensarma.pdf'>Dietary Biodiversity in Yajnavalkya–Samhita </a></td>
<td> Priyadarsan Sensarma</td>
<td>504</td>
</tr>
<tr>
<td>854</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_2_RBalasubramaniam.pdf'>Some Metallurgical Aspects of Gupta Period Gold Coin Manufacturing Technology </a></td>
<td> R Balasubramaniam and N Mahajan</td>
<td>1630</td>
</tr>
<tr>
<td>855</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_3_ACMandal.pdf'>Numismatic Study of Malhar Coins by the Energy Dispersive X–Ray Fluorescence (EDXRF) Technique </a></td>
<td> Atis Chandra Mandal‚ Sumita Santra‚ Debasis Mitra‚ Manoranjan Sarkar‚ Dipan </td>
<td>946</td>
</tr>
<tr>
<td>856</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_4_GAbraham.pdf'>Observational Astronomy </a></td>
<td> George Abraham and J Samuel Cornelius</td>
<td>383</td>
</tr>
<tr>
<td>857</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_5_RSingh.pdf'>Richard Bar and his contacts with the Indian Nobel Laureate Sir CV Raman </a></td>
<td> Rajinder Singh</td>
<td>678</td>
</tr>
<tr>
<td>858</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_6_BookReview.pdf'>Book Review: Ancient Indian Astronomy – Planetary Positions and Eclipses </a></td>
<td> A K Bag</td>
<td>429</td>
</tr>
<tr>
<td>859</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Culture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_7_Conference.pdf'>Conference: 12th World Sanskrit Conference – A Report </a></td>
<td> A K Bag</td>
<td>266</td>
</tr>
<tr>
<td>860</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_8_News.pdf'>News: Books Received for Review (2003) </a></td>
<td> </td>
<td>104</td>
</tr>
<tr>
<td>861</td>
<td>IJHS-38-2003-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol38_4_9_CHAMANewsletter.pdf'>Chama Newsletter </a></td>
<td> </td>
<td>138</td>
</tr>
<tr>
<td>862</td>
<td>IJHS-39-2004-Issue-1</td>
<td>Culture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_1_1_RSatyanarayana.pdf'>Vina Keyboards – Origin </a></td>
<td> R Satyanarayana</td>
<td>180</td>
</tr>
<tr>
<td>863</td>
<td>IJHS-39-2004-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_1_2_RNIyengar.pdf'>Profile of A Natural Disaster in Ancient Sanskrit Literature </a></td>
<td> R N Iyengar</td>
<td>621</td>
</tr>
<tr>
<td>864</td>
<td>IJHS-39-2004-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_1_3_MIDass.pdf'>Estimation of the Original Erection Site of the Delhi Iron Pillar at Udayagiri </a></td>
<td> Meera I Dass and R Balasubramaniam</td>
<td>632</td>
</tr>
<tr>
<td>865</td>
<td>IJHS-39-2004-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_1_4_JWisniak.pdf'>Dyes from Antiquity to Synthesis </a></td>
<td> Jaime Wisniak</td>
<td>460</td>
</tr>
<tr>
<td>866</td>
<td>IJHS-39-2004-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_1_5_JNSinha.pdf'>Science and Culture under Colonialism: India Between the World Wars </a></td>
<td> Jagdish N Sinha</td>
<td>315</td>
</tr>
<tr>
<td>867</td>
<td>IJHS-39-2004-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_1_6_BookReview.pdf'>Book Review: Astronomical Instruments in the Ramur Raza Library </a></td>
<td> S M R Ansari</td>
<td>114</td>
</tr>
<tr>
<td>868</td>
<td>IJHS-39-2004-Issue-1</td>
<td>Math</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_1_9_SRSarma.pdf'>Magic Square for 2004 </a></td>
<td> S R Sarma</td>
<td>27</td>
</tr>
<tr>
<td>869</td>
<td>IJHS-39-2004-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_1_10_News.pdf'>News: 22nd International Congress of History of Science‚ July 2005‚ Beijing </a></td>
<td> </td>
<td>21</td>
</tr>
<tr>
<td>870</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_1_SKAcharya.pdf'>Dani’s Hypothesis on the Symbol Formation in Brahmi </a></td>
<td> Subrata Kumar Acharya</td>
<td>112</td>
</tr>
<tr>
<td>871</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_2_KCHari.pdf'>PV Holay’s Interpretation of the RK-Jyotisa Verses on 19–Year Yuga </a></td>
<td> K Chandra Hari</td>
<td>223</td>
</tr>
<tr>
<td>872</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_3_RBalasubramaniam.pdf'>The Original Image Atop the Delhi Iron Pillar </a></td>
<td> R Balasubramaniam‚ Meera I Dass and Ellen M Raven</td>
<td>667</td>
</tr>
<tr>
<td>873</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_4_NAthiyaman.pdf'>Traditional Pearl and Chank Diving Technique in Gulf of Mannar: A Historical and Ethnographic Study </a></td>
<td> N Athiyaman and K Rajan</td>
<td>313</td>
</tr>
<tr>
<td>874</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_5_HistoricalNotes.pdf'>Historical Note: 5–Year Yuga in the Vedanga Jyotisa </a></td>
<td> K D Abhyankar</td>
<td>53</td>
</tr>
<tr>
<td>875</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_6_NRathnasree.pdf'>Historical Note: 1874 Transit Observations of AV Narsinga Rao at Visakhapatnam </a></td>
<td> N Rathnasree and Sanat Kumar</td>
<td>95</td>
</tr>
<tr>
<td>876</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_7_BookReviews.pdf'>Book Reviews </a></td>
<td> </td>
<td>85</td>
</tr>
<tr>
<td>877</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_8_Notices.pdf'>Notices </a></td>
<td> </td>
<td>26</td>
</tr>
<tr>
<td>878</td>
<td>IJHS-39-2004-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_2_9_Supplement.pdf'>Supplement: Siddhantakaustubha of Jagannathapandita </a></td>
<td> David Pingree</td>
<td>1117</td>
</tr>
<tr>
<td>879</td>
<td>IJHS-39-2004-Issue-3</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_3_1_ARBasu.pdf'>A New Knowledge of Madness–Nineteenth Century Asylum Psychiatry in Bengal </a></td>
<td> Amit Ranjan Basu</td>
<td>410</td>
</tr>
<tr>
<td>880</td>
<td>IJHS-39-2004-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_3_2_TVVenkateswaran.pdf'>Representation of Natural World in the Popular Science Texts during Nineteenth Century Tamil Nadu </a></td>
<td> T V Venkateswaran</td>
<td>444</td>
</tr>
<tr>
<td>881</td>
<td>IJHS-39-2004-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_3_3_ASDhumatkar.pdf'>Balaji Prabhakar Modak—A Nineteenth Century Science Propagator in Maharashtra </a></td>
<td> Abhida S Dhumatkar</td>
<td>371</td>
</tr>
<tr>
<td>882</td>
<td>IJHS-39-2004-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_3_4_ABasu.pdf'>The Conflict and Change–Over In Indian Chemistry </a></td>
<td> Aparajita Basu</td>
<td>279</td>
</tr>
<tr>
<td>883</td>
<td>IJHS-39-2004-Issue-3</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_3_5_HistoricalNotes.pdf'>Historical Notes: Julian Days in Astronomy </a></td>
<td> K Chandra Hari</td>
<td>68</td>
</tr>
<tr>
<td>884</td>
<td>IJHS-39-2004-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_3_6_SKMajumdar.pdf'>Historical Notes </a></td>
<td> Sisir K Majumdar</td>
<td>105</td>
</tr>
<tr>
<td>885</td>
<td>IJHS-39-2004-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_3_7_BookReview.pdf'>Book Reviews </a></td>
<td> Arun Kumar Biswas</td>
<td>157</td>
</tr>
<tr>
<td>886</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_1_RRajan.pdf'>Traditional Gemstone Cutting Technology of Kongu Region in Tamil Nadu </a></td>
<td> K Rajan and A Athiyaman</td>
<td>705</td>
</tr>
<tr>
<td>887</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_2_ANThakur.pdf'>Therapeutic Use of Urine in Early Indian Medicine </a></td>
<td> A N Thakur</td>
<td>159</td>
</tr>
<tr>
<td>888</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_3_KDAbhyankar.pdf'>Origin of the Moving Eccentric Circle Planetary Model in India </a></td>
<td> K D Abhyankar</td>
<td>150</td>
</tr>
<tr>
<td>889</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_4_SBRao.pdf'>Mean Planetary Positions According to Grahalaghavam </a></td>
<td> S Balachandra Rao‚ S K Uma and Padmaja Venugopal</td>
<td>414</td>
</tr>
<tr>
<td>890</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_5_GDYoung.pdf'>John Greaves’ Astronomica Quaedam: Orientalism and Ptolemaic Cosmography in Seventeenth Century England </a></td>
<td> Gregg De Young</td>
<td>509</td>
</tr>
<tr>
<td>891</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_6_HistoricalNotes.pdf'>Historical Notes </a></td>
<td> Sanjay C Patel</td>
<td>480</td>
</tr>
<tr>
<td>892</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_7_CmdSKChatterjee.pdf'>Historical Note: Uniform All India Nirayana Solar Calender </a></td>
<td> Commodore S K Chatterjee</td>
<td>237</td>
</tr>
<tr>
<td>893</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_8_JNSinha.pdf'>Book Review: Collected Works of Mahendralal Sircar‚ Eugene Lafont and the Science Movement </a></td>
<td> Jagdish N Sinha</td>
<td>61</td>
</tr>
<tr>
<td>894</td>
<td>IJHS-39-2004-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol39_4_9_News.pdf'>News </a></td>
<td> </td>
<td>41</td>
</tr>
<tr>
<td>895</td>
<td>IJHS-40-2005-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol1_2005_01.pdf'>Earliest Vedic Calendar </a></td>
<td> KD Abhyankar</td>
<td>2707</td>
</tr>
<tr>
<td>896</td>
<td>IJHS-40-2005-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol1_2005_02_ENVIRONMENT AND ECOLOGY IN THE RAMAYANA.pdf'>Environment and Ecology in the Ramayana </a></td>
<td> Mira Roy</td>
<td>6863</td>
</tr>
<tr>
<td>897</td>
<td>IJHS-40-2005-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol1_2005_03_MYSTICAL MATHEMATICS IN ANCIENT PLANETS.pdf'>Mystical Mathematics of Ancient Planets </a></td>
<td> RC Gupta</td>
<td>6720</td>
</tr>
<tr>
<td>898</td>
<td>IJHS-40-2005-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol1_2005_04_CONGRESS AND CONSERVATION.pdf'>Congress and Conservation-A Look at the NPC Reports </a></td>
<td> Jagdish N Sinha</td>
<td>9895</td>
</tr>
<tr>
<td>899</td>
<td>IJHS-40-2005-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol40_1_5_SSen.pdf'>Dawn of Nutrition Research in India&mdash; Pre&ndash;independence Era </a></td>
<td> Srabani Sen</td>
<td>337</td>
</tr>
<tr>
<td>900</td>
<td>IJHS-40-2005-Issue-1</td>
<td>nan</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol40_1_6_HistoricalNotes.pdf'>Historical Note:  Square Roots in the Sulbasutras </a></td>
<td> Toke Lindegaard Knudsen</td>
<td>57</td>
</tr>
<tr>
<td>901</td>
<td>IJHS-40-2005-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol40_1_7_KCHari.pdf'>Historical Note:  Accuracy of Lunar Eclipse Computations of the Grahalaghavam </a></td>
<td> K Chandra Hari</td>
<td>106</td>
</tr>
<tr>
<td>902</td>
<td>IJHS-40-2005-Issue-1</td>
<td>Astronomy</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol40_1_8_BookReview.pdf'>Book Review: History of Oriental Astronomy </a></td>
<td> A K Bag</td>
<td>180</td>
</tr>
<tr>
<td>903</td>
<td>IJHS-40-2005-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol1_2005_08_NEWS.pdf'>News </a></td>
<td> </td>
<td>3428</td>
</tr>
<tr>
<td>904</td>
<td>IJHS-40-2005-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol40_1_10_SupplementScientificPeriodicals.pdf'>Supplement: Growth of Scientific Periodicals in India </a></td>
<td> B K Sen</td>
<td>1024</td>
</tr>
<tr>
<td>905</td>
<td>IJHS-40-2005-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_01.pdf'>Eclipse Period Number 3339 in the Ṛgveda </a></td>
<td> RN Iyengar</td>
<td>5391</td>
</tr>
<tr>
<td>906</td>
<td>IJHS-40-2005-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_02_MANAGEMENT OF FISTULA IN ANO IN ANCIENT GREEK AND AYURVEDIC MEDICINE A HISTORICAL AN.pdf'>Management of Fistula in Ano in Ancient Greek and Ayurvedic Medicine -A Historical Analysis </a></td>
<td> P Ram Manohar et al.</td>
<td>18650</td>
</tr>
<tr>
<td>907</td>
<td>IJHS-40-2005-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_03_HIPPARCHUS'S 3600 BASED CHORD TABLE AND ITS PLACE IN THE HISTORY OF ANCIENT GREEK AN.pdf'>Hipparchus's 3600'-Based Chord Table and its Place in the History of Ancient Greek and Indian Trigon </a></td>
<td> Bo Klintberg</td>
<td>3133</td>
</tr>
<tr>
<td>908</td>
<td>IJHS-40-2005-Issue-2</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_04_HINDUS SCIENTIFIC CONTRIBUTIONS IN INDO CALENDAR.pdf'>Hindus' Scientific Contributions in Indo-Persian </a></td>
<td> SMR Ansari</td>
<td>21918</td>
</tr>
<tr>
<td>909</td>
<td>IJHS-40-2005-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_05_HISTORICAL NOTES_1.pdf'>Historical Notes: Some Comments on Kelkar Committee's Proposed All India Calendar </a></td>
<td> KD Abhyankar</td>
<td>1845</td>
</tr>
<tr>
<td>910</td>
<td>IJHS-40-2005-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_05_HISTORICAL NOTES_2.pdf'>Historical Notes: The Gifts of Physics to Modern Medicine </a></td>
<td> Sisir K Majumdar</td>
<td>9223</td>
</tr>
<tr>
<td>911</td>
<td>IJHS-40-2005-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_06_BOOK REVIEW.pdf'>Book Review: Father Engene Lafont of St. Xavier 's College, Kolkata and the Contemporary Science Mov </a></td>
<td> Deepak Kumar</td>
<td>2902</td>
</tr>
<tr>
<td>912</td>
<td>IJHS-40-2005-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_07_NEWS.pdf'>News </a></td>
<td> </td>
<td>5943</td>
</tr>
<tr>
<td>913</td>
<td>IJHS-40-2005-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol2_2005_08_SUPPLEMENT.pdf'>Supplement: Growth of Scientific Periodicals in India: (1901-1947) </a></td>
<td> BK Sen</td>
<td>9939</td>
</tr>
<tr>
<td>914</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_01_THE FIRST CATALOGUE ON FORGE WELDED IRON CANNONS BY NEOGI.pdf'>The First Catalogue of Forge-Welded Iron Cannons by Neogi </a></td>
<td> R Balasubramaniam</td>
<td>3913</td>
</tr>
<tr>
<td>915</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_02_RAJAGOPALA THE MASSIVE IRON CANNON AT THANJAVUR IN TAMIL NADU.pdf'>Rajaagopala -The Massive Iron Cannon at Thanjavur in Tamil Nadu </a></td>
<td> R Balasubramaniam, A Saxena and TR Anantharaman</td>
<td>28448</td>
</tr>
<tr>
<td>916</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_03_DAL MARDAN THE FORGE WELDED IRON CANNON AT BISHNUPUR.pdf'>Dal Mardan - The Forge-welded Iron Cannon at Bishnupur </a></td>
<td> R Balasubramaniam, K Bhattacharya and AK Nigam</td>
<td>2301</td>
</tr>
<tr>
<td>917</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_04_THE FORGE WELDED IRON CANNON AT BADA BURJ OF GOLCONDA FORT RAMPART.pdf'>The Forge -Welded Iron Cannon at Bada Burj of Golconda Fort Rampart </a></td>
<td> R Balasubramaniam, M Surender and S Sankaran</td>
<td>7456</td>
</tr>
<tr>
<td>918</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_05_THE FORGE WELDED IRON CANNON AT FATEH BURJ OF GOLCONDA FORST RAMPART.pdf'>The Forge-Welded Iron Cannon near Fateh Burj of Golconda Fort Rampart </a></td>
<td> R Balasubramaniam, S Sankaran and M Surender</td>
<td>5311</td>
</tr>
<tr>
<td>919</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_06_BHAVANI SANKAR THE FORGE WELDED IRON CANNON AT JHANSI FORT.pdf'>Bhavani Sankar - The Forge-welded Iron Cannon at Jhansi Fort </a></td>
<td> D Neff and R Balasubramaniam</td>
<td>26629</td>
</tr>
<tr>
<td>920</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_07_KADAK BIJLI THE FORGE WELDED IRON CANNON AT JHANSI FORT.pdf'>Kadak Bijli- The Forge-welded Iron Cannon at Jhansi Fort </a></td>
<td> R Balasubramaniam</td>
<td>21132</td>
</tr>
<tr>
<td>921</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_08_AZDAHA PAIKAR THE COMPOSITE IRON BROZE CANNON AT MUSA BURJ OF GOLCONDA FORT.pdf'>Azdaha Paikar- The Composite Iron-Bronze Cannon at Musa Burj of Golconda Fort </a></td>
<td> R Balasubramaniam</td>
<td>8487</td>
</tr>
<tr>
<td>922</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_09_FATH RAIHBAR THE MASSIVE BRONZE CANNON AT PETLA BURJ OF GOLCONDA FORT.pdf'>Fath Raihbar - The Massive Bronze Cannon at Petla Burj of Golconda Fort </a></td>
<td> R Balasubramaniam</td>
<td>8715</td>
</tr>
<tr>
<td>923</td>
<td>IJHS-40-2005-Issue-3</td>
<td>Metallurgy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_10_HISTORICAL NOTES.pdf'>Historical Notes: Fathullah Shirazi : Cannon, Multi- barrel Gun and Yarghu </a></td>
<td> AK Bag</td>
<td>1765</td>
</tr>
<tr>
<td>924</td>
<td>IJHS-40-2005-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol3_2005_11_SUPPELMENT.pdf'>Supplement: Growth of Scientific Periodicals in India- (1901-1947) </a></td>
<td> BK Sen</td>
<td>28728</td>
</tr>
<tr>
<td>925</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_01_IRON CANNONS OF CHINA.pdf'>Iron Cannons of China </a></td>
<td> Donald B Wagner</td>
<td>5363</td>
</tr>
<tr>
<td>926</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_02_MONSTER CANNON WROUGHT IRON BOMBARDS OF EUROPE.pdf'>Monster Cannon: Wrought Iron Bombards of Europe </a></td>
<td> Robert  Douglas Smith</td>
<td>6006</td>
</tr>
<tr>
<td>927</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_03_CANNONS OF EASTERN INDIA.pdf'>Cannons of Eastern India </a></td>
<td> Pranab Kumar Chattopadhyay</td>
<td>7624</td>
</tr>
<tr>
<td>928</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_04_FORGE WELDED CANNONS IN THE FORTS OF KARIMNAGAR DISTRICT IN THE ANDHRA PRADESH.pdf'>Forge-welded Cannons in the Forts of Karimnagar District in Andhrapradesh </a></td>
<td> S Jai Kishan</td>
<td>5678</td>
</tr>
<tr>
<td>929</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_05_DEVELOPMENT OF CANNON TECHNOLOGY IN INDIA.pdf'>Development of Cannon Technology in India </a></td>
<td> R Balasubramaniam</td>
<td>13544</td>
</tr>
<tr>
<td>930</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_06_EPIC OF SALTPETRE TO GUNPOWDER.pdf'>Epic of Saltpetre to Gunpowder </a></td>
<td> Arun Kumar Biswas</td>
<td>11534</td>
</tr>
<tr>
<td>931</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_07_GUNPOWDER ARTILLERY AND MILITARY ARCHITECTURE IN SOUTH INDIA (15-18TH CENTURY).pdf'>Gunpowder Artillery and Military Architecture in South India (15-18th Century) </a></td>
<td> Jean Deloche</td>
<td>8694</td>
</tr>
<tr>
<td>932</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_08_FIREPOWER CENTRIC WARFARE IN INDIA AND MILITARY MODERNIZATION OF THE MARATHAS 1740-1.pdf'>Firepower-centric Warfare in India and the Military Modernization of the Marathas: 1740-1 818 </a></td>
<td> Kaushik Roy</td>
<td>14140</td>
</tr>
<tr>
<td>933</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_09_ROCKETS UNDER HAIDAR ALI AND TIPU SULTAN'.pdf'>Rockets under Haidar Ali and Tipu Sultan </a></td>
<td> Kaushik Roy</td>
<td>24969</td>
</tr>
<tr>
<td>934</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Pages from Vol4_2005_10_HISTORICAL NOTES_1.pdf'>Historical Notes: Sukraniti on Guns, Cannon and Gunpowder </a></td>
<td> AK Bag</td>
<td>1806</td>
</tr>
<tr>
<td>935</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_10_HISTORICAL NOTES_2.pdf'>Historical Notes: Saltpetre Manufacture and Marketing in Medieval India </a></td>
<td> R Balasubramaniam and S Jai Kishan</td>
<td>3258</td>
</tr>
<tr>
<td>936</td>
<td>IJHS-40-2005-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_10_HISTORICAL NOTES_3.pdf'>Historical Notes: European Mercenary Artillerymen in Indian Subcontinent: 1500-1800 </a></td>
<td> R Balasubramaniam</td>
<td>1536</td>
</tr>
<tr>
<td>937</td>
<td>IJHS-40-2005-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_11_BOOK REVIEW.pdf'>Book Review: Science in Archaeology and Archaeo-Materials </a></td>
<td> DP Agrawal</td>
<td>2703</td>
</tr>
<tr>
<td>938</td>
<td>IJHS-40-2005-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_12_NEWS.pdf'>News </a></td>
<td> </td>
<td>491</td>
</tr>
<tr>
<td>939</td>
<td>IJHS-40-2005-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol4_2005_13_SUUPPLEMENT.pdf'>Supplement: Growth of Scientific Periodicals in India- (1901-1947) </a></td>
<td> BK Sen</td>
<td>19834</td>
</tr>
<tr>
<td>940</td>
<td>IJHS-41-2006-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_1_RNIyengar.pdf'>Some Celestial Observations associated with Krsna–lore </a></td>
<td> R N Iyengar</td>
<td>204</td>
</tr>
<tr>
<td>941</td>
<td>IJHS-41-2006-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_2_PSensarma.pdf'>Dietary Biodiversity in the Visnu– Samhita </a></td>
<td> Priyadarsan Sensarma</td>
<td>195</td>
</tr>
<tr>
<td>942</td>
<td>IJHS-41-2006-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_3_KCHari.pdf'>Polar Longitudes of the Suryasiddhanta and Hipparchus’ Commentary </a></td>
<td> K Chandra Hari</td>
<td>365</td>
</tr>
<tr>
<td>943</td>
<td>IJHS-41-2006-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_4_DBhattacharya.pdf'>Archaeoastronomy at Bhubaneswar: A Polygonal and Mathematical Model — Taraka </a></td>
<td> Deepak Bhattacharya and P C Naik</td>
<td>922</td>
</tr>
<tr>
<td>944</td>
<td>IJHS-41-2006-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_5_JAshraf.pdf'>Some Medieval Manuscripts on Horticulture </a></td>
<td> Jaweed Ashraf</td>
<td>252</td>
</tr>
<tr>
<td>945</td>
<td>IJHS-41-2006-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_6_HistoricalNotes.pdf'>Historical Note: Einstein and India: His Scientific, Intellectual, Social and Moral Link </a></td>
<td> Sisir K Majumdar</td>
<td>358</td>
</tr>
<tr>
<td>946</td>
<td>IJHS-41-2006-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_7_Einstien.pdf'>Historical Note: Einstein, Molecule and Medicine </a></td>
<td> Sisir K Majumdar</td>
<td>122</td>
</tr>
<tr>
<td>947</td>
<td>IJHS-41-2006-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_8_Magic Square.pdf'>Historical Note: Magic Square for 2006 </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>948</td>
<td>IJHS-41-2006-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_9_BookReview.pdf'>Book Review– Pi: A Source Book </a></td>
<td> R C Gupta</td>
<td>131</td>
</tr>
<tr>
<td>949</td>
<td>IJHS-41-2006-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_10_Notices.pdf'>Notices </a></td>
<td> </td>
<td>20</td>
</tr>
<tr>
<td>950</td>
<td>IJHS-41-2006-Issue-1</td>
<td>nan</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_1_11_Supplement_Grahalaghavam.pdf'>Supplement </a></td>
<td> </td>
<td>982</td>
</tr>
<tr>
<td>951</td>
<td>IJHS-41-2006-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_2_1_SBhujle.pdf'>Calculations of Tithis: An Extension of Surya Siddhanta Formulation </a></td>
<td> Sudha Bujhle and M N Vahia</td>
<td>274</td>
</tr>
<tr>
<td>952</td>
<td>IJHS-41-2006-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_2_2_KDAbhyankar.pdf'>Dhruvaka–Viksepa System of Astronomical Coordinates </a></td>
<td> K D Abhyankar</td>
<td>88</td>
</tr>
<tr>
<td>953</td>
<td>IJHS-41-2006-Issue-2</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_2_3_AKBiswas.pdf'>Brass and Tin Metallurgy in the Ancient & Medievel World: India’s Primacy and the Technology transfer to the West </a></td>
<td> Arun Kumar Biswas</td>
<td>201</td>
</tr>
<tr>
<td>954</td>
<td>IJHS-41-2006-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_2_4_VNSharma.pdf'>Astronomical tables of Zid–I Muhammad Shahi and their relation to Tabulae Astronomicae of De La Hire </a></td>
<td> Virendra N Sharma</td>
<td>611</td>
</tr>
<tr>
<td>955</td>
<td>IJHS-41-2006-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_2_5_HistoricalNotes.pdf'>Historical Notes: P.N Bose (1855–1934) — An Eminent Geologist </a></td>
<td> Ranatosh Chakrabarti</td>
<td>423</td>
</tr>
<tr>
<td>956</td>
<td>IJHS-41-2006-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_2_6_BookReview.pdf'>Book Review: The Role of Mathematics in Human Structure </a></td>
<td> Siddhartha Kundu</td>
<td>49</td>
</tr>
<tr>
<td>957</td>
<td>IJHS-41-2006-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_2_7_Obituary.pdf'>Orbituay: K V Sarma (1919–2005) </a></td>
<td> </td>
<td>216</td>
</tr>
<tr>
<td>958</td>
<td>IJHS-41-2006-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_2_8_SupplementGrahalaghvam.pdf'>Supplement </a></td>
<td> </td>
<td>5856</td>
</tr>
<tr>
<td>959</td>
<td>IJHS-41-2006-Issue-3</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_1_AKMishra.pdf'>Atomism of Nyaya–Vaisesika Vs Jainism— A Scientific Appraisal </a></td>
<td> Ashoka K Mishra</td>
<td>196</td>
</tr>
<tr>
<td>960</td>
<td>IJHS-41-2006-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_2_KCHari.pdf'>Epoch of Ramakasiddhanta </a></td>
<td> K Chandra Hari</td>
<td>105</td>
</tr>
<tr>
<td>961</td>
<td>IJHS-41-2006-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_3_NRaghavan.pdf'>Is Siva Iconography inspired by the Stars? </a></td>
<td> Nirupama Raghavan</td>
<td>784</td>
</tr>
<tr>
<td>962</td>
<td>IJHS-41-2006-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_4_RKDube.pdf'>Copper Production Process as described in an Early Fourteenth Century and Prakarta Text composed Thakkura Pheru </a></td>
<td> R K Dube</td>
<td>397</td>
</tr>
<tr>
<td>963</td>
<td>IJHS-41-2006-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_5_RNIyengar.pdf'>Historical Notes: Eclipse Period 3339 in Rigveda in support of R N Iyrengar’s Thesis </a></td>
<td> K D Abhyankar</td>
<td>37</td>
</tr>
<tr>
<td>964</td>
<td>IJHS-41-2006-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_6_RCGupta.pdf'>Historical Notes: Sulba–sutras: Earliest Studies and a Newly Published Manual </a></td>
<td> R C Gupta</td>
<td>78</td>
</tr>
<tr>
<td>965</td>
<td>IJHS-41-2006-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_7_SisirKMajumdar.pdf'>Historical Notes: Alexandria: The Greatest Centre of Learning in the Antiquity </a></td>
<td> Sisir K Majumdar</td>
<td>69</td>
</tr>
<tr>
<td>966</td>
<td>IJHS-41-2006-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_8_BookReview.pdf'>Book Review </a></td>
<td> Rajesh Kocchar</td>
<td>1322</td>
</tr>
<tr>
<td>967</td>
<td>IJHS-41-2006-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol41_3_9_SupplementGrahalaghavam.pdf'>Supplement </a></td>
<td> </td>
<td>8353</td>
</tr>
<tr>
<td>968</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_1_1_RKDubey.pdf'>Sources of Gold in India as described by Thakkura Pheru – An Assessment </a></td>
<td> R K Dubey</td>
<td>33</td>
</tr>
<tr>
<td>969</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol42_1_2_JKozhmthadan.pdf'>Jesuit contribution to the Origin and Development of Modern Science and Mathematics </a></td>
<td> Job Kozhamthadam</td>
<td>0</td>
</tr>
<tr>
<td>970</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol42_1_3_DRaina.pdf'>Jesuit collections of Indian Scientific Manuscripts: Ideologies and Interpretations </a></td>
<td> Dhruv Raina</td>
<td>0</td>
</tr>
<tr>
<td>971</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol42_1_4_SSahoo.pdf'>Scientist as interlocutor between Science and Society: Two Biographical Studies from Orissa (India) </a></td>
<td> Subhasis Sahoo and Binay Kumar Pattnaik</td>
<td>0</td>
</tr>
<tr>
<td>972</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol42_1_5_BSahai.pdf'>Historical Note: The Essence of Upanisads and the Emergence of Scientific Research </a></td>
<td> Baldeo Sahai</td>
<td>0</td>
</tr>
<tr>
<td>973</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_1_6_HJoglekar.pdf'>Historical Note: In Search of Indian Records of Supernovae </a></td>
<td> Hrishikesh Joglekar</td>
<td>113</td>
</tr>
<tr>
<td>974</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_1_7_NRatnasree.pdf'>Historical Note: Possible Indian Records of Supernova 1054 AD? </a></td>
<td> N Rathnasree and Sanath Kumar</td>
<td>192</td>
</tr>
<tr>
<td>975</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_1_8_BSShyalaja.pdf'>Historical Note: Records of Celestial Events by European Travellers during Medieval Times </a></td>
<td> B S Shylaja</td>
<td>16</td>
</tr>
<tr>
<td>976</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol42_1_9_BookReview.pdf'>Book Review: Jagadish Chandra Bose and National Science </a></td>
<td> Arun Kumar Biswas</td>
<td>0</td>
</tr>
<tr>
<td>977</td>
<td>IJHS-42-2007-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_1_10_Supplement.pdf'>Supplement: Karanakutuhalam of Bhaskaracarya II </a></td>
<td> S Balachandra Rao</td>
<td>212</td>
</tr>
<tr>
<td>978</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_1_PSensarma.pdf'>Enthnobiological Information in Parasara Samhita </a></td>
<td> Priyadarsan Sensarma</td>
<td>174</td>
</tr>
<tr>
<td>979</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_2_ASule.pdf'>Saptarsi' Visit to different Naksatras: Subtle Effect of Earth’s Precession </a></td>
<td> Ankit Sule et al.</td>
<td>169</td>
</tr>
<tr>
<td>980</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_3_AParekh.pdf'>Ayrabhata’s Root Extraction Methods      </a></td>
<td> Abhishek Parakh</td>
<td>107</td>
</tr>
<tr>
<td>981</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_4_RCGupta.pdf'>Yantras or Mystic Diagrams: A Wide Area for Study in Ancient and Medieval Indian Mathematics </a></td>
<td> R C Gupta</td>
<td>552</td>
</tr>
<tr>
<td>982</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Metallurgy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_5_RBalasubramaniam.pdf'>Zafarbaksh – The Composite Mughal Cannon of Aurangzeb at Fort William in Kolkata </a></td>
<td> R Balasubramaniam and Pranab K Chattopadhyay</td>
<td>576</td>
</tr>
<tr>
<td>983</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_6_KDAbhyankar.pdf'>Historical Note: BG Tilak and Ancient Indian Astronomy – A Reappraisal </a></td>
<td> K D Abhyankar</td>
<td>135</td>
</tr>
<tr>
<td>984</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_6_KDAbhyankar.pdf'>Historical Note: BG Tilak and Ancient Indian Astronomy - A Reappraisal </a></td>
<td> K D Abhyankar</td>
<td>135</td>
</tr>
<tr>
<td>985</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_7_KCHari.pdf'>Historical Note: Epoch of Lalla – An Overview </a></td>
<td> K Chandra Hari</td>
<td>103</td>
</tr>
<tr>
<td>986</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_8_RRanade.pdf'>Historical Note: Cultivation of Naturally Coloured Cotton in India in the 19th century  </a></td>
<td> Rekha Ranade</td>
<td>58</td>
</tr>
<tr>
<td>987</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_9_SKMajumdar.pdf'>Historical Note: Reception of Relativity Theory in Different Social, Political and Religious Ideolog </a></td>
<td> Sisir Kumar Majumdar</td>
<td>142</td>
</tr>
<tr>
<td>988</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_10_BookReviewDWajastyk.pdf'>Book Review: The Legacy of Susruta </a></td>
<td> D Wujastyk</td>
<td>59</td>
</tr>
<tr>
<td>989</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_11_BookReviewMSSriram.pdf'>Book Review: Galileo Galilei – When the World Stood Still </a></td>
<td> M S Sriram</td>
<td>64</td>
</tr>
<tr>
<td>990</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_12_BookReviewJNSinha.pdf'>Book Review: Chemical Sciences in Colonial India: The Science in Social History </a></td>
<td> Jagdish N Sinha</td>
<td>28</td>
</tr>
<tr>
<td>991</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_13_Obituary.pdf'>Obituary: Sushil Kumar Mukherjee (1914-2006)       </a></td>
<td> Arun Kumar Biswas</td>
<td>93</td>
</tr>
<tr>
<td>992</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_14_News.pdf'>News </a></td>
<td> </td>
<td>42</td>
</tr>
<tr>
<td>993</td>
<td>IJHS-42-2007-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_2_15_Supplement.pdf'>Supplement: Karanakutuhalam of Bhaskaracarya II </a></td>
<td> S Balachandra Rao</td>
<td>562</td>
</tr>
<tr>
<td>994</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_1_DBWagner.pdf'>Chinese Steel Making Techniques with a Note on Indian Wootz Steel in China </a></td>
<td> Donald B Wagner</td>
<td>521</td>
</tr>
<tr>
<td>995</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_2_AFeuerbach.pdf'>Production and Trade of Crucible Steel in Central Asia </a></td>
<td> Ann Feuerbach</td>
<td>272</td>
</tr>
<tr>
<td>996</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_3_JLCoze.pdf'>On the Question of Possible Transfer of Steel Technology from India to Europe through the Muslim Middle East </a></td>
<td> Jean Le Coze</td>
<td>398</td>
</tr>
<tr>
<td>997</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_4_AFeuerbach.pdf'>On the Origin of the terms Wootz‚ Hinduwani and Pulad </a></td>
<td> Ann Feuerbach‚ R Balasubramaniam and S Kalyanaraman</td>
<td>117</td>
</tr>
<tr>
<td>998</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_5_PKChattopadhyay.pdf'>From Wrought Iron to Steel: Beginning of Steel Making in Eastern India </a></td>
<td> Pranab K Chattopadhyay‚ Pradeep K Behera and Prasanta K Datta</td>
<td>465</td>
</tr>
<tr>
<td>999</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_6_VTripathi.pdf'>Towards the Wootz: Iron and Steel Technology in India </a></td>
<td> Vibha Tripathi</td>
<td>298</td>
</tr>
<tr>
<td>1000</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_7_RBalasubramaniam.pdf'>New Insights on Classification of Iron-Carbon Alloys‚ Specially High Carbon Steels‚ in Rasaratnasamuccaya </a></td>
<td> R Balasubramaniam and S Kalyanaraman</td>
<td>256</td>
</tr>
<tr>
<td>1001</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_8_SJaikishan.pdf'>Survey of Iron and Wootz Steel Production Sites in Northern Telangana </a></td>
<td> S Jaikishan</td>
<td>414</td>
</tr>
<tr>
<td>1002</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_9_SJaikishan.pdf'>Material Evidences for Wootz Steel Production in Northern Telangana </a></td>
<td> S Jaikishan and R Balasubramaniam</td>
<td>579</td>
</tr>
<tr>
<td>1003</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_10_SJaikishan.pdf'>Social Aspects of  Wootz Steel Manufacture in Northern Telangana </a></td>
<td> S Jaikishan and R Balasubramaniam</td>
<td>262</td>
</tr>
<tr>
<td>1004</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_11_RBalasubramaniam.pdf'>On the Varied Applications of Wootz Steel </a></td>
<td> R Balasubramaniam</td>
<td>494</td>
</tr>
<tr>
<td>1005</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_12_HistoricalNoteRBalasubramaniam.pdf'>Historical Note: Wootz Steel Received by Alexander </a></td>
<td> R Balasubramaniam</td>
<td>126</td>
</tr>
<tr>
<td>1006</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_13_HistoricalNoteGJuleff.pdf'>Historical Note: Crucibal Steel in Sri Lanka in the First Millennium AD and the Early Twentieth Century </a></td>
<td> Gill Juleff</td>
<td>24</td>
</tr>
<tr>
<td>1007</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_14_HistoricalNoteLPandey.pdf'>Historical Note: Swords of Sirohi </a></td>
<td> Lalit Pandey</td>
<td>31</td>
</tr>
<tr>
<td>1008</td>
<td>IJHS-42-2007-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_3_15_Historical NoteRBalasubramaniam.pdf'>Historical Note: Recreating Wootz Steel Outside India </a></td>
<td> R Balasubramaniam</td>
<td>96</td>
</tr>
<tr>
<td>1009</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_1_JWadsworth.pdf'>Damascus Steels: History‚ Processing‚ Properties and Carbon Dating </a></td>
<td> J Wadsworth</td>
<td>454</td>
</tr>
<tr>
<td>1010</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_2_JVerhoeven.pdf'>Pattern Formation in Wootz Damascus Steel Swords and Blades </a></td>
<td> John Verhoeven</td>
<td>358</td>
</tr>
<tr>
<td>1011</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_3_JLCoze.pdf'>Wootz Decarburisation during the forging of a Sword </a></td>
<td> Jean Le Coze and Asdin Aoufi</td>
<td>218</td>
</tr>
<tr>
<td>1012</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_4_PTCraddock.pdf'>Cast Iron: The Elusive Feedstock of Crucible Steel </a></td>
<td> Paul T Craddock</td>
<td>188</td>
</tr>
<tr>
<td>1013</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_5_VKumar.pdf'>Microstructural Characterization along the length of a Wedge Shaped Wootz Steel Implement </a></td>
<td> Vinod Kumar‚ M R Barnett‚ R Balasubramaniam and S Jaikishan</td>
<td>548</td>
</tr>
<tr>
<td>1014</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_6_MRBarnett.pdf'>New Insights on the Mechanism of Carbide Banding in Thermomechanically Processed Wootz Steel Obtained Using Electron Back Scattering Diffraction </a></td>
<td> M R Barnett and R Balasubramaniam</td>
<td>392</td>
</tr>
<tr>
<td>1015</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_7_RBalasubramaniam.pdf'>Analysis of Wootz Steel Crucibles from Northern Telangana </a></td>
<td> R Balasubramaniam‚ Anubhav Pandey and S Jaikishan</td>
<td>444</td>
</tr>
<tr>
<td>1016</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_8_SSrinivasan.pdf'>On Higher Carbon and Crucible Steels in Southern India: Further Insights from Mel-Siruvalur‚ Kodumanal and Pattinam </a></td>
<td> Sharada Srinivasan</td>
<td>401</td>
</tr>
<tr>
<td>1017</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_9_HistoricalNotes.pdf'>Historical Note: Konasamudram: The Famous Wootz Steel Production Center </a></td>
<td> S Jaikishan and R Balasubramaniam</td>
<td>74</td>
</tr>
<tr>
<td>1018</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_10_SJaikishan.pdf'>Historical Note: Interview with Wootz Steel Worker from Konapuram Village in Northern Telangana </a></td>
<td> S Jaikishan and R Balasubramaniam</td>
<td>68</td>
</tr>
<tr>
<td>1019</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_11_BookReview.pdf'>Book Review: Persian Steel: The Tanavoli Collection </a></td>
<td> R Balasubramaniam</td>
<td>137</td>
</tr>
<tr>
<td>1020</td>
<td>IJHS-42-2007-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol42_4_12_Supplement.pdf'>Supplement: Khadgalaksana Siromani of Navanappa </a></td>
<td> S Jaikishan</td>
<td>552</td>
</tr>
<tr>
<td>1021</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_1_RNIyengar.pdf'>Archaic Astronomy of Parauara and Vrddha Garga </a></td>
<td> R N Iyengar</td>
<td>220</td>
</tr>
<tr>
<td>1022</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_2_SSantra.pdf'>Recent Bronze Hoard from West Bengal: Analytical Studies </a></td>
<td> Sumita Santra‚ Gautam Sengupta‚ Dipan Bhattacharya‚ Manoranjan Sarkar‚ Prati</td>
<td>208</td>
</tr>
<tr>
<td>1023</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_3_JDeloche.pdf'>Water Resources in the Hill Forts of South India (14—18th Century) </a></td>
<td> Jean Deloche</td>
<td>344</td>
</tr>
<tr>
<td>1024</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_4_PKBondyopadhyay.pdf'>Two Recently Discovered Patents of Professor Jagadis Chunder Bose and India’s First Electronics Technology Transfer to the West </a></td>
<td> Probir K Bondyopadhyay and Suchanda Banerjee</td>
<td>435</td>
</tr>
<tr>
<td>1025</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_5_KDAbhyankar.pdf'>Historical Note: On the Precessional Movement of Saptarsis </a></td>
<td> K D Abhyankar</td>
<td>148</td>
</tr>
<tr>
<td>1026</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_6_RCGupta.pdf'>Historical Note: True Laksa—Scale Numeration System of the Valmiki—Ramayana </a></td>
<td> R C Gupta</td>
<td>99</td>
</tr>
<tr>
<td>1027</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_7_DBhattacharya.pdf'>Historical Note: Astro—Navigational Aspects of the Bhumi Anla </a></td>
<td> Deepak Bhattacharya and PC Naik</td>
<td>195</td>
</tr>
<tr>
<td>1028</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_8_DNUkidwe.pdf'>Historical Note: Srstikrama Construction of Sriyantra </a></td>
<td> D N Ukidwe</td>
<td>158</td>
</tr>
<tr>
<td>1029</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_9_DBhattacharya.pdf'>Historical Note: Select Palm Leaf Manuscripts in Orissa State Museum‚ Bhubaneswar on Astronomy and Mathematics </a></td>
<td> Deepak Bhattacharya</td>
<td>102</td>
</tr>
<tr>
<td>1030</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_10_SKMajumdar.pdf'>Historical Note: The Gifts of Chemistry to Modern Medicine </a></td>
<td> Sisir Kumar Majumdar</td>
<td>100</td>
</tr>
<tr>
<td>1031</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_11_BookReview_CPalit.pdf'>Book Review: Social History of Science in Colonial India </a></td>
<td> Chittabrata Palit</td>
<td>78</td>
</tr>
<tr>
<td>1032</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_12_BookReview_AKBiswas.pdf'>Book Review: The Bengal Renaissance </a></td>
<td> A K Biswas</td>
<td>113</td>
</tr>
<tr>
<td>1033</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_13_Obituary.pdf'>Obituary: KD Abhyankar (1928—2007) </a></td>
<td> </td>
<td>84</td>
</tr>
<tr>
<td>1034</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_14_News.pdf'>News </a></td>
<td> Shabnam Shukla</td>
<td>73</td>
</tr>
<tr>
<td>1035</td>
<td>IJHS-43-2008-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_1_15_Supplement.pdf'>Supplement: Karanakutuhalam of Bhaskaracarya II </a></td>
<td> S Balachandra Rao</td>
<td>291</td>
</tr>
<tr>
<td>1036</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Medicine</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_1_VJDeshpande.pdf'>Glimpses of Ayurveda in Medieval Chinese Medicine </a></td>
<td> Vijaya Jayant Deshpande</td>
<td>303</td>
</tr>
<tr>
<td>1037</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_2_JBhattacharya.pdf'>Encounter In Anatomical Knowledge: East And West </a></td>
<td> Jayanta Bhattacharya</td>
<td>252</td>
</tr>
<tr>
<td>1038</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_3_RAkhtar.pdf'>Environment and Cholera in Kashmir during Nineteenth Century </a></td>
<td> Rais Akhtar</td>
<td>196</td>
</tr>
<tr>
<td>1039</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_4_HSingh.pdf'>Ram Nath Chopra (1882—1973) — A Vissionary in Pharmaceutical Science </a></td>
<td> Harkishan Singh</td>
<td>224</td>
</tr>
<tr>
<td>1040</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_5_SKAcharya.pdf'>Historical Note: Ancient Methods of Preserving Copper Plate Grants </a></td>
<td> Subrata Kumar Acharya</td>
<td>126</td>
</tr>
<tr>
<td>1041</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_6_CPalit.pdf'>Historical Note: Popular Response to Epidemics in Colonial Bengal </a></td>
<td> Chittabrata Palit</td>
<td>90</td>
</tr>
<tr>
<td>1042</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_7_RKDube.pdf'>Historical Note: Superiority of Makrana (Rajasthan) Marbles </a></td>
<td> R K Dube</td>
<td>94</td>
</tr>
<tr>
<td>1043</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_8_SKMjumdar.pdf'>Historical Note: Socio—Political Thoughts of Einstein </a></td>
<td> Sisir K Majumdar</td>
<td>123</td>
</tr>
<tr>
<td>1044</td>
<td>IJHS-43-2008-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_9_BookReview.pdf'>Book Review: Story of the Delhi Iron Pillar </a></td>
<td> Arun Kumar Biswas</td>
<td>99</td>
</tr>
<tr>
<td>1045</td>
<td>IJHS-43-2008-Issue-2</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_2_10_Obituary.pdf'>Obituary: Priyavrata Sharma — A Legendary Personality (1920—2007) </a></td>
<td> P V Tiwari</td>
<td>250</td>
</tr>
<tr>
<td>1046</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_1_PGondhalekar.pdf'>Vedanga Jyotisa — Where and When? </a></td>
<td> Prabhakar Gondhalekar</td>
<td>217</td>
</tr>
<tr>
<td>1047</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_2_ACohen.pdf'>The Jewish calendar and its relation to the Christian holidays as described by a Muslim Mathematician—Astronomer in 852 AD </a></td>
<td> Ariel Cohen</td>
<td>219</td>
</tr>
<tr>
<td>1048</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_3_PKDatta.pdf'>Investigations on Ancient High — Tin Bronze Excavated From Lower Bengal Region of Tilpi </a></td>
<td> Prasanta K Datta‚ Pranab K Chattopadhyay and Barnali Mandal</td>
<td>431</td>
</tr>
<tr>
<td>1049</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_4_DBhattacharya.pdf'>Historical Note: Archaeo—Astronomy of Nataraja </a></td>
<td> Deepak Bhattacharya</td>
<td>282</td>
</tr>
<tr>
<td>1050</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_5_NRatnasree.pdf'>Historical Note: Karka—Rasi—Valaya—The Instrument on the Back Wall of the Misra Yantra </a></td>
<td> N Rathnasree‚ Anurag Garg‚ Arpita Pandey and R K Chikara</td>
<td>180</td>
</tr>
<tr>
<td>1051</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_6_RSingh.pdf'>Historical Note: Indo—American Relation with reference to Bernard Peters </a></td>
<td> Rajinder Singh</td>
<td>145</td>
</tr>
<tr>
<td>1052</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_7_BookReview.pdf'>Book Review: Studies in the History of the Exact Sciences in Honour of David Pingree </a></td>
<td> S Balachandra Rao</td>
<td>168</td>
</tr>
<tr>
<td>1053</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_8_Obituary.pdf'>Obituary: Kripa Shankar Shukla (1918—2007) </a></td>
<td> Yukio Ohashi</td>
<td>122</td>
</tr>
<tr>
<td>1054</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_9_News.pdf'>News: National Workshop on Preserving our Scientific Heritage‚ held at Indian Institute of Astrophysics‚ Bangalore‚ January 21—22‚ 2008 — A Report </a></td>
<td> A Vagiswari‚ Christina Birdie and Indira Chowdhury</td>
<td>94</td>
</tr>
<tr>
<td>1055</td>
<td>IJHS-43-2008-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_3_10_Supplement.pdf'>Supplement: Karanakutuhalam of Bhaskaracarya II </a></td>
<td> S Balachandra Rao</td>
<td>454</td>
</tr>
<tr>
<td>1056</td>
<td>IJHS-43-2008-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_1_PGondhalekar.pdf'>Intercalation in the Vedic Texts </a></td>
<td> Prabhakar Gondhalekar</td>
<td>282</td>
</tr>
<tr>
<td>1057</td>
<td>IJHS-43-2008-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_2_Sbalachandrarao.pdf'>Conjunctions‚ Transits and Occultations by Siddhantic Procedures </a></td>
<td> S Balachandra Rao‚ S K Uma and Padmaja Venugopal</td>
<td>372</td>
</tr>
<tr>
<td>1058</td>
<td>IJHS-43-2008-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_3_VMMallayya.pdf'>Interpolation of Sines by Successive Approximation Method </a></td>
<td> V Madhukar Mallayya</td>
<td>149</td>
</tr>
<tr>
<td>1059</td>
<td>IJHS-43-2008-Issue-4</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_4_SDucheyne.pdf'>Scientific Research Papers in the Philosophical Transactions of the Royal Society of London‚ 1665—1800: The Development of Physics in the footsteps of Sir Isaac Newton </a></td>
<td> S Ducheyne</td>
<td>681</td>
</tr>
<tr>
<td>1060</td>
<td>IJHS-43-2008-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_5_HSingh.pdf'>Historical Note: Khem Singh Grewal (1894—4965) — A Prominent Medico—Pharmaceutical Professional </a></td>
<td> Harkishan Singh</td>
<td>187</td>
</tr>
<tr>
<td>1061</td>
<td>IJHS-43-2008-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_6_SKMajumdar.pdf'>Historical Note: Robotics (Cybernetics) in Medical Science: Blessing or Blight </a></td>
<td> Sisir K Majumdar</td>
<td>55</td>
</tr>
<tr>
<td>1062</td>
<td>IJHS-43-2008-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_7_BookReviewKRajan.pdf'>Book Review: History of Iron Technology in India </a></td>
<td> K Rajan</td>
<td>47</td>
</tr>
<tr>
<td>1063</td>
<td>IJHS-43-2008-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_8_BookReviewBPrakash.pdf'>Book Review: Marvels of Indian Iron through the Ages </a></td>
<td> B Prakash</td>
<td>83</td>
</tr>
<tr>
<td>1064</td>
<td>IJHS-43-2008-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_9_News.pdf'>News </a></td>
<td> </td>
<td>18</td>
</tr>
<tr>
<td>1065</td>
<td>IJHS-43-2008-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol43_4_10_BooksreceivedforReview.pdf'>Books received for Review </a></td>
<td> </td>
<td>24</td>
</tr>
<tr>
<td>1066</td>
<td>IJHS-44-2009-Issue-1</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_0_Editorial.pdf'>Editorial </a></td>
<td> </td>
<td>318</td>
</tr>
<tr>
<td>1067</td>
<td>IJHS-44-2009-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_1_MRoy.pdf'>Ecological concept in Ayurveda: Nature-man relations </a></td>
<td> Mira Roy</td>
<td>71</td>
</tr>
<tr>
<td>1068</td>
<td>IJHS-44-2009-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_2_PSensarma.pdf'>Biodiversity: Methods of Conservation in the Usanah Samita </a></td>
<td> Priyadarsan Sensarma</td>
<td>35</td>
</tr>
<tr>
<td>1069</td>
<td>IJHS-44-2009-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_3_RBalasubramaniam.pdf'>On technical analysis of Cannon Shot Crater on Delhi Iron Pillar </a></td>
<td> R Balasubramaniama, V N Prabhakarb and Manish Shankara</td>
<td>342</td>
</tr>
<tr>
<td>1070</td>
<td>IJHS-44-2009-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_4_BPrakash.pdf'>Religious traditions of Ancient Iron and Steel Craftsmen of India and Japan </a></td>
<td> B. Prakash</td>
<td>459</td>
</tr>
<tr>
<td>1071</td>
<td>IJHS-44-2009-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_5_KRoy.pdf'>Science of Siege Warfare in India during the Great Mutiny: 1857-58 </a></td>
<td> Kaushik Roy</td>
<td>61</td>
</tr>
<tr>
<td>1072</td>
<td>IJHS-44-2009-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_6_Historical Notes.pdf'>Historical Notes: On the Sanskrit word, Svarnaja used for metal, tin </a></td>
<td> R.K. Dube</td>
<td>63</td>
</tr>
<tr>
<td>1073</td>
<td>IJHS-44-2009-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_7_KCHari.pdf'>Historical Notes: Identification of Asmaka </a></td>
<td> K Chandra Hari</td>
<td>62</td>
</tr>
<tr>
<td>1074</td>
<td>IJHS-44-2009-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_8_SKMajumdar.pdf'>Historical Notes: The Genius of Darwin- Two Hundred Years </a></td>
<td> Sisir K. Majumdar</td>
<td>40</td>
</tr>
<tr>
<td>1075</td>
<td>IJHS-44-2009-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_1_9_Book Review.pdf'>Book Review </a></td>
<td> M.S. Sriram</td>
<td>43</td>
</tr>
<tr>
<td>1076</td>
<td>IJHS-44-2009-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_0_Editorial.pdf'>Editorial </a></td>
<td> </td>
<td>144</td>
</tr>
<tr>
<td>1077</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_1_CPechhia.pdf'>Transmitting the Carakasamhita: A History of the Tradition </a></td>
<td> Cristina Pecchia</td>
<td>66</td>
</tr>
<tr>
<td>1078</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_2_PAMaas.pdf'>Towards a critical edition of the Carakasamhita Vimanasthana - First results </a></td>
<td> Philipp A Maas</td>
<td>636</td>
</tr>
<tr>
<td>1079</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_3_DWujastyk.pdf'>New Evidence for the Textual and Cultural History of the Susruta Samhita </a></td>
<td> Dominik Wujastyk</td>
<td>2110</td>
</tr>
<tr>
<td>1080</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_4_KGZysk.pdf'>Some reflections on Siddha medicine in Tamilnadu </a></td>
<td> Kenneth G Zysk</td>
<td>37</td>
</tr>
<tr>
<td>1081</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_5_PT Craddock.pdf'>Metals, minerals and medicine </a></td>
<td> Paul T Craddock</td>
<td>512</td>
</tr>
<tr>
<td>1082</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_6_ACerulli.pdf'>Narrative well-being: Anandarayamakhin's the Joy of Life (Jivanandanam) </a></td>
<td> Anthony Cerulli</td>
<td>65</td>
</tr>
<tr>
<td>1083</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_7_MSankaranarayana.pdf'>An analysis of formulation of Vaitarana  [Basti] on the basis of Ayurvedic texts and Commentaries </a></td>
<td> Manoj Sankaranarayana</td>
<td>85</td>
</tr>
<tr>
<td>1084</td>
<td>IJHS-44-2009-Issue-2</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_8_KPrasendanz.pdf'>Logic, Debate and Epistemology in Ancient Indian medicine and Philosophy - An Investigation </a></td>
<td> Karin Preisendanz</td>
<td>221</td>
</tr>
<tr>
<td>1085</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_9_HistoricalNotes.pdf'>Historical Note: Depiction of Human Anatomy in Indian Archaeology- A select report </a></td>
<td> Deepak Bhattacharya</td>
<td>323</td>
</tr>
<tr>
<td>1086</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_10_SPrema.pdf'>Historical Note: Eye Diseases in traditional Siddha System of Medicine - An Overview </a></td>
<td> S. Prema</td>
<td>159</td>
</tr>
<tr>
<td>1087</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_11_RSarkar.pdf'>Historical Note:  Ayurvedic Concept of Cancer and its treatment </a></td>
<td> Roma Sarkar</td>
<td>42</td>
</tr>
<tr>
<td>1088</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_12_SDas.pdf'>Historical Note: Dr. Subodh Mitra (1896-1961) - A Visionary of Cancer Treatment and Research in India </a></td>
<td> Sukta Das</td>
<td>158</td>
</tr>
<tr>
<td>1089</td>
<td>IJHS-44-2009-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_2_13_Supplement.pdf'>Supplement: Rasaprakasa Sudhakara </a></td>
<td> </td>
<td>145</td>
</tr>
<tr>
<td>1090</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_1_RNIyengar.pdf'>Connections Between The Vedanga Jyotisa And Other Vedic Literature </a></td>
<td> R N Iyengar</td>
<td>46</td>
</tr>
<tr>
<td>1091</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Metallurgy</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_2_WLox.pdf'>Bintie— The Wootz Steel In Ancient China </a></td>
<td> William Lox</td>
<td>234</td>
</tr>
<tr>
<td>1092</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_3_RBalasubramaniampdf.pdf'>New Insights On Architects Of Taj </a></td>
<td> R Balasubramaniam</td>
<td>162</td>
</tr>
<tr>
<td>1093</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_4_KRoy.pdf'>Technology Transfer And The Evolution Of Ordnance Establishment In British—India— 1639 to 1856 </a></td>
<td> Kaushik Roy</td>
<td>66</td>
</tr>
<tr>
<td>1094</td>
<td>IJHS-44-2009-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_5_Historical Notes.pdf'>Historical Notes </a></td>
<td> Sisir K Majumdar</td>
<td>87</td>
</tr>
<tr>
<td>1095</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_6_RBhattacharya.pdf'>The Circular Drona— KuRma and Sarathacakra Citis in the Sulbasu— Tras </a></td>
<td> R Bhattacharya</td>
<td>114</td>
</tr>
<tr>
<td>1096</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_7_AKBag.pdf'>History Of Science Program Of The Indian National Science Academy (1959— 2009) </a></td>
<td> A K Bag</td>
<td>35</td>
</tr>
<tr>
<td>1097</td>
<td>IJHS-44-2009-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_8_AKBiswaspdf.pdf'>Book Review </a></td>
<td> A K Biswas</td>
<td>24</td>
</tr>
<tr>
<td>1098</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_9_News.pdf'>Conference on Indian Astronomy and Mathematics In Ancient India— A Report </a></td>
<td> J M Delire</td>
<td>23</td>
</tr>
<tr>
<td>1099</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_3_10_SShuklapdf.pdf'>History Of Science Project Investigator’s Meet Cum Workshop On 13-15th April 2009 : A Report </a></td>
<td> Shabnam Shukla</td>
<td>18</td>
</tr>
<tr>
<td>1100</td>
<td>IJHS-44-2009-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_11_SupplementRasaprakasasudhakara.pdf'>Rasaprakasa Sudhakarachap— Ch2 Supplement </a></td>
<td> Damodar Joshi</td>
<td>46</td>
</tr>
<tr>
<td>1101</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_1_PGondhalekar.pdf'>The Vedic Naksatras— A Reappraisal </a></td>
<td> Prabhakar Gondhalekar</td>
<td>112</td>
</tr>
<tr>
<td>1102</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_2_MRoy.pdf'>Agriculture In The Vedic Period </a></td>
<td> Mira Roy</td>
<td>82</td>
</tr>
<tr>
<td>1103</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_3_RBalasubramaniam.pdf'>New Insights On Artisans Of Taj </a></td>
<td> R Balasubramaniam</td>
<td>330</td>
</tr>
<tr>
<td>1104</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_4_JDeloche.pdf'>Stableships Of Tiruppudaimarudur And Tirukkurunkudi (South India) </a></td>
<td> Jean Deloche</td>
<td>797</td>
</tr>
<tr>
<td>1105</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_5_HSingh.pdf'>Bishnupada Mukerji (1903—79): A Medicopharmaceutical Professional Of Eminence </a></td>
<td> Harkishan Singh</td>
<td>118</td>
</tr>
<tr>
<td>1106</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_6_Historical Notes.pdf'>Historical Notes:Spice And Herb— A Historical Overview </a></td>
<td> Sisir K Majumdar</td>
<td>20</td>
</tr>
<tr>
<td>1107</td>
<td>IJHS-44-2009-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_7_AKBag.pdf'>Book Review </a></td>
<td> A K Bag</td>
<td>34</td>
</tr>
<tr>
<td>1108</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_8_SeminarReport.pdf'>Seminar Report CNRS—NYU Workshop On Early Mathematics: A Report </a></td>
<td> Toke L Knudsen</td>
<td>13</td>
</tr>
<tr>
<td>1109</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_9_SShukla.pdf'>The 69th Session Of The Indian History Congress :Kannur 28-30 December 2008— A Report </a></td>
<td> Shabnam Shukla</td>
<td>17</td>
</tr>
<tr>
<td>1110</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_10_CPecchia.pdf'>14th World Sanskrit Conference— Section On Scientific Literature_A Report </a></td>
<td> Cristina Pecchia</td>
<td>21</td>
</tr>
<tr>
<td>1111</td>
<td>IJHS-44-2009-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_11_News.pdf'>Books Received For Review In IJHS 2009 </a></td>
<td> </td>
<td>13</td>
</tr>
<tr>
<td>1112</td>
<td>IJHS-44-2009-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_4_12_Reminiscenses.pdf'>Reminiscence </a></td>
<td> </td>
<td>10</td>
</tr>
<tr>
<td>1113</td>
<td>IJHS-44-2009-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol44_13_SupplementRasaprakasasudhakara.pdf'>Rasaprakasa Sudhakara— Chap4 </a></td>
<td> Damodar Joshi</td>
<td>184</td>
</tr>
<tr>
<td>1114</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>11</td>
</tr>
<tr>
<td>1115</td>
<td>IJHS-45-2010-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_1_RNIyengar.pdf'>Comets and Meteoritic Showers in the Rigveda and their significance </a></td>
<td> R.N. Iyengar</td>
<td>113</td>
</tr>
<tr>
<td>1116</td>
<td>IJHS-45-2010-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_2_JDeloche.pdf'>Roman Trade Routes in South India: Geographical and Technical Considerations (c. 1st cent. BC – 5th cent. AD) </a></td>
<td> Jean Deloche</td>
<td>180</td>
</tr>
<tr>
<td>1117</td>
<td>IJHS-45-2010-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_4_RCGupta.pdf'>Bhagyashree Bavare‚ Mahesh Shetti and P.P. Divakaran Techniques of Ancient Empirical Mathematics </a></td>
<td> R.C. Gupta</td>
<td>183</td>
</tr>
<tr>
<td>1118</td>
<td>IJHS-45-2010-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_5_BMandalarticle.pdf'>Understanding Alloy Design Principles and Cast Metal Technology in Hot Molds for Medieval Bengal </a></td>
<td> B. Mandal, Pranab K. Chattopadhyay, D. Misra et al.</td>
<td>937</td>
</tr>
<tr>
<td>1119</td>
<td>IJHS-45-2010-Issue-1</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_6_SKMajumdar.pdf'>Historical Note: Marx and Darwin Connection in London </a></td>
<td> Sisir Kr. Majumdar</td>
<td>15</td>
</tr>
<tr>
<td>1120</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_7_Bookreview.pdf'>Book Review </a></td>
<td> Madhvendra Narayan</td>
<td>27</td>
</tr>
<tr>
<td>1121</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_8_SeminarReport.pdf'>Seminar Report </a></td>
<td> Gulfishan Khan</td>
<td>20</td>
</tr>
<tr>
<td>1122</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_9_News.pdf'>News </a></td>
<td> </td>
<td>18</td>
</tr>
<tr>
<td>1123</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_10_Awards.pdf'>Awards and Honours </a></td>
<td> </td>
<td>13</td>
</tr>
<tr>
<td>1124</td>
<td>IJHS-45-2010-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_11_1_Supplement.pdf'>Supplement: Rasaprakasa Sudhakara </a></td>
<td> Damodar Joshi</td>
<td>45</td>
</tr>
<tr>
<td>1125</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_11_2_Supplement.pdf'>Supplement: Chapter 6— Sanskrit Text </a></td>
<td> </td>
<td>44</td>
</tr>
<tr>
<td>1126</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_11_3_Supplement.pdf'>Supplement: Chapter 6— English Translation </a></td>
<td> </td>
<td>59</td>
</tr>
<tr>
<td>1127</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_11_4_Supplement.pdf'>Supplement: Chapter 7— Sanskrit Text </a></td>
<td> </td>
<td>39</td>
</tr>
<tr>
<td>1128</td>
<td>IJHS-45-2010-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_1_11_5_Supplement.pdf'>Supplement: Chapter 7— English Translation </a></td>
<td> </td>
<td>43</td>
</tr>
<tr>
<td>1129</td>
<td>IJHS-45-2010-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>11</td>
</tr>
<tr>
<td>1130</td>
<td>IJHS-45-2010-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_1_NSingh.pdf'>Alcoholic Fermentation Techniques in Early Indian Tradition </a></td>
<td> Nand Lal Singh‚ Ramprasad‚ P K Mishra et al.</td>
<td>57</td>
</tr>
<tr>
<td>1131</td>
<td>IJHS-45-2010-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_2_PTaneja.pdf'>Enlargement of Vedis in the Sulbasutras </a></td>
<td> Padmavati Taneja and Nidhi Handa</td>
<td>152</td>
</tr>
<tr>
<td>1132</td>
<td>IJHS-45-2010-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_3_AKPanda.pdf'>Tracing Historical Perspective of Cordyceps sinensis — An Aphrodisiac in Sikkim Himalaya </a></td>
<td> Ashok Kumar Panda</td>
<td>38</td>
</tr>
<tr>
<td>1133</td>
<td>IJHS-45-2010-Issue-2</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_4_SSen.pdf'>Scientific Enquiry in Agriculture in Colonial India: A Historical Perspective </a></td>
<td> Srabani Sen</td>
<td>214</td>
</tr>
<tr>
<td>1134</td>
<td>IJHS-45-2010-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_5_AKBiswas.pdf'>Why did Scientific Renaissance take place in Europe and not in India </a></td>
<td> Arun Kumar Biswas</td>
<td>129</td>
</tr>
<tr>
<td>1135</td>
<td>IJHS-45-2010-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_6_RKochar.pdf'>Historical Notes: Rahu and Ketu in Mythological and Astronomological Contexts </a></td>
<td> Rajesh Kochhar</td>
<td>45</td>
</tr>
<tr>
<td>1136</td>
<td>IJHS-45-2010-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_7_AKBag.pdf'>Historical Notes: Role of Benaras in the Studies of History of Science </a></td>
<td> A K Bag</td>
<td>33</td>
</tr>
<tr>
<td>1137</td>
<td>IJHS-45-2010-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_8_Bookreview.pdf'>Book Review </a></td>
<td> A K Bag</td>
<td>20</td>
</tr>
<tr>
<td>1138</td>
<td>IJHS-45-2010-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_9_News.pdf'>News </a></td>
<td> Shabnam Shukla</td>
<td>19</td>
</tr>
<tr>
<td>1139</td>
<td>IJHS-45-2010-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_10_Obituary.pdf'>Obituary: Professor Ramamurthy Balasubramaniam (1961—2009) </a></td>
<td> </td>
<td>46</td>
</tr>
<tr>
<td>1140</td>
<td>IJHS-45-2010-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_11_1_Supplement_cover.pdf'>Supplement: A Commentary of Tantrasangraha in Keralabhasa: Kriyakalapa— Eng. Tr. with Notes </a></td>
<td> Venketswara Pai R‚ K Mahesh and K Ramasubramanian</td>
<td>45</td>
</tr>
<tr>
<td>1141</td>
<td>IJHS-45-2010-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_2_11_2_Supplement_text.pdf'>Supplement </a></td>
<td> Venketswara Pai R‚ K Mahesh and K Ramasubramanian</td>
<td>580</td>
</tr>
<tr>
<td>1142</td>
<td>IJHS-45-2010-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>12</td>
</tr>
<tr>
<td>1143</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_1_PGondalekha.pdf'>The Vedic Naksatra names of the Months </a></td>
<td> P Gondhalekar</td>
<td>93</td>
</tr>
<tr>
<td>1144</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_2_MNVahia.pdf'>Harappan Geometry and Symmetry_A Study of Geometrical Patterns on Indus Objects </a></td>
<td> M N Vahia and Nisha Yadav</td>
<td>979</td>
</tr>
<tr>
<td>1145</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_3_BSasisekara.pdf'>Adichanallur_A Prehistoric Mining Site </a></td>
<td> B Sasisekaran, S Sundararajan et al.</td>
<td>893</td>
</tr>
<tr>
<td>1146</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_4_RKDubey.pdf'>An Assessment of the Sanskrit word Hemaghna used for Lead Metal </a></td>
<td> R K Dube</td>
<td>39</td>
</tr>
<tr>
<td>1147</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_5_JLCoze.pdf'>About Wootz_the Question of Hinduwani or Ondanique </a></td>
<td> Jean Le Coze</td>
<td>32</td>
</tr>
<tr>
<td>1148</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_6_SRSarma.pdf'>The Date of Aryabhata _ Refutation of V Lakshmikantham’s ryabhata_Refutation of V Lakshmikantham’s Untenable View </a></td>
<td> S R Sarma</td>
<td>36</td>
</tr>
<tr>
<td>1149</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_7_HSingh.pdf'>Tribhovandas Kalyandas Gajjar (1863-1920)_Pioneer Industrial Chemist of India </a></td>
<td> Harkishan Singh</td>
<td>126</td>
</tr>
<tr>
<td>1150</td>
<td>IJHS-45-2010-Issue-3</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_8_SKSen.pdf'>Ashish Lahiri_Radhanath Sikdar Beyond the Peak </a></td>
<td> Sisir Sen</td>
<td>12</td>
</tr>
<tr>
<td>1151</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_9_NupurDasgup.pdf'>Minor Metal Crafts in Bengal_Tradition and Changes from the Medieval Times to the Present </a></td>
<td> Nupur Dasgupta</td>
<td>32</td>
</tr>
<tr>
<td>1152</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_10_NParthasar.pdf'>Indigenous Knowledge of the Medicinal Plant Resources of Coromandel Coast Forests of Peninsular India in Modern Period </a></td>
<td> N Parthasarathy</td>
<td>21</td>
</tr>
<tr>
<td>1153</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_11_News.pdf'>Workshop on the History of Indian Science at the Bibliotheque Nationale de France: A Report_and 70th Indian History Congress_A Report </a></td>
<td> Jerome Petit_Shabnam Shukla</td>
<td>25</td>
</tr>
<tr>
<td>1154</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_12_SupplementInn.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English Translation and Appendices (Chap 8) Part 1 </a></td>
<td> Damodar Joshi</td>
<td>62</td>
</tr>
<tr>
<td>1155</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_13_Sanskrittextc.pdf'>Rasaprakasa Sudhakara_Sanskrit Text with English Translation and Appendices (Chap 8) Part 2 </a></td>
<td> Damodar Joshi</td>
<td>90</td>
</tr>
<tr>
<td>1156</td>
<td>IJHS-45-2010-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_3_14_EnglishtextCha.pdf'>Rasaprakasa Sudhakara_Sanskrit Text with English Translation and Appendices (Chap 8)Part 3 </a></td>
<td> Damodar Joshi</td>
<td>225</td>
</tr>
<tr>
<td>1157</td>
<td>IJHS-45-2010-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>12</td>
</tr>
<tr>
<td>1158</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_1_ANarayan.pdf'>Dating the Surya Siddhanta using Computational Simulation of Proper Motions and Ecliptic Variations </a></td>
<td> Anil Narayan</td>
<td>129</td>
</tr>
<tr>
<td>1159</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_2_ASharan.pdf'>The Lost Knowledge_Accurate Positioning of Planets </a></td>
<td> Anand M Sharan</td>
<td>82</td>
</tr>
<tr>
<td>1160</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_3_RCKapoor.pdf'>The Historical Significance of the Total Solar Eclipse of Oct 17_1762 passing over Panjab </a></td>
<td> R C Kapoor</td>
<td>149</td>
</tr>
<tr>
<td>1161</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_4_GKhan.pdf'>Karim Khan and his Perceptions of Western Science during his visit to Britain in 1840-41 </a></td>
<td> Gulfishan Khan</td>
<td>100</td>
</tr>
<tr>
<td>1162</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_5_HSingh.pdf'>Khwaja Abdul Hamied (1898-1972)_Pioneer Scientist Industrialist </a></td>
<td> Harkishan Singh</td>
<td>338</td>
</tr>
<tr>
<td>1163</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_6_JNSinha.pdf'>Veterinary Science and Animal Husbandry in India_A Case of IVRI at Mukteswar_IzatnagarStudy </a></td>
<td> J N Sinha</td>
<td>30</td>
</tr>
<tr>
<td>1164</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_7_Historicalnotes.pdf'>Nandigrama of Ganesa Daivajna </a></td>
<td> S R Sarma</td>
<td>35</td>
</tr>
<tr>
<td>1165</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_8_Bookreview.pdf'>Thakkura Pheru_Ganitasarakaumudi_The Moonlight of the Essence of Mathematics (ed and tr by SaKHYa) </a></td>
<td> R C Gupta</td>
<td>24</td>
</tr>
<tr>
<td>1166</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_9_ReportsDPAgarwal.pdf'>Documentation and Study of Archaeometallurgical and Ethnometallurgical Evidence in Uttarakhand with Special Reference to Iron and Copper </a></td>
<td> D P Agrawal</td>
<td>20</td>
</tr>
<tr>
<td>1167</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_10_ReportsJayanta.pdf'>Anatomical Knowledge and the Anatomy of Medical Some Preliminary InquiriesKnowledge in India_Some Preliminary Inquiries </a></td>
<td> Jayanta Bhattacharya</td>
<td>34</td>
</tr>
<tr>
<td>1168</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_11_ReportShukla.pdf'>History of Technology & Technical Education in India_A Synthesis </a></td>
<td> Shabnam Shukla</td>
<td>14</td>
</tr>
<tr>
<td>1169</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_12_ReportMNarayan.pdf'>Mathematics and Astronomy in Medieval India </a></td>
<td> Madhvendra Narayan</td>
<td>30</td>
</tr>
<tr>
<td>1170</td>
<td>IJHS-45-2010-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_13_Bookreceived.pdf'>Book Received for Review </a></td>
<td> </td>
<td>11</td>
</tr>
<tr>
<td>1171</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_14_SupplementInner.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English Translationand (Chap 9-13)AppendicesPart 1 </a></td>
<td> Damodar Joshi</td>
<td>67</td>
</tr>
<tr>
<td>1172</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_15_SupChap9English.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English Translation Part2 </a></td>
<td> Damodar Joshi</td>
<td>30</td>
</tr>
<tr>
<td>1173</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_16_SupChap9Sankrit.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 3 </a></td>
<td> Damodar Joshi</td>
<td>31</td>
</tr>
<tr>
<td>1174</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_17_SupChap10Sankrit.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 4 </a></td>
<td> Damodar Joshi</td>
<td>34</td>
</tr>
<tr>
<td>1175</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_18_SupChap10English.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 5 </a></td>
<td> Damodar Joshi</td>
<td>38</td>
</tr>
<tr>
<td>1176</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_19_SupChap11Sankrit.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 6 </a></td>
<td> Damodar Joshi</td>
<td>52</td>
</tr>
<tr>
<td>1177</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_20_SupChap11English.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 7 </a></td>
<td> Damodar Joshi</td>
<td>54</td>
</tr>
<tr>
<td>1178</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_21_SupChap12Sankrit.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 8 </a></td>
<td> Damodar Joshi</td>
<td>28</td>
</tr>
<tr>
<td>1179</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_22_SupChap12English.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 9 </a></td>
<td> Damodar Joshi</td>
<td>23</td>
</tr>
<tr>
<td>1180</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_23_SupChap13Sankrit.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 10 </a></td>
<td> Damodar Joshi</td>
<td>28</td>
</tr>
<tr>
<td>1181</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_24_SupChap13English.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 11 </a></td>
<td> Damodar Joshi</td>
<td>23</td>
</tr>
<tr>
<td>1182</td>
<td>IJHS-45-2010-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_25_Appendices.pdf'>Rasaprakasa Sudhakara Sanskrit Text with English TranslationPart 12 </a></td>
<td> Damodar Joshi</td>
<td>54</td>
</tr>
<tr>
<td>1183</td>
<td>IJHS-45-2010-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_26_Index.pdf'>Index </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>1184</td>
<td>IJHS-45-2010-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_27_Cumulativeindex.pdf'>Cumulative Index </a></td>
<td> </td>
<td>24</td>
</tr>
<tr>
<td>1185</td>
<td>IJHS-45-2010-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol45_4_28_AnnualContents.pdf'>Annual Contents </a></td>
<td> </td>
<td>23</td>
</tr>
<tr>
<td>1186</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_1_PGondalekhar.pdf'>Possible Chronological Markers In The Vedic Texts </a></td>
<td> Prabhakar Gondhalekar</td>
<td>182</td>
</tr>
<tr>
<td>1187</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_2_RNIyenger.pdf'>Dhruva the Ancient Indian Pole Star: Fixity Rotation and Movement </a></td>
<td> </td>
<td>156</td>
</tr>
<tr>
<td>1188</td>
<td>IJHS-46-2011-Issue-1</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_3_OPJaiswal.pdf'>Genesitic Roots and Philosophical Evolution of Vijnanavada (Yogacrya) School of Buddhism </a></td>
<td> OP Jaiswal</td>
<td>37</td>
</tr>
<tr>
<td>1189</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_4_VMishra.pdf'>Computation of N : A Modern Generalization of Ancient Technique </a></td>
<td> Vinod Mishra</td>
<td>69</td>
</tr>
<tr>
<td>1190</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_5_JBhattacharyya.pdf'>Arrival of western medicine:Ayurvedic knowledge of anatomy and colonial confrontation </a></td>
<td> Jayanta Bhattacharya</td>
<td>225</td>
</tr>
<tr>
<td>1191</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_6_AKBiswas.pdf'>Science in the Path of Syncretism </a></td>
<td> Arun Kumar Biswas</td>
<td>62</td>
</tr>
<tr>
<td>1192</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_7_SKMajumdar.pdf'>Historical Notes: Indian Renaissance: The Making of Modern India </a></td>
<td> Sisir K Majumdar</td>
<td>63</td>
</tr>
<tr>
<td>1193</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_8_SRSarma.pdf'>Historical Notes: Sudoku Yantra </a></td>
<td> Sreeramula Rajeswara Sarma</td>
<td>166</td>
</tr>
<tr>
<td>1194</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_9_Bookreview.pdf'>Book Review: C K Raju; Cultural Foundations of Mathematics: The Nature of Mathematical Proof and the Transmission of the Calculus from India to Europe in the 16th c AD </a></td>
<td> Probir K Bondyopadhyay</td>
<td>26</td>
</tr>
<tr>
<td>1195</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_10_Project reportAKSeth.pdf'>Project Reports: A Historical Study of Epilepsy from 1900-2005 AD </a></td>
<td> Arun Kumar Sethi</td>
<td>23</td>
</tr>
<tr>
<td>1196</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_11_Project reportSSen.pdf'>Project Reports: 1960-1999: Four Decades of Biochemistry in India </a></td>
<td> Srabani Sen</td>
<td>25</td>
</tr>
<tr>
<td>1197</td>
<td>IJHS-46-2011-Issue-1</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_12_News.pdf'>News </a></td>
<td> </td>
<td>21</td>
</tr>
<tr>
<td>1198</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_14_Supplement.pdf'>Supplement: Kuttakarauiromani of Devaraja-Sankrit Text with Eng Notes and Appendices </a></td>
<td> Takao Hayashi</td>
<td>93</td>
</tr>
<tr>
<td>1199</td>
<td>IJHS-46-2011-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_1_15_Supplement.pdf'>Supplement: Madhyamanayanaprakarah: An Unknown Manuscript ascribed to Madhava with Eng tr and Notes </a></td>
<td> UKV Sarma; Venketeswara Pai et al</td>
<td>702</td>
</tr>
<tr>
<td>1200</td>
<td>IJHS-46-2011-Issue-2</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>10</td>
</tr>
<tr>
<td>1201</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Math</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_1_KJaouiche.pdf'>India's Contribution to Arab Mathematics </a></td>
<td> Khalil Jaouiche</td>
<td>98</td>
</tr>
<tr>
<td>1202</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_2_AKeller.pdf'>George Peacock's Arithmetic in the Changing Landscape of the History of Mathematics in India </a></td>
<td> Agathe Keller</td>
<td>89</td>
</tr>
<tr>
<td>1203</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_3_DRaina.pdf'>Situating the History of Indian Arithmetical Knowledge in George Peacock's Arithmetic </a></td>
<td> Dhruv Raina</td>
<td>49</td>
</tr>
<tr>
<td>1204</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_4_1_MJDurandRichard.pdf'>Peacock's Arithmetic: An Attempt to Reconcile Empiricism to Universality </a></td>
<td> Marie-Jose Durand-Richard</td>
<td>103</td>
</tr>
<tr>
<td>1205</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_7_SKMajumdar.pdf'>Historical Notes: Rabindranath's Thoughts on Science : An Overview (A Tribute in 313 his 150th Birth Anniversary) </a></td>
<td> Sisir K Majumdar</td>
<td>90</td>
</tr>
<tr>
<td>1206</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_8_BShailaja.pdf'>Inscriptions as Records of Celestial Events </a></td>
<td> B S Shylaja and Geetha Kydala</td>
<td>33</td>
</tr>
<tr>
<td>1207</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_9_Bookreview.pdf'>Book Review: Kim Plofker: Mathematics in India </a></td>
<td> A K Bag</td>
<td>39</td>
</tr>
<tr>
<td>1208</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_10_AKThakur.pdf'>Project Reports: Tribal Technology of Northeast India: Arunachal Pradesh </a></td>
<td> Amrendra Kumar Thakur</td>
<td>27</td>
</tr>
<tr>
<td>1209</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_11_SuktaDas.pdf'>Evolution of Three Premier Cancer Institutes of India - TMC, CNCI and CIWIA - An Assessment </a></td>
<td> Sukta Das</td>
<td>24</td>
</tr>
<tr>
<td>1210</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_12_NewsSRSarma.pdf'>News: Magic Square for 2011 </a></td>
<td> S R Sarma</td>
<td>30</td>
</tr>
<tr>
<td>1211</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_13_NewsKnudsen.pdf'>News: Conference on: Otto Neugebauer, A Mathematician's Journey Between History and Practice of the Exact Sciences-A Report </a></td>
<td> Toke L Knudsen</td>
<td>15</td>
</tr>
<tr>
<td>1212</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_14_NewsShukla.pdf'>VIIth Investigators' Meet on History of Science Projects, New Delhi - A Report </a></td>
<td> Shabnam Shukla</td>
<td>18</td>
</tr>
<tr>
<td>1213</td>
<td>IJHS-46-2011-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_15_Supplement.pdf'>Kuttakarauiromani of Devaraja - Sankrit Text with Eng tr, Notes and Appendices </a></td>
<td> Takao Hayashi</td>
<td>44</td>
</tr>
<tr>
<td>1214</td>
<td>IJHS-46-2011-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>1215</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_1_ANarayanan.pdf'>The Manda Puzzle in Indian Astronomy </a></td>
<td> Anil Narayanan</td>
<td>768</td>
</tr>
<tr>
<td>1216</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_1_BPrakash.pdf'>Ancient Indian Iron and Steel: An Archaeometallurgical Study </a></td>
<td> B Prakash</td>
<td>2010</td>
</tr>
<tr>
<td>1217</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_2_ANarayanan.pdf'>The Pulsating Indian Epicycle of the Sun </a></td>
<td> Anil Narayanan</td>
<td>454</td>
</tr>
<tr>
<td>1218</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_2_SSen.pdf'>Indian Cholera: A Myth </a></td>
<td> Srabani Sen</td>
<td>1356</td>
</tr>
<tr>
<td>1219</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_3_AKBiswas.pdf'>The Era of Science Enthusiasts in Bengal (1841-1891): Akshayakumar's; Vidyasagar and Rajendralala </a></td>
<td> Arun Kumar Biswas</td>
<td>176</td>
</tr>
<tr>
<td>1220</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_3_AKBiswas.pdf'>SRammohun Roy, His Intellectual Compatriots and their Scientific Contributions </a></td>
<td> Arun Kumar Biswas</td>
<td>148</td>
</tr>
<tr>
<td>1221</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_4_SNBiswas.pdf'>RG Chandra: A Self-taught Sky Watcher and his Contributions to Observational Astronomy </a></td>
<td> Sudhindra Nath Biswas, Utpal Mukhopadhyay and Saibal Ray</td>
<td>1128</td>
</tr>
<tr>
<td>1222</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_4(1)_PKBandyopadhyay.pdf'>The Violin and the Genesis of the Bose Institute in Calcutta </a></td>
<td> Probir K Bondyopadhyay and Lily Banerjee</td>
<td>3404</td>
</tr>
<tr>
<td>1223</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_5_RCGupta.pdf'>Historical Notes: Kali Chronograms of Narayana Bhattatiri (15th - 17th Centuries AD) </a></td>
<td> R C Gupta</td>
<td>38</td>
</tr>
<tr>
<td>1224</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_6_SKMajumdar.pdf'>Historical Notes: Acharya Prafulla Chandra Ray: A Scientist, Teacher, Author and a Patriotic Entrepreneur </a></td>
<td> Sisir K Majumdar</td>
<td>35</td>
</tr>
<tr>
<td>1225</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_5_AKBag.pdf'>Mathematics and Mathematical Researches in India during Fifth to Twentieth Centuries: Profiles and Prospects </a></td>
<td> AK Bag</td>
<td>143</td>
</tr>
<tr>
<td>1226</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_6_RNIyengar.pdf'>Historical Notes: Archaeo-Astronomical Significance of the Vedic Darsapaurnamasa Altar </a></td>
<td> R N Iyengar and V H Satheeshkumar</td>
<td>536</td>
</tr>
<tr>
<td>1227</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_7_Bookreview.pdf'>Book Review: Harkishan Singh: Pharmaceutical History of India </a></td>
<td> B N Dhawan</td>
<td>17</td>
</tr>
<tr>
<td>1228</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_8_SVSingh.pdf'>Project Report: A Study of Devaraja's Kuttakarasiromani </a></td>
<td> Saroj V Singh</td>
<td>48</td>
</tr>
<tr>
<td>1229</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_7_UBTewari.pdf'>Historical Notes: Professor Ganesh Prasad: An Epitome of Teaching and Research in Modern Mathematics in India </a></td>
<td> U B Tewari</td>
<td>55</td>
</tr>
<tr>
<td>1230</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_8_Bookreview.pdf'>Book Review </a></td>
<td> B N Dhawan</td>
<td>20</td>
</tr>
<tr>
<td>1231</td>
<td>IJHS-46-2011-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_2_9_Bookreview.pdf'>Project Report: History of Technical Education in India: 1900-2005 </a></td>
<td> Vol46_3_9_SSaha.pdf</td>
<td>39</td>
</tr>
<tr>
<td>1232</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_10_News.pdf'>News: Maritime Cultures and Traditions of Bay of Bengal </a></td>
<td> Shabnam Shukla</td>
<td>17</td>
</tr>
<tr>
<td>1233</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_9_Projectreports.pdf'>Project Reports: Stone Inscriptions as Records of Celestial Events </a></td>
<td> B S Shylaja and Geetha Kaidala</td>
<td>46</td>
</tr>
<tr>
<td>1234</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_10_ASBhat.pdf'>Project Reports: The Siddhanta Sekhara of Sripati (11th Century) - Text and English Translation </a></td>
<td> A Sripada Bhat</td>
<td>30</td>
</tr>
<tr>
<td>1235</td>
<td>IJHS-46-2011-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_11_Supplement.pdf'>Supplement: Kuttakarasiromani of Devaraja - Sanskrit Text with Eng tr, Notes and Appendices </a></td>
<td> Takao Hayashi</td>
<td>47</td>
</tr>
<tr>
<td>1236</td>
<td>IJHS-46-2011-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_3_12_Supplement.pdf'>Supplement: Translation of Verses with Notes </a></td>
<td> </td>
<td>260</td>
</tr>
<tr>
<td>1237</td>
<td>IJHS-46-2011-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_11_Announcements.pdf'>Announcements </a></td>
<td> </td>
<td>16</td>
</tr>
<tr>
<td>1238</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>12</td>
</tr>
<tr>
<td>1239</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_1_TRSPrasanna.pdf'>Ancient Indian Astronomy and the Aryan Invasion Theory </a></td>
<td> T R S Prasanna</td>
<td>475</td>
</tr>
<tr>
<td>1240</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_2_BVenkateswarlu.pdf'>Health Aspects in Pancatantra </a></td>
<td> Bandi Venkateshwarlu and Ala Narayana</td>
<td>117</td>
</tr>
<tr>
<td>1241</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_3_RCGupta.pdf'>Mahavira-Pheru Formula for Surface of a Sphere and some other Empirical Rules </a></td>
<td> R C Gupta</td>
<td>167</td>
</tr>
<tr>
<td>1242</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_4_SKMajumdar.pdf'>Historical Notes: Kadambini Ganguli (1861-1923): First Lady Medical Graduate in India </a></td>
<td> Sisir K Majumdar</td>
<td>92</td>
</tr>
<tr>
<td>1243</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_5_Purabi.pdf'>Historical Notes: Trend of Geometrical Researches in Calcutta University: 1881-1931 </a></td>
<td> Purabi Mukherji and Mala Bhattacharjee</td>
<td>32</td>
</tr>
<tr>
<td>1244</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_6_Bookreview.pdf'>Book Review: Jagdish N Sinha: Science, War and Imperialism: India in the Second World War </a></td>
<td> Mahendra Prasad Singh</td>
<td>18</td>
</tr>
<tr>
<td>1245</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_7_VJDeshpande.pdf'>Project Report: Evolution of Ayurvedic Ophthalmology in Ancient and Medieval India: A Critical Study </a></td>
<td> Vijaya Jayant Deshpande</td>
<td>33</td>
</tr>
<tr>
<td>1246</td>
<td>IJHS-46-2011-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_8_PPDeshpande.pdf'>Project Report: Catalogue of Forge welded iron Cannons in Western Maharashtra </a></td>
<td> P P Deshpande, Sachin Joshi and Shivendra Kadgaonkar</td>
<td>427</td>
</tr>
<tr>
<td>1247</td>
<td>IJHS-46-2011-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_9_News.pdf'>News </a></td>
<td> </td>
<td>52</td>
</tr>
<tr>
<td>1248</td>
<td>IJHS-46-2011-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_10_Supplement.pdf'>Supplement: Kuttakarasiromani of Devaraja-Sanskrit Text with Eng. tr, Notes and Appendices </a></td>
<td> Takao Hayashi</td>
<td>47</td>
</tr>
<tr>
<td>1249</td>
<td>IJHS-46-2011-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_12_Cumulativeindex.pdf'>Cumulative Index </a></td>
<td> </td>
<td>28</td>
</tr>
<tr>
<td>1250</td>
<td>IJHS-46-2011-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol46_4_13_Annualcontent.pdf'>Annual Contents </a></td>
<td> </td>
<td>19</td>
</tr>
<tr>
<td>1251</td>
<td>IJHS-47-2012-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>13</td>
</tr>
<tr>
<td>1252</td>
<td>IJHS-47-2012-Issue-1</td>
<td>Biology</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_1_LDi.pdf'>Ancient Chinese People's Knowledge of Macrofungi during the Period from 220 AD to 589 AD </a></td>
<td> Lu Di</td>
<td>2223</td>
</tr>
<tr>
<td>1253</td>
<td>IJHS-47-2012-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_2_DVDwivedi.pdf'>Bilva in Indian Tradition </a></td>
<td> Dhananjay Vasudeo Dwivedi</td>
<td>107</td>
</tr>
<tr>
<td>1254</td>
<td>IJHS-47-2012-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_3_SRSarma.pdf'>The Gurmukhi Astrolabe of the Maharaja of Patiala </a></td>
<td> Sreeramula Rajeswara Sarma</td>
<td>2045</td>
</tr>
<tr>
<td>1255</td>
<td>IJHS-47-2012-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_4_JNSinha.pdf'>Role of Scientists in Colonial Bengal </a></td>
<td> Jagdish N Sinha</td>
<td>36</td>
</tr>
<tr>
<td>1256</td>
<td>IJHS-47-2012-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_5_SKMajumdar.pdf'>Historical Notes: Swami Vivekananda's Thoughts on Science and Religion </a></td>
<td> Sisir K Majumdar</td>
<td>14</td>
</tr>
<tr>
<td>1257</td>
<td>IJHS-47-2012-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_6_SKSaha.pdf'>Historical Notes: Commissions and Committees on Technical Education in Independent India: An Appraisal </a></td>
<td> Samir Kumar Saha and Sangita Ghosh</td>
<td>68</td>
</tr>
<tr>
<td>1258</td>
<td>IJHS-47-2012-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_7_Bookreview.pdf'>Book Review </a></td>
<td> </td>
<td>21</td>
</tr>
<tr>
<td>1259</td>
<td>IJHS-47-2012-Issue-1</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_8_KRoy.pdf'>Project Reports: History of the Ordnance Establishments of British India: 1700-1947 </a></td>
<td> Kaushik Roy</td>
<td>31</td>
</tr>
<tr>
<td>1260</td>
<td>IJHS-47-2012-Issue-1</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_9_PKChattopadhyay.pdf'>Project Reports: Documentation of Cannons of Eastern India </a></td>
<td> Pranab K Chattopadhyay</td>
<td>529</td>
</tr>
<tr>
<td>1261</td>
<td>IJHS-47-2012-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_10_News.pdf'>News </a></td>
<td> </td>
<td>60</td>
</tr>
<tr>
<td>1262</td>
<td>IJHS-47-2012-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_12_Supplement_cover.pdf'>Supplement </a></td>
<td> </td>
<td>64</td>
</tr>
<tr>
<td>1263</td>
<td>IJHS-47-2012-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_1_14_Announcement.pdf'>Announcement </a></td>
<td> </td>
<td>14</td>
</tr>
<tr>
<td>1264</td>
<td>IJHS-47-2012-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>14</td>
</tr>
<tr>
<td>1265</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_1_Sdas.pdf'>Prevention of Cancer: Evolution of Concepts and Strategies </a></td>
<td> Sukta Das</td>
<td>50</td>
</tr>
<tr>
<td>1266</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_2_NKodlady.pdf'>Utilization of Borax In The PharmaceuticoTherapeutics of Ayurveda in India </a></td>
<td> Naveena Kodlady and B J Patgiri</td>
<td>114</td>
</tr>
<tr>
<td>1267</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_3_ASamanta.pdf'>Smallpox in Nineteenth Century Bengal </a></td>
<td> Arabinda Samanta</td>
<td>103</td>
</tr>
<tr>
<td>1268</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_4_VMRavikumar.pdf'>Colonialism and Green Science: History of Colonial Scientific Forestry in South India 1820-1920 </a></td>
<td> V M Ravi Kumar</td>
<td>48</td>
</tr>
<tr>
<td>1269</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_5_JDeloche.pdf'>Silting and Ancient Sea-Ports of the Tamil Country </a></td>
<td> Jean Deloche</td>
<td>193</td>
</tr>
<tr>
<td>1270</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_6_BSShylaja.pdf'>Historical Notes: Asymmetrical Vedis In Sulbasutras </a></td>
<td> B S Shylaja</td>
<td>173</td>
</tr>
<tr>
<td>1271</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_7_VRRaghvan.pdf'>Historical Notes: Patient-Centered Therapy of Ayurveda: Approaches and Applications </a></td>
<td> Vaidyaratnam R Raghavan</td>
<td>32</td>
</tr>
<tr>
<td>1272</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_8_SKMajumdar.pdf'>Historical Notes: International Chemistry Year: Centenary of Marie Curie's Second Nobel Laurel 1911 </a></td>
<td> Sisir K Majumdar</td>
<td>16</td>
</tr>
<tr>
<td>1273</td>
<td>IJHS-47-2012-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_9_Bookreview.pdf'>Book Review </a></td>
<td> Anil Narayanan</td>
<td>33</td>
</tr>
<tr>
<td>1274</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_10_AKBiswas.pdf'>Project Reports: Calcuttan Science 1784-1930 and the Awakening in India </a></td>
<td> Arun Kumar Biswas</td>
<td>26</td>
</tr>
<tr>
<td>1275</td>
<td>IJHS-47-2012-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_11_CPalit.pdf'>Project Reports: Science and Nationalism In Bengal 1876-1947: Asutosh Mookerjee and Mathematics </a></td>
<td> Chittabrata Palit</td>
<td>22</td>
</tr>
<tr>
<td>1276</td>
<td>IJHS-47-2012-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_2_12_News.pdf'>News </a></td>
<td> </td>
<td>29</td>
</tr>
<tr>
<td>1277</td>
<td>IJHS-47-2012-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>1278</td>
<td>IJHS-47-2012-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_1_ANarayanan.pdf'>The Manda Puzzle in Indian Astronomy </a></td>
<td> Anil Narayanan</td>
<td>768</td>
</tr>
<tr>
<td>1279</td>
<td>IJHS-47-2012-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_2_SSen.pdf'>Indian Cholera: A Myth </a></td>
<td> Srabani Sen</td>
<td>1356</td>
</tr>
<tr>
<td>1280</td>
<td>IJHS-47-2012-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_3_AKBiswas.pdf'>The Era of Science Enthusiasts in Bengal (1841-1891): Akshayakumar's; Vidyasagar and Rajendralala </a></td>
<td> Arun Kumar Biswas</td>
<td>176</td>
</tr>
<tr>
<td>1281</td>
<td>IJHS-47-2012-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_4_PKBandyopadhyay.pdf'>The Violin and the Genesis of the Bose Institute in Calcutta </a></td>
<td> Probir K Bondyopadhyay and Lily Banerjee</td>
<td>8639</td>
</tr>
<tr>
<td>1282</td>
<td>IJHS-47-2012-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_5_AKBag.pdf'>Mathematics and Mathematical Researches in India during Fifth to Twentieth Centuries: Profiles and Prospects </a></td>
<td> AK Bag</td>
<td>143</td>
</tr>
<tr>
<td>1283</td>
<td>IJHS-47-2012-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_6_RNIyengar.pdf'>Historical Notes: Archaeo-Astronomical Significance of the Vedic Darsapaurnamasa Altar </a></td>
<td> R N Iyengar and V H Satheeshkumar</td>
<td>536</td>
</tr>
<tr>
<td>1284</td>
<td>IJHS-47-2012-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_7_UBTewari.pdf'>Historical Notes: Professor Ganesh Prasad: An Epitome of Teaching and Research in Modern Mathematics in India </a></td>
<td> U B Tewari</td>
<td>55</td>
</tr>
<tr>
<td>1285</td>
<td>IJHS-47-2012-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_8_Bookreview.pdf'>Book Review </a></td>
<td> B N Dhawan</td>
<td>20</td>
</tr>
<tr>
<td>1286</td>
<td>IJHS-47-2012-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_9_Projectreports.pdf'>Project Reports: Stone Inscriptions as Records of Celestial Events </a></td>
<td> B S Shylaja and Geetha Kaidala</td>
<td>46</td>
</tr>
<tr>
<td>1287</td>
<td>IJHS-47-2012-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_10_ASBhat.pdf'>Project Reports: The Siddhanta Sekhara of Sripati (11th Century) - Text and English Translation </a></td>
<td> A Sripada Bhat</td>
<td>30</td>
</tr>
<tr>
<td>1288</td>
<td>IJHS-47-2012-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_3_11_Announcements.pdf'>Announcements </a></td>
<td> </td>
<td>16</td>
</tr>
<tr>
<td>1289</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_0_Editorial.pdf'>Editorial </a></td>
<td> </td>
<td>17</td>
</tr>
<tr>
<td>1290</td>
<td>IJHS-47-2012-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_1_Contents.pdf'>Contents </a></td>
<td> </td>
<td>11</td>
</tr>
<tr>
<td>1291</td>
<td>IJHS-47-2012-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_2_PRamManohar.pdf'>Accounts of Pathogenic Organisms in the Early Texts of Ayurveda </a></td>
<td> P Ram Manohar</td>
<td>247</td>
</tr>
<tr>
<td>1292</td>
<td>IJHS-47-2012-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_3_DPKaundinya.pdf'>Significance of Asakrt-Karma in Finding Manda-Karna </a></td>
<td> Deepak P Kaundinya's;K Ramasubramanian and M S Sriram</td>
<td>382</td>
</tr>
<tr>
<td>1293</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_4_RSridhan.pdf'>Folding Method of Narayana Pandita for the Construction of Samagarbha and Visama Magic Squares </a></td>
<td> Raja Sridharan and M D Srinivas</td>
<td>1002</td>
</tr>
<tr>
<td>1294</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_5_RSridhan.pdf'>Narayana Pandita's Enumeration of Combinations and Associated Representation of Numbers as Sums of Binomial Coefficients </a></td>
<td> Raja Sridharan's;R Sridharan and M D Srinivas</td>
<td>414</td>
</tr>
<tr>
<td>1295</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_6_ADutta.pdf'>Narayana's Treatment of Varga-Prakrti </a></td>
<td> Amartya Kumar Dutta</td>
<td>404</td>
</tr>
<tr>
<td>1296</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_7_AKBag.pdf'>Madhava- A Great Kerala Mathematician of Medieval Times </a></td>
<td> A K BAG</td>
<td>113</td>
</tr>
<tr>
<td>1297</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_8_SMadhavan.pdf'>Venvaroha from a Modern Perspective </a></td>
<td> S Madhavan</td>
<td>215</td>
</tr>
<tr>
<td>1298</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_9_MSSriram.pdf'>Relation between the Arc and the Rsine in Tantrasangraha and other Kerala Works </a></td>
<td> M S Sriram's;K Ramasubramanian and R Venketeswara Pai</td>
<td>312</td>
</tr>
<tr>
<td>1299</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_10_Malaya.pdf'>Sines and Interpolation in India </a></td>
<td> V Madhukar Mallayya</td>
<td>963</td>
</tr>
<tr>
<td>1300</td>
<td>IJHS-47-2012-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_11_PPDivakaran.pdf'>Birth of Calculus with Special Reference to Yuktibhasa </a></td>
<td> PP Divakaran</td>
<td>422</td>
</tr>
<tr>
<td>1301</td>
<td>IJHS-47-2012-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_12_Booksreceived.pdf'>Books Received </a></td>
<td> </td>
<td>17</td>
</tr>
<tr>
<td>1302</td>
<td>IJHS-47-2012-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_13_Cumulativeindex.pdf'>Cumulative Index </a></td>
<td> </td>
<td>35</td>
</tr>
<tr>
<td>1303</td>
<td>IJHS-47-2012-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol47_4_14_Annualcontent.pdf'>Annual Contents </a></td>
<td> </td>
<td>24</td>
</tr>
<tr>
<td>1304</td>
<td>IJHS-48-2013-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>1305</td>
<td>IJHS-48-2013-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_1_PTCraddock.pdf'>Two Millennia of the Sea-bourne metals trade with India </a></td>
<td> Paul T. Craddock</td>
<td>1053</td>
</tr>
<tr>
<td>1306</td>
<td>IJHS-48-2013-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_2_JBhattacharya.pdf'>Travel Accounts and the Eighteenth Century: Indian Medicine and Surgery through travelling gaze </a></td>
<td> Jayanta Bhattacharya</td>
<td>58</td>
</tr>
<tr>
<td>1307</td>
<td>IJHS-48-2013-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_3_AKBiswas.pdf'>Raman Krishnan and the IACS Episodes of the 1930's </a></td>
<td> Arun Kumar Biswas</td>
<td>231</td>
</tr>
<tr>
<td>1308</td>
<td>IJHS-48-2013-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_4_Rsingh.pdf'>Belated Nobel Prize for Max Born FRS </a></td>
<td> Rajinder Singh and Falk Riess</td>
<td>68</td>
</tr>
<tr>
<td>1309</td>
<td>IJHS-48-2013-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_5_Ssar.pdf'>Historical Notes: A Glimpse of Some Results of Ramanujan </a></td>
<td> Satyabachi Sar</td>
<td>43</td>
</tr>
<tr>
<td>1310</td>
<td>IJHS-48-2013-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_6_Pchakrabarti.pdf'>Har Gobind Khorana (1922-2011)-  A Pioneer Nobel Laureate in Molecular Biology </a></td>
<td> Parul Chakarbarti</td>
<td>20</td>
</tr>
<tr>
<td>1311</td>
<td>IJHS-48-2013-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_7_Bookreview.pdf'>Book Review </a></td>
<td> Madhvendra Narayan</td>
<td>23</td>
</tr>
<tr>
<td>1312</td>
<td>IJHS-48-2013-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_8_APPandey.pdf'>Project Reports: Indigenous Techniques of Weaving in Silk Industries: A Study in the context of Eastern Uttar Pradesh </a></td>
<td> Adya Prasad Pandey</td>
<td>20</td>
</tr>
<tr>
<td>1313</td>
<td>IJHS-48-2013-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_9_Msarkar.pdf'>Project Reports: Indigenous Knowledge System of the Fishermen of Sunderbans  in West Bengal and their Approaches to Health Sanitation and Climate </a></td>
<td> Mahua Sarkar</td>
<td>32</td>
</tr>
<tr>
<td>1314</td>
<td>IJHS-48-2013-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_10_News.pdf'>News </a></td>
<td> </td>
<td>22</td>
</tr>
<tr>
<td>1315</td>
<td>IJHS-48-2013-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_12_Supplement.pdf'>Supplement </a></td>
<td> Takao Hayashi</td>
<td>278</td>
</tr>
<tr>
<td>1316</td>
<td>IJHS-48-2013-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_1_13_Form IV.pdf'>Form IV </a></td>
<td> </td>
<td>10</td>
</tr>
<tr>
<td>1317</td>
<td>IJHS-48-2013-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>1318</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_1_NCShah.pdf'>Sesamum indicum (Sesame or Til): Seeds and oil - An Historical and Scientific evaluation from Indian perspective </a></td>
<td> N C Shah</td>
<td>749</td>
</tr>
<tr>
<td>1319</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_2_VDeshpande.pdf'>Ophthalmic Ideas in Ancient India </a></td>
<td> Vijaya J Deshpande</td>
<td>184</td>
</tr>
<tr>
<td>1320</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_3_JDeloche.pdf'>Water Supply Systems of the Senji (Gingee) Fort in South India(16-18th century) </a></td>
<td> Jean Deloche</td>
<td>2014</td>
</tr>
<tr>
<td>1321</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_4_AKBiswas.pdf'>The Muslim Community response to the Scientific Awakening in the Nineteenth Century India </a></td>
<td> Arun Kumar Biswas</td>
<td>64</td>
</tr>
<tr>
<td>1322</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Chemistry</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_5_JWisniak.pdf'>Chemistry of Resinous gums, Dyes, Alkaloids, and Active principles - Contributions of Pelletier and others in the Nineteenth Century </a></td>
<td> Jaime Wisniak</td>
<td>134</td>
</tr>
<tr>
<td>1323</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_6_BSShylaja.pdf'>Historical Notes: Daksinagni in Sulbasutras - An Astronomical Interpretation </a></td>
<td> B S Shylaja</td>
<td>86</td>
</tr>
<tr>
<td>1324</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_7_KBBasant.pdf'>Historical Notes: Summation of Convergent Geometric Series and the Concept of approachable Sunya </a></td>
<td> K B Basant and Satyananda Panda</td>
<td>668</td>
</tr>
<tr>
<td>1325</td>
<td>IJHS-48-2013-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_8_Correspondence.pdf'>Correspondences </a></td>
<td> Correspondences</td>
<td>19</td>
</tr>
<tr>
<td>1326</td>
<td>IJHS-48-2013-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_9_BookReview.pdf'>Book Review </a></td>
<td> Arun Kumar Biswas</td>
<td>18</td>
</tr>
<tr>
<td>1327</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_10_VTripathi.pdf'>"Project Reports: An Ethno-technological Study of Iron Working around Sonbhadra region" </a></td>
<td> Vibha Tripathi and Prabhakar Upadhyay</td>
<td>95</td>
</tr>
<tr>
<td>1328</td>
<td>IJHS-48-2013-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_11_MBhattacharjee.pdf'>Project Reports: Pioneer Mathematicians and their role in Calcutta University during the Nineteenth and Twentieth Century </a></td>
<td> Mala Bhattacharjee, Purabi Mukherji and Nandita Mallik</td>
<td>34</td>
</tr>
<tr>
<td>1329</td>
<td>IJHS-48-2013-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_12_News.pdf'>NEWS </a></td>
<td> </td>
<td>25</td>
</tr>
<tr>
<td>1330</td>
<td>IJHS-48-2013-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_2_13_Supplement_inner.pdf'>Supplement </a></td>
<td> Takao Hayashi</td>
<td>60</td>
</tr>
<tr>
<td>1331</td>
<td>IJHS-48-2013-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>19</td>
</tr>
<tr>
<td>1332</td>
<td>IJHS-48-2013-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_1_ANarayanan.pdf'>The Lunar Model in Ancient Indian Astronomy </a></td>
<td> Anil Narayanan</td>
<td>1467</td>
</tr>
<tr>
<td>1333</td>
<td>IJHS-48-2013-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_2_CYJagtap.pdf'>Purification and Detoxification procedures for metal Tamra in Medieval Indian Medicine </a></td>
<td> C Y Jagtap, B J Patgiri and P K Prajapati</td>
<td>96</td>
</tr>
<tr>
<td>1334</td>
<td>IJHS-48-2013-Issue-3</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_3_RCKapoor.pdf'>Did Ibn Sina observe the transit of Venus 1032 AD? </a></td>
<td> R C Kapoor</td>
<td>306</td>
</tr>
<tr>
<td>1335</td>
<td>IJHS-48-2013-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_4_SSarkar.pdf'>Bengali Entrepreneurs and Western Technology in the nineteenth century: A Social Perspective </a></td>
<td> Suvobrata Sarkar</td>
<td>2543</td>
</tr>
<tr>
<td>1336</td>
<td>IJHS-48-2013-Issue-3</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_5_CPalit.pdf'>Historical notes: Symbiotic relation between Geology and Botany- Pramatha Nath Bose and Girish Chandra Bose </a></td>
<td> Chittabrata Palit</td>
<td>25</td>
</tr>
<tr>
<td>1337</td>
<td>IJHS-48-2013-Issue-3</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_6_SKMajumdar.pdf'>History and Philosophy of Quantum Physics : An Overview </a></td>
<td> Sisir K Majumdar</td>
<td>26</td>
</tr>
<tr>
<td>1338</td>
<td>IJHS-48-2013-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_7_Correspondence.pdf'>Correspondence </a></td>
<td> </td>
<td>11</td>
</tr>
<tr>
<td>1339</td>
<td>IJHS-48-2013-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_8_Bookreview.pdf'>Book Reviews </a></td>
<td> </td>
<td>44</td>
</tr>
<tr>
<td>1340</td>
<td>IJHS-48-2013-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_9_Project Reports.pdf'>Project Reports: Brahmasiddhanta in Sakalyasamhita-Text, English Translation and Commentary </a></td>
<td> Somenath Chatterjee</td>
<td>47</td>
</tr>
<tr>
<td>1341</td>
<td>IJHS-48-2013-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_10_SSen.pdf'>Communicable Diseases and Germ Theory in Colonial India - An Assessment </a></td>
<td> Srabani Sen</td>
<td>47</td>
</tr>
<tr>
<td>1342</td>
<td>IJHS-48-2013-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_11_News.pdf'>NEWS </a></td>
<td> </td>
<td>134</td>
</tr>
<tr>
<td>1343</td>
<td>IJHS-48-2013-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_12_Supplement_cover.pdf'>Supplement:Ganitamanjari of Ganesa </a></td>
<td> Takao Hayashi</td>
<td>60</td>
</tr>
<tr>
<td>1344</td>
<td>IJHS-48-2013-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_3_13_Supplement_text.pdf'>Supplement: Ganitamanjari of Ganesa </a></td>
<td> Takao Hayashi</td>
<td>6452</td>
</tr>
<tr>
<td>1345</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_4_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>100</td>
</tr>
<tr>
<td>1346</td>
<td>IJHS-48-2013-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_4_1_BBaware.pdf'>Genesis and Early Evolution of Decimal Enumeration: Evidence from Number Names in Rigveda </a></td>
<td> Bhagyashree Bavare and P P Divakaran</td>
<td>284</td>
</tr>
<tr>
<td>1347</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_4_2_VNSharma.pdf'>Kapa-la Yantra at Sawai Jai Singh's Jaipur Observatory </a></td>
<td> Virendra N sharma</td>
<td>1157</td>
</tr>
<tr>
<td>1348</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_4_3_ AMSharan.pdf'>The Udayagiri Lion Pillar and its Astronomical Significance in Ancient India </a></td>
<td> Anand M Sharan</td>
<td>3232</td>
</tr>
<tr>
<td>1349</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_4_4_PMandal.pdf'>A Glimpse of the Garo Tangible Medicine: The Ruga-Garo Picture </a></td>
<td> Pratibha Mandal</td>
<td>788</td>
</tr>
<tr>
<td>1350</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_4_5_SuktaDas.pdf'>Prevention of Diabetes- A Historical Note </a></td>
<td> Sukta Das</td>
<td>148</td>
</tr>
<tr>
<td>1351</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol48_4_6_ RCGupta.pdf'>M Rangacharya and his Century Old Translation of the Ganita Sarasangraha </a></td>
<td> R C Gupta</td>
<td>151</td>
</tr>
<tr>
<td>1352</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol48_4_7_Correspondence.pdf'>Correspondence: The Lunar Model in Ancient Indian Astronomy </a></td>
<td> </td>
<td>98</td>
</tr>
<tr>
<td>1353</td>
<td>IJHS-48-2013-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol48_4_8_Book Review.pdf'>Book Review </a></td>
<td> </td>
<td>108</td>
</tr>
<tr>
<td>1354</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol48_4_9_Project Report_ Jbhattacharyya.pdf'>Indian Medicine through Travellers' Accounts, with emphasis on Anatomical Knowledge: 17-19th Century </a></td>
<td> Jayanta Bhattacharya</td>
<td>178</td>
</tr>
<tr>
<td>1355</td>
<td>IJHS-48-2013-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol48_4_10_ProjectReport_ BKSen.pdf'>Growth of Scientific Socities in India (1784-1947) </a></td>
<td> B K Sen</td>
<td>169</td>
</tr>
<tr>
<td>1356</td>
<td>IJHS-48-2013-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol48_4_11_ News.pdf'>News </a></td>
<td> S M Razaullah Ansari</td>
<td>155</td>
</tr>
<tr>
<td>1357</td>
<td>IJHS-48-2013-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol48_4_12_BookReceivedForReview.pdf'>Books received for Review in IJHS: 2013 </a></td>
<td> </td>
<td>107</td>
</tr>
<tr>
<td>1358</td>
<td>IJHS-48-2013-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol48_4_13_CumulativeIndex.pdf'>Cumulative Index : Vol. 48.1-4 (2013) </a></td>
<td> </td>
<td>124</td>
</tr>
<tr>
<td>1359</td>
<td>IJHS-48-2013-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in/(S(eh1ucortlbqqezipwgliy3mn))/writereaddata/UpLoadedFiles/IJHS/Vol48_4_14_AnnualContent.pdf'>Annual Contents: Vol. 48.1-4 (2013) </a></td>
<td> </td>
<td>117</td>
</tr>
<tr>
<td>1360</td>
<td>IJHS-49-2014-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_0_Contents.pdf'>Contents </a></td>
<td> Contents</td>
<td>101</td>
</tr>
<tr>
<td>1361</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_1_PKChattopadhyay.pdf'>Ho Tribes of Eastern India and their Metallurgical traditions </a></td>
<td> Pranab K Chattopadhayay and Ashok Purty</td>
<td>2960</td>
</tr>
<tr>
<td>1362</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_2_SNDhundi.pdf'>Critical review on Makaradhvaja- A Herbomineral Formulation </a></td>
<td> Shraddha N Dhundi & PK Prajapati</td>
<td>191</td>
</tr>
<tr>
<td>1363</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_3_Sdasgupta.pdf'>1803 Earthquake in Garhwal Himalaya-Archival materials with commentary </a></td>
<td> Sujit Dasgupta and Basab Mukhopadhyay</td>
<td>1057</td>
</tr>
<tr>
<td>1364</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_4_SKJain.pdf'>India's notable presence in Linnaeus' Botanical Classification </a></td>
<td> S K Jain and Harsh Singh</td>
<td>135</td>
</tr>
<tr>
<td>1365</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_5_Kmishra.pdf'>The medical maladies of Sir George Everest during the Great Trigonometric Survey of India </a></td>
<td> Shrikant Mishra and Bhavesh Trikamji</td>
<td>127</td>
</tr>
<tr>
<td>1366</td>
<td>IJHS-49-2014-Issue-1</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_6_Sbhowmik.pdf'>HISTORICAL NOTES- A glimpse of rule of logic in Gautama's Nyaya-Sutra </a></td>
<td> Subrata Bhowmik</td>
<td>118</td>
</tr>
<tr>
<td>1367</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_7_SKMajumdar.pdf'>Inquisitiveness for Science in Tagore Poems </a></td>
<td> Sisir K Majumdar</td>
<td>122</td>
</tr>
<tr>
<td>1368</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_8_JJShah.pdf'>Botanist Jaykrishnabhai: 1849-1929 </a></td>
<td> J J Shah</td>
<td>106</td>
</tr>
<tr>
<td>1369</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_9_Pmukherji.pdf'>Bengal School of Fluid Mechanics: Nineteenth and Twentieth Century </a></td>
<td> Purabi Mukherji and Mala Bhattacharjee</td>
<td>141</td>
</tr>
<tr>
<td>1370</td>
<td>IJHS-49-2014-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_10_Book Review.pdf'>Book Review </a></td>
<td> Book Review</td>
<td>137</td>
</tr>
<tr>
<td>1371</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_11_SKGeorge.pdf'>PROJECT REPORTS- English translation of Jyotsnika: An Ayurvedic text on Vi?avidya </a></td>
<td> Senu Kurien George</td>
<td>308</td>
</tr>
<tr>
<td>1372</td>
<td>IJHS-49-2014-Issue-1</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_12_Sbiswas.pdf'>Forestry Research in India (1861-2005): Historic Evolution with a Case Study </a></td>
<td> Subhasis Biswas</td>
<td>105</td>
</tr>
<tr>
<td>1373</td>
<td>IJHS-49-2014-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_1_13_News.pdf'>NEWS </a></td>
<td> NEWS</td>
<td>556</td>
</tr>
<tr>
<td>1374</td>
<td>IJHS-49-2014-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>22</td>
</tr>
<tr>
<td>1375</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_1_RN_Iyengar.pdf'>Parasara's Six Season Solar Zodiac and Heliacal Visibility of Star Agastya in 1350-1130 BC </a></td>
<td> R N Iyengar</td>
<td>641</td>
</tr>
<tr>
<td>1376</td>
<td>IJHS-49-2014-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_1_Editorial.pdf'>Editorial </a></td>
<td> </td>
<td>17</td>
</tr>
<tr>
<td>1377</td>
<td>IJHS-49-2014-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_2_GuestEditorial.pdf'>Guest Editorial </a></td>
<td> </td>
<td>21</td>
</tr>
<tr>
<td>1378</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_2_Dwivedi.pdf'>Plant Diseases and their Treatment in Sanskrit Literature </a></td>
<td> Dhananjay Vasudeo Dwivedi</td>
<td>79</td>
</tr>
<tr>
<td>1379</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_3_NHanda.pdf'>Methods of Interpolation in Indian Astronomy </a></td>
<td> Nidhi Handa and Padmavati Taneja</td>
<td>444</td>
</tr>
<tr>
<td>1380</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_3_KPlofker.pdf'>Sanskrit Astronomical Tables: The State of the Field </a></td>
<td> Kim Plofker</td>
<td>632</td>
</tr>
<tr>
<td>1381</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_4_AKeller.pdf'>Bhaskara I's Versified Solutions of a Linear Indeterminate Equation </a></td>
<td> Agathe Keller</td>
<td>331</td>
</tr>
<tr>
<td>1382</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_4_DJadhav.pdf'>Nemicandra's Rules for Computing Multiplier and Divisor </a></td>
<td> Dipak Jadhav</td>
<td>86</td>
</tr>
<tr>
<td>1383</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_5_Pustynski.pdf'>On Mathematical Complexity of Sriyantra </a></td>
<td> Vladislav-Veniamin Pustynski</td>
<td>790</td>
</tr>
<tr>
<td>1384</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_5_TKnudsen.pdf'>Versified Sine Tables in Jnanaraja's Siddhantasundara </a></td>
<td> Toke Knudsen</td>
<td>547</td>
</tr>
<tr>
<td>1385</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_6_VMallayya.pdf'>Trigonometric Tables in India </a></td>
<td> V Madhukar Mallayya</td>
<td>499</td>
</tr>
<tr>
<td>1386</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_6_NShah.pdf'>Techno-Scientific Education and the Indian National Congress (1885-1918) </a></td>
<td> Nirmala Shah</td>
<td>63</td>
</tr>
<tr>
<td>1387</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_7_DBhatacharya.pdf'>Historical Notes: Select Palm Leaf Manuscripts on Health Care </a></td>
<td> Deepak Bhattacharya</td>
<td>35</td>
</tr>
<tr>
<td>1388</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_7_KMahesh.pdf'>Sankramavakyas of the Vakyakarana </a></td>
<td> K Mahesh</td>
<td>355</td>
</tr>
<tr>
<td>1389</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_8_CMontelle.pdf'>The Karanakesari Tables for Computing Eclipse Phenomena </a></td>
<td> Clemency Montelle</td>
<td>2112</td>
</tr>
<tr>
<td>1390</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_8_RSridharan.pdf'>Historical Notes: Some Nineteenth Century Indian Mathematicians Prior to Ramanujan </a></td>
<td> R Sridharan</td>
<td>153</td>
</tr>
<tr>
<td>1391</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_9_SKMajumdar.pdf'>Historical Notes: Bankim Chandra-First Writer of Popular Science in Bengali </a></td>
<td> Sisir K Majumdar</td>
<td>41</td>
</tr>
<tr>
<td>1392</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_9_KRupa.pdf'>Makaranda Sarini and Allied Saurapakna Tables -A Study </a></td>
<td> K Rupa, Padmaja Venugopal and S Balachandra Rao</td>
<td>1068</td>
</tr>
<tr>
<td>1393</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_2_10_BookReview.pdf'>Book Review: R N Iyengar - Parasaratantra: Ancient Sanskrit Text on Astronomy and Natural Sciences </a></td>
<td> </td>
<td>76</td>
</tr>
<tr>
<td>1394</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_10_KBBasant.pdf'>Historical Notes: Some Applications of First Approachable Sunya and Derivation of other Approachable Sunyas </a></td>
<td> K B Basant and Satyananda Panda</td>
<td>1840</td>
</tr>
<tr>
<td>1395</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_11_RCGupta.pdf'>Book Review: Sita Sundar Ram-Bijapallava of Krsna Daivajna: Algebra in Sixteen Century India-A Critical Study </a></td>
<td> R C Gupta</td>
<td>51</td>
</tr>
<tr>
<td>1396</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_12_SNellickappilly.pdf'>Project Report: The Traditional Ayurveda Practicing by Parambarya Vaidyas in Kerala and their Unique Ethical Outlook </a></td>
<td> Sreekumar Nellickappilly</td>
<td>44</td>
</tr>
<tr>
<td>1397</td>
<td>IJHS-49-2014-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_13_PMandal.pdf'>Project Reports: The Garo Perception of Disease and Medicine: A History Since the British Regime in the Indian Sub-Continent </a></td>
<td> Pratibha Mandal</td>
<td>50</td>
</tr>
<tr>
<td>1398</td>
<td>IJHS-49-2014-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_14_NEWS.pdf'>NEWS </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>1399</td>
<td>IJHS-49-2014-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>22</td>
</tr>
<tr>
<td>1400</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_1_RN_Iyengar.pdf'>Parasara's Six Season Solar Zodiac and Heliacal Visibility of Star Agastya in 1350-1130 BC </a></td>
<td> R N Iyengar</td>
<td>641</td>
</tr>
<tr>
<td>1401</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_2_Dwivedi.pdf'>Plant Diseases and their Treatment in Sanskrit Literature </a></td>
<td> Dhananjay Vasudeo Dwivedi</td>
<td>79</td>
</tr>
<tr>
<td>1402</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_3_NHanda.pdf'>Methods of Interpolation in Indian Astronomy </a></td>
<td> Nidhi Handa and Padmavati Taneja</td>
<td>444</td>
</tr>
<tr>
<td>1403</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_4_DJadhav.pdf'>Nemicandra's Rules for Computing Multiplier and Divisor </a></td>
<td> Dipak Jadhav</td>
<td>86</td>
</tr>
<tr>
<td>1404</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_5_Pustynski.pdf'>On Mathematical Complexity of Sriyantra </a></td>
<td> Vladislav-Veniamin Pustynski</td>
<td>790</td>
</tr>
<tr>
<td>1405</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_6_NShah.pdf'>Techno-Scientific Education and the Indian National Congress (1885-1918) </a></td>
<td> Nirmala Shah</td>
<td>63</td>
</tr>
<tr>
<td>1406</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_7_DBhatacharya.pdf'>Historical Notes: Select Palm Leaf Manuscripts on Health Care </a></td>
<td> Deepak Bhattacharya</td>
<td>35</td>
</tr>
<tr>
<td>1407</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_8_RSridharan.pdf'>Historical Notes: Some Nineteenth Century Indian Mathematicians Prior to Ramanujan </a></td>
<td> R Sridharan</td>
<td>153</td>
</tr>
<tr>
<td>1408</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_9_SKMajumdar.pdf'>Historical Notes: Bankim Chandra-First Writer of Popular Science in Bengali </a></td>
<td> Sisir K Majumdar</td>
<td>41</td>
</tr>
<tr>
<td>1409</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_10_KBBasant.pdf'>Historical Notes: Some Applications of First Approachable Sunya and Derivation of other Approachable Sunyas </a></td>
<td> K B Basant and Satyananda Panda</td>
<td>1840</td>
</tr>
<tr>
<td>1410</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_11_RCGupta.pdf'>Book Review: Sita Sundar Ram-Bijapallava of Krsna Daivajna: Algebra in Sixteen Century India-A Critical Study </a></td>
<td> R C Gupta</td>
<td>51</td>
</tr>
<tr>
<td>1411</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_12_SNellickappilly.pdf'>Project Report: The Traditional Ayurveda Practicing by Parambarya Vaidyas in Kerala and their Unique Ethical Outlook </a></td>
<td> Sreekumar Nellickappilly</td>
<td>44</td>
</tr>
<tr>
<td>1412</td>
<td>IJHS-49-2014-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_13_PMandal.pdf'>Project Reports: The Garo Perception of Disease and Medicine: A History Since the British Regime in the Indian Sub-Continent </a></td>
<td> Pratibha Mandal</td>
<td>50</td>
</tr>
<tr>
<td>1413</td>
<td>IJHS-49-2014-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_3_14_NEWS.pdf'>NEWS </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>1414</td>
<td>IJHS-49-2014-issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_0_Contents.pdf'>Contents </a></td>
<td> </td>
<td>15</td>
</tr>
<tr>
<td>1415</td>
<td>IJHS-49-2014-issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_1_Editorial.pdf'>Editorial </a></td>
<td> </td>
<td>87</td>
</tr>
<tr>
<td>1416</td>
<td>IJHS-49-2014-issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_2_Guest_Editorial.pdf'>Guest Editorial </a></td>
<td> </td>
<td>78</td>
</tr>
<tr>
<td>1417</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_3_AChakravorty.pdf'>The Chemical Researches of Acharya Prafulla Chandra Ray </a></td>
<td> Animesh Chakravorty</td>
<td>254</td>
</tr>
<tr>
<td>1418</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_4_KBhattacharyya.pdf'>Early Research in Physical Chemistry in India </a></td>
<td> Kankan Bhattacharyya</td>
<td>52</td>
</tr>
<tr>
<td>1419</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_5_KNagarajan.pdf'>History of Natural Products Chemistry in India </a></td>
<td> K Nagarajan</td>
<td>596</td>
</tr>
<tr>
<td>1420</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_6_AVRRao.pdf'>Indian Organic Chemical Industry: Decades of Struggle & Achievements </a></td>
<td> K Nagarajan</td>
<td>576</td>
</tr>
<tr>
<td>1421</td>
<td>IJHS-49-2014-issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_7_HSingh.pdf'>Medicinal Chemistry Research in India </a></td>
<td> Harikishan Singh</td>
<td>415</td>
</tr>
<tr>
<td>1422</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_8_AKShukla.pdf'>A Short History of Electrochemistry in India </a></td>
<td> A K Shukla and T Prem Kumar</td>
<td>25</td>
</tr>
<tr>
<td>1423</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_9_MRoy.pdf'>Historical Notes: Manuscripts on Alchemy in India - Commentaries and Editions </a></td>
<td> Mira Roy</td>
<td>39</td>
</tr>
<tr>
<td>1424</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_10_BKSen.pdf'>Chemical Research in British India (1788-1900) </a></td>
<td> B K Sen</td>
<td>50</td>
</tr>
<tr>
<td>1425</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_11_DRaina.pdf'>The Making of a Classic: The Contemporary Significance of P. C. Ray's Historical Approach </a></td>
<td> Dhruv Raina</td>
<td>61</td>
</tr>
<tr>
<td>1426</td>
<td>IJHS-49-2014-issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_12_PKBasu.pdf'>Good Life, Self-Sufficiency and Chemical Knowledge: Through The Chemical Worls View of Late Jnan Chandra Ghosh </a></td>
<td> Prajit K Basu</td>
<td>53</td>
</tr>
<tr>
<td>1427</td>
<td>IJHS-49-2014-issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_13_Bookreview.pdf'>Book Reviews </a></td>
<td> </td>
<td>75</td>
</tr>
<tr>
<td>1428</td>
<td>IJHS-49-2014-issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_14_Bookreceived.pdf'>Books Received for Review </a></td>
<td> </td>
<td>17</td>
</tr>
<tr>
<td>1429</td>
<td>IJHS-49-2014-issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_15_CumulativeIndex.pdf'>Cumulative Index </a></td>
<td> </td>
<td>40</td>
</tr>
<tr>
<td>1430</td>
<td>IJHS-49-2014-issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol49_4_16_AnnualContents2014.pdf'>Annual Contents 2014 </a></td>
<td> </td>
<td>28</td>
</tr>
<tr>
<td>1431</td>
<td>IJHS-50-2015-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Contents.pdf'>Contents </a></td>
<td> </td>
<td>105</td>
</tr>
<tr>
<td>1432</td>
<td>IJHS-50-2015-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Message_President.pdf'>Massage  From: President INSA </a></td>
<td> Raghavendra Gadagkar</td>
<td>79</td>
</tr>
<tr>
<td>1433</td>
<td>IJHS-50-2015-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art01.pdf'>Editorial </a></td>
<td> D Balasubramanian, A K Bag</td>
<td>28</td>
</tr>
<tr>
<td>1434</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art02.pdf'>Early System of Naksatras, Calendar and Antiquity of the Vedic & Harappan Traditions </a></td>
<td> A K Bag</td>
<td>286</td>
</tr>
<tr>
<td>1435</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art03.pdf'>Soma, an Enigmatic, Mysterious Plant of the Vedic Aryas: An Appraisal </a></td>
<td> N C Shah</td>
<td>368</td>
</tr>
<tr>
<td>1436</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art04.pdf'>Crafts and Technologies of the Chalcolithic People of South Asia: An Overview </a></td>
<td> Vasant Shinde</td>
<td>52</td>
</tr>
<tr>
<td>1437</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art05.pdf'>The Metal Casting Traditions of South Asia: Continuity and Innovation </a></td>
<td> Paul T Craddock</td>
<td>900</td>
</tr>
<tr>
<td>1438</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art06.pdf'>Foundations of Immunology in Ayurvedic classics </a></td>
<td> Ram H Singh</td>
<td>104</td>
</tr>
<tr>
<td>1439</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art07.pdf'>From Persons to Hospital Cases: The Rise of Hospital Medicine and the Calcutta Medical College in India </a></td>
<td> Jayanta Bhattacharyra</td>
<td>899</td>
</tr>
<tr>
<td>1440</td>
<td>IJHS-50-2015-Issue-1</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art08.pdf'>Historical Note: Concept of Manas in Samkhya Darsana </a></td>
<td> Hetal Amin</td>
<td>65</td>
</tr>
<tr>
<td>1441</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art09.pdf'>Historical Note: Percetion of Food and Nutrition and Dietary Recommendation in Health and Disease: Focus on Caraka-Susruta Samhitas </a></td>
<td> Sukta Das</td>
<td>103</td>
</tr>
<tr>
<td>1442</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art10.pdf'>Historical Note: Old Water-Works on the Eastern Part of Mysore Plateau </a></td>
<td> Jean Deloche</td>
<td>391</td>
</tr>
<tr>
<td>1443</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art11.pdf'>Book Review: A Selected Works of Gurugovinda Chakravarti on Ancient and Medieval Indian Mathematics </a></td>
<td> AKBag</td>
<td>28</td>
</tr>
<tr>
<td>1444</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art12.pdf'>Book Review: History of Science in India, Vol. III: Chemical Science </a></td>
<td> D Banerjea</td>
<td>37</td>
</tr>
<tr>
<td>1445</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art13.pdf'>Project Report: Use of Solar Passice Concepts in the Avadh Architechtectural Buildings and their Modified Impact </a></td>
<td> Usha Bajpai</td>
<td>551</td>
</tr>
<tr>
<td>1446</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art14.pdf'>News: Magic Square for 2015 </a></td>
<td> S R Sharma</td>
<td>695</td>
</tr>
<tr>
<td>1447</td>
<td>IJHS-50-2015-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_1_Art15.pdf'>News: 900th Birth Anniversary of Bhaskaracarya: A Brief Report </a></td>
<td> Madhavendra Narayan</td>
<td>118</td>
</tr>
<tr>
<td>1448</td>
<td>IJHS-50-2015-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Contents.pdf'>Contents </a></td>
<td> </td>
<td>103</td>
</tr>
<tr>
<td>1449</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art01.pdf'>Descriptions and Classification of Cancer in the Classical Ayurvedic Texts </a></td>
<td> P  Ram Manohar</td>
<td>347</td>
</tr>
<tr>
<td>1450</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art02.pdf'>Some Medicinal Plants of Indian Puranas in Today’s Ethnomedicinal Perspective </a></td>
<td> Madhumita Nath </td>
<td>189</td>
</tr>
<tr>
<td>1451</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art03.pdf'>Classification of Substances in Vaidyanighantus -Medical Lexions </a></td>
<td> B Rama Rao</td>
<td>173</td>
</tr>
<tr>
<td>1452</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Math</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art04.pdf'>Allusions to Ancient Indian Mathematical Sciences in an Early Eighth Century Chinese Compilation by  </a></td>
<td> Vijaya J Deshpande</td>
<td>1431</td>
</tr>
<tr>
<td>1453</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art05.pdf'>Narayana’s Generalisation of Matra-Vrtta-Prastara and the Generalised Virahanka-Fibonacci Representa </a></td>
<td> Raja Sridharan</td>
<td>1800</td>
</tr>
<tr>
<td>1454</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art06.pdf'>Rationale for Vakyas Pertaining to the Sun in Karanapaddhati </a></td>
<td> Venketeswara Pai R</td>
<td>833</td>
</tr>
<tr>
<td>1455</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art07.pdf'>Lalah Bulhomal Lahori and the Production of Traditional Astronomical Instruments at Lahore in the Ni </a></td>
<td> S R Sarma</td>
<td>1283</td>
</tr>
<tr>
<td>1456</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art08.pdf'>Historical Note: Ambergris in Perfumery in the Past and Present Indian Context and the Western World </a></td>
<td> T M Srinivasan</td>
<td>813</td>
</tr>
<tr>
<td>1457</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art09.pdf'>Historical Note: Traditional Healing Practices in North East India </a></td>
<td> Ramashankar</td>
<td>374</td>
</tr>
<tr>
<td>1458</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art10.pdf'>Historical Note: Historical Antecedents of Cancer Surveillance from 1805 to 1891 </a></td>
<td> Wilson I B Onuigbo</td>
<td>119</td>
</tr>
<tr>
<td>1459</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art11.pdf'>Historical Note: Scientific Exploration of the Snow Fungus (Tremella fuciformis Berk.) </a></td>
<td> Ruixia Wang</td>
<td>369</td>
</tr>
<tr>
<td>1460</td>
<td>IJHS-50-2015-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art12.pdf'>Project Report: Metrological Traditions of South India </a></td>
<td> V Selvakumar</td>
<td>920</td>
</tr>
<tr>
<td>1461</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art13.pdf'>Book Review: Indian Astronomy -Concepts and Procedures by S Balachandra Rao  </a></td>
<td> A K Bhatnagar</td>
<td>105</td>
</tr>
<tr>
<td>1462</td>
<td>IJHS-50-2015-Issue-2</td>
<td>Culture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art14.pdf'>News: Cross Civilizational Interactions in Antiquity: India, Iran, Greece and China - A Report </a></td>
<td> Surajit Sarkar</td>
<td>108</td>
</tr>
<tr>
<td>1463</td>
<td>IJHS-50-2015-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_2_Art15.pdf'>News: Sir JC Bose Trust: An Appeal </a></td>
<td> Trustee, Sir JC Bose Trust</td>
<td>99</td>
</tr>
<tr>
<td>1464</td>
<td>IJHS-50-2015-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_CONTENTS.pdf'>Contents </a></td>
<td> </td>
<td>13</td>
</tr>
<tr>
<td>1465</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art01.pdf'>Ideas and Researches on Physical Concepts in India </a></td>
<td> AK Bag</td>
<td>568</td>
</tr>
<tr>
<td>1466</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art02.pdf'>Kanny Lall Dey– Pioneer Proponent of Indigenous Drugs </a></td>
<td> Harkishan Singh</td>
<td>113</td>
</tr>
<tr>
<td>1467</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art03.pdf'>Sir Asutosh and Rise of Modern Science in India </a></td>
<td> Kankan Bhattacharyya</td>
<td>86</td>
</tr>
<tr>
<td>1468</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art04.pdf'>The Doctoral Research of Acharya Prafulla Chandra Ray </a></td>
<td> Animesh Chakravorty</td>
<td>155</td>
</tr>
<tr>
<td>1469</td>
<td>IJHS-50-2015-Issue-3</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art05.pdf'>D M Bose and Cosmic Ray Research </a></td>
<td> S C Roy</td>
<td>1618</td>
</tr>
<tr>
<td>1470</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art06.pdf'>An Account of the Development of Nuclear Magnetic Resonance (NMR) in India </a></td>
<td> Girjesh Govil</td>
<td>192</td>
</tr>
<tr>
<td>1471</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art07.pdf'>Historical Notes: Electrochemistry and Fuel Cells: The Contribution of William Robert Grove </a></td>
<td> Jaime Wisniak</td>
<td>54</td>
</tr>
<tr>
<td>1472</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art08.pdf'>Historical Notes: Historiography and Commentary on the Nepal - India Earthquake of 26 August 1833 </a></td>
<td> Sujit Dasgupta</td>
<td>844</td>
</tr>
<tr>
<td>1473</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art09.pdf'>Historical Notes: Rabies, Anti-Rabic Vaccine and the Raj </a></td>
<td> Gagandip Cheema</td>
<td>29</td>
</tr>
<tr>
<td>1474</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art10.pdf'>Historical Notes: Features of Mathematical Sciences in India in the Second World War </a></td>
<td> Jagdish N Sinha</td>
<td>58</td>
</tr>
<tr>
<td>1475</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art11.pdf'>Historical Notes: Doctorate Degrees from India: 1877 (first award) to 1920 </a></td>
<td> B K Sen</td>
<td>11</td>
</tr>
<tr>
<td>1476</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art12.pdf'>Project Report: English Translation with critical notes and indexing of Pathyapathyaviniscaya - A 16 </a></td>
<td> P Ram Manohar</td>
<td>145</td>
</tr>
<tr>
<td>1477</td>
<td>IJHS-50-2015-Issue-3</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art13.pdf'>Book Review: Taming the Unknown - A History of Algebra from Antiquity to the Early Twentieth Century </a></td>
<td> Raja Sridhran</td>
<td>26</td>
</tr>
<tr>
<td>1478</td>
<td>IJHS-50-2015-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_3_Art14.pdf'>News </a></td>
<td> </td>
<td>7</td>
</tr>
<tr>
<td>1479</td>
<td>IJHS-50-2015-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_CONTENTS.pdf'>Contents </a></td>
<td> Issue 4</td>
<td>113</td>
</tr>
<tr>
<td>1480</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art01.pdf'>Sacrificially Important Trees Revealed in the Krsna Yajurveda Samhita- Their Description and Uses </a></td>
<td> Raghava S Boddupalli and Vedam Venkata Rama Sastri</td>
<td>4585</td>
</tr>
<tr>
<td>1481</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art02.pdf'>Identity and Attributes of Ayurvedic Medicinal Plant Brahmi/Aindri from Antiquity to the Modern Age </a></td>
<td> Ram H Singh</td>
<td>177</td>
</tr>
<tr>
<td>1482</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art03.pdf'>Survey of Zijes Written in the Subcontinent </a></td>
<td> S M Razaullah Ansari</td>
<td>3540</td>
</tr>
<tr>
<td>1483</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art04.pdf'>Nilakanthas Value of R-Sine for the Arc of Twenty-four Degrees </a></td>
<td> Takao Hayashi</td>
<td>931</td>
</tr>
<tr>
<td>1484</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art05.pdf'>HISTEM and the Making of Modern India — Some Questions and Explanations </a></td>
<td> Deepak Kumar</td>
<td>156</td>
</tr>
<tr>
<td>1485</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art06.pdf'>Historical Note: In Search of Roots: Tracing the History and Philosophy of Indian Medicine </a></td>
<td> Bhushan Patwardhan, Sharad Deshpande, Girish Tillu</td>
<td>163</td>
</tr>
<tr>
<td>1486</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art07.pdf'>Historical Note: Trigonometrical Survey of India and Naming of Peak XV as Mt. Everest </a></td>
<td> Shrikant Mishra et al.</td>
<td>216</td>
</tr>
<tr>
<td>1487</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art08.pdf'>Correspondence: Ideas and Researches on Physical Concepts in India </a></td>
<td> BV Subbarayappa</td>
<td>112</td>
</tr>
<tr>
<td>1488</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art09.pdf'>Book Review: Medicine, Trade and Empire: Garcia de Orta’s Colloquies on the Simples and Drugs of India (1563) in Context </a></td>
<td> S Sundara Rajan</td>
<td>121</td>
</tr>
<tr>
<td>1489</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art10.pdf'>Project Report: English Translation of Rasendra Cudamani </a></td>
<td> K Naveena</td>
<td>151</td>
</tr>
<tr>
<td>1490</td>
<td>IJHS-50-2015-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art11.pdf'>News: History of Science Seminar on the Indian Heritage: A Genomic View- A Report </a></td>
<td> Madhvendra Narayan</td>
<td>103</td>
</tr>
<tr>
<td>1491</td>
<td>IJHS-50-2015-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art12.pdf'>Books Received for Review and </a></td>
<td> Announcements</td>
<td>112</td>
</tr>
<tr>
<td>1492</td>
<td>IJHS-50-2015-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art13.pdf'>Cumulative Index </a></td>
<td> Year 2015</td>
<td>143</td>
</tr>
<tr>
<td>1493</td>
<td>IJHS-50-2015-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol50_2015_4_Art14.pdf'>Annual Contents </a></td>
<td> Volume 50.1-4 (2015)</td>
<td>118</td>
</tr>
<tr>
<td>1494</td>
<td>IJHS-51-2016-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art01.pdf'>Contents </a></td>
<td> Contents</td>
<td>149</td>
</tr>
<tr>
<td>1495</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art02.pdf'>Editorial: Tradition & Methodology of Knowledge Production </a></td>
<td> A K Bag</td>
<td>180</td>
</tr>
<tr>
<td>1496</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art03.pdf'>Guest Editorial </a></td>
<td> Rajan Gurukkal</td>
<td>115</td>
</tr>
<tr>
<td>1497</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art04.pdf'>An Introductory Outline of Knowledge Production in Pre-colonial India </a></td>
<td> Rajan Gurukkal</td>
<td>182</td>
</tr>
<tr>
<td>1498</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art05.pdf'>Metallurgy of Zinc, High-tin Bronze and Gold in Indian Antiquity: Methodological Aspects </a></td>
<td> Sharada Srinivasan</td>
<td>1338</td>
</tr>
<tr>
<td>1499</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art06.pdf'>Carakas Approach to Knowledge </a></td>
<td> M S Valiathan</td>
<td>259</td>
</tr>
<tr>
<td>1500</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art07.pdf'>Origins and Growth of Ayurvedic Knowledge </a></td>
<td> M R Raghava Varier</td>
<td>186</td>
</tr>
<tr>
<td>1501</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art08.pdf'>Knowledge Generation in Ayurveda: Methodological Aspects </a></td>
<td> S N Venugopalan Nair and Darshan Shankar</td>
<td>193</td>
</tr>
<tr>
<td>1502</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art09.pdf'>What is Indian about Indian Mathematics? </a></td>
<td> P P Divakaran</td>
<td>385</td>
</tr>
<tr>
<td>1503</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art10.pdf'>Heliacal Rising of Canopus in Indian Astronomy </a></td>
<td> S Balachandra Rao, Rupa K and Padmaja Venugopal</td>
<td>945</td>
</tr>
<tr>
<td>1504</td>
<td>IJHS-51-2016-Issue-1</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art11.pdf'>Inference as a Means of Valid Knowledge in Indian Epistemological Tradition </a></td>
<td> C Rajendran</td>
<td>144</td>
</tr>
<tr>
<td>1505</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art12.pdf'>Debate as a Methodology of Knowledge Production in Pre-Modern India </a></td>
<td> A Raghuramaraju</td>
<td>150</td>
</tr>
<tr>
<td>1506</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art13.pdf'>Translation as Method: Implications for History of Science </a></td>
<td> Sundar Sarukkai</td>
<td>174</td>
</tr>
<tr>
<td>1507</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art14.pdf'>In Search of the Beginnings and Growth of Knowledge Production in Tamil </a></td>
<td> R Champakalakshmi</td>
<td>182</td>
</tr>
<tr>
<td>1508</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art15.pdf'>A Note on Grammatical Knowledge in Early Tamilakam </a></td>
<td> Y Subbarayalu</td>
<td>155</td>
</tr>
<tr>
<td>1509</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art16.pdf'>Body Centric Knowledge: Traditions of Performance and Pedagogy in Kathakali </a></td>
<td> Mundoli Narayanan</td>
<td>192</td>
</tr>
<tr>
<td>1510</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art17.pdf'>The Polysemy of the Prabandha – Reading a Premodern Musical Genre </a></td>
<td> Naresh Keerthi</td>
<td>1565</td>
</tr>
<tr>
<td>1511</td>
<td>IJHS-51-2016-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_1_Art18.pdf'>From the Mythology of Vastusastra to the Methodology of Vastuvidya </a></td>
<td> RV Achari</td>
<td>778</td>
</tr>
<tr>
<td>1512</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art00.pdf'>Contents </a></td>
<td> </td>
<td>103</td>
</tr>
<tr>
<td>1513</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art01.pdf'>Agricultural Practices as gleaned from the Tamil Literature of the Sangam Age </a></td>
<td> T M Srinivasan</td>
<td>1207</td>
</tr>
<tr>
<td>1514</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art02.pdf'>Combinatorics as Found in the Gommatsara of Nemichandra </a></td>
<td> Dipak Jadhav and Anupam Jain</td>
<td>921</td>
</tr>
<tr>
<td>1515</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art03.pdf'>Records of Vyatipata in Stone Inscriptions </a></td>
<td> B S Shylaja and Geetha Kydala</td>
<td>1964</td>
</tr>
<tr>
<td>1516</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art04.pdf'>Pathophysiology and Treatment of Urolithiasis in Unani Medicine </a></td>
<td> I Mohammed Tabarak Hussain, Ghufran Ahmed, Nasreen</td>
<td>181</td>
</tr>
<tr>
<td>1517</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art05.pdf'>Techno-Engineering Education and the Railways in Colonial India </a></td>
<td> Debashis Mandal</td>
<td>142</td>
</tr>
<tr>
<td>1518</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art06.pdf'>Sahib Singh Sokhey (1887-1971): An Eminent Medico-Pharmaceutical Professional </a></td>
<td> Harkishan Singh</td>
<td>442</td>
</tr>
<tr>
<td>1519</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art07.pdf'>Historical Notes: Revisiting the Calendar Tradition of Ancient India </a></td>
<td> BN Narhari Achar</td>
<td>562</td>
</tr>
<tr>
<td>1520</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art08.pdf'>Historical Notes: Genesis and Progress in Concepts of Preventive Cardiology: A Historical Overview </a></td>
<td> Sukta Das</td>
<td>178</td>
</tr>
<tr>
<td>1521</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art09.pdf'>Historical Notes: Girish Chandra Bose and Agricultural Journalism </a></td>
<td> CB Palit</td>
<td>119</td>
</tr>
<tr>
<td>1522</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art10.pdf'>Historical Notes: Radhanath Sikdar and the Final Phase of Measuring Peak XV </a></td>
<td> Ashish Lahiri</td>
<td>128</td>
</tr>
<tr>
<td>1523</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art11.pdf'>Book Review: Flood Finbarr B—Objects of Translation – Material Culture and Medieval “Hindu-Muslim </a></td>
<td> Madhvendra Narayan</td>
<td>122</td>
</tr>
<tr>
<td>1524</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art12.pdf'>Project Report: Study of Indus Valley Scripts through Linguistic and Markov Chain Methods </a></td>
<td> Niladri Sarkar</td>
<td>3447</td>
</tr>
<tr>
<td>1525</td>
<td>IJHS-51-2016-Issue-2A</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_1_Art13.pdf'>Project Report: English Translation of Second part of Siddhanta Sekhara of Sripati </a></td>
<td> Sripad Bhat</td>
<td>138</td>
</tr>
<tr>
<td>1526</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art00.pdf'>Contents </a></td>
<td> </td>
<td>106</td>
</tr>
<tr>
<td>1527</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art01.pdf'>Editorial </a></td>
<td> D Balasubramanian and AK Bag</td>
<td>95</td>
</tr>
<tr>
<td>1528</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art02.pdf'>Guest Editorial </a></td>
<td> Partha P Majumder</td>
<td>89</td>
</tr>
<tr>
<td>1529</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art03.pdf'>Iconic Flora of Heritage Significance in India </a></td>
<td> H Y Mohan Ram</td>
<td>2759</td>
</tr>
<tr>
<td>1530</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art04.pdf'>The Holy Basil (Ocimum sanctum L.) and its Genome </a></td>
<td> Ajit K Shasany</td>
<td>588</td>
</tr>
<tr>
<td>1531</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art05.pdf'>Genome and Evolution of the Sacred Lotus </a></td>
<td> Partha P Majumder</td>
<td>112</td>
</tr>
<tr>
<td>1532</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art06.pdf'>Decoded Rice Genome for Decipherment of Origin, Domestication and Functional Attributes of Rice </a></td>
<td> Akhilesh K Tyagi</td>
<td>205</td>
</tr>
<tr>
<td>1533</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art07.pdf'>Origin, Diversity and Genome Sequence of Mango (Mangifera indica L.) </a></td>
<td> Nagendra K Singh, Ajay K Mahato et al.,</td>
<td>2668</td>
</tr>
<tr>
<td>1534</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art08.pdf'>Iconic Fauna of Heritage Significance in India </a></td>
<td> Raman Sukumar</td>
<td>1086</td>
</tr>
<tr>
<td>1535</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art09.pdf'>Genetic Structure of the Wild Populations of the Indian Rhinoceros (Rhinoceros unicornis) </a></td>
<td> Samuel Zschokke</td>
<td>388</td>
</tr>
<tr>
<td>1536</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art10.pdf'>Gene flow and Evolutionary History of Tigers in Central India </a></td>
<td> Sandeep Sharma</td>
<td>392</td>
</tr>
<tr>
<td>1537</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art11.pdf'>Evolutionary History and Population Genetic Structure of Asian Elephants in India </a></td>
<td> T N C Vidya</td>
<td>1157</td>
</tr>
<tr>
<td>1538</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art12.pdf'>The Dazzling Diversity and the Fundamental Unity: Peopling and the Genomic Structure of Ethnic India </a></td>
<td> Analabha Basu</td>
<td>146</td>
</tr>
<tr>
<td>1539</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art13.pdf'>Historical Note: Medical Genetics in Classical Ayurvedic Texts: A Critical Review </a></td>
<td> P Ram Manohar</td>
<td>829</td>
</tr>
<tr>
<td>1540</td>
<td>IJHS-51-2016-Issue-2B</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_2_2_Art14.pdf'>Historical Note: History and Development of Genetics Research in India: Three case studies </a></td>
<td> DP Kasbekar</td>
<td>403</td>
</tr>
<tr>
<td>1541</td>
<td>IJHS-51-2016-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art00.pdf'>Contents </a></td>
<td> Contents</td>
<td>203</td>
</tr>
<tr>
<td>1542</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art01.pdf'>Mud Plaster Wall Paintings of Bhaja Caves: Composition and Performance Characteristics </a></td>
<td> M Singh, S Vinodh Kumar and Sujata Waghmare</td>
<td>2860</td>
</tr>
<tr>
<td>1543</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art02.pdf'>Role of Experiments in the Progress of Science: Lessons from our History </a></td>
<td> D P Roy</td>
<td>1016</td>
</tr>
<tr>
<td>1544</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art03.pdf'>A Lahore Astrolabe of 1587 at Moscow: Enigmas in its Construction </a></td>
<td> Sergei Maslikov and Sreeramula Rajeswara Sarma</td>
<td>5721</td>
</tr>
<tr>
<td>1545</td>
<td>IJHS-51-2016-Issue-3</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art04.pdf'>Madras Lunatic Asylum: A Remarkable History in British India </a></td>
<td> Saumitra Basu</td>
<td>1814</td>
</tr>
<tr>
<td>1546</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art05.pdf'>Science, Science Literacy and Communication </a></td>
<td> G S Rautela and Kanchan Chowdhury</td>
<td>1972</td>
</tr>
<tr>
<td>1547</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art06.pdf'>Historical Note: On the Visibility of Agastya (Canopus) in India </a></td>
<td> K Chandra Hari</td>
<td>2180</td>
</tr>
<tr>
<td>1548</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art07.pdf'>Historical Note: The Nobel Laureate W.C. Roentgen and His X-Rays </a></td>
<td> Rajinder Singh</td>
<td>289</td>
</tr>
<tr>
<td>1549</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art08.pdf'>Historical Note: N C Rana: Life and His Contributions in Astrophysical Science </a></td>
<td> Utpal Mukhopadhyay and Saibal Ray</td>
<td>933</td>
</tr>
<tr>
<td>1550</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art09.pdf'>Project Report: Amarakosa – A Biological Assessment </a></td>
<td> S Sundara Rajan</td>
<td>439</td>
</tr>
<tr>
<td>1551</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Biology</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art10.pdf'>Project Report: A Study on River Channel Modifications of Jorhat District of Assam </a></td>
<td> Raktim Ranjan Saikia and D Nurul Amin</td>
<td>273</td>
</tr>
<tr>
<td>1552</td>
<td>IJHS-51-2016-Issue-3</td>
<td>Astronomy</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_2016_3_Art11.pdf'>Corrections and Additions: Survey of Zijes Written in the Subcontinent </a></td>
<td> S. M. Razaullah Ansari</td>
<td>264</td>
</tr>
<tr>
<td>1553</td>
<td>IJHS-51-2016-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Contents.pdf'>Contents </a></td>
<td> Contents</td>
<td>108</td>
</tr>
<tr>
<td>1554</td>
<td>IJHS-51-2016-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art01.pdf'>Editorial </a></td>
<td> AK Bag</td>
<td>177</td>
</tr>
<tr>
<td>1555</td>
<td>IJHS-51-2016-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art02.pdf'>Guest Editorial </a></td>
<td> Lotika Vardarajan and Surajit Sarkar</td>
<td>84</td>
</tr>
<tr>
<td>1556</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art03.pdf'>An Indic Text on Earth Science: Sasanian to Post-Sasanian Period </a></td>
<td> Daryoosh Akbarzadeh</td>
<td>361</td>
</tr>
<tr>
<td>1557</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art04.pdf'>Throne — Asandi, Pallanka, Simhasana: An Indian Perspective </a></td>
<td> Anamika Pathak</td>
<td>1823</td>
</tr>
<tr>
<td>1558</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Culture</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art05.pdf'>The Hybrid Creatures in Iranian and Indian Art </a></td>
<td> Katayoun Fekripour</td>
<td>2689</td>
</tr>
<tr>
<td>1559</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art06.pdf'>Commonalities between Yajna Ritual in India and Yasna Ritual in Iran </a></td>
<td> Azadeh Heidarpoor and Fariba Sharifian</td>
<td>166</td>
</tr>
<tr>
<td>1560</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art07.pdf'>Indian High-Tin Bronzes and the Grecian and Persian World </a></td>
<td> Sharada Srinivasan</td>
<td>3500</td>
</tr>
<tr>
<td>1561</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art08.pdf'>Vetikkampavidhi: A Malayalam Text on Pyrotechny </a></td>
<td> Abhilash Malayil</td>
<td>224</td>
</tr>
<tr>
<td>1562</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art09.pdf'>Central Asia: A Melting Pot of Persian, Greek, Indian and Chinese Cultural Traditions </a></td>
<td> Chhaya Bhattacharya-Haesner</td>
<td>5575</td>
</tr>
<tr>
<td>1563</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art10.pdf'>Taxila – An Alternative Urbanisation Between the Silk Road and the Uttarapatha (the Northern Road) </a></td>
<td> Surajit Sarkar</td>
<td>332</td>
</tr>
<tr>
<td>1564</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art11.pdf'>Buddhism in Khotan and Soghdiana </a></td>
<td> Fariba Sharifian</td>
<td>137</td>
</tr>
<tr>
<td>1565</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art12.pdf'>Krsna Iconography in Khotan Carpets: Spread of Hindu Religious Ideas in Xinjiang, China, Fourth–Seve </a></td>
<td> Zhang He</td>
<td>2460</td>
</tr>
<tr>
<td>1566</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art13.pdf'>The Benaki Collection of Fustat Textiles - Analysis and Provenance </a></td>
<td> Lotika Varadarajan</td>
<td>3970</td>
</tr>
<tr>
<td>1567</td>
<td>IJHS-51-2016-Issue-4</td>
<td>Biology</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art14.pdf'>From Balkh to Baghdad: Indian Science and the Birth of the Islamic Golden Age in the Eighth Century </a></td>
<td> Dominik Wujastyk</td>
<td>3272</td>
</tr>
<tr>
<td>1568</td>
<td>IJHS-51-2016-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art15.pdf'>Books Received for Review & Announcements </a></td>
<td> INSA</td>
<td>110</td>
</tr>
<tr>
<td>1569</td>
<td>IJHS-51-2016-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol51_4_2016_Art16.pdf'>Cumulative Index </a></td>
<td> Vol. 51.1-4 (2016)</td>
<td>135</td>
</tr>
<tr>
<td>1570</td>
<td>IJHS-52-2017-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art00.pdf'>Contents </a></td>
<td> Contents</td>
<td>205</td>
</tr>
<tr>
<td>1571</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art01.pdf'>Some Features of the Solutions of Kuttaka and Vargaprakrti </a></td>
<td> AK Bag</td>
<td>809</td>
</tr>
<tr>
<td>1572</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art02.pdf'>Ideas of Infinitesimal of Bhaskaracarya in Lilavati and Siddhantasiromani </a></td>
<td> A B Padmanabha Rao</td>
<td>411</td>
</tr>
<tr>
<td>1573</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art03.pdf'>The Hospital transcends into Hospital Medicine: A Brief Journey through Ancient,  Medieval and Colonial India </a></td>
<td> Jayanta Bhattacharya</td>
<td>620</td>
</tr>
<tr>
<td>1574</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art04.pdf'>Amoebic Dysentery and Introduction of Emetine Source Carapichea ipecacacuanha into Indian Subcontinent </a></td>
<td> Ramya Raman and Anantanarayanan Raman</td>
<td>644</td>
</tr>
<tr>
<td>1575</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art05.pdf'>Discovery of X-rays and its Impact in India </a></td>
<td> SC Roy</td>
<td>730</td>
</tr>
<tr>
<td>1576</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art06.pdf'>Historical Note: Ashutosh Mukherjee’s Contribution on Nineteenth Century Modern Mathematics: A Bird’s Eye View </a></td>
<td> Sabitri Ray Chaudhuri</td>
<td>50</td>
</tr>
<tr>
<td>1577</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art07.pdf'>Historical Note: G N Ramachandran: A Nobel Prize Nominee and Nominator </a></td>
<td> Rajinder Singh</td>
<td>127</td>
</tr>
<tr>
<td>1578</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art08.pdf'>Historical Note: Udoy Chand Dutt: Prominent Indian Materia Medica Promoters </a></td>
<td> Harkishan Singh</td>
<td>184</td>
</tr>
<tr>
<td>1579</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Biology</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art09.pdf'>Historical Note: Scientific Explorations and Commercial Sales of the Straw Mushroom  Volvariella volvacea (Bull.) Singer in Republican China:  A Brief Review </a></td>
<td> Ruxia Wang, Hui Cao, Jingsong Zhang and Qi Tan</td>
<td>723</td>
</tr>
<tr>
<td>1580</td>
<td>IJHS-52-2017-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art10.pdf'>Book Review: Rao, A B Padmanabha (trans. and ed.) Bhaskaracarya&#8217;s Lilavati Part I &amp; II </a></td>
<td> MS Sriram</td>
<td>374</td>
</tr>
<tr>
<td>1581</td>
<td>IJHS-52-2017-Issue-1</td>
<td>MindSciences</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_1_2017_Art11.pdf'>Project Report: History of Neurodegenerative Diseases and its impact on Aged Population in India: An Assessment </a></td>
<td> Saumitra Basu</td>
<td>378</td>
</tr>
<tr>
<td>1582</td>
<td>IJHS-52-2017-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Contents.pdf'>Contents </a></td>
<td> Contents</td>
<td>201</td>
</tr>
<tr>
<td>1583</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art01.pdf'>Angular Diameters (bimba) of the Sun, Moon and Earth’s Shadow-cone in Indian Astronomy: A Comparative Study </a></td>
<td> S Balachandra Rao, M Shailaja and V Vanaja</td>
<td>579</td>
</tr>
<tr>
<td>1584</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art02.pdf'>Novel Proofs for Summations in the Nisrstarthaduti </a></td>
<td> Aditya Kolachana, K Mahesh and K Ramasubramanian</td>
<td>2527</td>
</tr>
<tr>
<td>1585</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art03.pdf'>Sundial for Time–keeping in Jaisalmer Fort </a></td>
<td> Aalok Pandya, Tej Bahadur and Sandip Bhattachar</td>
<td>4035</td>
</tr>
<tr>
<td>1586</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art04.pdf'>Edward Blyth and the Asiatic Society </a></td>
<td> Aparajita Basu</td>
<td>343</td>
</tr>
<tr>
<td>1587</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art05.pdf'>Central Weaving Institute, Banaras: A Cultural Encounter between the Native and the Modern Form of Instructional Practices </a></td>
<td> Prakrati Bhargava</td>
<td>368</td>
</tr>
<tr>
<td>1588</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art06.pdf'>The History of Colonial Science and Medicine in British India: Centre-Periphery Perspective </a></td>
<td> Rahul Bhaumik</td>
<td>326</td>
</tr>
<tr>
<td>1589</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art07.pdf'>Historical Note:Cause of Sunrise, Sunset from Jnanesvari and its comparison to Aryabhatiya </a></td>
<td> Anand Dabak</td>
<td>394</td>
</tr>
<tr>
<td>1590</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art08.pdf'>Historical Note: Allusions of Rasayanasastra in Telugu Literature </a></td>
<td> Iragavarapu Suryanarayana</td>
<td>542</td>
</tr>
<tr>
<td>1591</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art09.pdf'>Historical Note: General Scientific Societies in British India </a></td>
<td> B K Sen</td>
<td>467</td>
</tr>
<tr>
<td>1592</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art10.pdf'>Historical Note: Syamadas Mukhopadhyay (1866-1937): A Reputed Geometrician of India </a></td>
<td> Purabi Mukherji and Mala Bhattacharjee</td>
<td>346</td>
</tr>
<tr>
<td>1593</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art12.pdf'>Book Review: Gauhar Raza, R Gopichandran, Gurdeep S Sappal and TV Venkateswaran (editors) : Moments of Eureka- Life & Works of Selected Indian Scientists </a></td>
<td> Kankan Bhattacharyya</td>
<td>193</td>
</tr>
<tr>
<td>1594</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art13.pdf'>Book Review: B S Shylaja and V S S Sastry : Jantar Mantar Observatories of Jai Singh </a></td>
<td> S Balachandra Rao</td>
<td>261</td>
</tr>
<tr>
<td>1595</td>
<td>IJHS-52-2017-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_2_2017__Art11.pdf'>Project Report: History of High Tin Bronze and Brass of Eastern India </a></td>
<td> Pranab K Chattopadhayay</td>
<td>2411</td>
</tr>
<tr>
<td>1596</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art01.pdf'>Identification of Mosquitoes, Nature of Diseases and Treatment in Early Sanskrit Literature </a></td>
<td> Sagan Deep Kaur and Lakhvir Singh</td>
<td>2140</td>
</tr>
<tr>
<td>1597</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art02.pdf'>Importance of Plants as depicted in Puranas </a></td>
<td> Dhananjay Vasudeo Dwivedi</td>
<td>277</td>
</tr>
<tr>
<td>1598</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art03.pdf'>Strivilasa – An Ayurvedic Manuscript on Cosmetic Procedures of Females, Aphrodisiacs, Diseases and M </a></td>
<td> Goli Penchala Prasad et al.</td>
<td>830</td>
</tr>
<tr>
<td>1599</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art04.pdf'>Western Medicine in French Pondichery (1690–1954) </a></td>
<td> Ramya Raman and Anantanarayanan Raman</td>
<td>4023</td>
</tr>
<tr>
<td>1600</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art05.pdf'>Institutionalization of Nursing as Profession in the Early Twentieth Century Bengal </a></td>
<td> Sneha Sanyal</td>
<td>411</td>
</tr>
<tr>
<td>1601</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art06.pdf'>Historical Notes: The Jaina School of Indian Mathematics </a></td>
<td> Dipak Jadhav</td>
<td>343</td>
</tr>
<tr>
<td>1602</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art07.pdf'>Historical Notes: Mango in Ancient Indian Sculptures and during Akbar Period </a></td>
<td> N C Shah</td>
<td>1153</td>
</tr>
<tr>
<td>1603</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art08.pdf'>Historical Note: Why and When were the Vijayanagara Walls Built? ..... </a></td>
<td> Jean Deloche</td>
<td>114</td>
</tr>
<tr>
<td>1604</td>
<td>IJHS-52-2017-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art09.pdf'>Historical Note: B B Ray and Controversy over the Spectral Raman-lines </a></td>
<td> Rajinder Singh</td>
<td>2836</td>
</tr>
<tr>
<td>1605</td>
<td>IJHS-52-2017-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art10.pdf'>Book Review: Scientifically Yours </a></td>
<td> Kankan Bhattacharyya</td>
<td>103</td>
</tr>
<tr>
<td>1606</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art11.pdf'>Book Review: Tracks of Change: Railways and Everyday Life in Colonial India </a></td>
<td> Debashis Mandal</td>
<td>126</td>
</tr>
<tr>
<td>1607</td>
<td>IJHS-52-2017-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_3_2017__Art12.pdf'>Project Report: History of Science Museums and Planetariums in India </a></td>
<td> Jayanta Sthanapati</td>
<td>3235</td>
</tr>
<tr>
<td>1608</td>
<td>IJHS-52-2017-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents.pdf'>Contents </a></td>
<td> Contents</td>
<td>1498</td>
</tr>
<tr>
<td>1609</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art01.pdf'>Date of Mahābhārata War Based on Astronomical References—A Reassessment </a></td>
<td> Ashok K Bhatnagar</td>
<td>5016</td>
</tr>
<tr>
<td>1610</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art02.pdf'>Aryabhata-II and his Concept of Concave Quadrilateral </a></td>
<td> Amalkumar Mukhopadhyay</td>
<td>449</td>
</tr>
<tr>
<td>1611</td>
<td>IJHS-52-2017-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art03.pdf'>Sisir Kumar Mitra, Scientific Achievements and the Fellowship of the Royal Society of London </a></td>
<td> Rajinder Singh</td>
<td>2697</td>
</tr>
<tr>
<td>1612</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art04.pdf'>History of the Scientific Study of the Tibeto-Burman Languages of North-East India </a></td>
<td> Satarupa Dattamajumdar</td>
<td>2297</td>
</tr>
<tr>
<td>1613</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art05.pdf'>Historical Notes: Some Thoughts on Hindu Medicine —An Address by Kaviraj Mahamahopadhyaya Gananath.. </a></td>
<td> N C Shah</td>
<td>3243</td>
</tr>
<tr>
<td>1614</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art06.pdf'>Historical Notes: Science Education and Science Writing in Hindi in the North West Provinces... </a></td>
<td> Pooja Mishra</td>
<td>943</td>
</tr>
<tr>
<td>1615</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art07.pdf'>Book Review: Bengal Water Craft: Boat-Building and Fishing Communities by Lotika Varadarajan </a></td>
<td> Smritikumar Sarkar</td>
<td>165</td>
</tr>
<tr>
<td>1616</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art08.pdf'>Book Review: India’s Nobel Prize: Nominators and Nominees, by Rajinder Singh </a></td>
<td> Kankan Bhattacharyya</td>
<td>95</td>
</tr>
<tr>
<td>1617</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art09.pdf'>Book Review: Inside Story of Nobel Peace Prize: Indian Contestants by Rajinder Singh </a></td>
<td> Kankan Bhattacharyya</td>
<td>102</td>
</tr>
<tr>
<td>1618</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art10.pdf'>Project Report: History of Technology Adoption and Development: The Case of Silk Industry.... </a></td>
<td> Anirban Mukherjee</td>
<td>120</td>
</tr>
<tr>
<td>1619</td>
<td>IJHS-52-2017-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art11.pdf'>Obituary: Lotika Varadarajan (1934-2017) </a></td>
<td> Surajit Sarkar</td>
<td>233</td>
</tr>
<tr>
<td>1620</td>
<td>IJHS-52-2017-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art12.pdf'>News: The 25th International Congress of History of Science and Technology... </a></td>
<td> Gulfishan Khan</td>
<td>128</td>
</tr>
<tr>
<td>1621</td>
<td>IJHS-52-2017-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/13-Books Received for Review.pdf'>Books Received (2017) </a></td>
<td> Madhvendra Narayan</td>
<td>126</td>
</tr>
<tr>
<td>1622</td>
<td>IJHS-52-2017-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol52_4_2017__Art13.pdf'>Ganitapancavimsi — Sanskrit Text with Introduction, English Translation and Notes </a></td>
<td> K S Shukla</td>
<td>15361</td>
</tr>
<tr>
<td>1623</td>
<td>IJHS-52-2017-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/17-Cumulativeindex.pdf'>Cumulative Index </a></td>
<td> Madhvendra Narayan</td>
<td>135</td>
</tr>
<tr>
<td>1624</td>
<td>IJHS-52-2017-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/18-Contentsall.pdf'>Annual Contents </a></td>
<td> Madhvendra Narayan</td>
<td>114</td>
</tr>
<tr>
<td>1625</td>
<td>IJHS-53-2018-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Contents.pdf'>Contents </a></td>
<td> Contents</td>
<td>106</td>
</tr>
<tr>
<td>1626</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art01.pdf'>Madhava’s Multi-pronged Approach for Obtaining the Praṇakalantara </a></td>
<td> Aditya Kolachana, K Mahesh and K Ramasubramanian</td>
<td>244</td>
</tr>
<tr>
<td>1627</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art02.pdf'>Ahargana in Makarandasarini and Other Indian Astronomical Texts </a></td>
<td> S K Uma and S Balachandra Rao</td>
<td>429</td>
</tr>
<tr>
<td>1628</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art03.pdf'>Medical Education on the Colonial Periphery: A Study of Medical Institutions in Patna and Dacca </a></td>
<td> Aishwaryarupa Majumdar</td>
<td>466</td>
</tr>
<tr>
<td>1629</td>
<td>IJHS-53-2018-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art04.pdf'>Celebrating the 90th Anniversary of the Raman Effect </a></td>
<td> Rajinder Singh</td>
<td>2161</td>
</tr>
<tr>
<td>1630</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art05.pdf'>Indian Arthropods in Early Sanskrit Literature: A Taxonomical Analysis </a></td>
<td> Sagan Deep Kaur and Lakhvir Singh</td>
<td>154</td>
</tr>
<tr>
<td>1631</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art06.pdf'>A Small History of Bedbugs in India </a></td>
<td> Shubhneet Kaushik</td>
<td>155</td>
</tr>
<tr>
<td>1632</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art07.pdf'>History of Development of Homoeopathy in India </a></td>
<td> Ajoy Kumar Ghosh</td>
<td>138</td>
</tr>
<tr>
<td>1633</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art08.pdf'>First Fifty Years (1900-1950) of Physiology in India </a></td>
<td> Amar K Chandra</td>
<td>194</td>
</tr>
<tr>
<td>1634</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art09.pdf'>Correspondence: Date of Mahabharata War Based on Astronomical References: A K Bhatnagar </a></td>
<td> B N Narahari Achar</td>
<td>169</td>
</tr>
<tr>
<td>1635</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art10.pdf'>Book Review: Ayurvedic Inheritance — A Reader’s Companion by M S Valiathan </a></td>
<td> Anantanarayanan Raman</td>
<td>156</td>
</tr>
<tr>
<td>1636</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art11.pdf'>Book Review: Technology of the Tribes of Northeast India by Amrendra Kumar Thakur </a></td>
<td> J N Sinha</td>
<td>111</td>
</tr>
<tr>
<td>1637</td>
<td>IJHS-53-2018-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_1_2018__Art12.pdf'>Project Report: Medicine and British Empire in South India: A Study of Psychiatry and Mental Asylums </a></td>
<td> Santhosh Abraham</td>
<td>124</td>
</tr>
<tr>
<td>1638</td>
<td>IJHS-53-2018-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>103</td>
</tr>
<tr>
<td>1639</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art01.pdf'>Concept of Sruti, Svara and Raga of Classical Music in Sanskrit Texts </a></td>
<td> RN Iyengar</td>
<td>1882</td>
</tr>
<tr>
<td>1640</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art02.pdf'>Brass, Zinc and the Beginning of Chemical Industry </a></td>
<td> Paul T Craddock</td>
<td>8906</td>
</tr>
<tr>
<td>1641</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art03.pdf'>Indigenous and Western Medicines in Colonial South India: Nature of Discourses and Impact  </a></td>
<td> D V Kanagarathinam </td>
<td>206</td>
</tr>
<tr>
<td>1642</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art04.pdf'>Punjab Agricultural College and Research Institute, Lyallpur (1906-1947): Generating Knowledge for.. </a></td>
<td> Kamlesh Mohan</td>
<td>365</td>
</tr>
<tr>
<td>1643</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art05.pdf'>Historical Note: History of  Yavaka from Ethno-pharmacological Perspective </a></td>
<td> Rajeshwari Singh, Mita Kotecha and N Srikant</td>
<td>1236</td>
</tr>
<tr>
<td>1644</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art06.pdf'>Historical Note: The Incredible Survival of Stone Wheel Manufacture in South India </a></td>
<td> Jean Deloche</td>
<td>21636</td>
</tr>
<tr>
<td>1645</td>
<td>IJHS-53-2018-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art07.pdf'>Correspondence: A Physics Museum in BHU in 1942  </a></td>
<td> B Anantha Dasannacharya</td>
<td>4325</td>
</tr>
<tr>
<td>1646</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art08.pdf'>Book Reviews: Vedic Mathematics mattu Vedagalalli Vijnana by S Balachandra Rao </a></td>
<td> B S Shylaja</td>
<td>118</td>
</tr>
<tr>
<td>1647</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art09.pdf'>Book Reviews: Plants of Kedarnath Wildlife Sanctuary, Western Himalaya: A Field Guide by ... </a></td>
<td> N C Shah</td>
<td>119</td>
</tr>
<tr>
<td>1648</td>
<td>IJHS-53-2018-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art10.pdf'>Book Reviews: A Brief History of Science by  Breakthrough Science Society, Kolkata </a></td>
<td> Kankan Bhattacharyya</td>
<td>106</td>
</tr>
<tr>
<td>1649</td>
<td>IJHS-53-2018-Issue-2</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_2_2018__Art11.pdf'>News: Workshop on Importance of Eclipses in the History of Astronomy </a></td>
<td> BS Shylaja</td>
<td>95</td>
</tr>
<tr>
<td>1650</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art01.pdf'>Harappan Shell Industry: An Overview </a></td>
<td> V H Sonawane</td>
<td>3176</td>
</tr>
<tr>
<td>1651</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art02.pdf'>Indus Ceramic Industries: Complexities, Challenges and Prospects </a></td>
<td> K Krishnan</td>
<td>529</td>
</tr>
<tr>
<td>1652</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art03.pdf'>Copper Vessels in the Indus Valley Civilization: A Case Study in the Light of Harinagar Hoard </a></td>
<td> Bhuvan Vikrama and Arakhita Pradhan</td>
<td>2013</td>
</tr>
<tr>
<td>1653</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art04.pdf'>Metals and Metallurgy in the Harappan Civilization </a></td>
<td> Vibha Tripathi</td>
<td>4035</td>
</tr>
<tr>
<td>1654</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art05.pdf'>Indigo — The Crop that Created History and then Itself Became History </a></td>
<td> Rajendra Prasad</td>
<td>142</td>
</tr>
<tr>
<td>1655</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art06.pdf'>Determination of Ascensional Difference in the Lagnaprakarana </a></td>
<td> Aditya Kolachana et al.</td>
<td>191</td>
</tr>
<tr>
<td>1656</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art07.pdf'>Historical Note: The Origin of the 28 Naksatras in Early Indian Astronomy and Astrology </a></td>
<td> Howard D Jones</td>
<td>159</td>
</tr>
<tr>
<td>1657</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art08.pdf'>Historical Note:Reactions of Emperor Bahadur Shah Zafar and Laureate Mirza Ghalib to the Celestial.. </a></td>
<td> R C Kapoor</td>
<td>840</td>
</tr>
<tr>
<td>1658</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art09.pdf'>Historical Note: Philippe Barbier and His Knowledge of Plants and Inorganic Principles in the... </a></td>
<td> Jaime Wisniak</td>
<td>283</td>
</tr>
<tr>
<td>1659</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art10.pdf'>Historical Note: Bibha Chowdhuri – Her Cosmic Ray Studies in Manchester </a></td>
<td> S C Roy and Rajinder Singh</td>
<td>4324</td>
</tr>
<tr>
<td>1660</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Math</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art11.pdf'>Book Review: The Continuation of Ancient Mathematics: Wang Xiatong’s Jigu suanjing, Algebra and... </a></td>
<td> R C Gupta</td>
<td>440</td>
</tr>
<tr>
<td>1661</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art12.pdf'>Book Review: CV Raman’s Laboratory and Discovery of the Raman Effect </a></td>
<td> Kankan Bhattacharyya</td>
<td>104</td>
</tr>
<tr>
<td>1662</td>
<td>IJHS-53-2018-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_3_2018__Art13.pdf'>Project Report: The State of Ayurveda in Colonial Bengal </a></td>
<td> Srabani Sen</td>
<td>126</td>
</tr>
<tr>
<td>1663</td>
<td>IJHS-53-2018-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1505</td>
</tr>
<tr>
<td>1664</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art01.pdf'>Editorial: Indo-European Encounter and Features of Modern Science in Pre-Colonial & Colonial India </a></td>
<td> AK Bag</td>
<td>496</td>
</tr>
<tr>
<td>1665</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art02.pdf'>Guest Editorial: Emergence of Modern Science in Colonial India </a></td>
<td> Arnab Rai Choudhuri and Deepak Kumar</td>
<td>94</td>
</tr>
<tr>
<td>1666</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art03.pdf'>Science Institutions in Colonial India: Some Snippets, Some Lessons </a></td>
<td> Deepak Kumar</td>
<td>137</td>
</tr>
<tr>
<td>1667</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art04.pdf'>Indo-Persian and Urdu Speaking Elites’ Discourses on the Modern European Science </a></td>
<td> Gulfishan Khan</td>
<td>3427</td>
</tr>
<tr>
<td>1668</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art05.pdf'>Two Early Pillars of Modern Scientific Education in India: The Meaning and Relevance of the... </a></td>
<td> John Lourdusamy</td>
<td>124</td>
</tr>
<tr>
<td>1669</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art06.pdf'>Curzon’s Role in the Development of Technical and University Education in India </a></td>
<td> Sujata Banerjee and Sunayana Maiti</td>
<td>118</td>
</tr>
<tr>
<td>1670</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art07.pdf'>Shanti Swarup Bhatnagar, Working through/against the Colonial System </a></td>
<td> Robert Anderson</td>
<td>1316</td>
</tr>
<tr>
<td>1671</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art08.pdf'>Judging Scientific Creativity: The Case of the Early Jagadis Bose </a></td>
<td> Subrata Dasgupta</td>
<td>151</td>
</tr>
<tr>
<td>1672</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art09.pdf'>How Costly was Raman’s Equipment for the Discovery of Raman Effect? </a></td>
<td> Rajinder Singh</td>
<td>946</td>
</tr>
<tr>
<td>1673</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art10.pdf'>K S Krishnan as Co-discoverer of Raman Effect and as Independent Scientist </a></td>
<td> DCV Mallik</td>
<td>124</td>
</tr>
<tr>
<td>1674</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art11.pdf'>From Atoms to Stars: Meghnad Saha (1893-1956) </a></td>
<td> Atri Mukhopadhyay</td>
<td>128</td>
</tr>
<tr>
<td>1675</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art12.pdf'>Going Beyond the Big Three of Calcutta Physicists: B B Ray, D M Bose and S K Mitra </a></td>
<td> Rajinder Singh</td>
<td>1586</td>
</tr>
<tr>
<td>1676</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art13.pdf'>Reflecting on Chemical Education: Nilratan Dhar and the Legacy of P C Ray </a></td>
<td> Madhumita Mazumdar</td>
<td>129</td>
</tr>
<tr>
<td>1677</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art14.pdf'>Shaping the Chemical Industry and Saving the Cotton Industry: Role of Sir P C Ray, a Visionary </a></td>
<td> Syamal Chakrabarti</td>
<td>2028</td>
</tr>
<tr>
<td>1678</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art15.pdf'>Organic Chemists of Pre-Independence India: With Special Focus on Natural Products </a></td>
<td> D Balasubramanian</td>
<td>513</td>
</tr>
<tr>
<td>1679</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art16.pdf'>Ronald Ross to U N Brahmachari: Medical Research in Colonial India </a></td>
<td> John Mathew</td>
<td>1298</td>
</tr>
<tr>
<td>1680</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art17.pdf'>History of X-ray Research in Colonial India </a></td>
<td> SC Roy</td>
<td>1023</td>
</tr>
<tr>
<td>1681</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art18.pdf'>Colonial Encounter on Indian Snakes and their Venoms: The Transmission and Transformation... </a></td>
<td> Rahul Bhaumik</td>
<td>138</td>
</tr>
<tr>
<td>1682</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art19.pdf'>Butto Krishna Paul & Co – An Enterprise for Localization of Foreign Medicines in Colonial Calcutta </a></td>
<td> Malika Basu</td>
<td>1385</td>
</tr>
<tr>
<td>1683</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art20.pdf'>Institutionalization of Leprosy Researches in Calcutta School of Tropical Medicine (CSTM) and... </a></td>
<td> Apalak Das</td>
<td>126</td>
</tr>
<tr>
<td>1684</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art21.pdf'>Institutionalizing of Veterinary Science in Colonial India </a></td>
<td> Maidul Rahaman</td>
<td>921</td>
</tr>
<tr>
<td>1685</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art22.pdf'>Birbal Sahni and His Father Ruchi Ram: Science in Punjab Emerging from the Shadows of the Raj </a></td>
<td> Ashok Sahni</td>
<td>950</td>
</tr>
<tr>
<td>1686</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art23.pdf'>Transnational History of Imperial Council of Agricultural Research, 1929–1947 </a></td>
<td> Vinod Kumar Singh</td>
<td>130</td>
</tr>
<tr>
<td>1687</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art24.pdf'>Environmental Science in India during First half of 20th Century </a></td>
<td> Baisakhi Bandyopadhyay</td>
<td>121</td>
</tr>
<tr>
<td>1688</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art25.pdf'>The Beginnings of Modern Astronomy Research in British India: Pogson and Evershed </a></td>
<td> Biman B Nath</td>
<td>646</td>
</tr>
<tr>
<td>1689</td>
<td>IJHS-53-2018-Issue-4</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art26.pdf'>The Forgotten Indian Pioneers of Fingerprint Science: Fallout of Colonialism </a></td>
<td> G S Sodhi and Jasjeet Kaur</td>
<td>1067</td>
</tr>
<tr>
<td>1690</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art27.pdf'>Prasanta Chandra Mahalanobis and the Beginning of the Indian Statistical Institute </a></td>
<td> Samir Kumar Saha</td>
<td>3294</td>
</tr>
<tr>
<td>1691</td>
<td>IJHS-53-2018-Issue-4</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art28.pdf'>Girindrasekhar Bose and the History of Psychoanalysis in India </a></td>
<td> Anup Dhar</td>
<td>145</td>
</tr>
<tr>
<td>1692</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art29.pdf'>The Emergence of Engineering as a Profession in Modern India </a></td>
<td> Aparajith Ramnath</td>
<td>124</td>
</tr>
<tr>
<td>1693</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art30.pdf'>Electrification of Colonial Calcutta: A Social Perspective </a></td>
<td> Suvobrata Sarkar</td>
<td>122</td>
</tr>
<tr>
<td>1694</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art31.pdf'>Role of Indian Science Congress Association, 1914-1947 </a></td>
<td> Sneha Sinha</td>
<td>122</td>
</tr>
<tr>
<td>1695</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Art32.pdf'>FRS Election as a Recognition for Scientists of Colonial India </a></td>
<td> Arnab Rai Choudhuri</td>
<td>533</td>
</tr>
<tr>
<td>1696</td>
<td>IJHS-53-2018-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018-Index.pdf'>Index </a></td>
<td> IJHS</td>
<td>99</td>
</tr>
<tr>
<td>1697</td>
<td>IJHS-53-2018-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018-Cumulativeindex.pdf'>Cumulative Index </a></td>
<td> IJHS</td>
<td>137</td>
</tr>
<tr>
<td>1698</td>
<td>IJHS-53-2018-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/35-Contentsall.pdf'>Annual Contents </a></td>
<td> IJHS</td>
<td>116</td>
</tr>
<tr>
<td>1699</td>
<td>IJHS-53-2018-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol53_4_2018__Books.pdf'>Books Received (2018) & Announcement </a></td>
<td> IJHS</td>
<td>120</td>
</tr>
<tr>
<td>1700</td>
<td>IJHS-54-2019-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>106</td>
</tr>
<tr>
<td>1701</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art01.pdf'>Determination of Kalalagna in the Lagnaprakarana </a></td>
<td> Aditya Kolachana, K Mahesh and K Ramasubramanian</td>
<td>174</td>
</tr>
<tr>
<td>1702</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art02.pdf'>A Painless Surgery Joseph Johnstone Performed on a Mesmerized Patient in Madras in 1847 </a></td>
<td> Ramya Raman and Anantanarayanan Raman</td>
<td>1127</td>
</tr>
<tr>
<td>1703</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art03.pdf'>Glycolic Ferment: The Work of Victor Barral and Raphaël Lépine </a></td>
<td> Jaime Wisniak</td>
<td>153</td>
</tr>
<tr>
<td>1704</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art04.pdf'>U N Brahmachari: Scientific Achievements and Nomination for the Nobel Prize and the Fellowship of... </a></td>
<td> Rajinder Singh and Syamal Roy</td>
<td>2943</td>
</tr>
<tr>
<td>1705</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art05.pdf'>The Relationship between Science and Technology and Evolution in Methods of Knowledge Production </a></td>
<td> R B Grover</td>
<td>621</td>
</tr>
<tr>
<td>1706</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art06.pdf'>A Brief History of Linguistic Science with special reference to the Bodo, Garo and Kokborok... </a></td>
<td> Satarupa Dattamajumdar</td>
<td>192</td>
</tr>
<tr>
<td>1707</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art07.pdf'>Historical Note: Ganeśa Daivajña on Multiplication Tables </a></td>
<td> S R Sarma</td>
<td>156</td>
</tr>
<tr>
<td>1708</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art08.pdf'>Historical Note: Dr. Radhikaram Dhekial Phookan: A Chemist from Assam </a></td>
<td> RC Deka, Gaurangi Maitra, Ranjit Kumar Dev Goswami</td>
<td>2214</td>
</tr>
<tr>
<td>1709</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art09.pdf'>Correspondence: On an Alternative Interpretation for the Application of Cara </a></td>
<td> B S Shylaja</td>
<td>982</td>
</tr>
<tr>
<td>1710</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art10.pdf'>Correspondence: Early Doctorates Conferred by Indian Universities </a></td>
<td> K Razi Naqvi</td>
<td>106</td>
</tr>
<tr>
<td>1711</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art11.pdf'>Book Review: Asutosh Mukhopadhyay: Mathematical Genius with the Magic Wand by Satyabachi Sar </a></td>
<td> U C De</td>
<td>115</td>
</tr>
<tr>
<td>1712</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art12.pdf'>Book Review: Nature’s Third Cycle: A Story of Sunspots by Arnab Rai Choudhuri </a></td>
<td> D C V Mallik</td>
<td>107</td>
</tr>
<tr>
<td>1713</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art13.pdf'>Editing Karaābharaa: A commentary on Karanaprakāśa by Śankaranārāyana Joyisa </a></td>
<td> K Mahesh</td>
<td>142</td>
</tr>
<tr>
<td>1714</td>
<td>IJHS-54-2019-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_1_2019__Art14.pdf'>Environmental and Ecological Change: Gleanings from Copperplate Inscriptions of Early Bengal </a></td>
<td> Rajat Sanyal</td>
<td>1885</td>
</tr>
<tr>
<td>1715</td>
<td>IJHS-54-2019-Issue-2</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>108</td>
</tr>
<tr>
<td>1716</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art01.pdf'>Structure of Indus Script </a></td>
<td> Nisha Yadav</td>
<td>795</td>
</tr>
<tr>
<td>1717</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art02.pdf'>Taxila Mirrors Preserved in India and Technology Transfer </a></td>
<td> Pranab K Chattopadhayay and Satyakam Sen</td>
<td>2029</td>
</tr>
<tr>
<td>1718</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art03.pdf'>An Investigation into Ancient Greco-Indian Medical Exchanges: Sostratus vs Susruta </a></td>
<td> Vijaya Jayant Deshpande</td>
<td>228</td>
</tr>
<tr>
<td>1719</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art04.pdf'>Gustave-Clement Fleury’s Work on Plant Growth and Vegetable Principles in the Nineteenth Century </a></td>
<td> Jaime Wisniak</td>
<td>208</td>
</tr>
<tr>
<td>1720</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art05.pdf'>Jagdish Chandra Bose and Plant Neurobiology: Part I </a></td>
<td> Prakash N Tandon</td>
<td>906</td>
</tr>
<tr>
<td>1721</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art06.pdf'>Forensic Science and Scientific Measures of Criminal Identification in British India </a></td>
<td> Saumitra Basu</td>
<td>161</td>
</tr>
<tr>
<td>1722</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art07.pdf'>Historical Note: The Trend of Research on Number Theory in Bengal and Bihar during the 20th Century </a></td>
<td> Purabi Mukherji</td>
<td>139</td>
</tr>
<tr>
<td>1723</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art08.pdf'>Historical Note: Metric Estimate of the Volume Measure used in the Madras Region at the Dawn of... </a></td>
<td> Venkatesh Parthasarathy</td>
<td>566</td>
</tr>
<tr>
<td>1724</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art09.pdf'>Historical Note: Scientific Activities of Fr. Alphonso De Penaranda: A Jesuit Priest in the late... </a></td>
<td> Subhankar Ghosh</td>
<td>112</td>
</tr>
<tr>
<td>1725</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art10.pdf'>Correspondence: On an Alternative Interpretation for the Application of Cara: A Response </a></td>
<td> Aditya Kolachana et al.</td>
<td>115</td>
</tr>
<tr>
<td>1726</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art11.pdf'>Book Review: Narada Silpasastra: Sanskrit Text on Architectural Civil Engineering </a></td>
<td> Sashikala Ananth</td>
<td>173</td>
</tr>
<tr>
<td>1727</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art12.pdf'>Book Review: Story of a Steel Bridge: The Howrah Bridge –A Testimony of Indo British Co-operation... </a></td>
<td> C V R Murty</td>
<td>117</td>
</tr>
<tr>
<td>1728</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art13.pdf'>Project Report: Plant Biology of Yajurveda </a></td>
<td> Raghava S Boddupalli</td>
<td>2961</td>
</tr>
<tr>
<td>1729</td>
<td>IJHS-54-2019-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_2_2019__Art14.pdf'>Project Report: Suryaprakasa of Suryadasa — Critical Edition, Eng. Tr. and Explanatory Notes for... </a></td>
<td> Sita Sundar Ram</td>
<td>160</td>
</tr>
<tr>
<td>1730</td>
<td>IJHS-54-2019-Issue-3</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1498</td>
</tr>
<tr>
<td>1731</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art01.pdf'>The Untapped Wealth of Manuscripts on Indian Astronomy and Mathematics </a></td>
<td> M. D. Srinivas</td>
<td>206</td>
</tr>
<tr>
<td>1732</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Math</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art02.pdf'>On the Persian Translation of Bhāskara’s Līlāvatī by Abu’l Faiẓ Faiẓī at the Court of Akbar </a></td>
<td> Sreeramula Rajeswara Sarma, Maryam Zamani</td>
<td>5741</td>
</tr>
<tr>
<td>1733</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art03.pdf'>Sidereal Ecliptic Coordinate System of Sūryasiddhānta </a></td>
<td> Raja Ram Mohan Roy</td>
<td>331</td>
</tr>
<tr>
<td>1734</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art04.pdf'>Precise Determination of the Ascendant in the Lagnaprakaraṇa - I </a></td>
<td> Aditya Kolachana, K. Mahesh, K. Ramasubramanian</td>
<td>166</td>
</tr>
<tr>
<td>1735</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art05.pdf'>Epigastric-heteropagus Twins Recorded in Madras Presidency in 1789 </a></td>
<td> Ramya Raman, Anantanarayanan Raman</td>
<td>280</td>
</tr>
<tr>
<td>1736</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art06.pdf'>Sukumar Chandra Sirkar and the Department of Optics at the IACS </a></td>
<td> Rajinder Singh</td>
<td>600</td>
</tr>
<tr>
<td>1737</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art07.pdf'>Agricultural Sciences in India and Struggle against Famine, Hunger and Malnutrition </a></td>
<td> Rajendra Prasad</td>
<td>137</td>
</tr>
<tr>
<td>1738</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art08.pdf'>Historical Note: Characterization of Pigments and Binders in Mural Painting Fragments from... </a></td>
<td> M. R. Singh, B. R. Mani</td>
<td>1133</td>
</tr>
<tr>
<td>1739</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art10.pdf'>Historical Note: The Sacred Road: A Contribution to the History of Ramesvaram Pilgrimages </a></td>
<td> Jean Deloche</td>
<td>24713</td>
</tr>
<tr>
<td>1740</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Math</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art11.pdf'>Historical Note: Hardinge Professorship of Higher Mathematics at Calcutta University </a></td>
<td> Sabitri Ray Chaudhuri</td>
<td>107</td>
</tr>
<tr>
<td>1741</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art12.pdf'>Book Review: Early Indian Metallurgy: The Production of Lead, Silver and Zinc through Three... </a></td>
<td> Sharada Srinivasan</td>
<td>94</td>
</tr>
<tr>
<td>1742</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art13.pdf'>Project Report: Practice of Folk Medicine by Rajbanshis of Sub-Himalayan Bengal: A Study in... </a></td>
<td> Rup Kumar Barman</td>
<td>1456</td>
</tr>
<tr>
<td>1743</td>
<td>IJHS-54-2019-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_3_2019__Art14.pdf'>Obituary: B. V. Subbarayappa: A Writer, Administrator and Veteran Historian of Science </a></td>
<td> K. Ramasubramanian</td>
<td>397</td>
</tr>
<tr>
<td>1744</td>
<td>IJHS-54-2019-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents_Vol54_4.pdf'>Contents </a></td>
<td> IJHS</td>
<td>38</td>
</tr>
<tr>
<td>1745</td>
<td>IJHS-54-2019-Issue-4</td>
<td>Astronomy</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_4_2019__Art01.pdf'>Guáman Poma’s Yupana and Inca Astronomy </a></td>
<td> Subhash Kak</td>
<td>3722</td>
</tr>
<tr>
<td>1746</td>
<td>IJHS-54-2019-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_4_2019__Art02.pdf'>On the Computation of Daily-motion in Ancient Indian Astronomy </a></td>
<td> Anil Narayanan</td>
<td>2286</td>
</tr>
<tr>
<td>1747</td>
<td>IJHS-54-2019-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_4_2019__Art03.pdf'>Kuṣṭha, Saussurea costus (Saussurea lappa): Its Unexplored History from the Atharvaveda </a></td>
<td> N. C. Shah</td>
<td>3581</td>
</tr>
<tr>
<td>1748</td>
<td>IJHS-54-2019-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_4_2019__Art04.pdf'>Cholera, Commerce and Quarantine: Interrogating the Science of Empire in Nineteenth Century India </a></td>
<td> Arabinda Samanta</td>
<td>95</td>
</tr>
<tr>
<td>1749</td>
<td>IJHS-54-2019-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_4_2019__Art05.pdf'>Dr. Koman’s Report and Responses of Native Physicians: A Discourse on Indigenous Systems of Medicine </a></td>
<td> Kanagarathinam D. V.</td>
<td>142</td>
</tr>
<tr>
<td>1750</td>
<td>IJHS-54-2019-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_4_2019__Art06.pdf'>Translating Nature: Changes in the Perception and Utilization of Science in the Halle Mission in... </a></td>
<td> Niklas Thode Jensen</td>
<td>3869</td>
</tr>
<tr>
<td>1751</td>
<td>IJHS-54-2019-Issue-4</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_4_2019__Art08.pdf'>Historical Note: C. V. Raman and Kolkata Media </a></td>
<td> Rajinder Singh</td>
<td>5540</td>
</tr>
<tr>
<td>1752</td>
<td>IJHS-54-2019-Issue-4</td>
<td>Agriculture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol54_4_2019__Art09.pdf'>Project Report: A Study on the Salt Production of Ancient Assam </a></td>
<td> Raktim Ranjan Saikia, Nurul Amin</td>
<td>406</td>
</tr>
<tr>
<td>1753</td>
<td>IJHS-55-2020-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>47</td>
</tr>
<tr>
<td>1754</td>
<td>IJHS-55-2020-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__Art01.pdf'>Precise Determination of the Ascendant in Lagnaprakarana – II </a></td>
<td> Aditya Kolachana, K. Mahesh, K. Ramasubramanian</td>
<td>226</td>
</tr>
<tr>
<td>1755</td>
<td>IJHS-55-2020-Issue-1</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__Art02.pdf'>Marble-like chûnnam in the 18th- and 19th-century Madras Presidency </a></td>
<td> Anantanarayanan Raman</td>
<td>1101</td>
</tr>
<tr>
<td>1756</td>
<td>IJHS-55-2020-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__Art03.pdf'>Retrograde motion as described in Brahmatulyaudāharaṇam of Viśvanātha </a></td>
<td> B. S. Shylaja, B. S. Shubha</td>
<td>689</td>
</tr>
<tr>
<td>1757</td>
<td>IJHS-55-2020-Issue-1</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__Art04.pdf'>An Alternative History of Technology in South Asia: The Unknown Viśvakarmās of Colonial Bengal </a></td>
<td> Suvobrata Sarkar</td>
<td>2267</td>
</tr>
<tr>
<td>1758</td>
<td>IJHS-55-2020-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__Art05.pdf'>Political Ecology of Cholera: Orissa and Colonial Sanitary Discourse </a></td>
<td> Chandi Prasad Nanda</td>
<td>141</td>
</tr>
<tr>
<td>1759</td>
<td>IJHS-55-2020-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__Art06.pdf'>Historical Note: Sir C. V. Raman Nobel Ceremony Coverage by the European Press </a></td>
<td> Rajinder Singh</td>
<td>6056</td>
</tr>
<tr>
<td>1760</td>
<td>IJHS-55-2020-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__Art07.pdf'>Project Report: Hundred Years of Forensic Science in India (1849–1947): A Historical Perspective </a></td>
<td> Saumitra Basu</td>
<td>5672</td>
</tr>
<tr>
<td>1761</td>
<td>IJHS-55-2020-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_1_2020__Art08.pdf'>Obituary to Dr Yukio Ôhashi </a></td>
<td> Michio Yano</td>
<td>171</td>
</tr>
<tr>
<td>1762</td>
<td>IJHS-55-2020-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>47</td>
</tr>
<tr>
<td>1763</td>
<td>IJHS-55-2020-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Art01.pdf'>Precise Determination of the Ascendant in the Lagnaprakaraṇa–III </a></td>
<td> Aditya Kolachana, K. Mahesh, K. Ramasubramanian</td>
<td>164</td>
</tr>
<tr>
<td>1764</td>
<td>IJHS-55-2020-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Art02.pdf'>G.M.M.C. Diploma of the Madras Medical College, 1847–1863 </a></td>
<td> Anantanarayanan Raman</td>
<td>14238</td>
</tr>
<tr>
<td>1765</td>
<td>IJHS-55-2020-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Art03.pdf'>The Silent Killer: Tracing the Trajectory of Tubercular Deaths in Colonial Bengal </a></td>
<td> Suvankar Dey</td>
<td>152</td>
</tr>
<tr>
<td>1766</td>
<td>IJHS-55-2020-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Art04.pdf'>Fractal Geometry in Water Conservation Structures: Step Wells and Tanks in India </a></td>
<td> Samirsinh P. Parmara, Debi Prasad Mishra</td>
<td>8403</td>
</tr>
<tr>
<td>1767</td>
<td>IJHS-55-2020-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Art05.pdf'>The Wartime Correspondence (1939–1945) between South African Geologist A. L. du Toit and Indian... </a></td>
<td> Sharad Master</td>
<td>741</td>
</tr>
<tr>
<td>1768</td>
<td>IJHS-55-2020-Issue-2</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Art06.pdf'>Historical Note: Traditional Use of Legume Seeds for Weighing Gold in India </a></td>
<td> Raghava S. Boddupalli</td>
<td>2930</td>
</tr>
<tr>
<td>1769</td>
<td>IJHS-55-2020-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Art07.pdf'>Project Report: Grahagaṇitādhyāya of Bhāskarācārya’s Siddhāntaśiromaṇi </a></td>
<td> M S Sriram</td>
<td>421</td>
</tr>
<tr>
<td>1770</td>
<td>IJHS-55-2020-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_2_2020__Art08.pdf'>Seminar Report: Religious Art and Culture in 2019: Thousand Faces of the Buddha </a></td>
<td> R. K. K. Rajarajana, Li-ling</td>
<td>11046</td>
</tr>
<tr>
<td>1771</td>
<td>IJHS-55-2020-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>40</td>
</tr>
<tr>
<td>1772</td>
<td>IJHS-55-2020-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Art01.pdf'>Akṣara the Basic Unit of Time Measure in Ancient India </a></td>
<td> R. N. Iyengar, H. S. Sudarshan, Anand Viswanathan</td>
<td>1284</td>
</tr>
<tr>
<td>1773</td>
<td>IJHS-55-2020-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Art02.pdf'>History of Mining in India </a></td>
<td> A. K. Soni</td>
<td>2634</td>
</tr>
<tr>
<td>1774</td>
<td>IJHS-55-2020-Issue-3</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Art03.pdf'>Hindi Protagonists of Science and Swadeshi in the First Half of the Twentieth Century </a></td>
<td> Dhrub Kumar Singh</td>
<td>122</td>
</tr>
<tr>
<td>1775</td>
<td>IJHS-55-2020-Issue-3</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Art04.pdf'>Frédéric Sacc (1819–1890) Contribution to Plant and Animal Physiology </a></td>
<td> Jaime Wisniak</td>
<td>115</td>
</tr>
<tr>
<td>1776</td>
<td>IJHS-55-2020-Issue-3</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Art05.pdf'>The History and Functioning of the Forest Department in Madras Presidency during 1856–1882 </a></td>
<td> S Kamini</td>
<td>97</td>
</tr>
<tr>
<td>1777</td>
<td>IJHS-55-2020-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Art06.pdf'>Historical Note: Kadambini Ganguly: A Forgotten Legend </a></td>
<td> Gargi Das</td>
<td>600</td>
</tr>
<tr>
<td>1778</td>
<td>IJHS-55-2020-Issue-3</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Art07.pdf'>Historical Note: Nikhil Rajan Sen – The Formative Years  </a></td>
<td> Rajinder Singh</td>
<td>3406</td>
</tr>
<tr>
<td>1779</td>
<td>IJHS-55-2020-Issue-3</td>
<td>Medicine</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_3_2020__Art08.pdf'>Project Report: Meta-analytical Study of Cardiac Drugs described by Ibn Sina (980–1037) in the... </a></td>
<td> Syed Ziaur Rahman, S. H. Zahid Jamal</td>
<td>152</td>
</tr>
<tr>
<td>1780</td>
<td>IJHS-55-2020-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>29</td>
</tr>
<tr>
<td>1781</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art01.pdf'>The Epigraphic Evidences on Ayurveda and Indian Medical Heritage </a></td>
<td> Goli Penchala Prasada, P. Murali Manohar...</td>
<td>886</td>
</tr>
<tr>
<td>1782</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art02.pdf'>Historical Perspectives of Geological Concepts from Biblical to Modern Times </a></td>
<td> Sudipta Lahiri, B. J. Sengupta</td>
<td>141</td>
</tr>
<tr>
<td>1783</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art03.pdf'>Letters between Geologists A. L. du Toit and M. S. Krishnan (1946–1947) on the Palaeoposition of... </a></td>
<td> Sharad Master</td>
<td>1118</td>
</tr>
<tr>
<td>1784</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art04.pdf'>Microscopic Imaging of Entrapped Slag in Ancient IronArtifact (300 BCE) from the Middle Ganga Plains </a></td>
<td> Vandana Singh, Manager Rajdeo Singh</td>
<td>2925</td>
</tr>
<tr>
<td>1785</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art05.pdf'>Woods used in 10th Century Trans Himalayan Tabo Buddhist Monastery of India </a></td>
<td> Sangeeta Guptaa, Deepa Bisht, Prachi Gupta</td>
<td>686</td>
</tr>
<tr>
<td>1786</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art10.pdf'>Indian Tradition of Palm Print Authentication and the Globetrotting Journey of Kohinoor Diamond </a></td>
<td> Jasjeet Kaur, G. S. Sodhi</td>
<td>1002</td>
</tr>
<tr>
<td>1787</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art06.pdf'>Historical Note: Plant Domestication in Indus Valley Civilisation </a></td>
<td> R. B. Mohanty, T. Panda</td>
<td>88</td>
</tr>
<tr>
<td>1788</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art07.pdf'>Historical Note: Professor Manindra Chandra Chaki (1913 – 2007): A Legendary Indian Geometrician </a></td>
<td> Sanatan Koley</td>
<td>252</td>
</tr>
<tr>
<td>1789</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art08.pdf'>Correspondence: Retrograde motion: The Derivation of Formula </a></td>
<td> Tejas Kumar, Shubha B S, Shylaja B S</td>
<td>173</td>
</tr>
<tr>
<td>1790</td>
<td>IJHS-55-2020-Issue-4</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__Art09.pdf'>Project Report: The Science and Technology of Manuscript Writing-aid and Folk Paintings in Medieval  </a></td>
<td> Robin Kumar Dutta, Barsha R. Goswami, Niranjan Lig</td>
<td>10214</td>
</tr>
<tr>
<td>1791</td>
<td>IJHS-55-2020-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__CIndex.pdf'>Cumulative Index: Vol 55.1-4 </a></td>
<td> IJHS</td>
<td>35</td>
</tr>
<tr>
<td>1792</td>
<td>IJHS-55-2020-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Vol55_4_2020__AnnualContents.pdf'>Annual Contents: Vol. 55.1-4 (2020) </a></td>
<td> IJHS</td>
<td>41</td>
</tr>
<tr>
<td>1793</td>
<td>IJHS-56-2021-issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Content.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1492</td>
</tr>
<tr>
<td>1794</td>
<td>IJHS-56-2021-issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/1-13.pdf'>Precise Determination of the Ascendant in the Lagnaprakaraṇa-IV </a></td>
<td> Aditya Kolachana, K. Mahesh and K. Ramasubramanian</td>
<td>8670</td>
</tr>
<tr>
<td>1795</td>
<td>IJHS-56-2021-issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/14-19.pdf'>Could the “Case for Revising the Date of Vedāṅga Jyotiṣa” be Flawed? </a></td>
<td> Prabhakar Gondhalekar</td>
<td>3539</td>
</tr>
<tr>
<td>1796</td>
<td>IJHS-56-2021-issue-1</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/20-27.pdf'>Genius and Premature Birth: Little Evidence that Claims About Historically Eminent Scientists are... </a></td>
<td> E Dutton, G Madison and Dimitri van der Linden</td>
<td>3551</td>
</tr>
<tr>
<td>1797</td>
<td>IJHS-56-2021-issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/28-36.pdf'>Whiggism, Creativity and the Historiography of Technoscience </a></td>
<td> Subrata Dasgupta</td>
<td>3476</td>
</tr>
<tr>
<td>1798</td>
<td>IJHS-56-2021-issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/37-48.pdf'>Putting Nicobar Islands on the Map: Intersections of Colonial Knowledge, Trade and... </a></td>
<td> Shaina Sehgal</td>
<td>3552</td>
</tr>
<tr>
<td>1799</td>
<td>IJHS-56-2021-issue-1</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/49-59.pdf'>An Assessment of Environment Friendly Methods of Khadi Manufacturing </a></td>
<td> Shruti Gupta, Deepali Rastogi and Ritu Mathur</td>
<td>14374</td>
</tr>
<tr>
<td>1800</td>
<td>IJHS-56-2021-issue-1</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/60-64.pdf'>Historical Notes: A Brief History of the Fertilizer Nitrogen </a></td>
<td> Rajendra Prasad and Y. S. Shivay</td>
<td>3509</td>
</tr>
<tr>
<td>1801</td>
<td>IJHS-56-2021-issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/65-69.pdf'>Historical Notes: A papier-maché Human Anatomical Model used in the Madras Medical Establishment... </a></td>
<td> Ramya Raman and Anantanarayanan Raman</td>
<td>7972</td>
</tr>
<tr>
<td>1802</td>
<td>IJHS-56-2021-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/0__Content.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1505</td>
</tr>
<tr>
<td>1803</td>
<td>IJHS-56-2021-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/1__Mahesh.pdf'>Elegant dissection proofs for algebraic identities in Nīlakantha's Āryabhatīyabhāsya </a></td>
<td> K. Mahesh, D. G. Sooryanarayan, K. Ramasubramanian</td>
<td>5468</td>
</tr>
<tr>
<td>1804</td>
<td>IJHS-56-2021-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/2__Chauthaiwale.pdf'>Computing the number of perfumes that constitute the gandhārṇava and kacchapuṭa of Varāhamihira </a></td>
<td> S Chauthaiwale · Jayant Deopujari · A Chauthaiwale</td>
<td>3671</td>
</tr>
<tr>
<td>1805</td>
<td>IJHS-56-2021-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/3__Thomas.pdf'>Parallels of Gundestrup cauldron interior art with Indic motifs </a></td>
<td> Thomas E. Petray Jr</td>
<td>2335</td>
</tr>
<tr>
<td>1806</td>
<td>IJHS-56-2021-Issue-2</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/4__Sasisekaran.pdf'>Archaeo-metallurgical study on two early historic punch marked coins </a></td>
<td> B. Sasisekaran and B. Raghunatha Rao</td>
<td>7365</td>
</tr>
<tr>
<td>1807</td>
<td>IJHS-56-2021-Issue-2</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/5__Jitendra.pdf'>Colonization of personality psychology in India: historical roots and contemporary status </a></td>
<td> Jitendra K. Singh</td>
<td>3749</td>
</tr>
<tr>
<td>1808</td>
<td>IJHS-56-2021-Issue-2</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/6__Arnab Rai Choudhuri.pdf'>Unsuccessful FRS nominations from colonial India </a></td>
<td> Arnab Rai Choudhuri</td>
<td>7500</td>
</tr>
<tr>
<td>1809</td>
<td>IJHS-56-2021-Issue-2</td>
<td>Other</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/7__Satyanad.pdf'>Book Review- Karanapaddhati of Putumana Somayājī by Venketeswara Pai... </a></td>
<td> Satyanad Kichenassamy</td>
<td>3765</td>
</tr>
<tr>
<td>1810</td>
<td>IJHS-56-2021-Issue-2</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/8__Maidul.pdf'>Project Report: Institutionalization of veterinary science in colonial India </a></td>
<td> Maidul Rahaman</td>
<td>3463</td>
</tr>
<tr>
<td>1811</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1498</td>
</tr>
<tr>
<td>1812</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/1.pdf'>Transit of sun through the seasonal naksatra cycle in the Vrddha-Gārgīya Jyotisa </a></td>
<td> R. N. Iyengar and Sunder Chakravarty</td>
<td>5789</td>
</tr>
<tr>
<td>1813</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/2.pdf'>Combinatorial techniques in Munīśvara’s Nisṛṣṭārthadūtī </a></td>
<td> K. Mahesh· Aditya Kolachana· K. Ramasubramanian</td>
<td>3566</td>
</tr>
<tr>
<td>1814</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/3.pdf'>The production of crucible steel by the ‘Mysore process’ at Ghattihosahalli, Chitradurga District... </a></td>
<td> K. Nagesh Rao,P. T. Craddock and T. R. Anantharamu</td>
<td>11445</td>
</tr>
<tr>
<td>1815</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/4.pdf'>Indigenous knowledge on ancient Indian alchemical alloying </a></td>
<td> N. Anantha Krishna et al.</td>
<td>8450</td>
</tr>
<tr>
<td>1816</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/5.pdf'>Formation-to-fall: natural history and the journey of a lesser-known genus of orchids, Monomeria </a></td>
<td> Uma Shankar</td>
<td>26324</td>
</tr>
<tr>
<td>1817</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/6.pdf'>Historical Note: Microstructural analysis and characterization of lime mortar of seventeenth... </a></td>
<td> M. R. Singh and Rajendra Yadav</td>
<td>8015</td>
</tr>
<tr>
<td>1818</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/7.pdf'>Correspondence: A remark on the editorial “Indo-European encounter and features of modern science... </a></td>
<td> B. A. Dasannacharya</td>
<td>3247</td>
</tr>
<tr>
<td>1819</td>
<td>IJHS-56-2021-Issue-3&4</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/8.pdf'>Project Report: Hati Puthi: the medieval Assamese manuscripts on elephant training and treatment </a></td>
<td> Rasna Rajkhowa</td>
<td>4367</td>
</tr>
<tr>
<td>1820</td>
<td>IJHS-57-2022-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1498</td>
</tr>
<tr>
<td>1821</td>
<td>IJHS-57-2022-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/1_PM Dolas.pdf'>Astronomical clues in unicorn iconography of the Harappan civilization </a></td>
<td> Prakash M. Dolas</td>
<td>6455</td>
</tr>
<tr>
<td>1822</td>
<td>IJHS-57-2022-Issue-1</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/2_NC Shah.pdf'>The identification, etymology and uses of Bombax ceiba (semal) sold by street vendors as Semarkanda </a></td>
<td> N. C. Shah</td>
<td>4879</td>
</tr>
<tr>
<td>1823</td>
<td>IJHS-57-2022-Issue-1</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/3_F Di Giacomo.pdf'>On some analogies of modern science with Plato’s science in Timaeus and on Plato’s influence... </a></td>
<td> Francesco Di Giacomo</td>
<td>3578</td>
</tr>
<tr>
<td>1824</td>
<td>IJHS-57-2022-Issue-1</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/4_S Dasgupta.pdf'>Jagadis Bose’s panvitalism as intellectual history </a></td>
<td> Subrata Dasgupta</td>
<td>3017</td>
</tr>
<tr>
<td>1825</td>
<td>IJHS-57-2022-Issue-1</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/5_P Sharma.pdf'>Satellite Instructional Television Experiment (SITE): a case study in the triumphs and... </a></td>
<td> Pranav Sharma</td>
<td>7085</td>
</tr>
<tr>
<td>1826</td>
<td>IJHS-57-2022-Issue-1</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/6_R Ghosh.pdf'>Contribution of Sir P.C. Rây in preparing chemical bombs and explosives for Indian freedom fighters </a></td>
<td> Rajarshi Ghosh</td>
<td>3274</td>
</tr>
<tr>
<td>1827</td>
<td>IJHS-57-2022-Issue-1</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/7_MA Wani.pdf'>Colonial masculinity and indigenous sikārī: a history of sport-hunting in Kashmir during Dogra rule </a></td>
<td> Mohd Ashraf Wani and Rouf Ahmad Bhat</td>
<td>2960</td>
</tr>
<tr>
<td>1828</td>
<td>IJHS-57-2022-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/8_S Kulangara.pdf'>Historical Note- Jvaranirnaya: a rare monograph on diagnosis of fevers from the pre-colonial era </a></td>
<td> Shyamasundaran Kulangara & Sushma N Salethoor</td>
<td>3028</td>
</tr>
<tr>
<td>1829</td>
<td>IJHS-57-2022-Issue-1</td>
<td>Other</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/9_B Goswami.pdf'>Book Review: Essays in History of Sciences in India: Agriculture, Medicine, Alchemical and... </a></td>
<td> Bijoya Goswami</td>
<td>2936</td>
</tr>
<tr>
<td>1830</td>
<td>IJHS-57-2022-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_Content.pdf'>Content </a></td>
<td> IJHS</td>
<td>1477</td>
</tr>
<tr>
<td>1831</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_1.pdf'>Skin disorders (twak rogas) revealed in the Atharvaveda:Descriptions of medicinal plants and utiliza </a></td>
<td> Raghava S Boddupalli</td>
<td>3702</td>
</tr>
<tr>
<td>1832</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_2.pdf'>Therapeutic elements of music in ancient India: a brief review in Bṛhattrayī </a></td>
<td> Abirlal Gangopadhyay </td>
<td>528</td>
</tr>
<tr>
<td>1833</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_3.pdf'>Insight into history of Areca nut and oral submucous fibrosis: a narrative review </a></td>
<td> Rashmi Venkatesh</td>
<td>418</td>
</tr>
<tr>
<td>1834</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_4.pdf'>Medical profession and unemployment in colonial Madras (1835–1930) </a></td>
<td> Gautam Chandra</td>
<td>466</td>
</tr>
<tr>
<td>1835</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_5.pdf'>Modernization of leather industry and chequered history of technical education in colonial Kanpur </a></td>
<td> Prakrati Bhargava</td>
<td>454</td>
</tr>
<tr>
<td>1836</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_6.pdf'>Fishing, migration, and settlement: a study of Kaibartas in Majuli Island, Assam </a></td>
<td> Debasish Dey</td>
<td>2196</td>
</tr>
<tr>
<td>1837</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Other</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_7.pdf'>Translation of Newton’s Principia into Arabic under the aegis of the East India Company: a rumour tu </a></td>
<td> K. Razi Naqvi</td>
<td>1768</td>
</tr>
<tr>
<td>1838</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_8.pdf'>Dr. Chunilal Bose: a forgotten scientist and a science communicator </a></td>
<td> Indranil Sanyal</td>
<td>627</td>
</tr>
<tr>
<td>1839</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_9.pdf'>Contribution of Satyendra Nath Bose in chemical sciences and related disciplines </a></td>
<td> Rajarshi Ghosh</td>
<td>348</td>
</tr>
<tr>
<td>1840</td>
<td>IJHS-57-2022-Issue-2</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_2_10.pdf'>Let There Be Light: Engineering, Entrepreneurship and Electricity in Colonial Bengal 1880–1945 by Su </a></td>
<td> Kamlesh Mohan</td>
<td>300</td>
</tr>
<tr>
<td>1841</td>
<td>IJHS-57-2022-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_Content.pdf'>Content </a></td>
<td> Content</td>
<td>1586</td>
</tr>
<tr>
<td>1842</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_1.pdf'>Indus zoomorphism and its avatars </a></td>
<td> M.V. Bhaskar</td>
<td>3887</td>
</tr>
<tr>
<td>1843</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_2.pdf'>Reassessing European impressions of Indian astronomy (1750–1850) </a></td>
<td> Ankur Kakkar</td>
<td>439</td>
</tr>
<tr>
<td>1844</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_3.pdf'>The origins of scientific disciplines: a counter-history of western science </a></td>
<td> Roberto G. Barbosa</td>
<td>454</td>
</tr>
<tr>
<td>1845</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_4.pdf'>Cattle plague and the introduction of veterinary education in colonial Bengal </a></td>
<td> Jhinuk Sarkar</td>
<td>376</td>
</tr>
<tr>
<td>1846</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Metallurgy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_5.pdf'>Technological modifi cations in the tanning and leather industry from pre-British to colonial Punjab </a></td>
<td> Mandakini Thakur</td>
<td>395</td>
</tr>
<tr>
<td>1847</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Other</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_6.pdf'>Meghnad Saha, F.R.S.: the multiple facets of a teacher </a></td>
<td> Samir Kumar Saha</td>
<td>355</td>
</tr>
<tr>
<td>1848</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_7.pdf'>History of ARIES: a premier research institute in the area of observational sciences </a></td>
<td> Ram Sagar</td>
<td>2635</td>
</tr>
<tr>
<td>1849</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_3_8.pdf'>Ethno-medico-botanical studies of Eruliga and Lambani tribes of Kanakapura taluk of Ramanagara distr </a></td>
<td> M. P. Shivamanjunatha</td>
<td>368</td>
</tr>
<tr>
<td>1850</td>
<td>IJHS-57-2022-Issue-3</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/S1-IndusZoomorphicIconCatalogue.pdf'>Indus zoomorphism and its avatars- supplement </a></td>
<td> M. V. Bhaskar</td>
<td>1065</td>
</tr>
<tr>
<td>1851</td>
<td>IJHS-57-2022-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_Content.pdf'>Content </a></td>
<td> Content</td>
<td>1469</td>
</tr>
<tr>
<td>1852</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_1.pdf'>Representation of the midnight sun in Greek and Indian astronomical texts </a></td>
<td> Vinay Iyer</td>
<td>914</td>
</tr>
<tr>
<td>1853</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_2.pdf'>Documenting Flora Indica: Dysentery, William Roxburgh and medical botany </a></td>
<td> Pranjali</td>
<td>399</td>
</tr>
<tr>
<td>1854</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_3.pdf'>Physics and physicists at Banaras Hindu University: circa 1916–1960 </a></td>
<td> Ritesh Gupta</td>
<td>1221</td>
</tr>
<tr>
<td>1855</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_4.pdf'>Dr. Gopaul Chunder Roy (1844–1887): An extraordinary life dedicated to the cause of medical science </a></td>
<td> Indranil Sanyal</td>
<td>1962</td>
</tr>
<tr>
<td>1856</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_5.pdf'>A review on rock paintings of India: Technique, pigment and conservation </a></td>
<td> Anjali Sharma</td>
<td>1106</td>
</tr>
<tr>
<td>1857</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Metallurgy</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_6.pdf'>Journey of natural pigments from ancient antiquity to present: Insights on sustainable development </a></td>
<td> Shrabana Sarkar</td>
<td>1243</td>
</tr>
<tr>
<td>1858</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Culture</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_7.pdf'>Perspective and retrospective of the Indian Social Science Academy, Allahabad, India </a></td>
<td> G. Parthasarathy</td>
<td>329</td>
</tr>
<tr>
<td>1859</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_8.pdf'>Gaṇitagannaḍi: An astronomical text of 1604 CE in Kannada by Śankaranārāyaṇa Joisaru of Śṛngeri </a></td>
<td> A. Sripada Bhat</td>
<td>333</td>
</tr>
<tr>
<td>1860</td>
<td>IJHS-57-2022-Issue-4</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_9.pdf'>The status of tribal medical system and practices in the Jungle Mahals, Eastern India, 1947–2000 </a></td>
<td> Nirmal Kumar Mahato</td>
<td>377</td>
</tr>
<tr>
<td>1861</td>
<td>IJHS-57-2022-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/57_4_10.pdf'>Lalit K. Gurjar M.Sc. </a></td>
<td> Paul T. Craddock</td>
<td>659</td>
</tr>
<tr>
<td>1862</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_Content.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1511</td>
</tr>
<tr>
<td>1863</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_1.pdf'>Calculation for ‘chain‑reduction’ in the Triśatībhāṣya </a></td>
<td> Taro Tokutake</td>
<td>1401</td>
</tr>
<tr>
<td>1864</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Chemistry</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_2.pdf'>Object‑numerals as listed in Nijaguṇa Śivayogī ’s Viveka‑Cintāmaṇi </a></td>
<td> Dipak Jadhav</td>
<td>467</td>
</tr>
<tr>
<td>1865</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_3.pdf'>An intellectual history of P.C. Ray’s papers on the nitrites of mercury </a></td>
<td> Subrata Dasgupta</td>
<td>454</td>
</tr>
<tr>
<td>1866</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_4.pdf'>Use of animals in the health management of elephants in medieval period of Assam, India </a></td>
<td> Rasna Rajkhowa, Bipul Ch. Saikia</td>
<td>1072</td>
</tr>
<tr>
<td>1867</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_5.pdf'>History of an observatory on the Agasthiyar hill top </a></td>
<td> R. Jayakrishnan</td>
<td>969</td>
</tr>
<tr>
<td>1868</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_6.pdf'>Indigenous poison healing traditions in Kerala </a></td>
<td> Y. Srinivasa Rao, Sindhu Thomas</td>
<td>418</td>
</tr>
<tr>
<td>1869</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_7.pdf'>Food, water and intoxicants in the battlefield practices of Rajasthan </a></td>
<td> Aalok Pandya</td>
<td>836</td>
</tr>
<tr>
<td>1870</td>
<td>IJHS-58-2023-Issue-1</td>
<td>nan</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_8.pdf'>Historical Note: Hundred years of geophysics (1834–1933) </a></td>
<td> Indrajit G. Roy</td>
<td>470</td>
</tr>
<tr>
<td>1871</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_9.pdf'>Historical Note: From forest to plantation: a brief history of the rubber tree </a></td>
<td> T. S. Suryanarayanan,  João Lúcio Azevedo</td>
<td>425</td>
</tr>
<tr>
<td>1872</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58_1_10.pdf'>Book Review: Science and religion in India... </a></td>
<td> Robert S. Anderson</td>
<td>312</td>
</tr>
<tr>
<td>1873</td>
<td>IJHS-58-2023-Issue-1</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/58-1_11.pdf'>Project Report: Science in the forest management in colonial Assam (1826–1947) </a></td>
<td> Geetashree Singh</td>
<td>347</td>
</tr>
<tr>
<td>1874</td>
<td>IJHS-58-2023-Issue-2</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_2_Contents.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1595</td>
</tr>
<tr>
<td>1875</td>
<td>IJHS-58-2023-Issue-2</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_2_1.pdf'>Planetary nodes and apses in the Sūrya-Siddhānta </a></td>
<td> Anil Narayanan and Nilesh Oak</td>
<td>3946</td>
</tr>
<tr>
<td>1876</td>
<td>IJHS-58-2023-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_2_2.pdf'>Recursion and iteration in combinatorics of Chandaśśāstra </a></td>
<td> Amba Kulkarni</td>
<td>3499</td>
</tr>
<tr>
<td>1877</td>
<td>IJHS-58-2023-Issue-2</td>
<td>Astronomy</td>
<td>Other</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_2_3.pdf'>A brief study on history and evolution of time </a></td>
<td> US Ganesamoorthy, CG Moorthy</td>
<td>2965</td>
</tr>
<tr>
<td>1878</td>
<td>IJHS-58-2023-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS58_2_4.pdf'>Historical profi le of Nardostachys jatamansi: an ancient incense & aromatic medicinal herb from... </a></td>
<td> N. C. Shah</td>
<td>4766</td>
</tr>
<tr>
<td>1879</td>
<td>IJHS-58-2023-Issue-2</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_2_5.pdf'>Revisiting the traditional medicine of the tribals in the Jungle Mahals, 1947–2000 </a></td>
<td> Nirmal Kumar Mahato</td>
<td>7121</td>
</tr>
<tr>
<td>1880</td>
<td>IJHS-58-2023-Issue-2</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_2_6.pdf'>Institutionalization of agricultural education in the nineteenth century colonial India: its... </a></td>
<td> Prakrati Bhargava</td>
<td>3033</td>
</tr>
<tr>
<td>1881</td>
<td>IJHS-58-2023-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS58_2_7.pdf'>Technologies of transportation: road, bridge and boat construction in colonial Punjab </a></td>
<td> Mandakini Thakur</td>
<td>2972</td>
</tr>
<tr>
<td>1882</td>
<td>IJHS-58-2023-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_2_8.pdf'>Project Report: The history of geographical surveys in India during the British period </a></td>
<td> C. S. Meenakshi</td>
<td>2941</td>
</tr>
<tr>
<td>1883</td>
<td>IJHS-58-2023-Issue-3</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents_58-3.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1475</td>
</tr>
<tr>
<td>1884</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_1.pdf'>Use of the concept of derivative in the computation of vyatīpāta in two Kerala texts </a></td>
<td> Venketeswara Pai R., M. S. Sriram</td>
<td>4733</td>
</tr>
<tr>
<td>1885</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_2.pdf'>Geometry of prāṇakalāntara in the Lagnaprakaraṇa </a></td>
<td> Nagakiran Yelluru, Aditya Kolachana</td>
<td>3329</td>
</tr>
<tr>
<td>1886</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_3.pdf'>Mahādevī-sāriṇī : A unique table providing true longitudes of planets </a></td>
<td> B. S. Shubha, B. S. Shylaja</td>
<td>5156</td>
</tr>
<tr>
<td>1887</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_4.pdf'>Colonialism, nationalism and reconstruction of history of science: the case of Goa </a></td>
<td> Nagendra Rao</td>
<td>2998</td>
</tr>
<tr>
<td>1888</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_5.pdf'>Advent, appropriation, and aesthetics of electric light in the princely state of Jammu and Kashmir,  </a></td>
<td> Baasit Abubakr, Saradindu Bhaduri</td>
<td>2972</td>
</tr>
<tr>
<td>1889</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_6.pdf'>Mountains of corpses: the deadliest attack of the 1918–19 influenza pandemic in the city of... </a></td>
<td> Saumitra Basu</td>
<td>4638</td>
</tr>
<tr>
<td>1890</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_7.pdf'>A study of diseases and deaths in colonial Bihar in twentieth century </a></td>
<td> Sudhanshu Kumar Jha, Shubham</td>
<td>3420</td>
</tr>
<tr>
<td>1891</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_8.pdf'>BooK Review: History of Indian astronomy: The Tirvalore tables... </a></td>
<td> B. S. Shylaja</td>
<td>2914</td>
</tr>
<tr>
<td>1892</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_9.pdf'>Book Review: Sir R.N. Mookerjee... </a></td>
<td> Samir Kumar Saha</td>
<td>2872</td>
</tr>
<tr>
<td>1893</td>
<td>IJHS-58-2023-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_58_3_10.pdf'>Project Report: Development of amateur astronomy in independent India with special reference to... </a></td>
<td> Sabyasachi Chatterjee</td>
<td>2946</td>
</tr>
<tr>
<td>1894</td>
<td>IJHS-58-2023-Issue-4</td>
<td>x_Misc</td>
<td>nan</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents_58_4IJHS.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1677</td>
</tr>
<tr>
<td>1895</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/01_58_4.pdf'>Equinoctial full moon of the Brahmāṇḍa Purāṇa and the nakṣatra solar zodiac starting from summer... </a></td>
<td> R. N. Iyengar, Sunder Chakravarty</td>
<td>1121</td>
</tr>
<tr>
<td>1896</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/02-58_4.pdf'>Construction and application of third diagonal in cyclic quadrilaterals by Nārāyaṇa Paṇḍita </a></td>
<td> Prasad A. Jawalgekar et al.</td>
<td>1173</td>
</tr>
<tr>
<td>1897</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/03-58_4.pdf'>Composition and characterisation of ancient lime mortar of Gopal Krishna temple, Alandi, India </a></td>
<td> Sarvesh Singh et al.</td>
<td>3422</td>
</tr>
<tr>
<td>1898</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Metallurgy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/04-58_4.pdf'>Reinvestigating the science and engineering behind the architectural marvels of Ahom dynasty in... </a></td>
<td> Anurag Borah</td>
<td>1059</td>
</tr>
<tr>
<td>1899</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/05-58_4.pdf'>Restoration and conservation of Sāncipāt manuscripts of Assam for preserving in ordinary rural setup </a></td>
<td> Asadulla Asraf Ali, Robin Kumar Dutta</td>
<td>2859</td>
</tr>
<tr>
<td>1900</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Agriculture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/06-58_4.pdf'>Historical Note: Origin, introduction, and cultural history of capsicum in India </a></td>
<td> N. C. Shah</td>
<td>1433</td>
</tr>
<tr>
<td>1901</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/07-58_4.pdf'>Book Review: History of the climate change on the Coromandel Coast (Ninth‒Nineteenth Centuries... </a></td>
<td> Anantanarayanan Raman</td>
<td>410</td>
</tr>
<tr>
<td>1902</td>
<td>IJHS-58-2023-Issue-4</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/08-58_4.pdf'>Book Review: Evolution of Neurosciences by P. N. Tandon and P. Sarat Chandra </a></td>
<td> Subrata Sinha</td>
<td>293</td>
</tr>
<tr>
<td>1903</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/09-58_4.pdf'>Project Report: The practice of folk medicine by the indigenous people of Sundarbans: A historical.. </a></td>
<td> Rup Kumar Barman</td>
<td>536</td>
</tr>
<tr>
<td>1904</td>
<td>IJHS-58-2023-Issue-4</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/10-58_4.pdf'>Correction: Geometry of prāṇakalāntara in the Lagnaprakaraṇa </a></td>
<td> IJHS</td>
<td>255</td>
</tr>
<tr>
<td>1905</td>
<td>IJHS-58-2023-Issue-4</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Cumulative Index_58_ijhs.pdf'>Cumulative Index & Annual Contents </a></td>
<td> IJHS</td>
<td>662</td>
</tr>
<tr>
<td>1906</td>
<td>IJHS-59-2024-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents_59_1_ijhs.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1497</td>
</tr>
<tr>
<td>1907</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/01-IJHS59_1.pdf'>Markers and agencies of anisotropy in the Indus sign system </a></td>
<td> M. V. Bhaskar</td>
<td>2627</td>
</tr>
<tr>
<td>1908</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Culture</td>
<td>Fareast</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/02-IJHS59_2.pdf'>Historical account of entomophagy among the Apatani tribe of Arunachal Pradesh: Current status... </a></td>
<td> Nending Muni, Pompi Bhadra and Jharna Chakravorty</td>
<td>1430</td>
</tr>
<tr>
<td>1909</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/03-IJHS59_1.pdf'>Infl uences of botanical knowledge from the East in the colonial medical developments: A case ... </a></td>
<td> K. Uthara</td>
<td>430</td>
</tr>
<tr>
<td>1910</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/04-IJHS59_1.pdf'>Dr. Suresh Prasad Sarbadhikari (1866–1921): A legendary surgeon and a Bengali pioneer of ovariotomy </a></td>
<td> Indranil Sanyal</td>
<td>2754</td>
</tr>
<tr>
<td>1911</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/05-IJHS59_1.pdf'>Jhum: An indigenous method of cultivation and British attitude towards it in Colonial Assam </a></td>
<td> Geetashree Singh</td>
<td>419</td>
</tr>
<tr>
<td>1912</td>
<td>IJHS-59-2024-Issue-1</td>
<td>MindSciences</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/06-IJHS59_1.pdf'>Questioning Basalla’s question (yet again): The view from cognitive </a></td>
<td> Subrata Dasgupta</td>
<td>557</td>
</tr>
<tr>
<td>1913</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/07-IJHS59_1.pdf'>Relevance of Ayurvedic prakṛti in literary studies with special reference to major characters of ... </a></td>
<td> K. R. Bhavana</td>
<td>476</td>
</tr>
<tr>
<td>1914</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Astronomy</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/08-IJHS59_1.pdf'>Historical Note: Pathway to Devasthal astronomical observatory, ARIES </a></td>
<td> Ram Sagar,  Gopal‑Krishna</td>
<td>4448</td>
</tr>
<tr>
<td>1915</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/09-IJHS59_1.pdf'>Book Review: Engineering education in India: Past, present and future </a></td>
<td> Gautam Biswas</td>
<td>268</td>
</tr>
<tr>
<td>1916</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/10-IJHS59_1.pdf'>Book Review: Science, war and imperialism: India in the second world war </a></td>
<td> Suvobrata Sarkar</td>
<td>309</td>
</tr>
<tr>
<td>1917</td>
<td>IJHS-59-2024-Issue-1</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/11-IJHS59_1.pdf'>Project Report: Archiving the work of Dr. Subhas Mukherjee: The architect of India’s test tube baby </a></td>
<td> Srabani Mukherjee, Rajvi Mehta</td>
<td>1798</td>
</tr>
<tr>
<td>1918</td>
<td>IJHS-59-2024-Issue-1</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Corrigendum_59_1.pdf'>Corrigendum </a></td>
<td> MV Bhaskar</td>
<td>65</td>
</tr>
<tr>
<td>1919</td>
<td>IJHS-59-2024-Issue-2</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents_59_2_ijhs.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1586</td>
</tr>
<tr>
<td>1920</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/01-43539_2024_127_OnlinePDF123-142.pdf'>Turagagati method for 4 × 4 pandiagonal magic squares by Nārāyana Pandita </a></td>
<td> M V Reddy et al.</td>
<td>5634</td>
</tr>
<tr>
<td>1921</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Culture</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/02-43539_2024_121_OnlinePDF143-158.pdf'>Locating Indian knowledge in modern libraries: Incorporating the traditional classification of ... </a></td>
<td> J. K. Bajaj and M. D. Srinivas</td>
<td>547</td>
</tr>
<tr>
<td>1922</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Biology</td>
<td>Islamic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/03-43539_2024_123_OnlinePDF159-164.pdf'>The Ukãy, Salvadora persica (Salvadoraceae): Historical and literary evidence... </a></td>
<td> Muthu V. Prakash, M. Anbarashan</td>
<td>870</td>
</tr>
<tr>
<td>1923</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/04-43539_2024_126_OnlinePDF165-177.pdf'>Politics, industrialization and technical education in colonial India: A case study of Imperial Inst </a></td>
<td> Prakrati Bhargava</td>
<td>482</td>
</tr>
<tr>
<td>1924</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/05-43539_2024_122_OnlinePDF178-191.pdf'>Displacement and sovereignty: Raja of Bilaspur and the Bhakra dam (1908–1947) </a></td>
<td> Pankaj Sharma · Balkrishan Shivram</td>
<td>819</td>
</tr>
<tr>
<td>1925</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Agriculture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/06-43539_2024_120_OnlinePDF192-203.pdf'>Indigenous knowledge for sustainable development: A case study of Kurmi Mahatos </a></td>
<td> Sanchita Bhattacharya</td>
<td>472</td>
</tr>
<tr>
<td>1926</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/07-43539_2024_125_OnlinePDF204-215.pdf'>Brief history of semiconductor science and technology and India’s role in the decade after the inven </a></td>
<td> P. K. Basu</td>
<td>559</td>
</tr>
<tr>
<td>1927</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/08-43539_2024_124_OnlinePDF216-222.pdf'>Historical Note: Yellapragada Subba Rao: The Unsung Hero of Science </a></td>
<td> Neelabh Datta</td>
<td>469</td>
</tr>
<tr>
<td>1928</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/09-43539_2024_129_OnlinePDF223-224.pdf'>Book Review: History of science, technology, environment, and medicine in India </a></td>
<td> J. N. Sinha</td>
<td>312</td>
</tr>
<tr>
<td>1929</td>
<td>IJHS-59-2024-Issue-2</td>
<td>Biology</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/10-43539_2024_128_OnlinePDF225-232.pdf'>Project Report: Plants of Atharvaveda: Their descriptions and medicinal uses </a></td>
<td> Raghava S. Boddupalli</td>
<td>687</td>
</tr>
<tr>
<td>1930</td>
<td>IJHS-59-2024-Issue-3</td>
<td>x_Other</td>
<td>x_Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/Contents_IJHS_59_3.pdf'>Contents </a></td>
<td> IJHS</td>
<td>1494</td>
</tr>
<tr>
<td>1931</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Astronomy</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_1.pdf'>On the calculation of the Moon’s latitude in Indian astronomy </a></td>
<td> Anil Narayanan</td>
<td>1407</td>
</tr>
<tr>
<td>1932</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_2.pdf'>The conception of negative numbers: A study of Kṛṣṇa Daivajña’s Bījapallava </a></td>
<td> Lalitha S R, Nagendra P R N, K Ramasubramanian</td>
<td>1039</td>
</tr>
<tr>
<td>1933</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Math</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_3.pdf'>Decision theory and probability theory: Pascal’s wager and pre‑modern Indian lotteries </a></td>
<td> Harald Wiese</td>
<td>1004</td>
</tr>
<tr>
<td>1934</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Biology</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_4.pdf'>The paleodietary reconstruction of Roopkund skeletons through trace element analysis </a></td>
<td> Sanjiv Kumar Juyal</td>
<td>780</td>
</tr>
<tr>
<td>1935</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Medicine</td>
<td>Dharmic</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_5.pdf'>Placing well‑being: The role of ecology in Āyurveda and Māvilan healing traditions </a></td>
<td> Pushya A. Gautama et al.</td>
<td>552</td>
</tr>
<tr>
<td>1936</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_6.pdf'>Understanding the various scientific theories in the history of science </a></td>
<td> Jun‑Young Oh</td>
<td>823</td>
</tr>
<tr>
<td>1937</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_7.pdf'>Historical perspectives of critical care in India and worldwide </a></td>
<td> Ujjwala Murkute</td>
<td>527</td>
</tr>
<tr>
<td>1938</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Medicine</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_8.pdf'>Book Review: Health, medicine and the encounters of cultures in India by Mumtaz Alam </a></td>
<td> Kamlesh Mohan</td>
<td>356</td>
</tr>
<tr>
<td>1939</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Culture</td>
<td>Western</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_9.pdf'>Project Report: History of linguistic science of the Austroasiatic group of languages with special.. </a></td>
<td> Satarupa Dattamajumdar Saha</td>
<td>487</td>
</tr>
<tr>
<td>1940</td>
<td>IJHS-59-2024-Issue-3</td>
<td>Other</td>
<td>Misc</td>
<td><a href='https://insa.nic.in//writereaddata/UpLoadedFiles/IJHS/IJHS_59_3_10.pdf'>Obituary to Professor S.M.R. Ansari </a></td>
<td> M. S. Sriram</td>
<td>431</td>
</tr>
</table>